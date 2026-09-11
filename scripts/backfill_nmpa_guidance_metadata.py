#!/usr/bin/env python3
"""Backfill document_number / effective_date on nmpa/guidance/*.zh.md from _index.json.

P0 metadata sync:
- Match data-layer slugs to _index.json entries and copy doc_number → document_number
- Replace migration effective_date values (2025-04-*) with years inferred from
  title / doc_number / slug when possible
- Mark known superseded published pairs (status + superseded_by); leave body notes

Usage:
    python scripts/backfill_nmpa_guidance_metadata.py
    python scripts/backfill_nmpa_guidance_metadata.py --dry-run
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Optional

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
GUIDANCE_DIR = ROOT / "nmpa" / "guidance"
INDEX_PATH = GUIDANCE_DIR / "_index.json"

SUPERSEDED_PAIRS = {
    "disposable-nasal-oxygen-cannula-2013": "disposable-nasal-oxygen-cannula-2024",
    "drainage-tubes-guidance": "disposable-drainage-tube-2024",
    "magnetic-therapy-device-2016": "magnetic-therapy-device-2024",
    "medical-nebulizer-2016": "medical-nebulizer-2024",
    "cmde-2009-95": "endotracheal-intubation-2024",
}


def split_frontmatter(text: str) -> tuple[Optional[dict], str]:
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end < 0:
        return None, text
    fm_raw = text[3:end].strip("\n")
    body = text[end + 4 :]
    if body.startswith("\n"):
        body = body[1:]
    try:
        fm = yaml.safe_load(fm_raw) or {}
    except yaml.YAMLError:
        return None, text
    if not isinstance(fm, dict):
        return None, text
    return fm, body


def yq(value: Any) -> str:
    if value is None:
        return "''"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    sv = str(value)
    if sv == "":
        return "''"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", sv):
        return f"'{sv}'"
    if re.search(r"[:#\[\]{}|>*&!%@`,]", sv) or "\n" in sv or sv != sv.strip():
        return json.dumps(sv, ensure_ascii=False)
    return sv


def dump_frontmatter(fm: dict) -> str:
    preferred = [
        "id", "title", "regulation", "category", "status", "superseded_by",
        "document_number", "source_url", "source_url_verified", "source_url_status",
        "source_format", "translation", "last_verified", "contributor",
        "migrated_from", "wordpress_id", "effective_date", "published_date",
        "promoted_from",
    ]
    lines = ["---"]
    keys = [k for k in preferred if k in fm] + [k for k in fm.keys() if k not in preferred]

    def emit_scalar(key: str, value: Any, indent: str = "") -> None:
        lines.append(f"{indent}{key}: {yq(value)}")

    for key in keys:
        value = fm[key]
        if isinstance(value, dict):
            lines.append(f"{key}:")
            for ck, cv in value.items():
                emit_scalar(ck, cv, indent="  ")
        elif isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"- {yq(item)}")
        else:
            emit_scalar(key, value)
    lines.append("---")
    return "\n".join(lines) + "\n"


def title_zh(fm: dict) -> str:
    t = fm.get("title", "")
    if isinstance(t, dict):
        return t.get("zh", "") or ""
    return str(t or "")


def infer_year(title: str, doc_number: str, slug: str) -> Optional[int]:
    preferred: list[int] = []
    for pat in (
        r"[（(](19\d{2}|20\d{2})\s*年?\s*修订",
        r"(19\d{2}|20\d{2})\s*年?\s*修订",
        r"\[(19\d{2}|20\d{2})\]",
        r"〔(19\d{2}|20\d{2})〕",
        r"(19\d{2}|20\d{2})年第?\d*号",
    ):
        for src in (title, doc_number):
            for m in re.finditer(pat, src or ""):
                preferred.append(int(m.group(1)))
    if preferred:
        return max(preferred)
    years: list[int] = []
    for src in (title, doc_number, slug):
        for m in re.finditer(r"(19\d{2}|20\d{2})", src or ""):
            y = int(m.group(1))
            if 1990 <= y <= 2026:
                years.append(y)
    return max(years) if years else None


def infer_doc_number_from_title(title: str) -> str:
    patterns = [
        r"((?:国食药监械|食药监械|食药监办械函|药监综械|国药监械|国家药监局)[^，。\n]{0,12}\[[12]\d{3}\]\d+号)",
        r"((?:国食药监械|食药监械|食药监办械函|药监综械|国药监械)〔[12]\d{3}〕\d+号)",
        r"((?:国食药监械|食药监械|食药监办械函|药监综械|国药监械)\[[12]\d{3}\]\d+号)",
    ]
    for pat in patterns:
        m = re.search(pat, title)
        if m:
            return m.group(1)
    m = re.search(r"[（(]((?:19|20)\d{2})年第(\d+)号[）)]", title)
    if m:
        return f"{m.group(1)}年第{m.group(2)}号"
    return ""


def is_migration_date(value: Any) -> bool:
    if value is None:
        return False
    s = str(value).strip().strip("'\"")
    return s.startswith("2025-04-")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    by_slug = {e["slug"]: e for e in index.get("entries", []) if e.get("slug")}

    updated = 0
    dn_filled = 0
    date_fixed = 0
    superseded_marked = 0

    for path in sorted(GUIDANCE_DIR.glob("*.zh.md")):
        slug = path.name[: -len(".zh.md")]
        text = path.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        if fm is None:
            continue

        changed = False
        entry = by_slug.get(slug)

        if entry and entry.get("doc_number"):
            current = str(fm.get("document_number") or "").strip()
            if not current:
                fm["document_number"] = entry["doc_number"]
                dn_filled += 1
                changed = True

        if not str(fm.get("document_number") or "").strip():
            inferred = infer_doc_number_from_title(title_zh(fm))
            if inferred:
                fm["document_number"] = inferred
                dn_filled += 1
                changed = True

        if entry and entry.get("source_url") and not str(fm.get("source_url") or "").strip():
            fm["source_url"] = entry["source_url"]
            changed = True

        title = title_zh(fm)
        doc_num = str(fm.get("document_number") or (entry or {}).get("doc_number") or "")
        if is_migration_date(fm.get("effective_date")):
            year = infer_year(title, doc_num, slug)
            if year and year != 2025:
                fm["effective_date"] = f"{year}-01-01"
                date_fixed += 1
                changed = True

        if slug in SUPERSEDED_PAIRS:
            new_slug = SUPERSEDED_PAIRS[slug]
            if fm.get("status") != "superseded":
                fm["status"] = "superseded"
                changed = True
            if fm.get("superseded_by") != new_slug:
                fm["superseded_by"] = new_slug
                superseded_marked += 1
                changed = True
            note_markers = ("该指导原则已修订", "该指南已更新", "该指导原则已更新", "**已修订：**")
            if not any(m in body[:1000] for m in note_markers):
                note = (
                    f"\n> **已修订：** 请参阅新版 "
                    f"[`{new_slug}`](/zh/nmpa/guidance/{new_slug})。\n"
                )
                if body.lstrip().startswith("# "):
                    nl = body.find("\n")
                    if nl > 0:
                        body = body[: nl + 1] + note + body[nl + 1 :]
                        changed = True
                else:
                    body = note + body
                    changed = True

        if not changed:
            continue

        new_text = dump_frontmatter(fm) + "\n" + body.lstrip("\n")
        if not new_text.endswith("\n"):
            new_text += "\n"

        if args.dry_run:
            print(
                f"  [DRY] {slug}: dn={fm.get('document_number', '')} "
                f"date={fm.get('effective_date', '')} status={fm.get('status')}"
            )
        else:
            path.write_text(new_text, encoding="utf-8")
            print(f"  [OK] {slug}")
        updated += 1

    print(
        f"\nDone: updated={updated} document_number_filled={dn_filled} "
        f"dates_fixed={date_fixed} superseded_marked={superseded_marked}"
    )


if __name__ == "__main__":
    main()
