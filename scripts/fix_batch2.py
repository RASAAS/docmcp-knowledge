#!/usr/bin/env python3
"""Fix additional issues found during URL verification."""
import json
from pathlib import Path

BASE = Path("eu_mdr/other_standards")

# === Batch 2 fixes ===
FIXES = [
    # phototherapy - IEC 60601-2-83:2019 URL fix
    ("phototherapy", "IEC 60601-2-83:2019", {
        "source_url": "https://webstore.iec.ch/en/publication/32219",
        "source_verified": "2026-06-27",
    }),
    # point_of_care_testing - ISO 22870:2016 is WITHDRAWN, replace with ISO 15189:2022
    ("point_of_care_testing", "ISO 22870:2016", {
        "number": "ISO 15189:2022",
        "id": "iso-15189-2022",
        "title": {
            "en": "Medical laboratories - Requirements for quality and competence (includes POCT requirements)",
            "zh": "医学实验室 - 质量和能力的要求（含即时检验POCT要求）"
        },
        "source_url": "https://www.iso.org/standard/76677.html",
        "source_verified": "2026-06-27",
        "status": "active",
    }),
    # reprocessing - ISO 15883-3:2025 does not exist, correct is 2024
    ("reprocessing", "ISO 15883-3:2025", {
        "number": "ISO 15883-3:2024",
        "id": "iso-15883-3-2024",
        "source_url": "https://www.iso.org/standard/84378.html",
        "source_verified": "2026-06-27",
    }),
    # surgical_implants - ISO 14607:2025 does not exist, correct is 2024
    ("surgical_implants", "ISO 14607:2025", {
        "number": "ISO 14607:2024",
        "id": "iso-14607-2024",
        "source_url": "https://www.iso.org/standard/82020.html",
        "source_verified": "2026-06-27",
    }),
    # surgical_implants - ISO 21535:2024 does not exist, correct is 2023
    ("surgical_implants", "ISO 21535:2024", {
        "number": "ISO 21535:2023",
        "id": "iso-21535-2023",
        "source_url": "https://www.iso.org/standard/77044.html",
        "source_verified": "2026-06-27",
    }),
    # software - IEC 62304:2006+AMD1:2015 missing title
    ("software", "IEC 62304:2006+AMD1:2015", {
        "title": {
            "en": "Medical device software - Software life cycle processes",
            "zh": "医疗器械软件 - 软件生命周期过程"
        },
        "source_verified": "2026-06-27",
    }),
    # usability - IEC 62366-1:2015+AMD1:2020 missing title
    ("usability", "IEC 62366-1:2015+AMD1:2020", {
        "title": {
            "en": "Medical devices - Part 1: Application of usability engineering to medical devices",
            "zh": "医疗器械 - 第1部分：可用性工程在医疗器械中的应用"
        },
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
                if k in ("number", "source_url", "title"):
                    if k == "title":
                        print(f"  FIX {cat}/{number}: title added")
                    else:
                        print(f"  FIX {cat}/{number}: {k} = {old} -> {v}")
            break
    if not found:
        print(f"  [NOT FOUND] {cat}/{number}")
    else:
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")

print("\nDone with batch 2 fixes.")
