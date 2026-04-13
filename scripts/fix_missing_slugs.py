"""Add slugs to entries that don't have them, then recover fulltext where possible."""

import json
import re
import hashlib
import shutil
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_nmpa_fulltext import (
    extract_actual_title, _title_similarity, fulltext_exists,
    FULLTEXT_DIR, INDEX_PATH
)

ROOT = Path(__file__).resolve().parent.parent
UNMATCHED_DIR = ROOT / "nmpa" / "guidance" / "_unmatched"


def title_to_slug(title: str, eid: str) -> str:
    """Generate slug from title or entry ID."""
    h = hashlib.md5(eid.encode()).hexdigest()[:6]
    clean = re.sub(r'[^\w\-]', '-', title[:30]).strip('-').lower()
    clean = re.sub(r'-+', '-', clean)
    if not clean:
        clean = eid[:20]
    return f"nmpa-gp-{clean}-{h}"


def strip_year_revision(title: str) -> str:
    t = re.sub(r'[（(]\d{4}年?\s*修订版[）)]', '', title)
    t = re.sub(r'注册技术审查指导原则', '注册审查指导原则', t)
    t = re.sub(r'注册技术指导原则', '注册审查指导原则', t)
    return t.strip()


def main():
    with open(INDEX_PATH) as f:
        data = json.load(f)
    entries = data["entries"]

    no_slug = [e for e in entries if not e.get("slug")]
    print(f"Entries without slug: {len(no_slug)}")

    added_slugs = 0
    for e in entries:
        if e.get("slug"):
            continue
        t = e.get("title", {})
        zh = t.get("zh", "") if isinstance(t, dict) else str(t)
        slug = title_to_slug(zh, e["id"])
        e["slug"] = slug
        added_slugs += 1

    print(f"Added slugs: {added_slugs}")

    with open(INDEX_PATH, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved index")

    missing = [e for e in entries if not fulltext_exists(e)]
    print(f"\nMissing fulltext: {len(missing)}")

    unmatched_files = sorted(UNMATCHED_DIR.glob("*.md"))
    print(f"Unmatched files: {len(unmatched_files)}")

    recovered = 0
    for f_path in unmatched_files:
        text = f_path.read_text(encoding="utf-8")[:3000]
        um_title = extract_actual_title(text) or f_path.stem

        best_sim = 0
        best_entry = None
        for e in missing:
            t = e.get("title", {})
            zh = t.get("zh", "") if isinstance(t, dict) else str(t)
            sim = max(
                _title_similarity(um_title, zh),
                _title_similarity(strip_year_revision(um_title), strip_year_revision(zh))
            )
            if sim > best_sim:
                best_sim = sim
                best_entry = e

        if best_sim >= 0.85 and best_entry:
            slug = best_entry.get("slug", "")
            if not slug:
                continue
            t = best_entry.get("title", {})
            zh = t.get("zh", "") if isinstance(t, dict) else str(t)

            dest = FULLTEXT_DIR / f"{slug}.zh.md"
            if dest.exists():
                continue

            shutil.copy2(f_path, dest)
            f_path.unlink()
            recovered += 1
            print(f"  {best_sim:.2f} [{f_path.name[:20]}] -> {slug}")
            print(f"    UM: {um_title[:60]}")
            print(f"    IX: {zh[:60]}")

    print(f"\nRecovered: {recovered}")


if __name__ == "__main__":
    main()
