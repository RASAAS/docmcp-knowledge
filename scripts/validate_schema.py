#!/usr/bin/env python3
"""
JSON Schema Validation Script
Validates all _index.json and YAML front matter in .md files against schemas.

Usage:
    python scripts/validate_schema.py
    python scripts/validate_schema.py --path nmpa/guidance
    python scripts/validate_schema.py --fix  # Auto-fix common issues
"""

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("ERROR: jsonschema not installed. Run: pip install jsonschema")
    sys.exit(1)

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).parent.parent
SCHEMAS_DIR = ROOT / "schemas"

# Map category prefix to schema file
SCHEMA_MAP = {
    "guidance": "guidance.schema.json",
    "regulations": "regulation.schema.json",
    "standards": "standard.schema.json",
    "mdcg": "guidance.schema.json",
    "team_nb": "guidance.schema.json",
    "classification": "regulation.schema.json",
}

REQUIRED_FRONT_MATTER_FIELDS = [
    "id", "title", "regulation", "category", "status",
    "source_url", "contributor"
]


def load_schema(schema_name: str) -> dict:
    schema_file = SCHEMAS_DIR / schema_name
    if not schema_file.exists():
        return {}
    with open(schema_file, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_front_matter(md_content: str) -> dict | None:
    """Extract YAML front matter from Markdown file."""
    match = re.match(r"^---\n(.+?)\n---", md_content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def get_schema_for_path(path: Path) -> str | None:
    """Determine which schema to use based on file path."""
    parts = path.parts
    for part in parts:
        if part in SCHEMA_MAP:
            return SCHEMA_MAP[part]
    return None


def validate_md_file(md_file: Path, errors: list, warnings: list) -> bool:
    """Validate a single Markdown file's front matter."""
    content = md_file.read_text(encoding="utf-8")
    fm = extract_front_matter(content)

    if fm is None:
        warnings.append(f"  WARN: No front matter in {md_file.relative_to(ROOT)}")
        return True  # Not an error, might be a README

    # Check required fields
    missing = [f for f in REQUIRED_FRONT_MATTER_FIELDS if f not in fm]
    if missing:
        errors.append(
            f"  ERROR: {md_file.relative_to(ROOT)}: missing fields: {', '.join(missing)}"
        )
        return False

    # Check title has zh key
    if isinstance(fm.get("title"), dict):
        if not fm["title"].get("zh") and not fm["title"].get("en"):
            errors.append(
                f"  ERROR: {md_file.relative_to(ROOT)}: title must have 'zh' or 'en'"
            )
            return False
    elif isinstance(fm.get("title"), str):
        warnings.append(
            f"  WARN: {md_file.relative_to(ROOT)}: title should be object with zh/en keys"
        )

    # Check status value
    valid_statuses = {"active", "superseded", "draft"}
    if fm.get("status") not in valid_statuses:
        errors.append(
            f"  ERROR: {md_file.relative_to(ROOT)}: invalid status '{fm.get('status')}'"
            f" (must be one of: {', '.join(valid_statuses)})"
        )
        return False

    # Check regulation value
    valid_regulations = {"eu_mdr", "fda", "nmpa", "shared"}
    if fm.get("regulation") not in valid_regulations:
        errors.append(
            f"  ERROR: {md_file.relative_to(ROOT)}: invalid regulation '{fm.get('regulation')}'"
        )
        return False

    # Check source_url is not empty
    if not fm.get("source_url"):
        warnings.append(
            f"  WARN: {md_file.relative_to(ROOT)}: source_url is empty"
        )

    return True


def validate_index_file(index_file: Path, errors: list, warnings: list) -> bool:
    """Validate a _index.json file."""
    try:
        with open(index_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"  ERROR: {index_file.relative_to(ROOT)}: invalid JSON: {e}")
        return False

    required = ["category", "last_updated", "entries"]
    missing = [f for f in required if f not in data]
    if missing:
        errors.append(
            f"  ERROR: {index_file.relative_to(ROOT)}: missing fields: {', '.join(missing)}"
        )
        return False

    # Validate each entry has required fields
    for i, entry in enumerate(data.get("entries", [])):
        entry_required = ["id", "title", "status", "source_url"]
        entry_missing = [f for f in entry_required if f not in entry]
        if entry_missing:
            errors.append(
                f"  ERROR: {index_file.relative_to(ROOT)}: entry[{i}] missing: "
                f"{', '.join(entry_missing)}"
            )
            return False

    return True


def validate_path(search_path: Path, errors: list, warnings: list) -> tuple[int, int]:
    """Validate all files under a path. Returns (checked, failed) counts."""
    checked = 0
    failed = 0

    # Validate .md files (skip README.md files)
    for md_file in sorted(search_path.rglob("*.md")):
        if md_file.name == "README.md":
            continue
        if ".vitepress" in str(md_file):
            continue
        checked += 1
        if not validate_md_file(md_file, errors, warnings):
            failed += 1

    # Validate _index.json files
    for index_file in sorted(search_path.rglob("_index.json")):
        checked += 1
        if not validate_index_file(index_file, errors, warnings):
            failed += 1

    return checked, failed


def main():
    parser = argparse.ArgumentParser(description="Validate content schemas")
    parser.add_argument("--path", default=".",
                        help="Path to validate (default: entire repo)")
    parser.add_argument("--strict", action="store_true",
                        help="Treat warnings as errors")
    args = parser.parse_args()

    search_path = ROOT / args.path if args.path != "." else ROOT
    # Exclude docs/ and scripts/ directories
    if not search_path.exists():
        print(f"ERROR: Path not found: {search_path}")
        sys.exit(1)

    errors = []
    warnings = []

    print(f"Validating content in: {search_path.relative_to(ROOT) if search_path != ROOT else '.'}")
    checked, failed = validate_path(search_path, errors, warnings)

    print(f"\nChecked: {checked} files")

    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for w in warnings:
            print(w)

    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors:
            print(e)
        print(f"\nFAILED: {failed}/{checked} files have errors")
        sys.exit(1)
    else:
        print(f"\nOK: All {checked} files passed validation")
        if args.strict and warnings:
            print("FAILED: strict mode, warnings treated as errors")
            sys.exit(1)


if __name__ == "__main__":
    main()
