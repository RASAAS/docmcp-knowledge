#!/usr/bin/env python3
"""
Convert MDCG guidance PDFs to structured Markdown using docling.

This is a standalone utility script — NOT a project dependency.
Install docling separately before using:
    pip install docling

Usage:
    # Convert a single PDF by URL
    python scripts/convert_mdcg_pdf.py --url https://health.ec.europa.eu/.../mdcg_2020-5_en.pdf --id mdcg-2020-5

    # Convert a single local PDF file
    python scripts/convert_mdcg_pdf.py --file /path/to/mdcg_2020-5_en.pdf --id mdcg-2020-5

    # Batch convert from a JSON list
    python scripts/convert_mdcg_pdf.py --batch eu_mdr/mdcg/_index.json --output-dir eu_mdr/mdcg/

    # Dry run (show what would be converted)
    python scripts/convert_mdcg_pdf.py --batch eu_mdr/mdcg/_index.json --dry-run

Output:
    Creates <id>.raw.md in the output directory with:
    - YAML front matter (title, source_url, converted_date)
    - Full text content extracted by docling
    - Tables preserved as Markdown tables
    - Images saved as <id>_img_<n>.png

Notes:
    - Output is RAW conversion — requires manual review and editing
    - Copyright: MDCG documents are EU public documents (CC BY 4.0 compatible)
    - Large PDFs (>50 pages) may take several minutes
    - For production use, review and clean up the raw output before committing
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from datetime import datetime
from pathlib import Path

try:
    from docling.document_converter import DocumentConverter
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions
    DOCLING_AVAILABLE = True
except ImportError:
    DOCLING_AVAILABLE = False


def check_docling() -> None:
    if not DOCLING_AVAILABLE:
        print("ERROR: docling is not installed.")
        print("Install it with: pip install docling")
        print("Note: docling requires Python 3.9+ and ~2GB disk space for models.")
        sys.exit(1)


def convert_pdf_to_markdown(
    source: str,
    doc_id: str,
    output_dir: Path,
    dry_run: bool = False,
    extract_images: bool = True,
    images_public_dir: Path | None = None,
) -> Path | None:
    """
    Convert a PDF (URL or local path) to Markdown using docling.

    Args:
        source: URL or local file path to the PDF
        doc_id: Document identifier (e.g. 'mdcg-2020-5')
        output_dir: Directory to write output files
        dry_run: If True, only show what would be done
        extract_images: If True, extract and save embedded images
        images_public_dir: VitePress public dir for images (default: docs/public/images/mdcg)

    Returns:
        Path to the output .raw.md file, or None on failure
    """
    check_docling()

    output_file = output_dir / f"{doc_id}.raw.md"

    if dry_run:
        print(f"  [DRY] Would convert: {source}")
        print(f"  [DRY] Output: {output_file}")
        return output_file

    print(f"  Converting: {source}")
    print(f"  Output: {output_file}")

    # Resolve image output directory
    repo_root = Path(__file__).parent.parent
    if images_public_dir is None:
        images_public_dir = repo_root / "docs" / "public" / "images" / "mdcg"

    try:
        from docling.document_converter import DocumentConverter, PdfFormatOption
        from docling.datamodel.pipeline_options import PdfPipelineOptions

        # Configure pipeline options
        pipeline_options = PdfPipelineOptions()
        pipeline_options.do_ocr = False          # Skip OCR for text-based PDFs
        pipeline_options.do_table_structure = True
        pipeline_options.images_scale = 2.0      # Higher resolution for extracted images
        pipeline_options.generate_picture_images = extract_images

        from docling.document_converter import DocumentConverter
        converter = DocumentConverter(
            format_options={
                "pdf": PdfFormatOption(pipeline_options=pipeline_options)
            }
        )
        result = converter.convert(source)

        if result is None or result.document is None:
            print(f"  ERROR: Conversion failed for {source}")
            return None

        doc = result.document

        # Save extracted images and build a mapping: picture_ref -> web path
        img_map: dict[str, str] = {}
        if extract_images:
            images_public_dir.mkdir(parents=True, exist_ok=True)
            img_idx = 0
            for element, _level in doc.iterate_items():
                # PictureItem elements hold extracted images
                elem_type = type(element).__name__
                if elem_type == "PictureItem" and hasattr(element, "image") and element.image:
                    img_idx += 1
                    img_filename = f"{doc_id}-fig{img_idx:02d}.png"
                    img_path = images_public_dir / img_filename
                    try:
                        element.image.pil_image.save(img_path, format="PNG")
                        # Web path relative to VitePress public dir
                        img_map[element.self_ref] = f"/images/mdcg/{img_filename}"
                        print(f"    Saved image: {img_filename}")
                    except Exception as img_err:
                        print(f"    WARN: Could not save image {img_idx}: {img_err}")

        # Export to Markdown
        md_content = doc.export_to_markdown()

        # Replace docling image placeholders with actual web paths
        # docling uses <!-- image --> or similar markers; replace with ![](path)
        if img_map:
            import re
            img_iter = iter(img_map.values())
            def replace_img(m):
                try:
                    return f"![]({next(img_iter)})"
                except StopIteration:
                    return m.group(0)
            md_content = re.sub(r'<!-- image -->', replace_img, md_content)

        # Build front matter
        now = datetime.now().strftime("%Y-%m-%d")
        is_url = source.startswith("http")
        front_matter = f"""---
document_id: {doc_id}
source_url: {source if is_url else ""}
source_file: {source if not is_url else ""}
converted_date: "{now}"
conversion_tool: docling
status: raw_conversion
review_required: true
---

> **NOTE**: This is a raw docling conversion. Review and edit before committing.
> Remove this notice and the `raw_conversion` status when review is complete.

"""

        final_content = front_matter + md_content

        output_dir.mkdir(parents=True, exist_ok=True)
        output_file.write_text(final_content, encoding="utf-8")
        img_note = f", {len(img_map)} images" if img_map else ""
        print(f"  Done: {output_file} ({len(md_content)} chars{img_note})")
        return output_file

    except Exception as e:
        print(f"  ERROR: {e}")
        return None


def batch_convert(index_file: Path, output_dir: Path, dry_run: bool = False) -> None:
    """
    Batch convert PDFs listed in an _index.json file.

    Only converts entries that:
    1. Have a source_url pointing to a PDF
    2. Don't already have a .zh.md file in the output directory
    """
    check_docling()

    if not index_file.exists():
        print(f"ERROR: Index file not found: {index_file}")
        sys.exit(1)

    with open(index_file, encoding="utf-8") as f:
        index = json.load(f)

    entries = index.get("entries", [])
    print(f"Found {len(entries)} entries in {index_file}")

    converted = 0
    skipped = 0
    failed = 0

    for entry in entries:
        doc_id = entry.get("id") or entry.get("slug", "")
        source_url = entry.get("source_url", "")

        if not doc_id or not source_url:
            print(f"  SKIP: Missing id or source_url for entry: {entry}")
            skipped += 1
            continue

        if not source_url.endswith(".pdf"):
            print(f"  SKIP: Not a PDF URL: {source_url}")
            skipped += 1
            continue

        # Skip if .zh.md already exists (hand-written content takes priority)
        existing_zh = output_dir / f"{doc_id}.zh.md"
        if existing_zh.exists():
            print(f"  SKIP: {doc_id}.zh.md already exists (hand-written)")
            skipped += 1
            continue

        # Skip if .raw.md already exists
        existing_raw = output_dir / f"{doc_id}.raw.md"
        if existing_raw.exists():
            print(f"  SKIP: {doc_id}.raw.md already exists")
            skipped += 1
            continue

        result = convert_pdf_to_markdown(source_url, doc_id, output_dir, dry_run=dry_run)
        if result:
            converted += 1
        else:
            failed += 1

    print(f"\nBatch complete: {converted} converted, {skipped} skipped, {failed} failed")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert MDCG guidance PDFs to Markdown using docling",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    source_group = parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument("--url", help="PDF URL to convert")
    source_group.add_argument("--file", help="Local PDF file path to convert")
    source_group.add_argument("--batch", help="Path to _index.json for batch conversion")

    parser.add_argument("--id", help="Document ID (required with --url or --file)")
    parser.add_argument(
        "--output-dir",
        default="eu_mdr/mdcg",
        help="Output directory (default: eu_mdr/mdcg)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be converted without doing it",
    )

    args = parser.parse_args()

    output_dir = Path(args.output_dir)

    if args.batch:
        batch_convert(Path(args.batch), output_dir, dry_run=args.dry_run)
    else:
        if not args.id:
            parser.error("--id is required when using --url or --file")
        source = args.url or args.file
        convert_pdf_to_markdown(source, args.id, output_dir, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
