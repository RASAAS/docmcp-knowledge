#!/usr/bin/env python3
"""
Batch convert MDCG PDFs using docling.
Run from repo root: python3 scripts/run_mdcg_conversion.py
"""
import sys
import json
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

try:
    from docling.document_converter import DocumentConverter
    from docling.datamodel.pipeline_options import PdfPipelineOptions
except ImportError:
    print("ERROR: docling not installed. Run: pip3 install docling")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = REPO_ROOT / "eu_mdr" / "mdcg" / "fulltext"

# 5 pilot files
PILOT_IDS = [
    "mdcg-2020-5",
    "mdcg-2020-6",
    "mdcg-2020-7",
    "mdcg-2020-8",
    "mdcg-2019-9",
]

# All 30 files (for batch mode)
ALL_IDS = [
    "mdcg-2019-7", "mdcg-2019-9", "mdcg-2019-15", "mdcg-2019-16",
    "mdcg-2020-1", "mdcg-2020-3", "mdcg-2020-5", "mdcg-2020-6",
    "mdcg-2020-7", "mdcg-2020-8", "mdcg-2020-13",
    "mdcg-2021-5", "mdcg-2021-6", "mdcg-2021-8", "mdcg-2021-24",
    "mdcg-2021-25", "mdcg-2021-27",
    "mdcg-2022-5", "mdcg-2022-21",
    "mdcg-2023-1", "mdcg-2023-4", "mdcg-2023-5", "mdcg-2023-6", "mdcg-2023-7",
    "mdcg-2024-3", "mdcg-2024-5", "mdcg-2024-10",
    "mdcg-2025-4", "mdcg-2025-6", "mdcg-2025-9",
]


def load_source_urls():
    """Load source URLs from .zh.md front matter."""
    urls = {}
    mdcg_dir = REPO_ROOT / "eu_mdr" / "mdcg"
    for f in mdcg_dir.glob("*.zh.md"):
        doc_id = f.stem.replace(".zh", "")
        content = f.read_text(encoding="utf-8")
        for line in content.split("\n"):
            if line.startswith("source_url:"):
                url = line.split("source_url:", 1)[1].strip()
                if url and url.startswith("http"):
                    urls[doc_id] = url
                break
    return urls


def convert_one(doc_id: str, source_url: str, converter: DocumentConverter):
    """Convert a single PDF and return the Markdown text."""
    out_file = OUTPUT_DIR / f"{doc_id}.md"
    if out_file.exists():
        print(f"  [SKIP] {doc_id} already converted")
        return out_file.read_text(encoding="utf-8")

    print(f"  [CONVERT] {doc_id} <- {source_url[:80]}...")
    try:
        result = converter.convert(source_url)
        if result is None or result.document is None:
            print(f"  [ERROR] Conversion returned None for {doc_id}")
            return None
        md = result.document.export_to_markdown()
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        out_file.write_text(md, encoding="utf-8")
        print(f"  [OK] {doc_id}: {len(md)} chars -> {out_file.name}")
        return md
    except Exception as e:
        print(f"  [ERROR] {doc_id}: {e}")
        return None


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="Convert all 30 files")
    parser.add_argument("--ids", nargs="+", help="Specific IDs to convert")
    args = parser.parse_args()

    if args.ids:
        target_ids = args.ids
    elif args.all:
        target_ids = ALL_IDS
    else:
        target_ids = PILOT_IDS

    print(f"Loading source URLs from .zh.md files...")
    urls = load_source_urls()
    print(f"Found {len(urls)} source URLs")

    print(f"\nInitializing docling converter...")
    converter = DocumentConverter()

    print(f"\nConverting {len(target_ids)} files to {OUTPUT_DIR}/")
    results = {}
    for doc_id in target_ids:
        if doc_id not in urls:
            print(f"  [SKIP] {doc_id}: no source_url found")
            continue
        md = convert_one(doc_id, urls[doc_id], converter)
        results[doc_id] = "ok" if md else "error"

    print(f"\n=== Summary ===")
    ok = sum(1 for v in results.values() if v == "ok")
    err = sum(1 for v in results.values() if v == "error")
    skip = len(target_ids) - len(results)
    print(f"OK: {ok}, Error: {err}, Skip (no URL): {skip}")
    print(f"Output dir: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
