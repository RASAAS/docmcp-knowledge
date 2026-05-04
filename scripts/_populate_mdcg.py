#!/usr/bin/env python3
"""
One-time script to populate MDCG _index.json from the official EC guidance page.
Merges existing entries with new ones parsed from the EC page.
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: requests not installed")
    sys.exit(1)

ROOT = Path(__file__).parent.parent
INDEX_PATH = ROOT / "eu_mdr" / "mdcg" / "_index.json"

MDCG_URL = (
    "https://health.ec.europa.eu/medical-devices-sector/"
    "new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en"
)

# Category mapping based on section headers in the page
SECTION_CATEGORIES = {
    "annex xvi": "annex_xvi",
    "borderline and classification": "classification",
    "class i devices": "class_i",
    "clinical investigation": "clinical_evaluation",
    "clinical evaluation": "clinical_evaluation",
    "performance studies": "clinical_evaluation",
    "covid-19": "covid19",
    "custom-made": "custom_made",
    "eudamed": "eudamed",
    "european medical device nomenclature": "emdn",
    "emdn": "emdn",
    "implant card": "implant_cards",
    "in-house": "in_house",
    "authorised representative": "importers_distributors",
    "importers": "importers_distributors",
    "distributors": "importers_distributors",
    "article 10a": "supply_interruption",
    "in vitro diagnostic": "ivd",
    "ivd": "ivd",
    "new technologies": "new_technologies",
    "notified bod": "notified_bodies",
    "person responsible": "prrc",
    "prrc": "prrc",
    "post-market": "pmsv",
    "vigilance": "pmsv",
    "pmsv": "pmsv",
    "standards": "standards",
    "unique device identifier": "udi",
    "udi": "udi",
    "other topic": "other",
    "other guidance": "other",
}

MONTHS = {
    "january": "01", "february": "02", "march": "03", "april": "04",
    "may": "05", "june": "06", "july": "07", "august": "08",
    "september": "09", "october": "10", "november": "11", "december": "12",
}


def parse_ec_page(html: str) -> list[dict]:
    """Parse EC MDCG guidance page HTML and extract structured entries.

    The EC page uses <tr class="ecl-table__row"> with cells:
      - data-ecl-table-header="Reference" : MDCG ref + download link
      - data-ecl-table-header="Title" : document title
      - data-ecl-table-header="Publication" : publication date
    """
    entries = []
    seen_ids = set()

    # Detect section headers (h2/h3) to determine category
    # Split by section headers and track which section each table row belongs to
    section_positions = []
    for m in re.finditer(r'<h[23][^>]*>(.*?)</h[23]>', html, re.DOTALL):
        header_text = re.sub(r'<[^>]+>', '', m.group(1)).strip().lower()
        cat = "other"
        for key, mapped_cat in SECTION_CATEGORIES.items():
            if key in header_text:
                cat = mapped_cat
                break
        section_positions.append((m.start(), cat))

    def get_category_at(pos: int) -> str:
        cat = "other"
        for sec_pos, sec_cat in section_positions:
            if sec_pos <= pos:
                cat = sec_cat
            else:
                break
        return cat

    # Parse table rows
    row_re = re.compile(r"<tr[^>]*class=\"ecl-table__row\"[^>]*>(.*?)</tr>", re.DOTALL)
    cell_re = re.compile(
        r'<td[^>]*data-ecl-table-header="(\w+)"[^>]*>(.*?)</td>', re.DOTALL
    )
    mdcg_re = re.compile(
        r"MDCG\s+(\d{4})[-\u2013](\d+)(?:[-/](\d+))?"
        r"(?:\s*[-\s]*?(?:[Rr]ev\.?\s*(\d+)|v(\d+)|ADD\.?\s*(\d+)))?",
        re.IGNORECASE,
    )
    date_re = re.compile(
        r"(January|February|March|April|May|June|July|August|"
        r"September|October|November|December)\s*(\d{4})",
        re.IGNORECASE,
    )

    for row_match in row_re.finditer(html):
        row_html = row_match.group(1)
        cells = {}
        for cell_match in cell_re.finditer(row_html):
            header = cell_match.group(1)
            content = cell_match.group(2)
            cells[header] = content

        ref_html = cells.get("Reference", "")
        title_html = cells.get("Title", "")
        pub_html = cells.get("Publication", "")

        # Extract MDCG ID
        mdcg_match = mdcg_re.search(ref_html)
        if not mdcg_match:
            continue

        year, num = mdcg_match.group(1), mdcg_match.group(2)
        sub_num = mdcg_match.group(3)
        rev_num = mdcg_match.group(4) or mdcg_match.group(5) or ""
        add_num = mdcg_match.group(6) or ""

        base_id = f"mdcg-{year}-{num}"
        if sub_num:
            base_id += f"-{sub_num}"

        if base_id in seen_ids:
            continue
        seen_ids.add(base_id)

        revision = ""
        if rev_num:
            revision = f"rev.{rev_num}"
        elif add_num:
            revision = f"ADD.{add_num}"

        # Extract title (strip HTML tags)
        title_text = re.sub(r'<[^>]+>', '', title_html).strip()

        # Build English title with reference
        ref_str = f"MDCG {year}-{num}"
        if sub_num:
            ref_str += f"-{sub_num}"
        if revision:
            ref_str += f" {revision}"

        if title_text:
            en_title = f"{ref_str}: {title_text}"
        else:
            en_title = ref_str

        # Parse publication date
        pub_text = re.sub(r'<[^>]+>', '', pub_html).strip()
        published_date = ""
        dm = date_re.search(pub_text)
        if dm:
            month = MONTHS.get(dm.group(1).lower(), "01")
            published_date = f"{dm.group(2)}-{month}-01"

        # Extract source URL
        source_url = ""
        url_match = re.search(r'href="([^"]+)"', ref_html)
        if url_match:
            source_url = url_match.group(1)
            if source_url.startswith("/"):
                source_url = f"https://health.ec.europa.eu{source_url}"

        # Determine category from section position
        current_category = get_category_at(row_match.start())

        entry = {
            "id": base_id,
            "title": {
                "zh": "",
                "en": en_title,
            },
            "slug": base_id,
            "status": "active",
            "source_url": source_url,
            "source_url_verified": datetime.now().strftime("%Y-%m-%d"),
            "published_date": published_date,
            "category": "eu_mdr/mdcg",
            "mdcg_category": current_category,
        }
        if revision:
            entry["revision"] = revision

        entries.append(entry)

    return entries


def main():
    print(f"Fetching EC MDCG guidance page...")
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0 (docmcp-knowledge-bot/2.0)"})
    resp = session.get(MDCG_URL, timeout=30)
    resp.raise_for_status()
    print(f"  Page fetched ({len(resp.text)} chars)")

    new_entries = parse_ec_page(resp.text)
    print(f"  Parsed {len(new_entries)} unique MDCG entries from page")

    # Load existing index
    existing = {}
    if INDEX_PATH.exists():
        with open(INDEX_PATH) as f:
            data = json.load(f)
        for e in data.get("entries", []):
            existing[e["id"]] = e
        print(f"  Existing index has {len(existing)} entries")

    # Merge: existing entries take precedence (they may have Chinese titles, verified URLs, etc.)
    merged = dict(existing)
    new_count = 0
    updated_count = 0

    for entry in new_entries:
        eid = entry["id"]
        if eid not in merged:
            merged[eid] = entry
            new_count += 1
        else:
            # Update revision if the new entry has one and existing doesn't
            if entry.get("revision") and not merged[eid].get("revision"):
                merged[eid]["revision"] = entry["revision"]
                updated_count += 1
            # Update source_url if existing has none
            if entry.get("source_url") and not merged[eid].get("source_url"):
                merged[eid]["source_url"] = entry["source_url"]
                merged[eid]["source_url_verified"] = entry["source_url_verified"]
            # Update published_date if existing has none
            if entry.get("published_date") and not merged[eid].get("published_date"):
                merged[eid]["published_date"] = entry["published_date"]

    # Sort by ID (year desc, number desc)
    def sort_key(e):
        m = re.match(r"mdcg-(\d{4})-(\d+)", e["id"])
        if m:
            return (-int(m.group(1)), -int(m.group(2)))
        return (0, 0)

    sorted_entries = sorted(merged.values(), key=sort_key)

    # Write output
    output = {
        "category": "eu_mdr/mdcg",
        "description": "MDCG guidance documents for EU MDR 2017/745 and EU IVDR 2017/746",
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "count": len(sorted_entries),
        "entries": sorted_entries,
    }

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n  Result: {len(sorted_entries)} total entries "
          f"({new_count} new, {updated_count} updated, {len(existing)} preserved)")
    print(f"  Written to: {INDEX_PATH}")


if __name__ == "__main__":
    main()
