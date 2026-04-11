#!/usr/bin/env python3
"""Translate fulltext documents using the Modal-deployed translation API.

Reads Chinese (.md) fulltext files, sends them to the TranslateGemma API
on Modal for zh->en translation, and saves the result as .en.md files.

The translation API processes text in segments to handle long documents.

Prerequisites:
    - TRANSLATE_API_URL env var (default: Modal endpoint)
    - TRANSLATE_API_TOKEN env var (Bearer token for auth)

Usage:
    python scripts/translate_fulltext.py --section nmpa/guidance --dry-run
    python scripts/translate_fulltext.py --section nmpa/guidance --limit 5
    python scripts/translate_fulltext.py --file nmpa/guidance/fulltext/cmde-2007-345.md
    python scripts/translate_fulltext.py --stats
"""

import argparse
import json
import logging
import os
import re
import sys
import time
from pathlib import Path
from typing import Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

KNOWLEDGE_ROOT = Path(__file__).parent.parent

DEFAULT_API_URL = (
    "https://m-yan82--translate-api-translateserver-serve.modal.run"
)
API_URL = os.getenv("TRANSLATE_API_URL", DEFAULT_API_URL)
API_TOKEN = os.getenv("TRANSLATE_API_TOKEN", "")

MAX_SEGMENTS_PER_REQUEST = 150
MAX_CHARS_PER_REQUEST = 400_000
SEGMENT_MIN_LENGTH = 20

# Markdown structural markers that should not be translated
SKIP_PATTERNS = [
    re.compile(r'^---\s*$'),
    re.compile(r'^\|[\s:|-]+\|$'),
    re.compile(r'^<!--.*-->$'),
    re.compile(r'^\s*$'),
    re.compile(r'^!\['),
    re.compile(r'^\*\*Source:\*\*'),
]


def should_skip_line(line: str) -> bool:
    """Check if a line should be kept as-is (not translated)."""
    for pattern in SKIP_PATTERNS:
        if pattern.match(line.strip()):
            return True
    return False


def is_table_row(line: str) -> bool:
    return line.strip().startswith('|') and line.strip().endswith('|')


def split_into_segments(text: str) -> list[dict]:
    """Split markdown text into translatable and non-translatable segments.

    Returns list of {"text": str, "translate": bool, "type": str}
    """
    lines = text.split('\n')
    segments = []
    current_translatable = []
    current_skip = []

    def flush_translatable():
        nonlocal current_translatable
        if current_translatable:
            joined = '\n'.join(current_translatable)
            if joined.strip():
                segments.append({
                    "text": joined,
                    "translate": True,
                    "type": "text",
                })
            current_translatable = []

    def flush_skip():
        nonlocal current_skip
        if current_skip:
            segments.append({
                "text": '\n'.join(current_skip),
                "translate": False,
                "type": "structural",
            })
            current_skip = []

    for line in lines:
        if should_skip_line(line):
            flush_translatable()
            current_skip.append(line)
        elif is_table_row(line):
            flush_translatable()
            flush_skip()
            segments.append({
                "text": line,
                "translate": True,
                "type": "table_row",
            })
        else:
            flush_skip()
            current_translatable.append(line)

    flush_translatable()
    flush_skip()

    return segments


def batch_segments(segments: list[dict]) -> list[list[dict]]:
    """Group translatable segments into API-friendly batches."""
    batches = []
    current_batch = []
    current_chars = 0

    for seg in segments:
        if not seg["translate"]:
            continue
        seg_chars = len(seg["text"])
        if (len(current_batch) >= MAX_SEGMENTS_PER_REQUEST or
                current_chars + seg_chars > MAX_CHARS_PER_REQUEST):
            if current_batch:
                batches.append(current_batch)
            current_batch = [seg]
            current_chars = seg_chars
        else:
            current_batch.append(seg)
            current_chars += seg_chars

    if current_batch:
        batches.append(current_batch)

    return batches


def translate_batch(texts: list[str], retries: int = 3) -> list[str]:
    """Call the translation API to translate a batch of texts."""
    import requests

    if not API_TOKEN:
        logger.error("TRANSLATE_API_TOKEN not set")
        return texts

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}",
    }
    payload = {
        "texts": texts,
        "lang_in": "zh",
        "lang_out": "en",
        "use_glossary": True,
    }

    for attempt in range(retries):
        try:
            resp = requests.post(
                f"{API_URL}/api/translate/text",
                json=payload,
                headers=headers,
                timeout=300,
            )
            resp.raise_for_status()
            data = resp.json()
            translations = data.get("translations", [])
            if len(translations) == len(texts):
                return translations
            logger.warning(f"  Translation count mismatch: "
                           f"sent {len(texts)}, got {len(translations)}")
            return translations + texts[len(translations):]
        except Exception as e:
            logger.warning(f"  Translation attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(5 * (attempt + 1))

    logger.error(f"  All translation attempts failed, returning originals")
    return texts


def translate_document(source_path: Path) -> Optional[str]:
    """Translate a Chinese markdown document to English."""
    text = source_path.read_text(encoding="utf-8")
    if not text.strip():
        return None

    segments = split_into_segments(text)
    translatable = [s for s in segments if s["translate"]]

    if not translatable:
        logger.warning(f"  No translatable content found")
        return None

    total_chars = sum(len(s["text"]) for s in translatable)
    logger.info(f"  {len(translatable)} segments, {total_chars} chars to translate")

    batches = batch_segments(segments)
    logger.info(f"  Split into {len(batches)} API batches")

    translation_map = {}
    for bi, batch in enumerate(batches):
        texts = [s["text"] for s in batch]
        logger.info(f"  Batch {bi + 1}/{len(batches)}: "
                    f"{len(texts)} segments, {sum(len(t) for t in texts)} chars")
        translated = translate_batch(texts)
        for seg, trans in zip(batch, translated):
            translation_map[id(seg)] = trans
        if bi < len(batches) - 1:
            time.sleep(2)

    result_parts = []
    for seg in segments:
        if seg["translate"]:
            trans = translation_map.get(id(seg), seg["text"])
            result_parts.append(trans)
        else:
            result_parts.append(seg["text"])

    return '\n'.join(result_parts)


def get_en_path(zh_path: Path) -> Path:
    """Get the English translation output path for a Chinese fulltext file."""
    stem = zh_path.stem
    if stem.endswith('.zh'):
        stem = stem[:-3]
    return zh_path.parent / f"{stem}.en.md"


def process_section(section: str, limit: int = 0, dry_run: bool = False,
                    force: bool = False):
    """Translate all fulltext files in a section (e.g. nmpa/guidance)."""
    parts = section.split('/')
    if len(parts) != 2:
        logger.error(f"Section must be framework/type (e.g. nmpa/guidance)")
        return

    framework, doc_type = parts
    fulltext_dir = KNOWLEDGE_ROOT / framework / doc_type / "fulltext"

    if not fulltext_dir.exists():
        logger.error(f"Directory not found: {fulltext_dir}")
        return

    zh_files = sorted(fulltext_dir.glob("*.md"))
    zh_files = [f for f in zh_files if not f.stem.endswith('.en')]

    candidates = []
    already_done = 0
    for zh_path in zh_files:
        en_path = get_en_path(zh_path)
        if not force and en_path.exists():
            already_done += 1
            continue
        candidates.append(zh_path)

    total_candidates = len(candidates)
    if limit > 0:
        candidates = candidates[:limit]

    logger.info(f"Translating {len(candidates)} files from {fulltext_dir}")
    logger.info(f"  Total ZH files: {len(zh_files)}, "
                f"Already translated: {already_done}, "
                f"Remaining: {total_candidates}")

    success = 0
    failed = 0

    for i, zh_path in enumerate(candidates):
        logger.info(f"[{i+1}/{len(candidates)}] {zh_path.name}")

        if dry_run:
            continue

        en_text = translate_document(zh_path)
        if not en_text:
            failed += 1
            continue

        en_path = get_en_path(zh_path)
        en_path.write_text(en_text, encoding="utf-8")
        logger.info(f"  Saved: {en_path.name} ({len(en_text)} chars)")
        success += 1

    logger.info(f"\nTranslation complete: {success} succeeded, {failed} failed")


def process_file(file_path: str, dry_run: bool = False):
    """Translate a single file."""
    path = KNOWLEDGE_ROOT / file_path
    if not path.exists():
        logger.error(f"File not found: {path}")
        return

    logger.info(f"Translating: {path.name}")

    if dry_run:
        segments = split_into_segments(path.read_text(encoding="utf-8"))
        translatable = [s for s in segments if s["translate"]]
        total_chars = sum(len(s["text"]) for s in translatable)
        logger.info(f"  Would translate {len(translatable)} segments, "
                    f"{total_chars} chars")
        return

    en_text = translate_document(path)
    if en_text:
        en_path = get_en_path(path)
        en_path.write_text(en_text, encoding="utf-8")
        logger.info(f"  Saved: {en_path.name} ({len(en_text)} chars)")


def show_stats():
    """Show translation statistics across all sections."""
    print(f"\n=== Fulltext Translation Statistics ===\n")

    for fw_dir in sorted(KNOWLEDGE_ROOT.iterdir()):
        if not fw_dir.is_dir() or fw_dir.name.startswith('.') or fw_dir.name in ('scripts', 'docs', 'schemas'):
            continue

        for type_dir in sorted(fw_dir.iterdir()):
            if not type_dir.is_dir():
                continue
            ft_dir = type_dir / "fulltext"
            if not ft_dir.exists():
                continue

            all_md = list(ft_dir.glob("*.md"))
            zh_files = [f for f in all_md if not f.stem.endswith('.en')]
            en_files = [f for f in all_md if f.stem.endswith('.en')]

            if not zh_files:
                continue

            translated = 0
            for zh_f in zh_files:
                en_path = get_en_path(zh_f)
                if en_path.exists():
                    translated += 1

            pct = translated / len(zh_files) * 100 if zh_files else 0
            section = f"{fw_dir.name}/{type_dir.name}"
            print(f"  {section:30s}  "
                  f"ZH: {len(zh_files):3d}  "
                  f"EN: {translated:3d}  "
                  f"({pct:.0f}%)")

    print()


def main():
    parser = argparse.ArgumentParser(
        description="Translate fulltext documents using Modal API",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--section", type=str,
                       help="Section to translate (e.g. nmpa/guidance)")
    group.add_argument("--file", type=str,
                       help="Single file to translate (relative to repo root)")
    group.add_argument("--stats", action="store_true",
                       help="Show translation coverage statistics")

    parser.add_argument("--limit", type=int, default=0,
                        help="Max files to translate (0 = all)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview without translating")
    parser.add_argument("--force", action="store_true",
                        help="Re-translate even if .en.md exists")
    args = parser.parse_args()

    if args.stats:
        show_stats()
    elif args.file:
        process_file(args.file, dry_run=args.dry_run)
    elif args.section:
        process_section(args.section, limit=args.limit,
                        dry_run=args.dry_run, force=args.force)


if __name__ == "__main__":
    main()
