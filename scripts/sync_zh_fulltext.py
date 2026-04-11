"""Sync translated fulltext (.zh.md) into VitePress zh pages.

For each docs/zh/<framework>/<doc_type>/<slug>.md page that has a
`<!-- fulltext-start -->` marker, replace everything after that marker
with the corresponding fulltext/<slug>.zh.md content from the data layer.

Usage:
    python scripts/sync_zh_fulltext.py              # all sections
    python scripts/sync_zh_fulltext.py --section fda # FDA only
    python scripts/sync_zh_fulltext.py --dry-run     # preview only
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SECTIONS = {
    "imdrf":  {"docs": "docs/zh/_shared/imdrf", "data": "_shared/imdrf/fulltext"},
    "mdcg":   {"docs": "docs/zh/eu_mdr/mdcg",   "data": "eu_mdr/mdcg/fulltext"},
    "fda":    {"docs": "docs/zh/fda/guidance",   "data": "fda/guidance/fulltext"},
    "nmpa":   {"docs": "docs/zh/nmpa/guidance",  "data": "nmpa/guidance/fulltext"},
}

FULLTEXT_MARKER = "<!-- fulltext-start -->"


def sync_page(docs_path: Path, zh_fulltext_path: Path, dry_run: bool = False) -> bool:
    if not docs_path.exists():
        return False
    if not zh_fulltext_path.exists():
        return False

    page_text = docs_path.read_text(encoding="utf-8")
    marker_pos = page_text.find(FULLTEXT_MARKER)
    if marker_pos == -1:
        return False

    header = page_text[:marker_pos + len(FULLTEXT_MARKER)]
    zh_content = zh_fulltext_path.read_text(encoding="utf-8")

    new_page = header + "\n\n---\n\n## \u5b98\u65b9\u6587\u4ef6\u5168\u6587\n\n" + zh_content + "\n"

    if dry_run:
        old_lines = page_text.count("\n")
        new_lines = new_page.count("\n")
        print(f"  [DRY-RUN] {docs_path.name}: {old_lines} -> {new_lines} lines")
        return True

    docs_path.write_text(new_page, encoding="utf-8")
    print(f"  [OK] {docs_path.name} ({len(new_page)} bytes)")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--section", choices=list(SECTIONS.keys()) + ["all"], default="all")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    sections = SECTIONS if args.section == "all" else {args.section: SECTIONS[args.section]}
    total = 0

    for name, cfg in sections.items():
        docs_dir = ROOT / cfg["docs"]
        data_dir = ROOT / cfg["data"]
        if not docs_dir.exists():
            continue

        print(f"\n[{name.upper()}]")
        for docs_page in sorted(docs_dir.glob("*.md")):
            slug = docs_page.stem
            zh_fulltext = data_dir / f"{slug}.zh.md"
            if sync_page(docs_page, zh_fulltext, args.dry_run):
                total += 1

    print(f"\nTotal: {total} pages updated")


if __name__ == "__main__":
    main()
