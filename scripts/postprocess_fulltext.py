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
    content = deduplicate_headers(content)
    content = collapse_blank_lines(content)

    changed = content != original
    stats = {
        'toc_removed': toc_removed,
        'footnotes': fn_count,
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
    changed_count = 0

    for path in files:
        stats = process_file(path, dry_run=args.dry_run)
        prefix = '[DRY]' if args.dry_run else '[OK] '
        if stats['changed']:
            changed_count += 1
            print(f"{prefix} {path.name}: removed {stats['toc_removed']} TOC table(s), "
                  f"reformatted {stats['footnotes']} footnote(s)")
        total_toc += stats['toc_removed']
        total_fn += stats['footnotes']

    mode = 'DRY RUN' if args.dry_run else 'DONE'
    print(f"\n{mode}: {changed_count}/{len(files)} files changed, "
          f"{total_toc} TOC tables removed, {total_fn} footnotes reformatted")


if __name__ == '__main__':
    main()
