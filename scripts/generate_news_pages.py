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

FRAMEWORKS = [
    "eu_mdr", "fda", "nmpa",
    "uk_mhra", "canada", "australia_tga", "japan_pmda", "korea_mfds",
    "switzerland", "brazil_anvisa", "saudi_sfda", "singapore_hsa",
    "mexico_cofepris", "argentina_anmat", "newzealand_medsafe",
    "taiwan_tfda", "indonesia_bpom", "malaysia_mda",
    "thailand_fda", "israel_moh", "hongkong_mdco", "india_cdsco",
]

FRAMEWORK_NAMES = {
    "eu_mdr": {"en": "EU MDR/IVDR", "zh": "EU MDR/IVDR"},
    "fda": {"en": "FDA", "zh": "FDA"},
    "nmpa": {"en": "NMPA", "zh": "NMPA"},
    "uk_mhra": {"en": "UK MHRA", "zh": "UK MHRA"},
    "canada": {"en": "Health Canada", "zh": "Health Canada"},
    "australia_tga": {"en": "Australia TGA", "zh": "Australia TGA"},
    "japan_pmda": {"en": "Japan PMDA", "zh": "Japan PMDA"},
    "korea_mfds": {"en": "Korea MFDS", "zh": "Korea MFDS"},
    "switzerland": {"en": "Swissmedic", "zh": "Swissmedic"},
    "brazil_anvisa": {"en": "Brazil ANVISA", "zh": "Brazil ANVISA"},
    "saudi_sfda": {"en": "Saudi SFDA", "zh": "Saudi SFDA"},
    "singapore_hsa": {"en": "Singapore HSA", "zh": "Singapore HSA"},
    "india_cdsco": {"en": "India CDSCO", "zh": "India CDSCO"},
    "mexico_cofepris": {"en": "Mexico COFEPRIS", "zh": "Mexico COFEPRIS"},
    "argentina_anmat": {"en": "Argentina ANMAT", "zh": "Argentina ANMAT"},
    "taiwan_tfda": {"en": "Taiwan TFDA", "zh": "Taiwan TFDA"},
    "newzealand_medsafe": {"en": "New Zealand Medsafe", "zh": "New Zealand Medsafe"},
    "indonesia_bpom": {"en": "Indonesia BPOM", "zh": "Indonesia BPOM"},
    "malaysia_mda": {"en": "Malaysia MDA", "zh": "Malaysia MDA"},
    "thailand_fda": {"en": "Thailand FDA", "zh": "Thailand FDA"},
    "israel_moh": {"en": "Israel MOH", "zh": "Israel MOH"},
    "hongkong_mdco": {"en": "Hong Kong MDCO", "zh": "Hong Kong MDCO"},
}

AGENCY_URLS = {
    "india_cdsco": "https://cdsco.gov.in/",
    "taiwan_tfda": "https://www.fda.gov.tw/",
    "indonesia_bpom": "https://www.pom.go.id/",
    "malaysia_mda": "https://www.mda.gov.my/",
    "thailand_fda": "https://www.fda.moph.go.th/",
    "israel_moh": "https://www.gov.il/en/departments/ministry_of_health/",
    "hongkong_mdco": "https://www.mdco.gov.hk/",
}

CATEGORY_LABELS = {
    "regulation_update": {"en": "Regulation Update", "zh": "\u6cd5\u89c4\u66f4\u65b0"},
    "guidance_new": {"en": "New Guidance", "zh": "\u65b0\u6307\u5357\u53d1\u5e03"},
    "standard_revision": {"en": "Standard Revision", "zh": "\u6807\u51c6\u4fee\u8ba2"},
    "recall": {"en": "Recall Notice", "zh": "\u53ec\u56de\u901a\u77e5"},
    "notice": {"en": "Notice", "zh": "\u516c\u544a\u901a\u77e5"},
    "safety_communication": {"en": "Safety Communication", "zh": "\u5b89\u5168\u901a\u62a5"},
    "product_approval": {"en": "Product Approval", "zh": "\u4ea7\u54c1\u5ba1\u6279"},
    "enforcement": {"en": "Enforcement", "zh": "\u6267\u6cd5\u884c\u52a8"},
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


def generate_index_page(items: list[dict], lang: str, framework: str = "") -> str:
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
        agency_url = AGENCY_URLS.get(framework, "")
        fw_name = FRAMEWORK_NAMES.get(framework, {}).get(lang, framework)
        if framework and agency_url:
            if lang == "zh":
                lines.append(f"::: info 数据源对接中")
                lines.append(f"{fw_name} 的官方数据源正在对接中。该机构官方网站使用动态渲染技术，暂时无法通过自动化方式采集。")
                lines.append(f"")
                lines.append(f"请直接访问官方网站获取最新信息：[{fw_name} 官网]({agency_url})")
                lines.append(f":::")
            else:
                lines.append(f"::: info Data Source Integration In Progress")
                lines.append(f"The official data source for {fw_name} is currently being integrated. The agency website uses dynamic rendering and cannot be automatically collected at this time.")
                lines.append(f"")
                lines.append(f"Please visit the official website for the latest information: [{fw_name} Official Site]({agency_url})")
                lines.append(f":::")
        else:
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
            fw_name = FRAMEWORK_NAMES.get(fw, {}).get(lang, fw)
            fw_content = generate_index_page(fw_items, lang, framework=fw)
            fw_content = fw_content.replace(
                f"# {'法规速递' if lang == 'zh' else 'Regulatory News'}",
                f"# {fw_name} {'法规速递' if lang == 'zh' else 'Regulatory News'}",
                1
            )
            fw_path = out_dir / f"{fw}.md"
            fw_path.write_text(fw_content, encoding="utf-8")
            print(f"  Generated {fw_path} ({len(fw_items)} items)")

    print("Done.")


if __name__ == "__main__":
    main()
