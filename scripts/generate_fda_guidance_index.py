#!/usr/bin/env python3
"""Generate English FDA CDRH guidance index + per-document pages from _index.json.

Does NOT bulk-write Chinese pages. ZH index is a pointer to the English catalog;
the 3 existing ZH fulltext pages are left untouched.

Usage:
    python scripts/generate_fda_guidance_index.py
    python scripts/generate_fda_guidance_index.py --dry-run
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from json_to_markdown import _escape_vue_tags  # noqa: E402

INDEX_PATH = ROOT / "fda" / "guidance" / "_index.json"
FULLTEXT_DIR = ROOT / "fda" / "guidance" / "fulltext"
DOCS_EN = ROOT / "docs" / "en" / "fda"
DOCS_ZH = ROOT / "docs" / "zh" / "fda"
SIDEBAR_EN = ROOT / "docs" / ".vitepress" / "sidebar-en.ts"

PRESERVE_SLUGS = {
    "cybersecurity-premarket",
    "postmarket-cybersecurity",
    "remanufacturing",
}

CATEGORY_META = [
    ("digital_health_cyber", "Digital Health & Cybersecurity"),
    ("premarket", "Premarket (510(k) / PMA / De Novo / IDE)"),
    ("quality_manufacturing", "Quality / QMSR / Manufacturing"),
    ("ivd", "IVD / Companion Diagnostics"),
    ("labeling_udi", "Labeling / UDI"),
    ("postmarket", "Postmarket / Recalls / Vigilance"),
    ("radiation_imaging", "Radiation / Imaging"),
    ("clinical_rwe", "Clinical / Real-World Evidence"),
    ("other", "General / Other"),
]
CAT_LABEL = {k: v for k, v in CATEGORY_META}

FULLTEXT_MARKER = "<!-- fulltext-start -->"
FULLTEXT_END_MARKER = "<!-- fulltext-end -->"


def load_index() -> dict:
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


def fulltext_body(entry: dict) -> str:
    slug = entry.get("slug") or ""
    path = FULLTEXT_DIR / f"{slug}.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""


def strip_fulltext_header(text: str) -> str:
    """Drop the leading # title / Source / Published block if present."""
    if "\n---\n" in text:
        return text.split("\n---\n", 1)[1].strip()
    return text.strip()


def render_en_page(entry: dict, fulltext: str) -> str:
    title = entry.get("title") or {}
    title_en = title.get("en") or ""
    title_zh = title.get("zh") or ""
    source_url = entry.get("source_url") or ""
    pdf_url = entry.get("pdf_url") or ""
    pub = entry.get("published_date") or ""
    cat = entry.get("fda_category") or "other"
    cat_label = CAT_LABEL.get(cat, cat)
    gtype = entry.get("guidance_type") or "Guidance Document"
    docket = entry.get("docket") or ""
    topics = entry.get("topics") or []
    topics_s = ", ".join(topics) if isinstance(topics, list) else str(topics)

    desc = title_zh or f"FDA CDRH Final {gtype}"
    lines = [
        "---",
        f"title: {json.dumps(title_en, ensure_ascii=False)}",
        f"description: {json.dumps(desc, ensure_ascii=False)}",
        f"published: {pub}",
        "---",
        "",
        f"# {title_en}",
        "",
    ]
    if pub:
        lines += [f"**Published**: {pub}", ""]
    lines += [
        f"**Status**: Final",
        f"**Type**: {gtype}",
        f"**Category**: {cat_label}",
    ]
    if topics_s:
        lines.append(f"**Topics**: {topics_s}")
    if docket:
        lines.append(f"**Docket**: {docket}")
    lines.append("")
    if source_url:
        lines += [
            "::: tip Official Source",
            f"[{source_url}]({source_url})",
        ]
        if pdf_url:
            lines.append(f"PDF: [{pdf_url}]({pdf_url})")
        lines += [":::", ""]

    if fulltext.strip():
        body = strip_fulltext_header(fulltext)
        lines += [
            FULLTEXT_MARKER,
            "",
            "---",
            "",
            "## Official Full Text",
            "",
            _escape_vue_tags(body),
            "",
            FULLTEXT_END_MARKER,
            "",
        ]
    else:
        lines += [
            "::: warning",
            "Full text has not been extracted into this knowledge base. "
            "Use the official FDA source link above. This catalog page is metadata only.",
            ":::",
            "",
        ]
    return "\n".join(lines)


def render_en_index(entries: list[dict], has_fulltext: dict) -> str:
    by_cat: dict[str, list] = defaultdict(list)
    for e in entries:
        by_cat[e.get("fda_category") or "other"].append(e)

    ft_count = sum(1 for e in entries if has_fulltext.get(e.get("id"), False))
    lines = [
        "---",
        "title: FDA Guidance Documents",
        f"generated: '{date.today().isoformat()}'",
        f"doc_count: {len(entries)}",
        "---",
        "",
        "# FDA Guidance Documents",
        "",
        "Currently effective **CDRH Final** guidance (Guidance Document and Special Controls). "
        "Draft, CPG, Memorandum, and Small Entity Compliance Guides are excluded.",
        "",
        f"Total **{len(entries)}** documents, **{ft_count}** with extracted full text. "
        "Newest first within each category. Catalog pages without full text link to the official FDA source.",
        "",
        "## Categories",
        "",
    ]
    for cat, label in CATEGORY_META:
        n = len(by_cat.get(cat, []))
        if not n:
            continue
        lines.append(f"- [{label}](#{cat}) ({n})")
    lines.append("")

    for cat, label in CATEGORY_META:
        cat_entries = by_cat.get(cat, [])
        if not cat_entries:
            continue
        cat_entries = sorted(
            cat_entries,
            key=lambda e: (e.get("published_date") or "", e.get("title", {}).get("en") or ""),
            reverse=True,
        )
        ft_n = sum(1 for e in cat_entries if has_fulltext.get(e.get("id"), False))
        lines += [
            f"## {label} {{#{cat}}}",
            "",
            f"{len(cat_entries)} documents, {ft_n} with full text.",
            "",
        ]
        for e in cat_entries:
            title = (e.get("title") or {}).get("en") or e.get("slug")
            slug = e.get("slug") or ""
            pub = e.get("published_date") or ""
            suffix = f" ({pub})" if pub else ""
            marker = "" if has_fulltext.get(e.get("id"), False) else " _(catalog)_"
            lines.append(f"- [{title}](./guidance/{slug}){suffix}{marker}")
        lines.append("")
    return "\n".join(lines)


def render_zh_index(entries: list[dict]) -> str:
    preserved = [e for e in entries if e.get("slug") in PRESERVE_SLUGS]
    lines = [
        "---",
        "title: FDA 指南文件",
        "---",
        "",
        "# FDA 指南文件",
        "",
        "本波次以**英文目录**为准：已同步目前有效的 CDRH Final 指南（Guidance Document 与 Special Controls）。",
        "中文全文仍为既有 3 篇；其余条目请查阅 [English catalog](/en/fda/guidance)。",
        "",
        f"英文目录共 **{len(entries)}** 份。已收录中文全文 **{len(preserved)}** 份：",
        "",
    ]
    for e in preserved:
        title = (e.get("title") or {}).get("zh") or (e.get("title") or {}).get("en")
        slug = e.get("slug")
        pub = e.get("published_date") or ""
        suffix = f" ({pub})" if pub else ""
        lines.append(f"- [{title}](./guidance/{slug}){suffix}")
    lines.append("")
    return "\n".join(lines)


def sidebar_items(entries: list[dict]) -> list:
    by_cat: dict[str, list] = defaultdict(list)
    for e in entries:
        by_cat[e.get("fda_category") or "other"].append(e)

    items = [
        {"text": "<- FDA Overview", "link": "/en/fda/"},
        {"text": "Guidance Index", "link": "/en/fda/guidance"},
    ]
    for cat, label in CATEGORY_META:
        cat_entries = by_cat.get(cat, [])
        if not cat_entries:
            continue
        cat_entries = sorted(
            cat_entries,
            key=lambda e: (e.get("published_date") or "", (e.get("title") or {}).get("en") or ""),
            reverse=True,
        )
        children = []
        for e in cat_entries:
            title = (e.get("title") or {}).get("en") or e.get("slug")
            # Sidebar labels stay short
            if len(title) > 72:
                title = title[:69] + "..."
            children.append({
                "text": title,
                "link": f"/en/fda/guidance/{e.get('slug')}",
            })
        items.append({
            "text": f"{label} ({len(cat_entries)})",
            "collapsed": True,
            "items": children,
        })
    return items


def merge_sidebar_en(entries: list[dict], dry_run: bool) -> None:
    payload = {"/en/fda/guidance/": sidebar_items(entries)}
    existing = {}
    if SIDEBAR_EN.exists():
        raw = SIDEBAR_EN.read_text(encoding="utf-8")
        try:
            existing = json.loads(raw.split("export default ", 1)[1])
        except Exception:
            existing = {}
    existing.update(payload)
    content = (
        "// Auto-generated by scripts/generate_docs_index.py — DO NOT EDIT\n"
        "export default " + json.dumps(existing, ensure_ascii=False, indent=2) + "\n"
    )
    if dry_run:
        print(f"  [DRY] Would write {SIDEBAR_EN.relative_to(ROOT)}")
        return
    SIDEBAR_EN.write_text(content, encoding="utf-8")
    print(f"  Wrote {SIDEBAR_EN.relative_to(ROOT)}")


def main():
    parser = argparse.ArgumentParser(description="Generate FDA CDRH EN guidance pages")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    data = load_index()
    entries = data.get("entries") or []
    print(f"Loaded {len(entries)} FDA guidance entries")

    has_fulltext = {}
    wrote_pages = 0
    for e in entries:
        slug = e.get("slug") or ""
        ft = fulltext_body(e)
        has_fulltext[e.get("id")] = bool(ft.strip())
        out = DOCS_EN / "guidance" / f"{slug}.md"
        # Always regenerate EN pages from cleaned fulltext (duplicate H1 /
        # rejoined paragraphs). PRESERVE_SLUGS still drives the ZH index list.
        page = render_en_page(e, ft)
        if args.dry_run:
            wrote_pages += 1
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")
        wrote_pages += 1

    en_index = render_en_index(entries, has_fulltext)
    zh_index = render_zh_index(entries)
    if args.dry_run:
        print(f"  [DRY] Would write {wrote_pages} EN pages")
        print(f"  [DRY] Would write docs/en/fda/guidance.md and docs/zh/fda/guidance.md")
    else:
        (DOCS_EN / "guidance.md").write_text(en_index, encoding="utf-8")
        (DOCS_ZH / "guidance.md").write_text(zh_index, encoding="utf-8")
        print(f"  Wrote {wrote_pages} EN pages")
        print("  Wrote docs/en/fda/guidance.md")
        print("  Wrote docs/zh/fda/guidance.md (pointer)")

    merge_sidebar_en(entries, dry_run=args.dry_run)

    ft_n = sum(1 for v in has_fulltext.values() if v)
    print(f"Fulltext: {ft_n} / {len(entries)}")


if __name__ == "__main__":
    main()
