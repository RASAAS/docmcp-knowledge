"""Recover fulltext for missing entries from unmatched files.

For each unmatched file, find the MISSING entry with highest title similarity.
If similarity >= 0.7, copy the file as that entry's fulltext.
"""

import json
import re
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


def strip_year_revision(title: str) -> str:
    t = re.sub(r'[（(]\d{4}年?\s*修订版[）)]', '', title)
    t = re.sub(r'注册技术审查指导原则', '注册审查指导原则', t)
    t = re.sub(r'注册技术指导原则', '注册审查指导原则', t)
    t = re.sub(r'技术审查指导原则', '审查指导原则', t)
    return t.strip()


def main():
    with open(INDEX_PATH) as f:
        entries = json.load(f).get("entries", [])

    missing = [e for e in entries if not fulltext_exists(e)]
    print(f"Missing entries: {len(missing)}")

    unmatched_files = sorted(UNMATCHED_DIR.glob("*.md"))
    print(f"Unmatched files: {len(unmatched_files)}")

    recovered = 0
    used_entries = set()

    for f_path in unmatched_files:
        text = f_path.read_text(encoding="utf-8")[:3000]
        um_title = extract_actual_title(text) or f_path.stem

        best_sim_raw = 0
        best_sim_norm = 0
        best_entry = None

        for e in missing:
            if e["id"] in used_entries:
                continue
            t = e.get("title", {})
            zh = t.get("zh", "") if isinstance(t, dict) else str(t)

            sim_raw = _title_similarity(um_title, zh)
            sim_norm = _title_similarity(strip_year_revision(um_title),
                                         strip_year_revision(zh))
            sim = max(sim_raw, sim_norm)
            if sim > best_sim_raw:
                best_sim_raw = sim
                best_entry = e

        if best_sim_raw >= 0.7 and best_entry:
            slug = best_entry.get("slug", "")
            if not slug:
                continue
            dest = FULLTEXT_DIR / f"{slug}.zh.md"
            shutil.copy2(f_path, dest)
            f_path.unlink()
            used_entries.add(best_entry["id"])
            recovered += 1

            t = best_entry.get("title", {})
            zh = t.get("zh", "") if isinstance(t, dict) else str(t)
            print(f"  {best_sim_raw:.2f} [{f_path.name[:20]}] -> {slug}")
            print(f"    UM: {um_title[:60]}")
            print(f"    IX: {zh[:60]}")

    print(f"\nRecovered: {recovered}")


if __name__ == "__main__":
    main()
