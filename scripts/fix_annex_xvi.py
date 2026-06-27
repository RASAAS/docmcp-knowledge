#!/usr/bin/env python3
"""Fix annex_xvi: move ISO 10993-1:2025 to biocompatibility, remove EN ISO 14155:2020/A11:2024."""
import json
from pathlib import Path

BASE = Path("eu_mdr/other_standards")

# 1. Read annex_xvi
annex_path = BASE / "standards-annex_xvi.json"
annex = json.loads(annex_path.read_text())

# Move ISO 10993-1:2025 to biocompatibility
iso_10993_1 = None
en_14155 = None
keep = []
for s in annex["standards"]:
    if s["number"] == "ISO 10993-1:2025":
        iso_10993_1 = s
        print(f"MOVE annex_xvi -> biocompatibility: {s['number']}")
    elif "14155" in s["number"] and "EN" in s["number"]:
        en_14155 = s
        print(f"REMOVE from annex_xvi (EN harmonised amendment): {s['number']}")
    else:
        keep.append(s)

annex["standards"] = keep
annex_path.write_text(json.dumps(annex, indent=2, ensure_ascii=False) + "\n")

# 2. Add ISO 10993-1:2025 to biocompatibility with correct data
if iso_10993_1:
    bio_path = BASE / "standards-biocompatibility.json"
    bio = json.loads(bio_path.read_text())
    # Fix source_url (was incorrect)
    iso_10993_1["source_url"] = "https://www.iso.org/standard/86328.html"
    iso_10993_1["applicable_gsprs"] = ["10", "10.1", "10.4"]
    iso_10993_1["source_verified"] = "2026-06-27"
    if "note" in iso_10993_1:
        del iso_10993_1["note"]
    # Check not already present
    existing = [s["number"] for s in bio["standards"]]
    if iso_10993_1["number"] not in existing:
        bio["standards"].insert(0, iso_10993_1)
        bio_path.write_text(json.dumps(bio, indent=2, ensure_ascii=False) + "\n")
        print(f"  Added to biocompatibility: {iso_10993_1['number']}")

print("\nDone. annex_xvi now has", len(keep), "standards")
