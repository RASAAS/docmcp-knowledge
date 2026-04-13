"""Check: are those best=0.33 entries actually the same doc with year diff?"""

import json
import re
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_nmpa_fulltext import (
    extract_actual_title, _title_similarity, fulltext_exists,
    FULLTEXT_DIR, INDEX_PATH, _extract_core_subject
)

ROOT = Path(__file__).resolve().parent.parent
UNMATCHED_DIR = ROOT / "nmpa" / "guidance" / "_unmatched"


def strip_year_revision(title: str) -> str:
    """Remove year/revision markers for comparison."""
    t = re.sub(r'[（(]\d{4}年?\s*修订版[）)]', '', title)
    t = re.sub(r'[（(]\d{4}\s*修订版?[）)]', '', t)
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

    match_count = 0
    for f in unmatched_files:
        text = f.read_text(encoding="utf-8")[:3000]
        um_title = extract_actual_title(text) or f.stem
        um_stripped = strip_year_revision(um_title)

        best_sim = 0
        best_entry = None

        for e in missing:
            t = e.get("title", {})
            zh = t.get("zh", "") if isinstance(t, dict) else str(t)
            zh_stripped = strip_year_revision(zh)
            sim = _title_similarity(um_stripped, zh_stripped)
            if sim > best_sim:
                best_sim = sim
                best_entry = (e["id"], zh, e.get("slug", ""))

        if best_sim >= 0.6:
            match_count += 1
            print(f"  {best_sim:.2f} [{f.name[:20]}]")
            print(f"    UM: {um_title[:60]}")
            print(f"    IX: {best_entry[1][:60]} (slug={best_entry[2][:30]})")

    print(f"\nYear-normalized matches (sim >= 0.6): {match_count}")

    print(f"\n\n=== What about the 216 missing entries? Where might their fulltexts be? ===")
    print(f"Sample missing entries (showing top 30):")
    for e in missing[:30]:
        t = e.get("title", {})
        zh = t.get("zh", "") if isinstance(t, dict) else str(t)
        dn = e.get("doc_number", "")
        pub = e.get("published_date", "")
        print(f"  [{e['id'][:20]}] {zh[:60]} | dn={dn[:20]} pub={pub}")


if __name__ == "__main__":
    main()
