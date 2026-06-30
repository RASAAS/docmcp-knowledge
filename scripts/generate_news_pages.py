#!/usr/bin/env python3
"""Generate VitePress markdown pages from regulatory_news JSON files.

Reads regulatory_news/{framework}.json and generates:
  - docs/en/news/index.md (English timeline)
  - docs/zh/news/index.md (Chinese timeline)
  - Per-framework pages (docs/{lang}/news/{framework}.md)

Run: python scripts/generate_news_pages.py
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
NEWS_DIR = REPO_ROOT / "regulatory_news"
DOCS_DIR = REPO_ROOT / "docs"

FRAMEWORKS = ["eu_mdr", "fda", "nmpa", "_shared"]

FRAMEWORK_NAMES = {
    "eu_mdr": {"en": "EU MDR/IVDR", "zh": "EU MDR/IVDR"},
    "fda": {"en": "FDA", "zh": "FDA"},
    "nmpa": {"en": "NMPA", "zh": "NMPA"},
    "_shared": {"en": "Shared Standards", "zh": "通用标准"},
}

CATEGORY_LABELS = {
    "regulation_update": {"en": "Regulation Update", "zh": "法规更新"},
    "guidance_new": {"en": "New Guidance", "zh": "新指南发布"},
    "standard_revision": {"en": "Standard Revision", "zh": "标准修订"},
    "recall": {"en": "Recall Notice", "zh": "召回通知"},
    "notice": {"en": "Notice", "zh": "公告通知"},
}

IMPORTANCE_EMOJI = {
    "high": "!!!",
    "medium": "!!",
    "low": "!",
}


def load_all_items() -> list[dict]:
    """Load and merge all news items from JSON files."""
    all_items: list[dict] = []
    for fw in FRAMEWORKS:
        fp = NEWS_DIR / f"{fw}.json"
        if not fp.exists():
            continue
        data = json.loads(fp.read_text(encoding="utf-8"))
        all_items.extend(data.get("items", []))
    all_items.sort(key=lambda x: x.get("published_date", ""), reverse=True)
    return all_items


def render_item_md(item: dict, lang: str) -> str:
    """Render a single news item as markdown."""
    title = item.get("title", {}).get(lang, item.get("title", {}).get("en", "Untitled"))
    summary = item.get("summary", {}).get(lang, item.get("summary", {}).get("en", ""))
    fw = item.get("framework", "")
    cat = item.get("category", "")
    importance = item.get("importance", "medium")
    source_url = item.get("source_url", "")
    source_name = item.get("source_name", "")
    published = item.get("published_date", "N/A")
    tags = item.get("tags", [])

    fw_label = FRAMEWORK_NAMES.get(fw, {}).get(lang, fw)
    cat_label = CATEGORY_LABELS.get(cat, {}).get(lang, cat)
    imp_mark = IMPORTANCE_EMOJI.get(importance, "")

    lines = [
        f"### {title}",
        "",
        f"**{published}** | {fw_label} | {cat_label} | {imp_mark} {importance.upper()}",
        "",
    ]
    if summary:
        lines.append(summary)
        lines.append("")
    if tags:
        tag_str = ", ".join(f"`{t}`" for t in tags)
        tag_label = "Tags" if lang == "en" else "标签"
        lines.append(f"**{tag_label}**: {tag_str}")
        lines.append("")
    if source_url:
        link_label = "View Source" if lang == "en" else "查看来源"
        source_text = f" ({source_name})" if source_name else ""
        lines.append(f"[{link_label}{source_text}]({source_url})")
        lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def generate_index_page(items: list[dict], lang: str) -> str:
    """Generate the main news index page."""
    if lang == "zh":
        title = "法规速递"
        desc = "医疗器械合规领域的最新法规动态、标准更新和指南发布。"
    else:
        title = "Regulatory News"
        desc = "Latest regulatory updates, standard revisions, and guidance publications in the medical device compliance space."

    lines = [
        "---",
        f"title: {title}",
        "---",
        "",
        f"# {title}",
        "",
        f"> {desc}",
        "",
    ]

    if not items:
        no_news = "No news available yet." if lang == "en" else "暂无法规动态。"
        lines.append(no_news)
        return "\n".join(lines)

    for item in items:
        lines.append(render_item_md(item, lang))

    return "\n".join(lines)


def main():
    all_items = load_all_items()
    print(f"Loaded {len(all_items)} news items total")

    for lang in ["en", "zh"]:
        out_dir = DOCS_DIR / lang / "news"
        out_dir.mkdir(parents=True, exist_ok=True)

        index_content = generate_index_page(all_items, lang)
        index_path = out_dir / "index.md"
        index_path.write_text(index_content, encoding="utf-8")
        print(f"  Generated {index_path}")

        for fw in FRAMEWORKS:
            fw_items = [i for i in all_items if i.get("framework") == fw]
            if not fw_items:
                continue
            fw_name = FRAMEWORK_NAMES.get(fw, {}).get(lang, fw)
            fw_content = generate_index_page(fw_items, lang)
            fw_content = fw_content.replace(
                f"# {'法规速递' if lang == 'zh' else 'Regulatory News'}",
                f"# {fw_name} {'法规速递' if lang == 'zh' else 'Regulatory News'}",
                1
            )
            fw_path = out_dir / f"{fw}.md"
            fw_path.write_text(fw_content, encoding="utf-8")
            print(f"  Generated {fw_path}")

    print("Done.")


if __name__ == "__main__":
    main()
