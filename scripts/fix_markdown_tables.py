#!/usr/bin/env python3
"""Fix broken markdown tables from WordPress migration.

Problems:
1. No leading/trailing `|` on rows
2. Header rows split across multiple lines with trailing `  ` (soft breaks)
3. Separator rows like `---|---|---` without leading `|`

Fix: Reconstruct proper markdown tables with `| col | col |` format.
"""
import re
import sys
from pathlib import Path


def is_separator_line(line: str) -> bool:
    """Check if line is a table separator like `---|---|---`."""
    stripped = line.strip().rstrip("  ")
    # Remove leading | if present
    stripped = stripped.lstrip("|").rstrip("|").strip()
    parts = [p.strip() for p in stripped.split("|")]
    return all(re.match(r'^:?-{2,}:?$', p) for p in parts) and len(parts) >= 2


def is_table_data_line(line: str) -> bool:
    """Check if line looks like a table data row (contains | but is not a separator)."""
    stripped = line.strip()
    if not stripped or stripped.startswith("#") or stripped.startswith(">"):
        return False
    if "|" not in stripped:
        return False
    if is_separator_line(stripped):
        return False
    return True


def normalize_row(line: str, expected_cols: int = 0) -> str:
    """Normalize a table row to have leading/trailing pipes."""
    stripped = line.strip().rstrip("  ")
    # Remove existing leading/trailing pipes
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    cells = [c.strip() for c in stripped.split("|")]
    # Pad or trim to expected column count if specified
    if expected_cols > 0:
        while len(cells) < expected_cols:
            cells.append("")
        cells = cells[:expected_cols]
    return "| " + " | ".join(cells) + " |"


def normalize_separator(line: str, expected_cols: int = 0) -> str:
    """Normalize separator row."""
    stripped = line.strip().rstrip("  ")
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    parts = [p.strip() for p in stripped.split("|")]
    if expected_cols > 0:
        while len(parts) < expected_cols:
            parts.append("---")
        parts = parts[:expected_cols]
    return "| " + " | ".join(parts) + " |"


def fix_tables_in_content(content: str) -> str:
    """Fix all broken tables in markdown content."""
    lines = content.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Detect separator line (the key indicator of a table)
        if is_separator_line(line):
            # Look backwards to find header lines
            # Header may be split across multiple lines with trailing `  `
            header_lines = []
            j = len(result) - 1
            while j >= 0:
                prev = result[j]
                if is_table_data_line(prev) or (prev.strip().endswith("  ") and "|" in prev):
                    header_lines.insert(0, result.pop(j))
                    j -= 1
                else:
                    break

            if not header_lines:
                # No header found, just normalize separator and continue
                result.append(normalize_separator(line))
                i += 1
                continue

            # Merge multi-line headers into single line
            merged_header = ""
            for hl in header_lines:
                part = hl.strip().rstrip("  ")
                if merged_header:
                    # Check if previous part ended mid-cell (no trailing |)
                    # and this part starts without |
                    prev_cells = merged_header.split("|")
                    curr_parts = part.split("|")
                    # Merge: append first part of current to last cell of previous
                    if len(prev_cells) > 0 and len(curr_parts) > 0:
                        prev_cells[-1] = prev_cells[-1].strip() + curr_parts[0].strip()
                        merged_header = "|".join(prev_cells)
                        if len(curr_parts) > 1:
                            merged_header += "|" + "|".join(curr_parts[1:])
                else:
                    merged_header = part

            # Count columns from separator
            sep_stripped = line.strip().rstrip("  ").lstrip("|").rstrip("|")
            num_cols = len([p for p in sep_stripped.split("|") if p.strip()])

            # Normalize header and separator
            result.append(normalize_row(merged_header, num_cols))
            result.append(normalize_separator(line, num_cols))

            # Process data rows
            i += 1
            while i < len(lines):
                data_line = lines[i]
                if is_table_data_line(data_line):
                    result.append(normalize_row(data_line, num_cols))
                    i += 1
                else:
                    break
            continue

        result.append(line)
        i += 1

    return "\n".join(result)


def main():
    repo_root = Path(__file__).resolve().parent.parent
    scan_dirs = [
        repo_root / "docs" / "zh" / "insights",
        repo_root / "docs" / "zh" / "nmpa" / "guidance",
        repo_root / "docs" / "zh" / "nmpa" / "regulations",
    ]

    dry_run = "--dry-run" in sys.argv
    fixed_count = 0

    for scan_dir in scan_dirs:
        if not scan_dir.exists():
            continue
        for md_file in scan_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            # Quick check: does file have broken tables?
            if not re.search(r'^---\|', content, re.MULTILINE):
                continue

            fixed = fix_tables_in_content(content)
            if fixed != content:
                fixed_count += 1
                if dry_run:
                    print(f"[DRY-RUN] Would fix: {md_file.relative_to(repo_root)}")
                else:
                    md_file.write_text(fixed, encoding="utf-8")
                    print(f"[FIXED] {md_file.relative_to(repo_root)}")

    print(f"\nTotal: {fixed_count} files {'would be ' if dry_run else ''}fixed")


if __name__ == "__main__":
    main()
