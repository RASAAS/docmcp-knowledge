"""Translate IMDRF fulltext Markdown files (EN -> ZH) via local translation API.

Uses the med-doc-translator text API endpoint to translate each section
of the Markdown files while preserving structure, images, links, and tables.

Usage:
    python scripts/translate_fulltext.py                 # translate all missing .zh.md
    python scripts/translate_fulltext.py --force          # re-translate all
    python scripts/translate_fulltext.py --file <id>      # translate one specific file
    python scripts/translate_fulltext.py --dry-run        # show what would be translated
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

import requests

FULLTEXT_DIR = Path(__file__).resolve().parent.parent / "_shared" / "imdrf" / "fulltext"
TRANSLATE_API = "http://100.93.45.36:8050/api/translate/text"

HEADING_RE = re.compile(r"^(#{1,6}\s+)")
SKIP_LINE_PATTERNS = [
    re.compile(r"^\s*$"),
    re.compile(r"^!\[.*\]\(data:image"),
    re.compile(r"^---\s*$"),
    re.compile(r"^\*\*Source\*\*:"),
    re.compile(r"^\*\*Document Number\*\*:"),
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
    """Split Markdown into translatable sections.

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

    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.post(TRANSLATE_API, json=payload, timeout=300)
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


def translate_in_batches(segments: list[str], batch_size: int = 30) -> list[str]:
    """Translate segments in batches to stay within API limits."""
    results: list[str] = []
    total = len(segments)

    for start in range(0, total, batch_size):
        batch = segments[start:start + batch_size]
        end = min(start + batch_size, total)
        print(f"    Translating segments {start+1}-{end}/{total}...")

        translated = call_translate_api(batch)
        results.extend(translated)

        if end < total:
            time.sleep(1)

    return results


def translate_file(source_path: Path, output_path: Path) -> bool:
    """Translate a single Markdown fulltext file."""
    content = source_path.read_text(encoding="utf-8")

    first_heading = ""
    for line in content.split("\n"):
        if line.startswith("# "):
            first_heading = line
            break

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

    translated = translate_in_batches(all_segments)

    output_lines: list[str] = []
    seg_idx = 0

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


def main():
    parser = argparse.ArgumentParser(description="Translate IMDRF fulltext EN -> ZH")
    parser.add_argument("--force", action="store_true", help="Re-translate existing .zh.md files")
    parser.add_argument("--file", type=str, help="Translate a specific file ID (without .md)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be translated")
    args = parser.parse_args()

    if not FULLTEXT_DIR.exists():
        print(f"Fulltext directory not found: {FULLTEXT_DIR}")
        sys.exit(1)

    source_files = sorted(FULLTEXT_DIR.glob("*.md"))
    source_files = [f for f in source_files if not f.name.endswith(".zh.md")]

    if args.file:
        source_files = [f for f in source_files if f.stem == args.file]
        if not source_files:
            print(f"File not found: {args.file}.md")
            sys.exit(1)

    print(f"IMDRF Fulltext Translation (EN -> ZH)")
    print(f"Source dir: {FULLTEXT_DIR}")
    print(f"API: {TRANSLATE_API}")
    print(f"Files: {len(source_files)}")
    print()

    # Health check
    try:
        r = requests.get(TRANSLATE_API.replace("/translate/text", "/health"), timeout=5)
        r.raise_for_status()
        print(f"API health: OK")
    except Exception as e:
        print(f"API health check failed: {e}")
        sys.exit(1)

    translated = 0
    skipped = 0
    failed = 0

    for src in source_files:
        zh_path = src.with_suffix(".zh.md")
        if zh_path.exists() and not args.force:
            print(f"  [SKIP] {src.name} -> .zh.md exists ({zh_path.stat().st_size} bytes)")
            skipped += 1
            continue

        if args.dry_run:
            size = src.stat().st_size
            print(f"  [DRY-RUN] Would translate: {src.name} ({size} bytes)")
            continue

        print(f"  Translating: {src.name}")
        start = time.time()
        try:
            ok = translate_file(src, zh_path)
            elapsed = time.time() - start
            if ok:
                zh_size = zh_path.stat().st_size
                print(f"    [OK] {zh_path.name} ({zh_size} bytes, {elapsed:.1f}s)")
                translated += 1
            else:
                skipped += 1
        except Exception as e:
            elapsed = time.time() - start
            print(f"    [FAILED] {e} ({elapsed:.1f}s)")
            failed += 1

        if translated > 0:
            time.sleep(2)

    print(f"\nDone: {translated} translated, {skipped} skipped, {failed} failed")


if __name__ == "__main__":
    main()
