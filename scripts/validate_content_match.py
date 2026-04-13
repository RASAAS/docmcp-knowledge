#!/usr/bin/env python3
"""CI gate: validate that all fulltext files match their index titles.

Detects two types of mismatches:
1. True mismatch: content is about a completely different topic
2. Attachment mismatch: title is in the header but body is a different
   guidance document (NMPA multi-attachment pattern)

Exit code 0 = all OK, exit code 1 = mismatches found.

Usage:
    python scripts/validate_content_match.py
    python scripts/validate_content_match.py --changed-only
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
INDEX_PATH = ROOT / "nmpa" / "guidance" / "_index.json"
FULLTEXT_DIR = ROOT / "nmpa" / "guidance" / "fulltext"

sys.path.insert(0, str(ROOT / "scripts"))
from fetch_nmpa_fulltext import (  # noqa: E402
    content_matches_title,
    is_catalog_content,
    is_draft_content,
)


def _get_changed_slugs() -> set[str] | None:
    """Get slugs for fulltext files changed in this PR (git diff vs base)."""
    base_ref = os.environ.get("GITHUB_BASE_REF", "")
    if not base_ref:
        return None

    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", f"origin/{base_ref}...HEAD"],
            capture_output=True, text=True, cwd=str(ROOT),
        )
        if result.returncode != 0:
            return None

        slugs = set()
        for line in result.stdout.strip().split('\n'):
            line = line.strip()
            if line.startswith("nmpa/guidance/fulltext/") and line.endswith(".md"):
                fname = line.split("/")[-1]
                if not fname.endswith(".en.md"):
                    slugs.add(fname[:-3])
        return slugs
    except Exception:
        return None


def main():
    parser = argparse.ArgumentParser(description="Validate fulltext-title consistency")
    parser.add_argument("--changed-only", action="store_true",
                        help="Only check files changed in this PR")
    args = parser.parse_args()

    if not INDEX_PATH.exists():
        print("Index not found, skipping validation")
        return

    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    entries = data.get("entries", [])
    slug_to_entry = {}
    for e in entries:
        s = e.get("slug", "")
        if s:
            slug_to_entry[s] = e

    changed_slugs = None
    if args.changed_only:
        changed_slugs = _get_changed_slugs()
        if changed_slugs is not None:
            print(f"Checking {len(changed_slugs)} changed fulltext files")
        else:
            print("Could not determine changed files, checking all")

    mismatches = []
    checked = 0

    for slug, entry in slug_to_entry.items():
        if changed_slugs is not None and slug not in changed_slugs:
            continue

        fp = FULLTEXT_DIR / f"{slug}.md"
        if not fp.exists():
            continue

        content = fp.read_text(encoding="utf-8", errors="replace")
        body = content
        sep = content.find("\n---\n")
        if sep >= 0:
            body = content[sep + 5:]

        if not body or len(body) < 200:
            continue

        checked += 1
        title_zh = entry.get("title", {}).get("zh", "")

        if is_catalog_content(body):
            mismatches.append((slug, title_zh, "catalog"))
            continue

        if is_draft_content(body):
            mismatches.append((slug, title_zh, "draft"))
            continue

        if not content_matches_title(body, title_zh):
            mismatches.append((slug, title_zh, "title_mismatch"))

    print(f"\nChecked {checked} fulltext files")

    if mismatches:
        print(f"\nFOUND {len(mismatches)} issue(s):\n")
        for slug, title, reason in mismatches:
            print(f"  [{reason}] {slug}.md")
            print(f"    Title: {title[:60]}")
            print()
        sys.exit(1)
    else:
        print("All fulltext files match their index titles.")


if __name__ == "__main__":
    main()
