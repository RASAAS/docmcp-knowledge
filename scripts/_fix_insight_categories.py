#!/usr/bin/env python3
"""Fix misclassified insight articles.

Moves articles to correct categories based on content analysis.
"""

import json
import re
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
INSIGHTS_DIR = REPO / "insights"
DOCS_ZH = REPO / "docs" / "zh" / "insights"
DOCS_EN = REPO / "docs" / "en" / "insights"

# Articles that need to be moved: (current_subcat, slug, target_subcat)
MOVES = [
    # MDR language requirements is an EU MDR topic, not NMPA
    ("nmpa-updates", "mdr-language-requirements", "eu-mdr-updates"),
]


def read_front_matter(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end < 0:
        return {}
    import yaml
    return yaml.safe_load(content[3:end]) or {}


def update_front_matter(path: Path, old_subcat: str, new_subcat: str):
    """Update subcategory and category in front matter."""
    content = path.read_text(encoding="utf-8")
    content = content.replace(
        f"subcategory: {old_subcat}",
        f"subcategory: {new_subcat}",
    )
    content = content.replace(
        f"category: insights/{old_subcat}",
        f"category: insights/{new_subcat}",
    )
    path.write_text(content, encoding="utf-8")


def move_article(old_subcat: str, slug: str, new_subcat: str, dry_run: bool = False):
    """Move an article from one subcategory to another."""
    print(f"\nMoving: {slug}")
    print(f"  From: insights/{old_subcat} -> insights/{new_subcat}")

    # 1. Move data layer file
    old_data = INSIGHTS_DIR / old_subcat / f"{slug}.zh.md"
    new_data = INSIGHTS_DIR / new_subcat / f"{slug}.zh.md"
    if old_data.exists():
        if dry_run:
            print(f"  [DRY] mv {old_data.relative_to(REPO)} -> {new_data.relative_to(REPO)}")
        else:
            new_data.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(old_data), str(new_data))
            update_front_matter(new_data, old_subcat, new_subcat)
            print(f"  Moved data layer: {new_data.relative_to(REPO)}")

    # 2. Move docs/zh page
    old_docs_zh = DOCS_ZH / old_subcat / f"{slug}.md"
    new_docs_zh = DOCS_ZH / new_subcat / f"{slug}.md"
    if old_docs_zh.exists():
        if dry_run:
            print(f"  [DRY] mv {old_docs_zh.relative_to(REPO)} -> {new_docs_zh.relative_to(REPO)}")
        else:
            new_docs_zh.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(old_docs_zh), str(new_docs_zh))
            update_front_matter(new_docs_zh, old_subcat, new_subcat)
            print(f"  Moved docs/zh: {new_docs_zh.relative_to(REPO)}")

    # 3. Move docs/en page (if exists)
    old_docs_en = DOCS_EN / old_subcat / f"{slug}.md"
    new_docs_en = DOCS_EN / new_subcat / f"{slug}.md"
    if old_docs_en.exists():
        if dry_run:
            print(f"  [DRY] mv {old_docs_en.relative_to(REPO)} -> {new_docs_en.relative_to(REPO)}")
        else:
            new_docs_en.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(old_docs_en), str(new_docs_en))
            update_front_matter(new_docs_en, old_subcat, new_subcat)
            print(f"  Moved docs/en: {new_docs_en.relative_to(REPO)}")

    # 4. Update _index.json: remove from old, add to new
    if not dry_run:
        _update_indexes(old_subcat, new_subcat, slug)


def _update_indexes(old_subcat: str, new_subcat: str, slug: str):
    """Move entry from old index to new index."""
    old_idx_path = INSIGHTS_DIR / old_subcat / "_index.json"
    new_idx_path = INSIGHTS_DIR / new_subcat / "_index.json"

    moved_entry = None

    # Remove from old index
    if old_idx_path.exists():
        old_idx = json.loads(old_idx_path.read_text(encoding="utf-8"))
        old_entries = old_idx.get("entries", [])
        new_old_entries = []
        for e in old_entries:
            if slug in e.get("id", ""):
                moved_entry = e
                print(f"  Removed from {old_subcat} index: {e['id']}")
            else:
                new_old_entries.append(e)
        old_idx["entries"] = new_old_entries
        old_idx["count"] = len(new_old_entries)
        old_idx_path.write_text(
            json.dumps(old_idx, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    # Add to new index
    if moved_entry:
        # Update subcategory in the entry
        moved_entry["subcategory"] = new_subcat

        if new_idx_path.exists():
            new_idx = json.loads(new_idx_path.read_text(encoding="utf-8"))
        else:
            new_idx = {
                "category": f"insights/{new_subcat}",
                "last_updated": "",
                "count": 0,
                "entries": [],
            }

        # Check for duplicates
        existing_ids = {e.get("id") for e in new_idx.get("entries", [])}
        if moved_entry["id"] not in existing_ids:
            new_idx["entries"].append(moved_entry)
            new_idx["count"] = len(new_idx["entries"])
            from datetime import datetime
            new_idx["last_updated"] = datetime.now().strftime("%Y-%m-%d")
            new_idx_path.write_text(
                json.dumps(new_idx, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            print(f"  Added to {new_subcat} index: {moved_entry['id']}")


if __name__ == "__main__":
    import sys
    dry_run = "--dry-run" in sys.argv

    print("=== Insight Category Fix ===")
    for old_subcat, slug, new_subcat in MOVES:
        move_article(old_subcat, slug, new_subcat, dry_run=dry_run)

    print("\nDone. Run generate_docs_index.py to regenerate sidebar/indexes.")
