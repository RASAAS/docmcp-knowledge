"""Translate regulatory fulltext Markdown files via translation API.

Supports all regulatory document sections (IMDRF, ISO/IEC, MDCG, FDA, NMPA)
and bidirectional translation (EN->ZH and ZH->EN).

Uses the med-doc-translator text API endpoint to translate each section
of the Markdown files while preserving structure, images, links, and tables.

By default, uses Modal GPU-accelerated API (requires TRANSLATE_API_TOKEN).
Set TRANSLATE_API_URL to use a different endpoint (e.g. local Ollama).

Usage:
    # Set Modal API token (required for default Modal endpoint)
    export TRANSLATE_API_TOKEN="your-token-here"

    # Translate all English fulltexts to Chinese across all sections
    python scripts/translate_fulltext.py

    # Translate specific section only
    python scripts/translate_fulltext.py --section imdrf

    # Use local API instead of Modal
    TRANSLATE_API_URL=http://localhost:8050/api/translate/text python scripts/translate_fulltext.py

    # Translate Chinese to English (for NMPA docs)
    python scripts/translate_fulltext.py --section nmpa --direction zh-en

    # Translate a single file by ID
    python scripts/translate_fulltext.py --section imdrf --file imdrf-samd-n10-2013

    # Re-translate existing translations
    python scripts/translate_fulltext.py --force

    # Preview without translating
    python scripts/translate_fulltext.py --dry-run
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent

# Modal GPU-accelerated API (default) -- requires TRANSLATE_API_TOKEN env var
MODAL_TRANSLATE_API = "https://m-yan82--translate-api-translateserver-serve.modal.run/api/translate/text"
# Local Ollama fallback (slower, no auth needed)
LOCAL_TRANSLATE_API = "http://100.93.45.36:8050/api/translate/text"

TRANSLATE_API = os.environ.get("TRANSLATE_API_URL", MODAL_TRANSLATE_API)
TRANSLATE_API_TOKEN = os.environ.get("TRANSLATE_API_TOKEN", "")

# All sections with fulltext directories, keyed by CLI name
# Each maps to: (data_dir relative to ROOT, source_lang)
SECTIONS = {
    "imdrf":  {"path": "_shared/imdrf/fulltext",  "source_lang": "en"},
    "iso_iec": {"path": "_shared/iso_iec/fulltext", "source_lang": "en"},
    "mdcg":   {"path": "eu_mdr/mdcg/fulltext",     "source_lang": "en"},
    "fda":    {"path": "fda/guidance/fulltext",     "source_lang": "en"},
    "nmpa":   {"path": "nmpa/guidance/fulltext",    "source_lang": "zh"},
}

HEADING_RE = re.compile(r"^(#{1,6}\s+)")
SKIP_LINE_PATTERNS = [
    re.compile(r"^\s*$"),
    re.compile(r"^!\[.*\]\(data:image"),
    re.compile(r"^---\s*$"),
    re.compile(r"^\*\*Source\*\*:"),
    re.compile(r"^\*\*Document Number\*\*:"),
    re.compile(r"^\*\*来源\*\*:"),
    re.compile(r"^\*\*文件编号\*\*:"),
]
TABLE_SEPARATOR_RE = re.compile(r"^\|[\s\-:|]+\|$")


def should_skip_line(line: str) -> bool:
    """Lines that should be preserved as-is (images, separators, metadata)."""
    for pat in SKIP_LINE_PATTERNS:
        if pat.match(line):
            return True
    return False


def is_table_line(line: str) -> bool:
    return line.strip().startswith("|") and line.strip().endswith("|")


def split_into_sections(content: str) -> list[dict]:
    """Split Markdown into translatable and non-translatable sections.

    Returns a list of dicts:
      {"type": "translate", "lines": [...]}  -- text to translate
      {"type": "keep", "lines": [...]}       -- pass through as-is
    """
    lines = content.split("\n")
    sections: list[dict] = []
    current_type = "keep"
    current_lines: list[str] = []

    def flush():
        nonlocal current_lines
        if current_lines:
            sections.append({"type": current_type, "lines": list(current_lines)})
            current_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]

        if should_skip_line(line):
            if current_type != "keep":
                flush()
                current_type = "keep"
            current_lines.append(line)
            i += 1
            continue

        if line.strip().startswith("```"):
            if current_type != "keep":
                flush()
                current_type = "keep"
            current_lines.append(line)
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                current_lines.append(lines[i])
                i += 1
            if i < len(lines):
                current_lines.append(lines[i])
                i += 1
            continue

        if is_table_line(line):
            if current_type != "keep":
                flush()
                current_type = "keep"
            while i < len(lines) and is_table_line(lines[i]):
                current_lines.append(lines[i])
                i += 1
            continue

        if current_type != "translate":
            flush()
            current_type = "translate"
        current_lines.append(line)
        i += 1

    flush()
    return sections


def merge_translate_lines(lines: list[str]) -> list[str]:
    """Merge consecutive text lines into paragraph-level segments for translation.

    Headings are kept as individual segments. Consecutive non-heading lines
    are joined into a single paragraph (preserving Markdown list markers).
    """
    segments: list[str] = []
    buffer: list[str] = []

    def flush_buf():
        nonlocal buffer
        if buffer:
            segments.append("\n".join(buffer))
            buffer = []

    for line in lines:
        if HEADING_RE.match(line):
            flush_buf()
            segments.append(line)
        elif line.strip().startswith(("- ", "* ", "1. ", "2. ", "3. ", "4. ", "5. ",
                                      "6. ", "7. ", "8. ", "9. ")):
            flush_buf()
            segments.append(line)
        elif line.strip() == "":
            flush_buf()
        else:
            buffer.append(line)

    flush_buf()
    return segments


def call_translate_api(texts: list[str], lang_in: str = "en", lang_out: str = "zh",
                       max_retries: int = 3) -> list[str]:
    """Call the translation API with retry logic."""
    payload = {
        "texts": texts,
        "lang_in": lang_in,
        "lang_out": lang_out,
        "use_glossary": True,
    }

    headers = {"Content-Type": "application/json"}
    if TRANSLATE_API_TOKEN:
        headers["Authorization"] = f"Bearer {TRANSLATE_API_TOKEN}"

    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.post(TRANSLATE_API, json=payload, headers=headers,
                                 timeout=600)
            resp.raise_for_status()
            data = resp.json()
            return data["translations"]
        except requests.exceptions.Timeout:
            print(f"    [WARN] API timeout (attempt {attempt}/{max_retries})")
            if attempt < max_retries:
                time.sleep(5 * attempt)
        except requests.exceptions.RequestException as e:
            print(f"    [ERROR] API call failed: {e}")
            if attempt < max_retries:
                time.sleep(3 * attempt)
            else:
                raise

    raise RuntimeError("Translation API failed after max retries")


def translate_in_batches(segments: list[str], lang_in: str = "en",
                         lang_out: str = "zh", batch_size: int = 50) -> list[str]:
    """Translate segments in batches to stay within API limits."""
    results: list[str] = []
    total = len(segments)

    for start in range(0, total, batch_size):
        batch = segments[start:start + batch_size]
        end = min(start + batch_size, total)
        print(f"    Translating segments {start+1}-{end}/{total}...")

        translated = call_translate_api(batch, lang_in=lang_in, lang_out=lang_out)
        results.extend(translated)

        if end < total:
            time.sleep(1)

    return results


def translate_file(source_path: Path, output_path: Path,
                   lang_in: str = "en", lang_out: str = "zh") -> bool:
    """Translate a single Markdown fulltext file."""
    content = source_path.read_text(encoding="utf-8")

    sections = split_into_sections(content)

    all_segments: list[str] = []
    segment_map: list[tuple[int, int, int]] = []

    for sec_idx, section in enumerate(sections):
        if section["type"] != "translate":
            continue
        merged = merge_translate_lines(section["lines"])
        start = len(all_segments)
        all_segments.extend(merged)
        end = len(all_segments)
        segment_map.append((sec_idx, start, end))

    if not all_segments:
        print(f"    [SKIP] No translatable content found")
        return False

    print(f"    Sections: {len(sections)} ({len(segment_map)} translatable)")
    print(f"    Total segments to translate: {len(all_segments)}")

    translated = translate_in_batches(all_segments, lang_in=lang_in, lang_out=lang_out)

    output_lines: list[str] = []

    for sec_idx, section in enumerate(sections):
        if section["type"] == "keep":
            output_lines.extend(section["lines"])
        else:
            mapping = None
            for m in segment_map:
                if m[0] == sec_idx:
                    mapping = m
                    break

            if mapping is None:
                output_lines.extend(section["lines"])
                continue

            _, start, end = mapping
            for i in range(start, end):
                if i < len(translated):
                    output_lines.append(translated[i])
                    output_lines.append("")

    result = "\n".join(output_lines)
    result = re.sub(r"\n{3,}", "\n\n", result)
    output_path.write_text(result.strip() + "\n", encoding="utf-8")
    return True


def get_translated_suffix(lang_out: str) -> str:
    """Get the file suffix for translated files."""
    return f".{lang_out}.md"


def collect_files(section_name: str, section_info: dict,
                  direction: str | None = None) -> tuple[Path, str, str, str]:
    """Collect source files and determine translation direction.

    Returns (fulltext_dir, source_suffix, target_suffix, lang_in, lang_out).
    """
    fulltext_dir = ROOT / section_info["path"]
    source_lang = section_info["source_lang"]

    if direction:
        lang_in, lang_out = direction.split("-")
    elif source_lang == "zh":
        lang_in, lang_out = "zh", "en"
    else:
        lang_in, lang_out = "en", "zh"

    if lang_in == source_lang:
        source_suffix = ".md"
    else:
        source_suffix = f".{lang_in}.md"

    target_suffix = f".{lang_out}.md"

    return fulltext_dir, source_suffix, target_suffix, lang_in, lang_out


def main():
    parser = argparse.ArgumentParser(
        description="Translate regulatory fulltext Markdown files"
    )
    parser.add_argument(
        "--section",
        choices=list(SECTIONS.keys()) + ["all"],
        default="all",
        help="Which section to translate (default: all)"
    )
    parser.add_argument(
        "--direction",
        choices=["en-zh", "zh-en"],
        default=None,
        help="Translation direction (default: auto based on section source language)"
    )
    parser.add_argument("--force", action="store_true",
                        help="Re-translate existing translated files")
    parser.add_argument("--file", type=str,
                        help="Translate a specific file ID (without .md suffix)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be translated without doing it")
    args = parser.parse_args()

    sections_to_process = (
        list(SECTIONS.keys()) if args.section == "all"
        else [args.section]
    )

    print("=" * 60)
    print("Regulatory Fulltext Translation Pipeline")
    print(f"API: {TRANSLATE_API}")
    print(f"Sections: {', '.join(sections_to_process)}")
    if args.direction:
        print(f"Direction override: {args.direction}")
    print("=" * 60)

    if not args.dry_run:
        health_url = TRANSLATE_API.replace("/translate/text", "/health")
        try:
            r = requests.get(health_url, timeout=30)
            r.raise_for_status()
            print("API health: OK")
        except Exception as e:
            print(f"API health check failed: {e}")
            print(f"  URL: {health_url}")
            if "modal.run" in TRANSLATE_API and not TRANSLATE_API_TOKEN:
                print("  HINT: Set TRANSLATE_API_TOKEN env var for Modal API")
            sys.exit(1)

    grand_total = {"translated": 0, "skipped": 0, "failed": 0, "no_source": 0}

    for section_name in sections_to_process:
        section_info = SECTIONS[section_name]
        fulltext_dir, source_suffix, target_suffix, lang_in, lang_out = \
            collect_files(section_name, section_info, args.direction)

        if not fulltext_dir.exists():
            print(f"\n[{section_name}] Fulltext dir not found: {fulltext_dir}")
            grand_total["no_source"] += 1
            continue

        source_files = sorted(fulltext_dir.glob(f"*{source_suffix}"))
        # Exclude already-translated files from source list
        source_files = [f for f in source_files
                        if not any(f.name.endswith(f".{lang}.md")
                                   for lang in ("zh", "en") if f".{lang}.md" != source_suffix)]

        if args.file:
            source_files = [f for f in source_files if f.stem == args.file]
            if not source_files:
                print(f"\n[{section_name}] File not found: {args.file}{source_suffix}")
                continue

        if not source_files:
            print(f"\n[{section_name}] No source files found in {fulltext_dir}")
            continue

        print(f"\n{'=' * 60}")
        print(f"[{section_name.upper()}] {lang_in.upper()} -> {lang_out.upper()}")
        print(f"Source dir: {fulltext_dir}")
        print(f"Files: {len(source_files)}")
        print(f"Source suffix: {source_suffix} -> Target suffix: {target_suffix}")
        print("-" * 60)

        translated = 0
        skipped = 0
        failed = 0

        for src in source_files:
            stem = src.stem
            if stem.endswith(f".{lang_out}"):
                continue
            target_path = src.parent / f"{stem}{target_suffix}"

            if target_path.exists() and not args.force:
                print(f"  [SKIP] {src.name} -> {target_path.name} exists "
                      f"({target_path.stat().st_size} bytes)")
                skipped += 1
                continue

            if args.dry_run:
                size = src.stat().st_size
                print(f"  [DRY-RUN] Would translate: {src.name} ({size} bytes) "
                      f"-> {target_path.name}")
                continue

            print(f"  Translating: {src.name} -> {target_path.name}")
            start = time.time()
            try:
                ok = translate_file(src, target_path, lang_in=lang_in, lang_out=lang_out)
                elapsed = time.time() - start
                if ok:
                    zh_size = target_path.stat().st_size
                    print(f"    [OK] {target_path.name} ({zh_size} bytes, {elapsed:.1f}s)")
                    translated += 1
                else:
                    skipped += 1
            except Exception as e:
                elapsed = time.time() - start
                print(f"    [FAILED] {e} ({elapsed:.1f}s)")
                failed += 1

            if translated > 0:
                time.sleep(2)

        print(f"  Result: {translated} translated, {skipped} skipped, {failed} failed")
        grand_total["translated"] += translated
        grand_total["skipped"] += skipped
        grand_total["failed"] += failed

    print(f"\n{'=' * 60}")
    print(f"TOTAL: {grand_total['translated']} translated, "
          f"{grand_total['skipped']} skipped, "
          f"{grand_total['failed']} failed")
    if grand_total["no_source"] > 0:
        print(f"  ({grand_total['no_source']} sections had no fulltext directory)")


if __name__ == "__main__":
    main()
