#!/usr/bin/env python3
"""
Parse NMPA clinical evaluation exemption list markdown into structured JSON.

Input:  nmpa/regulations/clinical-evaluation-exemption-list-2025.zh.md
Output: nmpa/regulations/clinical_evaluation_exemption_2025.json

Structure per entry:
  - classification_code: str (L1 "02", L3 "01-03-04", or multi like "02-04-09,02-04-10")
  - product_name: str
  - product_description: str
  - device_class: str ("II" or "III")
  - remarks: str (备注)
  - scope: "l1" | "l3" | "special" (whether entire L1 subcategory or specific product)
"""

import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
SRC_PATH = REPO_ROOT / "nmpa" / "regulations" / "clinical-evaluation-exemption-list-2025.zh.md"
OUT_PATH = REPO_ROOT / "nmpa" / "regulations" / "clinical_evaluation_exemption_2025.json"

CODE_L1_RE = re.compile(r"^\d{2}$")
CODE_L3_RE = re.compile(r"^\d{2}-\d{2}-\d{2}$")
MULTI_CODE_RE = re.compile(r"^(\d{2}-\d{2}-\d{2})(\s+\d{2}-\d{2}-\d{2})+$")

CLASS_NORM = {
    "I": "I", "Ⅰ": "I",
    "II": "II", "Ⅱ": "II",
    "III": "III", "Ⅲ": "III",
    "II/ III": "II/III", "Ⅱ/ Ⅲ": "II/III", "Ⅱ/Ⅲ": "II/III",
    "II/III": "II/III",
}


def normalize_class(raw: str) -> str:
    raw = raw.strip().replace(" ", " ")
    return CLASS_NORM.get(raw, raw)


def parse_table(text: str) -> list[dict]:
    body = text.split("---", 2)[-1].strip()
    lines = body.split("\n")

    table_started = False
    raw_rows: list[str] = []
    pending_overflow = ""

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if pending_overflow:
                raw_rows.append(pending_overflow)
                pending_overflow = ""
            continue

        if stripped.startswith("分类编码"):
            table_started = True
            continue
        if not table_started:
            continue

        if stripped.startswith("---") and "|" in stripped:
            continue

        if "|" in stripped:
            if pending_overflow:
                raw_rows.append(pending_overflow)
                pending_overflow = ""
            raw_rows.append(stripped)
        else:
            if raw_rows:
                raw_rows[-1] += "\n" + stripped

    if pending_overflow:
        raw_rows.append(pending_overflow)

    entries = []
    for row in raw_rows:
        cols = [c.strip().strip("*").strip() for c in row.split("|")]
        while len(cols) < 5:
            cols.append("")

        raw_code = cols[0]
        product_name = cols[1]
        product_desc = cols[2]
        device_class = normalize_class(cols[3])
        remarks = cols[4] if len(cols) > 4 else ""

        raw_code_clean = re.sub(r"\s+", " ", raw_code).strip()
        codes_found = re.findall(r"\d{2}-\d{2}-\d{2}", raw_code_clean)

        if CODE_L1_RE.match(raw_code_clean):
            scope = "l1"
            code = raw_code_clean
        elif CODE_L3_RE.match(raw_code_clean):
            scope = "l3"
            code = raw_code_clean
        elif codes_found:
            scope = "l3"
            code = ",".join(codes_found)
        elif not raw_code_clean and product_name:
            scope = "special"
            code = ""
        else:
            scope = "special"
            code = raw_code_clean

        if not product_name and not product_desc:
            continue

        entries.append({
            "classification_code": code,
            "product_name": product_name,
            "product_description": product_desc,
            "device_class": device_class,
            "remarks": remarks,
            "scope": scope,
        })

    return entries


def main():
    dry_run = "--dry-run" in sys.argv

    if not SRC_PATH.exists():
        print(f"Source not found: {SRC_PATH}")
        sys.exit(1)

    text = SRC_PATH.read_text(encoding="utf-8")
    entries = parse_table(text)

    from collections import Counter
    scopes = Counter(e["scope"] for e in entries)
    classes = Counter(e["device_class"] for e in entries)

    print(f"Parsed {len(entries)} exemption entries")
    print(f"  By scope: {dict(scopes)}")
    print(f"  By class: {dict(classes)}")

    l1_entries = [e for e in entries if e["scope"] == "l1"]
    print(f"\nL1-level exemptions ({len(l1_entries)}):")
    for e in l1_entries:
        print(f"  {e['classification_code']} {e['product_name'][:40]} [{e['device_class']}]")

    if dry_run:
        print("\n[DRY RUN] First 5 L3 entries:")
        l3 = [e for e in entries if e["scope"] == "l3"]
        for e in l3[:5]:
            print(f"  {e['classification_code']} {e['product_name'][:40]} [{e['device_class']}]")
    else:
        out = {
            "version": "2025",
            "source": "NMPA 2025 Clinical Evaluation Exemption List",
            "effective_date": "2025-05-15",
            "total_entries": len(entries),
            "entries": entries,
        }
        OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(OUT_PATH, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        print(f"\nWrote {OUT_PATH}")


if __name__ == "__main__":
    main()
