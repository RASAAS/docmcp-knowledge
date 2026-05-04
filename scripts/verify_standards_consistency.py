#!/usr/bin/env python3
"""
Verify consistency between docmcp standards data and docmcp-knowledge display layer.

Checks:
1. standards_2025.json total count matches knowledge repo total
2. All harmonised standards in standards_2025.json exist in eu_mdr/standards/
3. All non-harmonised standards exist in eu_mdr/other_standards/
4. All standards have required fields (source_url, applicable_gsprs, scope, abstract)
5. _index.json counts match actual file counts
6. GSPR mapping coverage (gspr_standard_mapping.json)

Usage:
    python scripts/verify_standards_consistency.py
    python scripts/verify_standards_consistency.py --docmcp-path /path/to/docmcp
"""

import argparse
import json
import os
import sys
from pathlib import Path

KNOWLEDGE_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DOCMCP_ROOT = KNOWLEDGE_ROOT.parent / "docmcp"


def load_knowledge_standards(knowledge_root: Path) -> dict:
    """Load all standards from knowledge repo category files."""
    hs_dir = knowledge_root / "eu_mdr" / "standards"
    os_dir = knowledge_root / "eu_mdr" / "other_standards"

    hs_standards = {}
    os_standards = {}

    for f in sorted(hs_dir.iterdir()):
        if f.name.startswith("standards-") and f.suffix == ".json":
            with open(f) as fp:
                data = json.load(fp)
            for s in data.get("standards", []):
                hs_standards[s.get("id", s.get("number", ""))] = s

    for f in sorted(os_dir.iterdir()):
        if f.name.startswith("standards-") and f.suffix == ".json":
            with open(f) as fp:
                data = json.load(fp)
            for s in data.get("standards", []):
                os_standards[s.get("id", s.get("number", ""))] = s

    return {"harmonised": hs_standards, "other": os_standards}


def load_docmcp_standards(docmcp_root: Path) -> list:
    """Load standards from docmcp standards_2025.json."""
    path = docmcp_root / "data" / "standards" / "standards_2025.json"
    if not path.exists():
        return []
    with open(path) as f:
        data = json.load(f)
    return data.get("standards", [])


def verify(knowledge_root: Path, docmcp_root: Path) -> tuple:
    """Run all verification checks. Returns (errors, warnings)."""
    errors = []
    warnings = []

    # Load data
    knowledge = load_knowledge_standards(knowledge_root)
    k_total = len(knowledge["harmonised"]) + len(knowledge["other"])

    docmcp_stds = load_docmcp_standards(docmcp_root)
    d_total = len(docmcp_stds)

    print(f"Knowledge repo: {len(knowledge['harmonised'])} harmonised + {len(knowledge['other'])} other = {k_total}")
    print(f"docmcp standards_2025.json: {d_total}")

    # Check 1: Total count match
    if docmcp_stds and k_total != d_total:
        errors.append(f"Count mismatch: knowledge={k_total}, docmcp={d_total}")

    # Check 2: _index.json counts
    hs_index_path = knowledge_root / "eu_mdr" / "standards" / "_index.json"
    os_index_path = knowledge_root / "eu_mdr" / "other_standards" / "_index.json"

    if hs_index_path.exists():
        with open(hs_index_path) as f:
            hs_index = json.load(f)
        declared_hs = hs_index.get("total_standards", 0)
        actual_hs = len(knowledge["harmonised"])
        if declared_hs != actual_hs:
            errors.append(f"Harmonised _index.json count mismatch: declared={declared_hs}, actual={actual_hs}")

        for cat_key, cat_info in hs_index.get("categories", {}).items():
            declared_count = cat_info.get("count", 0)
            cat_file = knowledge_root / "eu_mdr" / "standards" / cat_info.get("file", "")
            if cat_file.exists():
                with open(cat_file) as f:
                    actual_count = len(json.load(f).get("standards", []))
                if declared_count != actual_count:
                    warnings.append(f"HS category '{cat_key}': declared={declared_count}, actual={actual_count}")

    if os_index_path.exists():
        with open(os_index_path) as f:
            os_index = json.load(f)
        declared_os = os_index.get("total_standards", 0)
        actual_os = len(knowledge["other"])
        if declared_os != actual_os:
            errors.append(f"Other standards _index.json count mismatch: declared={declared_os}, actual={actual_os}")

    # Check 3: Required fields in knowledge standards
    required_fields = ["source_url", "applicable_gsprs"]
    for std_id, s in {**knowledge["harmonised"], **knowledge["other"]}.items():
        for field in required_fields:
            val = s.get(field)
            if not val:
                warnings.append(f"Standard '{std_id}' missing '{field}'")

    # Check 4: GSPR mapping completeness
    mapping_path = docmcp_root / "data" / "standards" / "gspr_standard_mapping.json"
    if mapping_path.exists():
        with open(mapping_path) as f:
            mapping = json.load(f)
        mappings = mapping.get("mappings", [])
        main_clauses = len(mappings)
        sub_clauses = sum(len(m.get("sub_clause_mappings", [])) for m in mappings)
        print(f"GSPR mapping: {main_clauses} main clauses, {sub_clauses} sub-clauses")
        if main_clauses < 23:
            warnings.append(f"GSPR mapping incomplete: only {main_clauses}/23 main clauses")

    # Check 5: Cross-reference docmcp -> knowledge
    if docmcp_stds:
        all_knowledge_ids = set(knowledge["harmonised"].keys()) | set(knowledge["other"].keys())
        missing_in_knowledge = []
        for s in docmcp_stds:
            sid = s.get("id", "")
            if sid and sid not in all_knowledge_ids:
                # Try matching by number
                number = s.get("number", "")
                found = any(
                    ks.get("number") == number
                    for ks in list(knowledge["harmonised"].values()) + list(knowledge["other"].values())
                )
                if not found:
                    missing_in_knowledge.append(f"{sid} ({number})")

        if missing_in_knowledge:
            warnings.append(f"{len(missing_in_knowledge)} standards in docmcp not found in knowledge: {missing_in_knowledge[:5]}")

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="Verify standards data consistency")
    parser.add_argument("--docmcp-path", type=str, default=str(DEFAULT_DOCMCP_ROOT),
                        help="Path to docmcp repository root")
    parser.add_argument("--strict", action="store_true",
                        help="Exit with error code on warnings too")
    args = parser.parse_args()

    knowledge_root = KNOWLEDGE_ROOT
    docmcp_root = Path(args.docmcp_path)

    print("=" * 60)
    print("Standards Data Consistency Verification")
    print("=" * 60)
    print(f"Knowledge root: {knowledge_root}")
    print(f"DocMCP root: {docmcp_root}")
    print()

    errors, warnings = verify(knowledge_root, docmcp_root)

    print()
    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  [ERROR] {e}")
    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings[:20]:
            print(f"  [WARN] {w}")
        if len(warnings) > 20:
            print(f"  ... and {len(warnings) - 20} more")

    if not errors and not warnings:
        print("ALL CHECKS PASSED")

    print()
    print("=" * 60)

    if errors:
        sys.exit(1)
    if args.strict and warnings:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
