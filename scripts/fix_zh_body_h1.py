#!/usr/bin/env python3
"""Fix body H1 headers in ZH guidance files to match corrected frontmatter titles.

After fix_zh_titles.py corrects the frontmatter title, the body text may still
have a garbled H1 line (e.g., "# 果果果..."). This script replaces the first
`# <text>` line in the body with the corrected frontmatter title.

Usage:
    python scripts/fix_zh_body_h1.py --dry-run
    python scripts/fix_zh_body_h1.py
"""

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZH_DIR = ROOT / "docs" / "zh" / "fda" / "guidance"


def fix_body_h1(filepath: Path, dry_run: bool = False) -> bool:
    """Fix the first body H1 to match the frontmatter title."""
    text = filepath.read_text(encoding="utf-8")

    # Extract frontmatter title
    title_match = re.search(r'^title:\s*"(.+?)"', text, re.MULTILINE)
    if not title_match:
        return False
    fm_title = title_match.group(1)

    # Find the first H1 in body (after frontmatter closing ---)
    fm_end = text.find("\n---\n", 3)
    if fm_end == -1:
        return False
    body_start = fm_end + 5

    body = text[body_start:]
    h1_match = re.search(r'^(# .+)$', body, re.MULTILINE)
    if not h1_match:
        return False

    old_h1 = h1_match.group(1)
    new_h1 = f"# {fm_title}"

    if old_h1 == new_h1:
        return False

    new_body = body[:h1_match.start()] + new_h1 + body[h1_match.end():]
    new_text = text[:body_start] + new_body

    if not dry_run:
        filepath.write_text(new_text, encoding="utf-8")
    else:
        old_display = old_h1[:60] + "..." if len(old_h1) > 60 else old_h1
        new_display = new_h1[:60] + "..." if len(new_h1) > 60 else new_h1
        print(f"  {filepath.stem}:")
        print(f"    OLD: {old_display}")
        print(f"    NEW: {new_display}")

    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    files = sorted(ZH_DIR.glob("*.md"))
    fixed = 0
    for f in files:
        if fix_body_h1(f, dry_run=args.dry_run):
            fixed += 1

    action = "Would fix" if args.dry_run else "Fixed"
    print(f"\n{action} {fixed} body H1 headers out of {len(files)} files")


if __name__ == "__main__":
    main()
