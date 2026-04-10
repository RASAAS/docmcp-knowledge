#!/usr/bin/env python3
"""Migrate NMPA regulations and guidance fulltext to the standardized fulltext pipeline.

This script:
1. Scans existing .zh.md files in nmpa/regulations/ and nmpa/guidance/
2. Matches them to _index.json entries using frontmatter title (zh) field
3. Adds 'slug' field to _index.json entries
4. Creates fulltext/{slug}.md files (stripped of frontmatter, pure body content)
5. Optionally updates source_url from reguverse.com to official NMPA links

Usage:
    python scripts/migrate_nmpa_fulltext.py --dry-run
    python scripts/migrate_nmpa_fulltext.py
"""

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

KNOWLEDGE_ROOT = Path(__file__).parent.parent


def normalize_title(title: str) -> str:
    """Normalize a Chinese title for fuzzy matching."""
    t = unicodedata.normalize("NFKC", title)
    t = re.sub(r"[（(].*?[）)]", "", t)
    t = re.sub(r"[\s\u3000]+", "", t)
    t = t.replace("——", "").replace("—", "").replace("-", "")
    t = re.sub(r"[,，.。、;；:：""''\"']", "", t)
    return t.lower()


def extract_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and body from markdown text."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---\n", 3)
    if end == -1:
        return {}, text
    fm_text = text[4:end]
    body = text[end + 5:].lstrip("\n")

    fm = {}
    current_key = None
    current_dict = None
    for line in fm_text.split("\n"):
        if not line.strip() or line.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        if indent >= 2 and current_dict is not None and current_key:
            m = re.match(r"\s+(\w+):\s*(.*)", line)
            if m:
                current_dict[m.group(1)] = m.group(2).strip().strip("'\"")
        else:
            m = re.match(r"([\w_-]+):\s*(.*)", line)
            if m:
                key = m.group(1)
                val = m.group(2).strip().strip("'\"")
                if val == "":
                    current_key = key
                    current_dict = {}
                    fm[key] = current_dict
                else:
                    fm[key] = val
                    current_key = None
                    current_dict = None
    return fm, body


def build_file_info(doc_type: str) -> list[dict]:
    """Build info list from .zh.md files with frontmatter data."""
    base_dir = KNOWLEDGE_ROOT / "nmpa" / doc_type
    results = []
    for zh_file in sorted(base_dir.glob("*.zh.md")):
        slug = zh_file.stem.replace(".zh", "")
        text = zh_file.read_text(encoding="utf-8")
        fm, body = extract_frontmatter(text)

        title_data = fm.get("title", {})
        if isinstance(title_data, dict):
            title_zh = title_data.get("zh", "")
        elif isinstance(title_data, str):
            title_zh = title_data
        else:
            title_zh = ""

        doc_id = fm.get("id", "")

        results.append({
            "slug": slug,
            "title_zh": title_zh,
            "title_normalized": normalize_title(title_zh),
            "doc_id": doc_id,
            "body": body,
            "lines": len(body.splitlines()),
            "source_url": fm.get("source_url", ""),
            "file": str(zh_file),
        })
    return results


def match_entries(data: dict, file_infos: list[dict]) -> dict:
    """Match _index.json entries to .zh.md files by title fuzzy matching."""
    entries = data.get("entries", [])

    title_to_info = {}
    for info in file_infos:
        if info["title_normalized"]:
            title_to_info[info["title_normalized"]] = info

    matched = {}
    unmatched_entries = []

    for entry in entries:
        entry_title = entry.get("title", {}).get("zh", "")
        if not entry_title:
            continue

        entry_norm = normalize_title(entry_title)
        eid = entry["id"]

        if entry_norm in title_to_info:
            matched[eid] = title_to_info[entry_norm]
            continue

        best_match = None
        best_len = 0
        for norm_title, info in title_to_info.items():
            if norm_title in entry_norm or entry_norm in norm_title:
                match_len = min(len(norm_title), len(entry_norm))
                if match_len > best_len:
                    best_len = match_len
                    best_match = info

        if best_match and best_len >= 6:
            matched[eid] = best_match
        else:
            unmatched_entries.append((eid, entry_title))

    return matched, unmatched_entries


def process_doc_type(doc_type: str, dry_run: bool = False) -> tuple[int, int]:
    """Process a single doc type (regulations or guidance)."""
    print(f"\n{'='*60}")
    print(f"Processing nmpa/{doc_type}")
    print(f"{'='*60}")

    index_path = KNOWLEDGE_ROOT / "nmpa" / doc_type / "_index.json"
    if not index_path.exists():
        print(f"  SKIP: {index_path} not found")
        return 0, 0

    with open(index_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    file_infos = build_file_info(doc_type)
    print(f"Found {len(file_infos)} .zh.md files")
    print(f"Index has {len(data.get('entries', []))} entries")

    matched, unmatched = match_entries(data, file_infos)
    print(f"Matched: {len(matched)} entries to .zh.md files")
    if unmatched:
        print(f"Unmatched index entries (no .zh.md file): {len(unmatched)}")

    used_slugs = {info["slug"] for info in matched.values()}
    unused_files = [info for info in file_infos if info["slug"] not in used_slugs]
    if unused_files:
        print(f"\nUnmatched .zh.md files (not in _index.json): {len(unused_files)}")
        for info in unused_files[:5]:
            print(f"  {info['slug']}: {info['title_zh'][:50]}")

    updated_entries = 0
    for entry in data.get("entries", []):
        eid = entry["id"]
        if eid in matched:
            info = matched[eid]
            slug = info["slug"]
            if entry.get("slug") != slug:
                entry["slug"] = slug
                updated_entries += 1

    if updated_entries > 0:
        if not dry_run:
            with open(index_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"\nUpdated _index.json: {updated_entries} entries got slug field")
        else:
            print(f"\nWould update _index.json: {updated_entries} entries with slug field")

    fulltext_dir = KNOWLEDGE_ROOT / "nmpa" / doc_type / "fulltext"
    if not dry_run:
        fulltext_dir.mkdir(parents=True, exist_ok=True)

    created = 0
    all_infos_to_create = list(matched.values())
    for info in unused_files:
        if info not in all_infos_to_create:
            all_infos_to_create.append(info)

    for info in all_infos_to_create:
        slug = info["slug"]
        body = info["body"]
        if not body.strip() or len(body.strip()) < 20:
            continue

        out_path = fulltext_dir / f"{slug}.md"
        if out_path.exists():
            continue

        if not dry_run:
            out_path.write_text(body, encoding="utf-8")
            created += 1
        else:
            print(f"  Would create: fulltext/{slug}.md ({info['lines']} lines)")
            created += 1

    if created:
        print(f"\n{'Created' if not dry_run else 'Would create'} {created} fulltext files in nmpa/{doc_type}/fulltext/")

    return updated_entries, created


def main():
    parser = argparse.ArgumentParser(description="Migrate NMPA fulltext to standardized pipeline")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done")
    parser.add_argument("--type", "-t", default="", help="Process specific type (regulations, guidance)")
    args = parser.parse_args()

    doc_types = ["regulations", "guidance"] if not args.type else [args.type]

    total_updated = 0
    total_created = 0

    for doc_type in doc_types:
        updated, created = process_doc_type(doc_type, dry_run=args.dry_run)
        total_updated += updated
        total_created += created

    print(f"\n{'='*60}")
    print(f"TOTAL: {total_updated} index entries updated, {total_created} fulltext files {'created' if not args.dry_run else 'would be created'}")

    for doc_type in doc_types:
        fulltext_dir = KNOWLEDGE_ROOT / "nmpa" / doc_type / "fulltext"
        if fulltext_dir.exists():
            count = len(list(fulltext_dir.glob("*.md")))
            print(f"  nmpa/{doc_type}/fulltext/: {count} files")


if __name__ == "__main__":
    main()
