#!/usr/bin/env python3
"""Promote NMPA guidance fulltext into data-layer *.zh.md stubs.

For each active `_index.json` entry that has fulltext but no
`nmpa/guidance/{slug}.zh.md`, create a VitePress/data-layer page with
frontmatter matching existing conventions and body from fulltext.

Skips drafts/catalogs. When old + new revision siblings exist, prefers the
latest revision and does not promote clearly superseded older versions if a
newer 修订版 is already published or also being promoted.

Usage:
    python scripts/promote_nmpa_guidance_fulltext.py
    python scripts/promote_nmpa_guidance_fulltext.py --dry-run
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parent.parent
GUIDANCE_DIR = ROOT / "nmpa" / "guidance"
FULLTEXT_DIR = GUIDANCE_DIR / "fulltext"
INDEX_PATH = GUIDANCE_DIR / "_index.json"

# Reuse draft/catalog detectors from fetch script when importable
sys.path.insert(0, str(ROOT / "scripts"))
try:
    from fetch_nmpa_fulltext import is_catalog_content, is_draft_content
except Exception:  # pragma: no cover
    def is_draft_content(text: str) -> bool:
        return bool(re.search(r"征求意见稿", (text or "")[:3000]))

    def is_catalog_content(text: str) -> bool:
        return False


def strip_year_revision(title: str) -> str:
    """Normalize title core for revision sibling detection (aligned with expand_index_v2)."""
    t = re.sub(r"[（(]\d{4}年?\s*修订版[）)]", "", title)
    t = re.sub(r"\d{4}年?\s*修订版", "", t)
    t = re.sub(r"注册技术审查指导原则", "注册审查指导原则", t)
    t = re.sub(r"注册技术指导原则", "注册审查指导原则", t)
    t = re.sub(r"技术审查指导原则", "审查指导原则", t)
    return t.strip()


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


def find_fulltext(slug: str) -> Optional[Path]:
    for name in (f"{slug}.zh.md", f"{slug}.md"):
        path = FULLTEXT_DIR / name
        if path.exists():
            return path
    return None


def existing_data_slugs() -> set[str]:
    return {p.name[: -len(".zh.md")] for p in GUIDANCE_DIR.glob("*.zh.md")}


def yaml_quote(value: str) -> str:
    if value == "":
        return "''"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return f"'{value}'"
    if re.search(r"[:#\[\]{}|>*&!%@`,]", value) or value != value.strip() or "\n" in value:
        return json.dumps(value, ensure_ascii=False)
    return value


def build_frontmatter(
    *,
    entry_id: str,
    title_zh: str,
    title_en: str,
    doc_number: str,
    source_url: str,
    effective_date: str,
    status: str = "active",
) -> str:
    lines = [
        "---",
        f"id: {yaml_quote(entry_id)}",
        "title:",
        f"  zh: {yaml_quote(title_zh)}",
        f"  en: {yaml_quote(title_en or '')}",
        "regulation: nmpa",
        "category: nmpa/guidance",
        f"status: {status}",
    ]
    if doc_number:
        lines.append(f"document_number: {yaml_quote(doc_number)}")
    if source_url:
        lines.append(f"source_url: {yaml_quote(source_url)}")
    lines.extend(
        [
            "source_format: markdown",
            "translation: original",
            f"effective_date: {yaml_quote(effective_date)}",
            "contributor: RASAAS",
            "promoted_from: fulltext",
            "---",
            "",
        ]
    )
    return "\n".join(lines)


def prepare_body(fulltext: str, title_zh: str) -> str:
    body = fulltext.strip()
    # Drop YAML frontmatter if a fulltext file accidentally has one
    if body.startswith("---"):
        end = body.find("\n---", 3)
        if end > 0:
            body = body[end + 4 :].lstrip("\n")
    # Ensure leading H1
    if not re.match(r"^#\s+", body):
        body = f"# {title_zh}\n\n{body}"
    else:
        # Normalize first H1 to official title when present
        body = re.sub(r"^#\s+.+", f"# {title_zh}", body, count=1)
    if not body.endswith("\n"):
        body += "\n"
    return body


def revision_score(entry: dict) -> tuple[int, int]:
    """Higher is better: prefer higher year, then titles marked 修订."""
    title = (entry.get("title") or {}).get("zh", "") if isinstance(entry.get("title"), dict) else str(entry.get("title") or "")
    doc = entry.get("doc_number") or ""
    year = infer_year(title, doc, entry.get("slug", "")) or 0
    is_rev = 1 if ("修订" in title) else 0
    return (year, is_rev)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0, help="Optional max promotes (0=all)")
    args = parser.parse_args()

    index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    entries = index.get("entries", [])
    data_slugs = existing_data_slugs()

    # Candidates: active + has fulltext + missing data .zh.md
    candidates: list[dict] = []
    skipped_draft = 0
    skipped_catalog = 0
    skipped_short = 0
    missing_ft = 0

    for entry in entries:
        if entry.get("status") != "active":
            continue
        slug = entry.get("slug") or ""
        if not slug or slug in data_slugs:
            continue
        ft = find_fulltext(slug)
        if not ft:
            missing_ft += 1
            continue
        text = ft.read_text(encoding="utf-8", errors="ignore")
        title = (entry.get("title") or {}).get("zh", "") if isinstance(entry.get("title"), dict) else str(entry.get("title") or "")
        if is_draft_content(text) or "征求意见稿" in title:
            skipped_draft += 1
            continue
        if is_catalog_content(text):
            skipped_catalog += 1
            continue
        if len(text.strip()) < 200:
            skipped_short += 1
            continue
        candidates.append({**entry, "_fulltext_path": str(ft), "_title_zh": title, "_body": text})

    # Prefer latest revision among siblings (including already-published data slugs)
    by_core: dict[str, list[dict]] = defaultdict(list)
    all_active = [e for e in entries if e.get("status") == "active"]
    for e in all_active:
        title = (e.get("title") or {}).get("zh", "") if isinstance(e.get("title"), dict) else str(e.get("title") or "")
        by_core[strip_year_revision(title)].append(e)

    cand_by_slug = {e["slug"]: e for e in candidates}
    skip_old: set[str] = set()
    for core, group in by_core.items():
        if len(group) < 2:
            continue
        ranked = sorted(group, key=revision_score, reverse=True)
        best = ranked[0]
        best_score = revision_score(best)
        for other in ranked[1:]:
            if other["slug"] not in cand_by_slug:
                continue
            # Skip promoting older sibling when a newer one exists in catalog
            # and either is already published or also a promote candidate.
            if revision_score(other) < best_score:
                if best["slug"] in data_slugs or best["slug"] in cand_by_slug:
                    skip_old.add(other["slug"])

    to_promote = [e for e in candidates if e["slug"] not in skip_old]
    if args.limit and args.limit > 0:
        to_promote = to_promote[: args.limit]

    promoted = 0
    failures: list[str] = []

    for entry in to_promote:
        slug = entry["slug"]
        title_zh = entry["_title_zh"] or slug
        title_en = ""
        if isinstance(entry.get("title"), dict):
            title_en = entry["title"].get("en") or ""
        doc_number = entry.get("doc_number") or ""
        source_url = entry.get("source_url") or ""
        year = infer_year(title_zh, doc_number, slug)
        effective_date = f"{year}-01-01" if year else "2020-01-01"
        entry_id = entry.get("id") or f"nmpa-{slug}"

        try:
            body = prepare_body(entry["_body"], title_zh)
            fm = build_frontmatter(
                entry_id=entry_id,
                title_zh=title_zh,
                title_en=title_en,
                doc_number=doc_number,
                source_url=source_url,
                effective_date=effective_date,
            )
            out = GUIDANCE_DIR / f"{slug}.zh.md"
            content = fm + body
            if args.dry_run:
                print(f"  [DRY] promote {slug} <- {Path(entry['_fulltext_path']).name} ({len(body)} chars)")
            else:
                if out.exists():
                    failures.append(f"{slug}: target already exists")
                    continue
                out.write_text(content, encoding="utf-8")
                print(f"  [OK] {slug}")
            promoted += 1
        except Exception as exc:  # noqa: BLE001
            failures.append(f"{slug}: {exc}")

    print(
        "\nSummary:\n"
        f"  candidates_raw={len(candidates)}\n"
        f"  skipped_old_revision={len(skip_old)}\n"
        f"  skipped_draft={skipped_draft}\n"
        f"  skipped_catalog={skipped_catalog}\n"
        f"  skipped_short={skipped_short}\n"
        f"  promoted={promoted}\n"
        f"  failures={len(failures)}"
    )
    if skip_old:
        print("  skipped_old_slugs:", ", ".join(sorted(skip_old)[:20]), ("..." if len(skip_old) > 20 else ""))
    if failures:
        print("  failure_details:")
        for f in failures[:30]:
            print("   -", f)


if __name__ == "__main__":
    main()
