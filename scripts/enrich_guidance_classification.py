#!/usr/bin/env python3
"""
Enrich NMPA guidance _index.json with classification codes.

Strategy (accuracy-first):
1. HIGH confidence: Extract XX-YY / XX-YY-ZZ codes from keyword context in ZH text,
   then validate against classification_catalog.json
2. MEDIUM confidence: Extract codes from slug/filename if they match catalog
3. CROSS-CUTTING: Mark general/guidance/naming/review_point as scope="cross_cutting"
4. NO ASSOCIATION: Leave classification_codes=[] for entries without reliable signals

Output: updated _index.json with new fields:
  - classification_codes: list of validated codes (L2 or L3)
  - classification_confidence: "high" | "medium" | "cross_cutting" | "none"
  - classification_l1_codes: list of L1 codes (derived from classification_codes)
"""

import json
import os
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
GUIDANCE_DIR = REPO_ROOT / "nmpa" / "guidance"
CATALOG_PATH = REPO_ROOT / "nmpa" / "classification" / "classification_catalog.json"
INDEX_PATH = GUIDANCE_DIR / "_index.json"

CROSS_CUTTING_CATEGORIES = {"general", "guidance", "naming", "review_point"}

KW_PATTERN = re.compile(
    r"(?:分类编码|产品编码|产品分类|管理类别代号|类别代号|分类代号|注册分类|"
    r"分类目录|一级产品类别|二级产品类别|品名举例|所属分类|类代号|属于.*?分类)"
    r"[^\n]{0,60}?"
    r"(\d{2}-\d{2}(?:-\d{2})?)",
    re.MULTILINE,
)

BROAD_PATTERN = re.compile(r"\b(\d{2}-\d{2}(?:-\d{2})?)\b")

SLUG_CODE_PATTERN = re.compile(r"(?:^|-)(\d{2}-\d{2}(?:-\d{2})?)(?:-|$)")


def load_valid_codes(catalog_path: Path) -> tuple[set, set, dict]:
    """Load valid L2 and L3 codes from classification catalog.
    Returns (valid_l2, valid_l3, l3_to_l1_map)
    """
    with open(catalog_path, encoding="utf-8") as f:
        catalog = json.load(f)

    valid_l2 = set()
    valid_l3 = set()
    code_to_l1 = {}

    for item in catalog.get("items", []):
        l2 = item.get("l2_code", "")
        l3 = item.get("code", "")
        l1 = item.get("l1_code", "")
        if l2:
            valid_l2.add(l2)
            code_to_l1[l2] = l1
        if l3:
            valid_l3.add(l3)
            code_to_l1[l3] = l1

    return valid_l2, valid_l3, code_to_l1


def _remove_substring_false_positives(codes: set, text: str, valid_l3: set) -> set:
    """Remove L2 codes that only appear as substrings of L3 codes in the text.

    Problem 1 (tail): text has '02-06-01', broad match picks up '06-01' (valid L2).
    Problem 2 (middle): text has '08-05-04', broad match picks up '05-04' (valid L2)
      because regex \b treats '-' as a non-word char, making \b05 match after '-'.

    Solution: For each candidate L2 code, verify it appears at least once NOT as part
    of a longer XX-YY-ZZ pattern in the raw text.
    """
    cleaned = set()
    for c in codes:
        parts = c.split("-")
        if len(parts) == 2:
            # L2 code: check if every occurrence is part of a longer L3 pattern
            # Search for standalone occurrences: not preceded by \d\d- and not followed by -\d\d
            standalone_pattern = re.compile(
                r"(?<!\d-)" + re.escape(c) + r"(?!-\d{2}\b)"
            )
            if not standalone_pattern.search(text):
                continue
        cleaned.add(c)
    return cleaned


def extract_codes_from_text(text: str, valid_l2: set, valid_l3: set) -> tuple[set, set]:
    """Extract classification codes from text using keyword context and broad matching.
    Returns (high_confidence_codes, medium_confidence_codes)
    """
    kw_codes = set(KW_PATTERN.findall(text))
    validated_kw = {c for c in kw_codes if c in valid_l2 or c in valid_l3}
    validated_kw = _remove_substring_false_positives(validated_kw, text, valid_l3)

    broad_codes = set(BROAD_PATTERN.findall(text))
    validated_broad = {c for c in broad_codes if c in valid_l2 or c in valid_l3}
    validated_broad = _remove_substring_false_positives(validated_broad, text, valid_l3)

    high = validated_kw
    medium = validated_broad - validated_kw
    return high, medium


def extract_codes_from_slug(slug: str, valid_l2: set, valid_l3: set) -> set:
    """Extract classification codes embedded in the slug/filename."""
    matches = SLUG_CODE_PATTERN.findall(slug)
    return {m for m in matches if m in valid_l2 or m in valid_l3}


def derive_l1_codes(codes: list[str], code_to_l1: dict) -> list[str]:
    """Derive unique L1 codes from a list of L2/L3 codes."""
    l1s = set()
    for c in codes:
        l1 = code_to_l1.get(c)
        if l1:
            l1s.add(l1)
    return sorted(l1s)


def main():
    dry_run = "--dry-run" in sys.argv

    valid_l2, valid_l3, code_to_l1 = load_valid_codes(CATALOG_PATH)
    print(f"Loaded catalog: {len(valid_l2)} L2 codes, {len(valid_l3)} L3 codes")

    with open(INDEX_PATH, encoding="utf-8") as f:
        index = json.load(f)

    zh_files = {
        f.replace(".zh.md", ""): GUIDANCE_DIR / f
        for f in os.listdir(GUIDANCE_DIR)
        if f.endswith(".zh.md")
    }
    print(f"Found {len(zh_files)} ZH guidance files")

    stats = {"high": 0, "medium": 0, "cross_cutting": 0, "none": 0}

    for entry in index["entries"]:
        slug = entry.get("slug", "")
        category = entry.get("category", "")

        all_codes = set()
        confidence = "none"

        if category in CROSS_CUTTING_CATEGORIES:
            confidence = "cross_cutting"
        else:
            high_codes = set()
            medium_codes = set()

            if slug in zh_files:
                zh_path = zh_files[slug]
                with open(zh_path, encoding="utf-8") as f:
                    text = f.read()
                h, m = extract_codes_from_text(text, valid_l2, valid_l3)
                high_codes.update(h)
                medium_codes.update(m)

            slug_codes = extract_codes_from_slug(slug, valid_l2, valid_l3)
            if slug_codes:
                medium_codes.update(slug_codes)

            if high_codes:
                all_codes = high_codes | medium_codes
                confidence = "high"
            elif medium_codes:
                all_codes = medium_codes
                confidence = "medium"

        sorted_codes = sorted(all_codes)
        l1_codes = derive_l1_codes(sorted_codes, code_to_l1) if sorted_codes else []

        entry["classification_codes"] = sorted_codes
        entry["classification_l1_codes"] = l1_codes
        entry["classification_confidence"] = confidence

        stats[confidence] += 1

    print(f"\n=== Results ===")
    print(f"  High confidence: {stats['high']}")
    print(f"  Medium confidence: {stats['medium']}")
    print(f"  Cross-cutting: {stats['cross_cutting']}")
    print(f"  No association: {stats['none']}")
    print(f"  Total: {sum(stats.values())}")

    if dry_run:
        print("\n[DRY RUN] Showing samples:")
        for conf in ["high", "medium", "cross_cutting", "none"]:
            samples = [
                e for e in index["entries"]
                if e.get("classification_confidence") == conf
            ][:3]
            for s in samples:
                title = s.get("title", {})
                if isinstance(title, dict):
                    title = title.get("zh", "") or title.get("en", "")
                print(
                    f"  [{conf}] {title[:50]} -> "
                    f"codes={s['classification_codes']}, l1={s['classification_l1_codes']}"
                )
    else:
        with open(INDEX_PATH, "w", encoding="utf-8") as f:
            json.dump(index, f, ensure_ascii=False, indent=2)
        print(f"\nWrote updated _index.json")


if __name__ == "__main__":
    main()
