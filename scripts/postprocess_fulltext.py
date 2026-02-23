"""
Post-process docling-converted fulltext Markdown files.

Problems fixed:
1. TOC tables: docling converts PDF table-of-contents into wide Markdown tables
   with repeated columns and dot-filled page references. These are useless on web
   (sidebar provides navigation) and cause horizontal overflow. → Removed.
2. Inline footnotes: PDF footnotes are inlined into the body as bare "1 Some text"
   lines. → Reformatted as blockquote-style footnotes.
3. Duplicate disclaimer lines at the top of each file (repeated title/date lines
   that docling emits before the real content). → Deduplicated.

Usage:
    python3 scripts/postprocess_fulltext.py [--dry-run]
"""

import re
import argparse
from pathlib import Path


REPO_ROOT = Path(__file__).parent.parent
FULLTEXT_DIR = REPO_ROOT / "eu_mdr" / "mdcg" / "fulltext"


# ── helpers ──────────────────────────────────────────────────────────────────

def is_toc_table_line(line: str) -> bool:
    """Return True if a Markdown table row looks like a TOC entry (dot-filled)."""
    return bool(re.search(r'\.{8,}', line))


def split_into_table_blocks(lines: list[str]) -> list[tuple[str, list[str]]]:
    """
    Split lines into alternating non-table and table blocks.
    Returns list of ('text'|'table', [lines]) tuples.
    """
    blocks = []
    current_type = None
    current = []

    for line in lines:
        in_table = line.startswith('|')
        block_type = 'table' if in_table else 'text'
        if block_type != current_type:
            if current:
                blocks.append((current_type, current))
            current_type = block_type
            current = [line]
        else:
            current.append(line)

    if current:
        blocks.append((current_type, current))
    return blocks


def is_toc_table(table_lines: list[str]) -> bool:
    """Return True if this table block is a table-of-contents."""
    dot_lines = sum(1 for l in table_lines if is_toc_table_line(l))
    return dot_lines >= 2  # at least 2 rows with dot-fills = TOC


# Headings that precede a TOC table and should be removed with it
TOC_HEADING_RE = re.compile(r'^#{1,3}\s*(table of contents|contents|index)\s*$', re.IGNORECASE)


def remove_toc_tables(content: str) -> tuple[str, int]:
    """Remove TOC tables (and their preceding heading) from content."""
    lines = content.split('\n')
    blocks = split_into_table_blocks(lines)
    removed = 0
    out_blocks = []
    for btype, blines in blocks:
        if btype == 'table' and is_toc_table(blines):
            removed += 1
            # Also remove the preceding heading block if it's a TOC heading
            if out_blocks:
                prev_entry = out_blocks[-1]
                prev_type = prev_entry[0]
                prev_lines = prev_entry[1]
                if prev_type == 'text':
                    # Strip trailing blank lines, check if last non-blank is a TOC heading
                    stripped = [l for l in prev_lines if l.strip()]
                    if stripped and TOC_HEADING_RE.match(stripped[-1]):
                        # Remove that heading line from the previous block
                        new_prev = []
                        for l in prev_lines:
                            if l.strip() and TOC_HEADING_RE.match(l):
                                continue
                            new_prev.append(l)
                        out_blocks[-1] = (prev_type, new_prev)
        else:
            out_blocks.append((btype, blines))
    return '\n'.join(line for (_t, block) in out_blocks for line in block), removed


# ── footnote reformatting ─────────────────────────────────────────────────────

# Pattern: a line that starts with one or more digits, then a space, then text.
# Must NOT be inside a table (no leading |).
# Must be preceded by a blank line (i.e., it's a standalone paragraph).
FOOTNOTE_RE = re.compile(r'^(\d+)\s{1,4}(.+)$')


def reformat_footnotes(content: str) -> tuple[str, int]:
    """
    Convert inline footnote lines to a footnotes section at the end.

    Detects lines matching: ^<digits> <text>
    that appear after a blank line and are not inside a table.
    Groups them into a "---\n**Footnotes**" block at the end of the document.
    """
    lines = content.split('\n')
    footnotes = []
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Skip table rows
        if line.startswith('|'):
            new_lines.append(line)
            i += 1
            continue

        m = FOOTNOTE_RE.match(line)
        if m:
            num = m.group(1)
            text = m.group(2).strip()

            # Collect continuation lines (non-empty, non-table, not a new footnote)
            # Limit to max 3 continuation lines to avoid swallowing normal paragraphs
            j = i + 1
            cont_count = 0
            while j < len(lines) and cont_count < 3:
                next_line = lines[j]
                if next_line == '':
                    break
                if next_line.startswith('|'):
                    break
                if FOOTNOTE_RE.match(next_line):
                    break
                # Heading or HR
                if next_line.startswith('#') or next_line.startswith('---'):
                    break
                # If next line looks like a new sentence/paragraph (starts uppercase after period)
                if cont_count > 0 and re.match(r'^[A-Z][a-z]', next_line) and text.endswith('.'):
                    break
                text += ' ' + next_line.strip()
                j += 1
                cont_count += 1

            footnotes.append((num, text))
            # Remove the blank line before this footnote if present
            if new_lines and new_lines[-1] == '':
                new_lines.pop()
            i = j
        else:
            new_lines.append(line)
            i += 1

    if not footnotes:
        return content, 0

    # Append footnotes as a simple ordered list (no plugin needed)
    fn_block = ['\n', '---', '', '**Footnotes**', '']
    for num, text in footnotes:
        fn_block.append(f'{num}. {text}')
    fn_block.append('')

    return '\n'.join(new_lines) + '\n'.join(fn_block), len(footnotes)


# ── fragmented table merging ─────────────────────────────────────────────────

def merge_fragmented_tables(content: str) -> tuple[str, int]:
    """
    docling sometimes splits a single logical table into multiple consecutive
    Markdown table blocks separated by a blank line, each with different column
    counts. This happens when PDF rows span multiple columns (rowspan/colspan).

    Strategy: scan for consecutive table blocks separated by at most 1 blank line.
    If they appear to be fragments of the same table (same or similar content
    domain), merge them into a single table with the maximum column count.

    A group of tables is considered fragmented if:
    - They are separated by at most 1 blank line (no text between them)
    - At least one pair of adjacent tables has different column counts
    - The first table has >= 2 columns
    """
    lines = content.split('\n')
    # Re-split into blocks but also track blank-line separators
    blocks: list[tuple[str, list[str]]] = []  # ('text'|'table'|'blank', lines)
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('|'):
            # Collect table block
            tbl = []
            while i < len(lines) and lines[i].startswith('|'):
                tbl.append(lines[i])
                i += 1
            blocks.append(('table', tbl))
        elif line.strip() == '':
            # Collect consecutive blank lines
            blanks = []
            while i < len(lines) and lines[i].strip() == '':
                blanks.append(lines[i])
                i += 1
            blocks.append(('blank', blanks))
        else:
            # Collect text block
            txt = []
            while i < len(lines) and lines[i].strip() != '' and not lines[i].startswith('|'):
                txt.append(lines[i])
                i += 1
            blocks.append(('text', txt))

    # Find groups of tables separated only by single blank lines
    merged = 0
    out_blocks: list[tuple[str, list[str]]] = []
    bi = 0
    while bi < len(blocks):
        btype, blines = blocks[bi]
        if btype != 'table':
            out_blocks.append((btype, blines))
            bi += 1
            continue

        # Try to collect a group of consecutive tables (separated by <=1 blank line)
        group_tables = [blines]
        group_blanks: list[list[str]] = []  # blanks between tables
        j = bi + 1
        while j < len(blocks):
            next_type, next_lines = blocks[j]
            if next_type == 'blank' and len(next_lines) <= 1:
                # Peek ahead: is the next non-blank block a table?
                if j + 1 < len(blocks) and blocks[j + 1][0] == 'table':
                    group_blanks.append(next_lines)
                    group_tables.append(blocks[j + 1][1])
                    j += 2
                    continue
            break

        if len(group_tables) == 1:
            # No adjacent tables found
            out_blocks.append(('table', blines))
            bi += 1
            continue

        # Check if any pair has different column counts
        col_counts = []
        for tbl in group_tables:
            data_rows = [l for l in tbl if l.strip() and not is_separator_row(l)]
            if data_rows:
                col_counts.append(len(parse_table_row(data_rows[0])))
            else:
                col_counts.append(0)

        if len(set(col_counts)) == 1:
            # All same column count — not fragmented, keep as-is
            for k, tbl in enumerate(group_tables):
                out_blocks.append(('table', tbl))
                if k < len(group_blanks):
                    out_blocks.append(('blank', group_blanks[k]))
            bi = j
            continue

        # Fragmented tables detected — merge into one with max col count
        max_cols = max(col_counts)
        merged_rows: list[str] = []
        separator_written = False

        for tbl in group_tables:
            for line in tbl:
                if not line.strip():
                    continue
                if is_separator_row(line):
                    if not separator_written:
                        merged_rows.append('| ' + ' | '.join(['---'] * max_cols) + ' |')
                        separator_written = True
                    continue
                cells = parse_table_row(line)
                # Pad or trim to max_cols
                while len(cells) < max_cols:
                    cells.append('')
                merged_rows.append('| ' + ' | '.join(cells[:max_cols]) + ' |')

        out_blocks.append(('table', merged_rows))
        merged += 1
        bi = j

    result_lines = []
    for btype, blines in out_blocks:
        result_lines.extend(blines)
    return '\n'.join(result_lines), merged


# ── repeated-column table cleanup ────────────────────────────────────────────

def parse_table_row(line: str) -> list[str]:
    """Parse a Markdown table row into a list of cell strings."""
    # Strip leading/trailing | and split
    stripped = line.strip()
    if stripped.startswith('|'):
        stripped = stripped[1:]
    if stripped.endswith('|'):
        stripped = stripped[:-1]
    return [c.strip() for c in stripped.split('|')]


def is_separator_row(line: str) -> bool:
    """Return True if this is a Markdown table separator row (---|---|...)."""
    return bool(re.match(r'^\|?[\s\-:]+(\|[\s\-:]+)+\|?$', line.strip()))


def deduplicate_table_columns(content: str) -> tuple[str, int]:
    """
    Fix tables where docling expanded merged cells by repeating content across columns.

    Strategy: process row by row within each table.
    - If ALL non-empty cells in a row are identical (merged-cell row), collapse to 1 cell
      and render as a bold heading row: | **content** |
    - Otherwise keep the row as-is.

    Only applies to tables with >= 3 columns where at least one row has all-identical cells.
    """
    lines = content.split('\n')
    blocks = split_into_table_blocks(lines)
    fixed = 0
    out_blocks = []

    for btype, blines in blocks:
        if btype != 'table':
            out_blocks.append((btype, blines))
            continue

        # Determine column count from first non-separator row
        data_rows = [l for l in blines if l.strip() and not is_separator_row(l)]
        if not data_rows:
            out_blocks.append((btype, blines))
            continue

        col_count = len(parse_table_row(data_rows[0]))
        if col_count < 3:
            out_blocks.append((btype, blines))
            continue

        # Check if any row has all-identical non-empty cells (merged-cell indicator)
        has_merged = False
        for row in data_rows:
            cells = parse_table_row(row)
            non_empty = [c for c in cells if c.strip()]
            if len(non_empty) >= 2 and len(set(non_empty)) == 1:
                has_merged = True
                break

        if not has_merged:
            out_blocks.append((btype, blines))
            continue

        # Rebuild: collapse all-identical rows to a single bold heading cell
        new_blines = []
        separator_written = False
        for line in blines:
            if not line.strip():
                new_blines.append(line)
                continue
            if is_separator_row(line):
                if not separator_written:
                    new_blines.append('| ' + ' | '.join(['---'] * col_count) + ' |')
                    separator_written = True
                continue
            cells = parse_table_row(line)
            non_empty = [c for c in cells if c.strip()]
            if len(non_empty) >= 2 and len(set(non_empty)) == 1:
                # All non-empty cells identical → merged-cell row → bold heading spanning all cols
                merged_text = non_empty[0]
                # Pad to col_count with empty cells after the bold heading
                padded = [f'**{merged_text}**'] + [''] * (col_count - 1)
                new_blines.append('| ' + ' | '.join(padded) + ' |')
            else:
                # Normal row: keep as-is, pad to col_count if needed
                while len(cells) < col_count:
                    cells.append('')
                new_blines.append('| ' + ' | '.join(cells[:col_count]) + ' |')

        out_blocks.append((btype, new_blines))
        fixed += 1

    return '\n'.join(line for (_t, block) in out_blocks for line in block), fixed


# ── duplicate header deduplication ───────────────────────────────────────────

def deduplicate_headers(content: str) -> str:
    """
    docling often emits the document title/date 2-3 times at the top.
    Remove exact duplicate consecutive paragraphs (non-table, non-heading).
    """
    lines = content.split('\n')
    seen_paragraphs: set[str] = set()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Collect a paragraph (lines until blank)
        if line.strip() and not line.startswith('#') and not line.startswith('|') \
                and not line.startswith('>') and not line.startswith('-') \
                and not line.startswith('*') and not line.startswith('['):
            para_lines = []
            j = i
            while j < len(lines) and lines[j].strip():
                para_lines.append(lines[j])
                j += 1
            para_text = ' '.join(para_lines).strip()
            # Only deduplicate short paragraphs (likely repeated titles/dates)
            if len(para_text) < 300 and para_text in seen_paragraphs:
                i = j  # skip this duplicate paragraph
                continue
            seen_paragraphs.add(para_text)
        out.append(line)
        i += 1
    return '\n'.join(out)


# ── collapse excess blank lines ───────────────────────────────────────────────

def collapse_blank_lines(content: str) -> str:
    """Replace 3+ consecutive blank lines with 2."""
    return re.sub(r'\n{4,}', '\n\n\n', content)


# ── main processing ───────────────────────────────────────────────────────────

def process_file(path: Path, dry_run: bool) -> dict:
    original = path.read_text(encoding='utf-8')
    content = original

    content, toc_removed = remove_toc_tables(content)
    content, fn_count = reformat_footnotes(content)
    content, frag_merged = merge_fragmented_tables(content)
    content, dup_cols_fixed = deduplicate_table_columns(content)
    content = deduplicate_headers(content)
    content = collapse_blank_lines(content)

    changed = content != original
    stats = {
        'toc_removed': toc_removed,
        'footnotes': fn_count,
        'frag_merged': frag_merged,
        'dup_cols_fixed': dup_cols_fixed,
        'changed': changed,
    }

    if changed and not dry_run:
        path.write_text(content, encoding='utf-8')

    return stats


def main():
    parser = argparse.ArgumentParser(description='Post-process docling fulltext Markdown files')
    parser.add_argument('--dry-run', action='store_true', help='Show what would change without writing')
    parser.add_argument('--file', help='Process a single file (basename, e.g. mdcg-2020-5.md)')
    args = parser.parse_args()

    if args.file:
        files = [FULLTEXT_DIR / args.file]
    else:
        files = sorted(FULLTEXT_DIR.glob('*.md'))

    total_toc = 0
    total_fn = 0
    total_frag = 0
    total_dup = 0
    changed_count = 0

    for path in files:
        stats = process_file(path, dry_run=args.dry_run)
        prefix = '[DRY]' if args.dry_run else '[OK] '
        if stats['changed']:
            changed_count += 1
            print(f"{prefix} {path.name}: removed {stats['toc_removed']} TOC, "
                  f"reformatted {stats['footnotes']} footnotes, "
                  f"merged {stats['frag_merged']} frag-tables, "
                  f"fixed {stats['dup_cols_fixed']} dup-col tables")
        total_toc += stats['toc_removed']
        total_fn += stats['footnotes']
        total_frag += stats['frag_merged']
        total_dup += stats['dup_cols_fixed']

    mode = 'DRY RUN' if args.dry_run else 'DONE'
    print(f"\n{mode}: {changed_count}/{len(files)} files changed, "
          f"{total_toc} TOC removed, {total_fn} footnotes, "
          f"{total_frag} frag-tables merged, {total_dup} dup-col fixed")


if __name__ == '__main__':
    main()
