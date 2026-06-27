#!/usr/bin/env python3
"""Fix known link/version errors in other_standards JSON files."""
import json
from pathlib import Path

BASE = Path("eu_mdr/other_standards")

# Corrections: (category, number, corrections_dict)
FIXES = [
    # audiology
    ("audiology", "IEC 60645-5:2004", {
        "source_url": "https://webstore.iec.ch/en/publication/2774",
    }),
    ("audiology", "IEC 60118-0:2024", {
        "number": "IEC 60118-0:2022",
        "id": "iec-60118-0-2022",
        "title": {
            "en": "Electroacoustics - Hearing aids - Part 0: Measurement of the performance characteristics of hearing aids",
            "zh": "电声学 - 助听器 - 第0部分：助听器性能特性的测量"
        },
        "source_url": "https://webstore.iec.ch/en/publication/62974",
        "source_verified": "2026-06-27",
    }),
    # biocompatibility
    ("biocompatibility", "ISO 10993-15:2023", {
        "number": "ISO 10993-15:2019",
        "id": "iso-10993-15-2019",
        "source_url": "https://www.iso.org/standard/68937.html",
        "source_verified": "2026-06-27",
    }),
    ("biocompatibility", "ISO 10993-17:2023", {
        "source_url": "https://www.iso.org/standard/75323.html",
        "source_verified": "2026-06-27",
    }),
    # connectors
    ("connectors", "ISO 80369-7:2021", {
        "source_url": "https://www.iso.org/standard/79173.html",
        "source_verified": "2026-06-27",
    }),
    ("connectors", "ISO 80369-2:2024", {
        "source_url": "https://www.iso.org/standard/79601.html",
        "source_verified": "2026-06-27",
    }),
    # dental
    ("dental", "ISO 1942:2020", {
        "source_url": "https://www.iso.org/standard/72249.html",
        "source_verified": "2026-06-27",
    }),
]

for cat, number, corrections in FIXES:
    path = BASE / f"standards-{cat}.json"
    data = json.loads(path.read_text())
    found = False
    for s in data["standards"]:
        if s["number"] == number:
            found = True
            for k, v in corrections.items():
                old = s.get(k, "N/A")
                s[k] = v
                if k in ("number", "source_url"):
                    print(f"  FIX {cat}/{number}: {k} = {old} -> {v}")
            break
    if not found:
        print(f"  [NOT FOUND] {cat}/{number}")
    else:
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")

print("\nDone with known fixes.")
