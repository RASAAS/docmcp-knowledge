#!/usr/bin/env python3
"""
Fetch EU MDR Harmonised Standards from EUR-Lex

Automated pipeline:
  1. Fetch consolidated Implementing Decision 2021/1182 from EUR-Lex
  2. Parse Annex table to extract all harmonised standards
  3. Apply latest amendment (2026/193) additions
  4. Categorize standards by topic
  5. Generate category-split JSON files for data layer
  6. Generate diff report for human review

Sources:
  - Base: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02021D1182-20251020
  - Amendment: https://eur-lex.europa.eu/eli/dec_impl/2026/193/oj
  - Consolidated URL pattern: CELEX:02021D1182-{YYYYMMDD}

Usage:
    python scripts/fetch_eu_mdr_standards.py --fetch          # Fetch + parse from EUR-Lex
    python scripts/fetch_eu_mdr_standards.py --generate       # Generate JSON from cached data
    python scripts/fetch_eu_mdr_standards.py --diff           # Show diff vs current data layer
    python scripts/fetch_eu_mdr_standards.py --fetch --generate --diff  # Full pipeline
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: beautifulsoup4 not installed. Run: pip install beautifulsoup4")
    sys.exit(1)

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)

ROOT = Path(__file__).parent.parent
CACHE_DIR = ROOT / "scripts" / ".cache"
DATA_DIR = ROOT / "eu_mdr" / "standards"

# EUR-Lex URLs
CONSOLIDATED_VERSIONS = [
    # Most recent first; script tries each until one works
    "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02021D1182-20251020",
    "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02021D1182-20250409",
]
AMENDMENT_2026_193_URL = "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32026D0193"

# Category classification rules
# Each rule: (regex_pattern_for_standard_number_or_title, category_key)
CATEGORY_RULES = [
    # Quality management
    (r"13485", "quality_management"),
    # Risk management
    (r"14971|24971", "risk_management"),
    # Biocompatibility
    (r"10993|Biological evaluation", "biocompatibility"),
    # Electrical safety & EMC
    (r"60601|62353|EMC|electrical", "electrical_safety"),
    # Sterilization & packaging
    (r"11135|11137|11607|11737|13408|14160|14180|17665|25424|556-|285:|18562|Steriliz|steriliz|Aseptic|STERILE", "sterilization"),
    # Software & usability
    (r"62304|62366|IEC 82304|usability|software", "software"),
    # Labelling & symbols
    (r"15223|20417|label|symbol", "labelling"),
    # Clinical investigation
    (r"14155|clinical investigation", "clinical_investigation"),
    # Medical gloves
    (r"455-|Medical gloves", "medical_gloves"),
    # Surgical clothing & drapes
    (r"13795|14683|Surgical clothing|face mask", "surgical_textiles"),
    # Non-active surgical implants
    (r"14630|21535|21536|7197|surgical implant|neurosurgical", "surgical_implants"),
    # Patient handling
    (r"1865-|Patient handling|ambulance", "patient_handling"),
    # Connectors
    (r"80369|connector", "connectors"),
    # Processing & reprocessing
    (r"17664|Processing of health care", "processing"),
]

CATEGORY_NAMES = {
    "quality_management": {"zh": "Quality Management / Zhi Liang Guan Li", "en": "Quality Management"},
    "risk_management": {"zh": "Feng Xian Guan Li", "en": "Risk Management"},
    "biocompatibility": {"zh": "Sheng Wu Xiang Rong Xing", "en": "Biocompatibility"},
    "electrical_safety": {"zh": "Dian Qi An Quan Yu EMC", "en": "Electrical Safety & EMC"},
    "sterilization": {"zh": "Mie Jun Yu Bao Zhuang", "en": "Sterilization & Packaging"},
    "software": {"zh": "Ruan Jian Yu Ke Yong Xing", "en": "Software & Usability"},
    "labelling": {"zh": "Biao Qian Yu Shuo Ming Shu", "en": "Labelling & Symbols"},
    "clinical_investigation": {"zh": "Lin Chuang Diao Cha", "en": "Clinical Investigation"},
    "medical_gloves": {"zh": "Yi Yong Shou Tao", "en": "Medical Gloves"},
    "surgical_textiles": {"zh": "Shou Shu Yi Wu Yu Kou Zhao", "en": "Surgical Textiles & Masks"},
    "surgical_implants": {"zh": "Fei You Yuan Wai Ke Zhi Ru Wu", "en": "Non-active Surgical Implants"},
    "patient_handling": {"zh": "Huan Zhe Ban Yun She Bei", "en": "Patient Handling Equipment"},
    "connectors": {"zh": "Xiao Kou Jing Lian Jie Qi", "en": "Small-bore Connectors"},
    "processing": {"zh": "Qi Xie Chu Li Yu Zai Chu Li", "en": "Device Processing & Reprocessing"},
}


def fetch_html(url: str, cache_name: str) -> Optional[str]:
    """Fetch HTML from URL with caching."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_file = CACHE_DIR / f"{cache_name}.html"

    # Use cache if less than 24 hours old
    if cache_file.exists():
        age_hours = (datetime.now().timestamp() - cache_file.stat().st_mtime) / 3600
        if age_hours < 24:
            print(f"  Using cached: {cache_file.name} ({age_hours:.1f}h old)")
            return cache_file.read_text(encoding="utf-8")

    print(f"  Fetching: {url}")
    try:
        resp = requests.get(url, timeout=30, headers={
            "User-Agent": "Mozilla/5.0 (docmcp-knowledge-bot/2.0)",
            "Accept": "text/html",
        })
        resp.raise_for_status()
        html = resp.text
        cache_file.write_text(html, encoding="utf-8")
        print(f"  Saved to cache: {cache_file.name} ({len(html)} bytes)")
        return html
    except requests.RequestException as e:
        print(f"  ERROR fetching {url}: {e}")
        return None


def parse_annex_table(html: str) -> list[dict]:
    """Parse the Annex table from consolidated Implementing Decision HTML."""
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all("table")

    # Find the Annex table (contains numbered standard entries)
    annex_table = None
    for table in tables:
        first_row = table.find("tr")
        if first_row:
            text = first_row.get_text(strip=True)
            if "No" in text and ("Reference" in text or "standard" in text.lower()):
                annex_table = table
                break

    if not annex_table:
        # Fallback: find table with most rows containing EN ISO/IEC references
        best_table = None
        best_count = 0
        for table in tables:
            count = sum(1 for row in table.find_all("tr")
                        if re.search(r"EN\s+(ISO|IEC|\d)", row.get_text()))
            if count > best_count:
                best_count = count
                best_table = table
        annex_table = best_table

    if not annex_table:
        print("ERROR: Could not find Annex table in HTML")
        return []

    standards = []
    rows = annex_table.find_all("tr")
    for row in rows[1:]:  # Skip header
        cells = row.find_all("td")
        if len(cells) < 2:
            continue

        row_num = cells[0].get_text(strip=True)
        full_text = cells[1].get_text("\n", strip=True)

        # Split into lines: first line is standard number, rest is title
        lines = [l.strip() for l in full_text.split("\n") if l.strip()]
        if not lines:
            continue

        std_number = lines[0]
        # Check if this looks like a standard number
        if not re.match(r"EN\s", std_number):
            continue

        title_lines = lines[1:]
        # Separate amendments listed in the same cell
        amendments = []
        title_parts = []
        for line in title_lines:
            if re.match(r"EN\s+(ISO|IEC|\d)", line):
                amendments.append(line)
            else:
                title_parts.append(line)

        title = " ".join(title_parts)
        entry = {
            "number": std_number,
            "title": title,
            "row_number": row_num.rstrip("."),
        }
        if amendments:
            entry["amendments"] = amendments

        standards.append(entry)

    return standards


def parse_amendment_additions(html: str) -> list[dict]:
    """Parse 2026/193 amendment to extract new standard entries."""
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()

    # Find "the following entries are added" section
    additions = []
    # Match standard references in the amendment text
    pattern = r"(EN\s+(?:ISO|IEC)\s+[\d\-]+(?::[\d]+)?(?:/A\d+:[\d]+)?)"
    matches = re.findall(pattern, text)

    # Remove duplicates while preserving order
    seen = set()
    for match in matches:
        if match not in seen:
            seen.add(match)
            additions.append(match)

    return additions


def classify_standard(entry: dict) -> str:
    """Classify a standard into a category based on number and title."""
    search_text = f"{entry['number']} {entry.get('title', '')}"
    for pattern, category in CATEGORY_RULES:
        if re.search(pattern, search_text, re.IGNORECASE):
            return category
    return "other"


def fetch_and_parse(args) -> list[dict]:
    """Step 1: Fetch from EUR-Lex and parse standards list."""
    print("\n=== Step 1: Fetching consolidated Implementing Decision 2021/1182 ===")

    html = None
    for url in CONSOLIDATED_VERSIONS:
        html = fetch_html(url, "consolidated_2021_1182")
        if html:
            break

    if not html:
        print("ERROR: Could not fetch any consolidated version")
        return []

    standards = parse_annex_table(html)
    print(f"  Parsed {len(standards)} standards from consolidated version")

    # Step 2: Fetch and apply 2026/193 amendment
    print("\n=== Step 2: Checking 2026/193 amendment ===")
    amend_html = fetch_html(AMENDMENT_2026_193_URL, "amendment_2026_193")
    if amend_html:
        new_stds = parse_amendment_additions(amend_html)
        existing_numbers = {s["number"] for s in standards}
        added = 0
        for std_num in new_stds:
            if std_num not in existing_numbers:
                # Check if this is an amendment to an existing standard
                is_amendment = "/A" in std_num
                if is_amendment:
                    # Find base standard and add as amendment
                    base = re.match(r"(EN\s+(?:ISO|IEC)\s+[\d\-]+(?::[\d]+)?)", std_num)
                    if base:
                        base_num = base.group(1)
                        for s in standards:
                            if s["number"] == base_num:
                                if "amendments" not in s:
                                    s["amendments"] = []
                                if std_num not in s["amendments"]:
                                    s["amendments"].append(std_num)
                                break
                else:
                    standards.append({
                        "number": std_num,
                        "title": "",  # Title needs manual review
                        "row_number": str(len(standards) + 1),
                        "source": "2026/193",
                        "needs_review": True,
                    })
                    added += 1
        print(f"  2026/193: {added} new standards added, amendments updated")
    else:
        print("  WARNING: Could not fetch 2026/193 amendment")

    # Classify all standards
    for s in standards:
        s["category"] = classify_standard(s)

    # Save raw parsed data
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    raw_file = CACHE_DIR / "parsed_standards.json"
    with open(raw_file, "w", encoding="utf-8") as f:
        json.dump({
            "fetched_at": datetime.now().isoformat(),
            "source": "EUR-Lex Implementing Decision 2021/1182 (consolidated)",
            "amendment": "2026/193",
            "total_count": len(standards),
            "standards": standards,
        }, f, indent=2, ensure_ascii=False)
    print(f"\n  Raw data saved: {raw_file} ({len(standards)} standards)")

    return standards


def generate_json(standards: list[dict]):
    """Step 3: Generate category-split JSON files for data layer."""
    print("\n=== Step 3: Generating data layer JSON files ===")

    if not standards:
        standards = _load_from_cache()
        if not standards:
            return

    # Classify all standards (in case loaded from cache without classification)
    for s in standards:
        if "category" not in s or s["category"] == "other":
            s["category"] = classify_standard(s)

    # Group by category
    categories = {}
    for s in standards:
        cat = s.get("category", "other")
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(s)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d")

    # Generate per-category files
    for cat_key, cat_standards in sorted(categories.items()):
        cat_name = CATEGORY_NAMES.get(cat_key, {"en": cat_key, "zh": cat_key})
        entries = []
        for s in cat_standards:
            entry = {
                "id": f"eu_mdr-hs-{s['number'].replace(' ', '-').replace(':', '-').replace('/', '-').lower()}",
                "number": s["number"],
                "title": s.get("title", ""),
                "scope": "eu_mdr",
                "status": "active",
                "source_url": "https://eur-lex.europa.eu/eli/dec_impl/2021/1182",
                "source_verified": now,
                "category": cat_key,
            }
            if s.get("amendments"):
                entry["amendments"] = s["amendments"]
            if s.get("needs_review"):
                entry["needs_review"] = True
            entries.append(entry)

        output = {
            "category": cat_key,
            "category_name": cat_name,
            "regulation": "eu_mdr",
            "source": "Implementing Decision (EU) 2021/1182 (consolidated)",
            "source_url": "https://eur-lex.europa.eu/eli/dec_impl/2021/1182",
            "last_updated": now,
            "count": len(entries),
            "entries": entries,
        }

        out_file = DATA_DIR / f"standards-{cat_key}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        print(f"  {out_file.name}: {len(entries)} standards")

    # Generate _index.json
    index = {
        "directory": "eu_mdr/standards",
        "description": "EU MDR Harmonised Standards (Implementing Decision 2021/1182)",
        "source_url": "https://eur-lex.europa.eu/eli/dec_impl/2021/1182",
        "latest_amendment": "2026/193",
        "latest_amendment_url": "https://eur-lex.europa.eu/eli/dec_impl/2026/193/oj",
        "last_updated": now,
        "total_standards": len(standards),
        "categories": {
            cat_key: {
                "name": CATEGORY_NAMES.get(cat_key, {"en": cat_key}),
                "count": len(cat_stds),
                "file": f"standards-{cat_key}.json",
            }
            for cat_key, cat_stds in sorted(categories.items())
        },
    }
    index_file = DATA_DIR / "_index.json"
    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    print(f"  _index.json: {len(categories)} categories, {len(standards)} total")


def _load_from_cache() -> list[dict]:
    """Load standards from cache file."""
    raw_file = CACHE_DIR / "parsed_standards.json"
    if raw_file.exists():
        with open(raw_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            standards = data["standards"]
        print(f"  Loaded {len(standards)} standards from cache")
        return standards
    print("ERROR: No standards data. Run with --fetch first.")
    return []


def show_diff(standards: list[dict]):
    """Step 4: Compare fetched data with current data layer."""
    print("\n=== Step 4: Diff vs current data layer ===")

    if not standards:
        standards = _load_from_cache()
        if not standards:
            return

    # Classify for display
    for s in standards:
        if "category" not in s or s["category"] == "other":
            s["category"] = classify_standard(s)

    # Load current data layer
    current_standards = {}
    for json_file in DATA_DIR.glob("standards-*.json"):
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            for entry in data.get("entries", []):
                current_standards[entry["number"]] = entry

    fetched_numbers = {s["number"] for s in standards}
    current_numbers = set(current_standards.keys())

    added = fetched_numbers - current_numbers
    removed = current_numbers - fetched_numbers
    common = fetched_numbers & current_numbers

    print(f"\n  Current data layer: {len(current_numbers)} standards")
    print(f"  Fetched from EUR-Lex: {len(fetched_numbers)} standards")
    print(f"  ---")
    print(f"  New (to add): {len(added)}")
    print(f"  Removed (to delete): {len(removed)}")
    print(f"  Common (to verify): {len(common)}")

    if added:
        print(f"\n  +++ NEW STANDARDS ({len(added)}):")
        for num in sorted(added):
            s = next((x for x in standards if x["number"] == num), {})
            cat = s.get("category", "?")
            review = " [NEEDS REVIEW]" if s.get("needs_review") else ""
            print(f"    + {num} [{cat}]{review}")
            if s.get("title"):
                print(f"      {s['title'][:100]}")

    if removed:
        print(f"\n  --- REMOVED STANDARDS ({len(removed)}):")
        for num in sorted(removed):
            print(f"    - {num}")

    needs_review = [s for s in standards if s.get("needs_review")]
    if needs_review:
        print(f"\n  !!! NEEDS HUMAN REVIEW ({len(needs_review)}):")
        for s in needs_review:
            print(f"    ! {s['number']} - title missing or from amendment")

    # Generate review report
    report = {
        "generated_at": datetime.now().isoformat(),
        "current_count": len(current_numbers),
        "fetched_count": len(fetched_numbers),
        "added": sorted(added),
        "removed": sorted(removed),
        "needs_review": [s["number"] for s in needs_review],
        "status": "READY" if not needs_review else "NEEDS_REVIEW",
    }
    report_file = CACHE_DIR / "diff_report.json"
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\n  Diff report saved: {report_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch EU MDR Harmonised Standards from EUR-Lex"
    )
    parser.add_argument("--fetch", action="store_true",
                        help="Fetch and parse from EUR-Lex")
    parser.add_argument("--generate", action="store_true",
                        help="Generate data layer JSON files")
    parser.add_argument("--diff", action="store_true",
                        help="Show diff vs current data layer")
    args = parser.parse_args()

    if not any([args.fetch, args.generate, args.diff]):
        parser.print_help()
        sys.exit(0)

    standards = []

    if args.fetch:
        standards = fetch_and_parse(args)

    if args.generate:
        generate_json(standards)

    if args.diff:
        show_diff(standards)

    print("\nDone.")


if __name__ == "__main__":
    main()
