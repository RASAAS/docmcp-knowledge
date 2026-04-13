"""Analyze coverage gaps and find retrievable entries."""

import json
import re
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "nmpa" / "guidance" / "_index.json"
FULLTEXT_DIR = ROOT / "nmpa" / "guidance" / "fulltext"
DISC_PATH = ROOT / "nmpa" / "guidance" / "_discovered_urls.json"


def fulltext_exists(entry: dict) -> bool:
    slug = entry.get("slug", "")
    eid = entry.get("id", "")
    for name in [slug, re.sub(r'[^\w\-.]', '_', eid)] if eid else [slug]:
        if not name:
            continue
        if (FULLTEXT_DIR / f"{name}.md").exists():
            return True
        if (FULLTEXT_DIR / f"{name}.zh.md").exists():
            return True
    return False


def analyze():
    with open(INDEX_PATH) as f:
        entries = json.load(f).get("entries", [])
    with open(DISC_PATH) as f:
        discovered = json.load(f)

    total = len(entries)
    with_ft = sum(1 for e in entries if fulltext_exists(e))
    missing = [e for e in entries if not fulltext_exists(e)]

    print(f"Total entries: {total}")
    print(f"With fulltext: {with_ft}")
    print(f"Missing fulltext: {len(missing)}")

    has_urls = 0
    no_urls = 0
    by_doc_number = Counter()

    for e in missing:
        eid = e["id"]
        disc = discovered.get(eid, {})
        urls = disc.get("urls", [])
        if not urls:
            old = disc.get("url", "")
            if old:
                urls = [old]
        if urls:
            has_urls += 1
        else:
            no_urls += 1
            dn = e.get("doc_number", "")
            if dn:
                by_doc_number[dn] += 1

    print(f"\nMissing entries with discovered URLs: {has_urls}")
    print(f"Missing entries without any URLs: {no_urls}")

    if by_doc_number:
        print(f"\nMissing entries by doc_number (top 20):")
        for dn, count in by_doc_number.most_common(20):
            print(f"  {count:3d}  {dn}")

    has_source_url = sum(1 for e in missing if e.get("source_url"))
    print(f"\nMissing entries with source_url: {has_source_url}")

    print(f"\nSample missing entries (first 10):")
    for e in missing[:10]:
        title = e.get("title", {})
        t = title.get("zh", "") if isinstance(title, dict) else str(title)
        eid = e["id"]
        disc = discovered.get(eid, {})
        urls = disc.get("urls", [])
        source = e.get("source_url", "")
        print(f"  [{eid[:12]}] {t[:50]} | urls={len(urls)} source={bool(source)}")

    print(f"\nMissing entries WITH source_url (first 10):")
    for e in missing:
        if not e.get("source_url"):
            continue
        title = e.get("title", {})
        t = title.get("zh", "") if isinstance(title, dict) else str(title)
        source = e["source_url"]
        print(f"  {t[:50]} | {source[:80]}")


if __name__ == "__main__":
    analyze()
