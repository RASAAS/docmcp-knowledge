#!/usr/bin/env python3
"""
Add missing ISO/IEC counterparts to other-standards for EN ISO/EN IEC harmonised standards.
Each harmonised standard (EN ISO xxx) should have a corresponding international standard (ISO xxx)
in the other-standards categories.
"""

import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HS_DIR = REPO / "eu_mdr" / "standards"
OS_DIR = REPO / "eu_mdr" / "other_standards"

# Mapping: (EN_number) -> (target_other_category, iso_source_url)
# URLs need to be looked up from ISO/IEC websites
MISSING_STANDARDS = [
    {
        "en_number": "EN ISO 10993-4:2017",
        "target_cat": "biocompatibility",
        "iso_url": "https://www.iso.org/standard/63448.html",
        "note": "ISO 10993-4:2017"
    },
    {
        "en_number": "EN ISO 10993-5:2009",
        "target_cat": "biocompatibility",
        "iso_url": "https://www.iso.org/standard/36406.html",
        "note": "ISO 10993-5:2009"
    },
    {
        "en_number": "EN ISO 10993-9:2021",
        "target_cat": "biocompatibility",
        "iso_url": "https://www.iso.org/standard/64580.html",
        "note": "ISO 10993-9:2019 (EN adopted as 2021)"
    },
    {
        "en_number": "EN ISO 10993-10:2023",
        "target_cat": "biocompatibility",
        "iso_url": "https://www.iso.org/standard/75279.html",
        "note": "ISO 10993-10:2021 (EN adopted as 2023)"
    },
    {
        "en_number": "EN ISO 10993-12:2021",
        "target_cat": "biocompatibility",
        "iso_url": "https://www.iso.org/standard/75769.html",
        "note": "ISO 10993-12:2021"
    },
    {
        "en_number": "EN ISO 10993-15:2023",
        "target_cat": "biocompatibility",
        "iso_url": "https://www.iso.org/standard/64583.html",
        "note": "ISO 10993-15:2019 (EN adopted as 2023)"
    },
    {
        "en_number": "EN ISO 10993-17:2023",
        "target_cat": "biocompatibility",
        "iso_url": "https://www.iso.org/standard/80072.html",
        "note": "ISO 10993-17:2023"
    },
    {
        "en_number": "EN ISO 10993-18:2020",
        "target_cat": "biocompatibility",
        "iso_url": "https://www.iso.org/standard/64750.html",
        "note": "ISO 10993-18:2020"
    },
    {
        "en_number": "EN ISO 10993-23:2021",
        "target_cat": "biocompatibility",
        "iso_url": "https://www.iso.org/standard/74151.html",
        "note": "ISO 10993-23:2021"
    },
    {
        "en_number": "EN ISO 80369-2:2024",
        "target_cat": "connectors",
        "iso_url": "https://www.iso.org/standard/83056.html",
        "note": "ISO 80369-2:2024"
    },
    {
        "en_number": "EN IEC 60118-0:2024",
        "target_cat": "audiology",
        "iso_url": "https://webstore.iec.ch/en/publication/68736",
        "note": "IEC 60118-0:2024"
    },
    {
        "en_number": "EN ISO 13408-1:2024",
        "target_cat": "sterilization",
        "iso_url": "https://www.iso.org/standard/81899.html",
        "note": "ISO 13408-1:2023 (EN adopted as 2024)"
    },
    {
        "en_number": "EN ISO 13408-6:2021",
        "target_cat": "sterilization",
        "iso_url": "https://www.iso.org/standard/77547.html",
        "note": "ISO 13408-6:2021"
    },
    {
        "en_number": "EN ISO 14160:2021",
        "target_cat": "sterilization",
        "iso_url": "https://www.iso.org/standard/75213.html",
        "note": "ISO 14160:2020 (EN adopted as 2021)"
    },
    {
        "en_number": "EN ISO 25424:2019",
        "target_cat": "sterilization",
        "iso_url": "https://www.iso.org/standard/69545.html",
        "note": "ISO 25424:2018 (EN adopted as 2019)"
    },
    {
        "en_number": "EN ISO 14630:2024",
        "target_cat": "surgical_implants",
        "iso_url": "https://www.iso.org/standard/84371.html",
        "note": "ISO 14630:2024"
    },
    {
        "en_number": "EN ISO 21535:2024",
        "target_cat": "surgical_implants",
        "iso_url": "https://www.iso.org/standard/82019.html",
        "note": "ISO 21535:2023 (EN adopted as 2024)"
    },
    {
        "en_number": "EN ISO 21536:2024",
        "target_cat": "surgical_implants",
        "iso_url": "https://www.iso.org/standard/82016.html",
        "note": "ISO 21536:2023 (EN adopted as 2024)"
    },
    {
        "en_number": "EN ISO 12870:2025",
        "target_cat": "ophthalmic",
        "iso_url": "https://www.iso.org/standard/84282.html",
        "note": "ISO 12870:2024 (EN adopted as 2025)"
    },
    {
        "en_number": "EN ISO 14607:2025",
        "target_cat": "surgical_implants",
        "iso_url": "https://www.iso.org/standard/82543.html",
        "note": "ISO 14607:2024 (EN adopted as 2025)"
    },
    {
        "en_number": "EN ISO 15883-1:2025",
        "target_cat": "reprocessing",
        "iso_url": "https://www.iso.org/standard/81647.html",
        "note": "ISO 15883-1:2024 (EN adopted as 2025)"
    },
    {
        "en_number": "EN ISO 15883-2:2025",
        "target_cat": "reprocessing",
        "iso_url": "https://www.iso.org/standard/81648.html",
        "note": "ISO 15883-2:2024 (EN adopted as 2025)"
    },
    {
        "en_number": "EN ISO 15883-3:2025",
        "target_cat": "reprocessing",
        "iso_url": "https://www.iso.org/standard/81649.html",
        "note": "ISO 15883-3:2024 (EN adopted as 2025)"
    },
    {
        "en_number": "EN ISO 22675:2025",
        "target_cat": "physiotherapy",
        "iso_url": "https://www.iso.org/standard/83696.html",
        "note": "ISO 22675:2024 (EN adopted as 2025)"
    },
    {
        "en_number": "EN ISO 23908:2025",
        "target_cat": "needles_syringes",
        "iso_url": "https://www.iso.org/standard/84236.html",
        "note": "ISO 23908:2024 (EN adopted as 2025)"
    },
]


def main():
    # Read harmonised standards for full metadata
    harmonised = {}
    for jf in sorted(HS_DIR.glob("standards-*.json")):
        data = json.loads(jf.read_text())
        for s in data.get("standards", []):
            harmonised[s["number"]] = s

    changes = []

    for item in MISSING_STANDARDS:
        en_num = item["en_number"]
        target_cat = item["target_cat"]
        iso_url = item["iso_url"]

        if en_num not in harmonised:
            print(f"  [SKIP] {en_num} not found in harmonised standards")
            continue

        hs_data = harmonised[en_num]

        # Derive ISO number
        iso_num = en_num.replace("EN ISO ", "ISO ").replace("EN IEC ", "IEC ")

        # Build new entry
        new_entry = {
            "id": "iso-" + iso_num.lower().replace(" ", "-").replace(":", "-").replace("/", "-").replace("+", "-"),
            "number": iso_num,
            "title": hs_data.get("title", {}),
            "status": "active",
            "applicable_gsprs": hs_data.get("applicable_gsprs", []),
            "standard_type": "non_harmonised",
            "source_url": iso_url,
            "source_verified": "2026-06-27",
            "note": f"International version of harmonised standard {en_num}"
        }

        # Load target category JSON
        target_file = OS_DIR / f"standards-{target_cat}.json"
        if not target_file.exists():
            print(f"  [ERROR] Target file not found: {target_file}")
            continue

        data = json.loads(target_file.read_text())
        standards = data.get("standards", [])

        # Check if already exists
        existing_nums = [s["number"] for s in standards]
        if iso_num in existing_nums:
            print(f"  [SKIP] {iso_num} already in {target_cat}")
            continue

        standards.append(new_entry)
        data["standards"] = standards
        target_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
        changes.append(f"ADD {iso_num} -> {target_cat}")
        print(f"  [ADD] {iso_num} -> {target_cat}")

    print(f"\nTotal changes: {len(changes)}")


if __name__ == "__main__":
    main()
