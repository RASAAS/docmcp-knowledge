#!/usr/bin/env python3
"""
Generate VitePress docs index pages from data layer Markdown files.

Reads *.zh.md files from data directories (nmpa/, eu_mdr/, fda/, _shared/)
and generates/updates docs/zh/ index pages with document listings.

Usage:
    python scripts/generate_docs_index.py --output-root .
    python scripts/generate_docs_index.py --output-root . --regulation nmpa
    python scripts/generate_docs_index.py --output-root . --dry-run
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import unquote

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)


# Mapping: data layer dir -> (docs page path, section title, regulation, sync_content)
# sync_content=True: auto-generate index + sync full content files to docs/zh/
# sync_content=False: only generate index page (no full content sync)
#
# NOTE: eu_mdr/*, fda/*, _shared, nmpa/standards, nmpa/classification have
# hand-written index pages (PR #5/#6) — do NOT add them here.
SECTION_MAP = {
    "nmpa/guidance":            ("docs/zh/nmpa/guidance.md",            "NMPA 注册审查指导原则",   "nmpa",     True),
    "nmpa/regulations":         ("docs/zh/nmpa/regulations.md",         "NMPA 法规规章",           "nmpa",     True),
    "insights/nmpa-updates":    ("docs/zh/insights/nmpa-updates.md",    "NMPA 合规动态",           "insights", True),
    "insights/eu-mdr-updates":  ("docs/zh/insights/eu-mdr-updates.md",  "EU MDR 合规动态",         "insights", True),
    "insights/fda-updates":     ("docs/zh/insights/fda-updates.md",     "FDA 合规动态",            "insights", True),
    "insights/analysis":        ("docs/zh/insights/analysis.md",        "法规解读分析",            "insights", True),
    "insights/clinical-evaluation": ("docs/zh/insights/clinical-evaluation.md", "临床评价方法论", "insights", True),
}

# Category grouping for NMPA guidance — matched against Chinese title keywords (order matters: first match wins)
# Each entry: (keyword_in_title, group_name)
NMPA_GUIDANCE_GROUPS_ZH = [
    # 人工智能 / 软件
    ("人工智能", "人工智能与软件"),
    ("软件", "人工智能与软件"),
    ("算法", "人工智能与软件"),
    # 临床评价
    ("临床评价", "临床评价"),
    ("临床试验", "临床评价"),
    ("同品种", "临床评价"),
    ("免于临床", "临床评价"),
    # 注册申报
    ("注册申报", "注册申报"),
    ("备案资料", "注册申报"),
    ("申报资料", "注册申报"),
    ("注册收费", "注册申报"),
    ("说明书更改", "注册申报"),
    ("延续注册", "注册申报"),
    ("首次注册", "注册申报"),
    ("变更注册", "注册申报"),
    ("变更备案", "注册申报"),
    ("进口医疗器械", "注册申报"),
    ("自检", "注册申报"),
    # 创新与优先
    ("创新医疗器械", "创新与优先审批"),
    ("优先审批", "创新与优先审批"),
    # 骨科与植入
    ("骨科", "骨科与植入器械"),
    ("植入", "骨科与植入器械"),
    ("骨填充", "骨科与植入器械"),
    ("骨内固定", "骨科与植入器械"),
    ("骨修补", "骨科与植入器械"),
    ("颅骨", "骨科与植入器械"),
    ("种植", "骨科与植入器械"),
    # 心血管
    ("心血管", "心血管器械"),
    ("导管", "心血管器械"),
    ("球囊", "心血管器械"),
    ("支架", "心血管器械"),
    ("起搏", "心血管器械"),
    # 眼科
    ("眼科", "眼科器械"),
    ("近视", "眼科器械"),
    ("弱视", "眼科器械"),
    ("角膜", "眼科器械"),
    # 口腔
    ("口腔", "口腔器械"),
    ("牙科", "口腔器械"),
    ("牙", "口腔器械"),
    # 呼吸
    ("呼吸", "呼吸器械"),
    ("雾化", "呼吸器械"),
    ("通气", "呼吸器械"),
    ("复苏", "呼吸器械"),
    # 影像与诊断
    ("影像", "影像与诊断器械"),
    ("诊断", "影像与诊断器械"),
    ("造影", "影像与诊断器械"),
    ("射线", "影像与诊断器械"),
    ("内窥镜", "影像与诊断器械"),
    ("胃镜", "影像与诊断器械"),
    # 伤口与敷料
    ("敷料", "伤口护理与生物材料"),
    ("创面", "伤口护理与生物材料"),
    ("伤口", "伤口护理与生物材料"),
    ("胶原", "伤口护理与生物材料"),
    ("藻酸盐", "伤口护理与生物材料"),
    ("修复材料", "伤口护理与生物材料"),
    ("再生", "伤口护理与生物材料"),
    ("补片", "伤口护理与生物材料"),
    ("神经修复", "伤口护理与生物材料"),
    # 灭菌与生物相容性
    ("灭菌", "灭菌与生物相容性"),
    ("生物相容", "灭菌与生物相容性"),
    ("动物试验", "灭菌与生物相容性"),
    # 质量管理
    ("质量管理", "质量管理"),
    ("网络销售", "质量管理"),
    ("可用性", "质量管理"),
    ("基本原则", "质量管理"),
    # 输液与护理
    ("输液", "输液与护理器械"),
    ("引流", "输液与护理器械"),
    ("注射", "输液与护理器械"),
    ("穿刺", "输液与护理器械"),
    ("麻醉", "输液与护理器械"),
    ("鼻镜", "输液与护理器械"),
]


def read_front_matter(md_file: Path) -> Optional[dict]:
    """Parse YAML front matter from a Markdown file."""
    try:
        content = md_file.read_text(encoding="utf-8")
        if not content.startswith("---"):
            return None
        end = content.find("---", 3)
        if end == -1:
            return None
        fm_str = content[3:end].strip()
        return yaml.safe_load(fm_str)
    except Exception:
        return None


def get_doc_entries(data_dir: Path, section_key: str) -> List[dict]:
    """Read all .zh.md files in a data directory and extract metadata."""
    entries = []
    if not data_dir.exists():
        return entries

    for md_file in sorted(data_dir.glob("*.zh.md")):
        fm = read_front_matter(md_file)
        if not fm:
            continue

        title_zh = ""
        title_val = fm.get("title", {})
        if isinstance(title_val, dict):
            title_zh = title_val.get("zh", "")
        elif isinstance(title_val, str):
            title_zh = title_val

        if not title_zh:
            title_zh = md_file.stem.replace("-", " ").replace(".zh", "")

        entries.append({
            "slug": md_file.stem.replace(".zh", ""),
            "title_zh": title_zh,
            "doc_number": fm.get("document_number", ""),
            "effective_date": fm.get("effective_date", ""),
            "published_date": fm.get("published_date", ""),
            "status": fm.get("status", "active"),
            "source_url": fm.get("source_url", ""),
            "regulation": fm.get("regulation", ""),
            "category": fm.get("category", section_key),
            "file": md_file,
        })

    return entries


def group_nmpa_guidance(entries: List[dict]) -> Dict[str, List[dict]]:
    """Group NMPA guidance entries by device category using Chinese title keywords."""
    groups: Dict[str, List[dict]] = {"其他": []}

    for entry in entries:
        title = entry["title_zh"]
        matched = False
        for keyword, group_name in NMPA_GUIDANCE_GROUPS_ZH:
            if keyword in title:
                if group_name not in groups:
                    groups[group_name] = []
                groups[group_name].append(entry)
                matched = True
                break
        if not matched:
            groups["其他"].append(entry)

    # Remove empty groups
    return {k: v for k, v in groups.items() if v}


def format_entry_line(entry: dict, data_root: Path, docs_page: Path) -> str:
    """Format a single document entry as a Markdown list item with link."""
    title = entry["title_zh"]
    slug = entry["slug"]
    doc_num = entry["doc_number"]
    date = entry["effective_date"][:7] if entry["entry"].get("effective_date", "") else entry["effective_date"]

    # Relative path from docs page to data file
    data_file = entry["file"]
    try:
        rel = data_file.relative_to(data_root)
        # VitePress link: relative from docs page
        docs_dir = docs_page.parent
        # Calculate relative path
        link = "/" + str(rel).replace("\\", "/").replace(".zh.md", "")
    except ValueError:
        link = "#"

    parts = [f"[{title}]({link})"]
    if doc_num:
        parts.append(f"`{doc_num}`")
    if date:
        parts.append(date[:7] if len(date) > 7 else date)

    return "| " + " | ".join(parts) + " |"


def generate_section_page(
    section_key: str,
    docs_page_path: str,
    section_title: str,
    entries: List[dict],
    repo_root: Path,
    dry_run: bool = False,
) -> None:
    """Generate or update a docs/zh/ index page for a section."""
    docs_page = repo_root / docs_page_path
    docs_page.parent.mkdir(parents=True, exist_ok=True)

    # Read existing page to preserve any manually written intro
    existing_content = ""
    auto_marker = "<!-- AUTO-GENERATED: do not edit below this line -->"
    if docs_page.exists():
        existing_content = docs_page.read_text(encoding="utf-8")

    # Build front matter
    fm = {
        "title": section_title,
        "generated": datetime.now().strftime("%Y-%m-%d"),
        "doc_count": len(entries),
    }
    fm_str = "---\n"
    fm_str += f"title: {section_title}\n"
    fm_str += f"generated: '{fm['generated']}'\n"
    fm_str += f"doc_count: {fm['doc_count']}\n"
    fm_str += "---\n\n"

    # Build intro section (preserve existing if present, otherwise generate)
    if auto_marker in existing_content:
        intro = existing_content.split(auto_marker)[0]
    else:
        intro = fm_str + f"# {section_title}\n\n"

    # Build auto-generated table section
    auto_section = f"{auto_marker}\n\n"
    auto_section += f"> 共 **{len(entries)}** 篇文档，最后更新：{datetime.now().strftime('%Y-%m-%d')}\n\n"

    if section_key == "nmpa/guidance":
        # Group by device category
        groups = group_nmpa_guidance(entries)
        for group_name, group_entries in sorted(groups.items()):
            auto_section += f"## {group_name}\n\n"
            auto_section += "| 文档名称 | 文号 | 发布年份 |\n"
            auto_section += "|----------|------|----------|\n"
            for entry in sorted(group_entries, key=lambda e: e["effective_date"], reverse=True):
                auto_section += _entry_row(entry, repo_root) + "\n"
            auto_section += "\n"
    else:
        # Simple flat table
        auto_section += "| 文档名称 | 文号 | 发布年份 |\n"
        auto_section += "|----------|------|----------|\n"
        for entry in sorted(entries, key=lambda e: e["effective_date"], reverse=True):
            auto_section += _entry_row(entry, repo_root) + "\n"
        auto_section += "\n"

    new_content = intro + auto_section

    if dry_run:
        print(f"  [DRY] Would write {docs_page_path} ({len(entries)} entries)")
        return

    docs_page.write_text(new_content, encoding="utf-8")
    print(f"  Updated {docs_page_path} ({len(entries)} entries)")


def sync_content_to_docs(section_key: str, entries: List[dict], repo_root: Path, dry_run: bool = False) -> int:
    """
    Copy data layer *.zh.md files into docs/zh/<section_key>/ for VitePress rendering.
    Strips the .zh suffix so the route becomes /zh/<section_key>/<slug>.
    Returns count of files synced.
    """
    synced = 0
    dest_dir = repo_root / "docs" / "zh" / section_key
    if not dry_run:
        dest_dir.mkdir(parents=True, exist_ok=True)

    for entry in entries:
        src_file: Path = entry["file"]
        # URL-decode slug to avoid %-encoded filenames that break VitePress/Rollup
        clean_slug = unquote(entry["slug"])
        dest_file = dest_dir / (clean_slug + ".md")
        if dry_run:
            print(f"    [DRY] sync {src_file.relative_to(repo_root)} -> {dest_file.relative_to(repo_root)}")
            synced += 1
            continue
        content = src_file.read_text(encoding="utf-8")
        # Rewrite image paths: /assets/images/ -> /images/ (VitePress public dir)
        content = content.replace("](/assets/images/", "](/images/")
        # Remove blob: URLs (WordPress editor temp objects, not downloadable)
        content = re.sub(r'!\[([^\]]*)\]\(blob:https?://[^)]+\)', r'[formula]', content)
        dest_file.write_text(content, encoding="utf-8")
        synced += 1
    return synced


def sync_en_content_to_docs(section_key: str, entries: List[dict], repo_root: Path, dry_run: bool = False) -> int:
    """
    Copy data layer *.en.md files into docs/en/<section_key>/ for VitePress rendering.
    Strips the .en suffix so the route becomes /en/<section_key>/<slug>.
    Only syncs files that have substantive English content (not just frontmatter/placeholders).
    Returns count of files synced.
    """
    synced = 0
    dest_dir = repo_root / "docs" / "en" / section_key
    if not dry_run:
        dest_dir.mkdir(parents=True, exist_ok=True)

    for entry in entries:
        src_file: Path = entry["file"]
        # Derive the .en.md path from the .zh.md path
        en_src = src_file.parent / src_file.name.replace(".zh.md", ".en.md")
        if not en_src.exists():
            continue

        content = en_src.read_text(encoding="utf-8")
        # Skip placeholder files that haven't been translated yet
        if "Translation needed" in content or "> This document requires" in content:
            continue

        clean_slug = unquote(entry["slug"])
        dest_file = dest_dir / (clean_slug + ".md")
        if dry_run:
            print(f"    [DRY] sync-en {en_src.relative_to(repo_root)} -> {dest_file.relative_to(repo_root)}")
            synced += 1
            continue

        # Rewrite image paths
        content = content.replace("](/assets/images/", "](/images/")
        content = re.sub(r'!\[([^\]]*)\]\(blob:https?://[^)]+\)', r'[formula]', content)
        dest_file.write_text(content, encoding="utf-8")
        synced += 1
    return synced


def _entry_row(entry: dict, repo_root: Path) -> str:
    """Format a table row for a document entry."""
    title = entry["title_zh"]
    doc_num = entry.get("doc_number", "")
    # Support both effective_date (docs) and published_date (insights)
    date_raw = entry.get("effective_date", "") or entry.get("published_date", "")
    date = date_raw[:4] if date_raw else ""

    # Internal VitePress route (synced to docs/zh/<section_key>/<slug>)
    section_key = entry.get("category", "")
    slug = unquote(entry["slug"])
    link = f"/zh/{section_key}/{slug}"

    title_cell = f"[{title}]({link})"
    doc_num_cell = f"`{doc_num}`" if doc_num else ""
    date_cell = date

    return f"| {title_cell} | {doc_num_cell} | {date_cell} |"


def get_en_entries(entries: List[dict], repo_root: Path) -> List[dict]:
    """
    Filter entries that have substantive English .en.md content.
    Returns a list of entries with English title available.
    """
    en_entries = []
    for entry in entries:
        src_file: Path = entry["file"]
        en_src = src_file.parent / src_file.name.replace(".zh.md", ".en.md")
        if not en_src.exists():
            continue
        content = en_src.read_text(encoding="utf-8")
        if "Translation needed" in content or "> This document requires" in content:
            continue
        # Extract English title from frontmatter
        fm = read_front_matter(en_src)
        title_en = ""
        if fm:
            title_val = fm.get("title", {})
            if isinstance(title_val, dict):
                title_en = title_val.get("en", "")
            elif isinstance(title_val, str):
                title_en = title_val
        if not title_en:
            title_en = entry["title_zh"]  # fallback to Chinese title
        en_entries.append({**entry, "title_en": title_en})
    return en_entries


def generate_sidebar_json(all_section_entries: Dict[str, List[dict]], repo_root: Path, dry_run: bool = False) -> None:
    """
    Generate docs/.vitepress/sidebar.json with dynamic sidebar items.

    VitePress uses longest-prefix matching for sidebar:
      /zh/nmpa/           -> static sidebar in config.ts (overview pages)
      /zh/nmpa/guidance/  -> dynamic grouped sidebar (guidance sub-pages)
      /zh/nmpa/regulations/ -> dynamic sidebar (regulation sub-pages)
      /zh/insights/       -> dynamic sidebar (insights pages)
    """
    sidebar: Dict[str, list] = {}

    en_sidebar: Dict[str, list] = {}

    for section_key, entries in all_section_entries.items():
        items = []
        for entry in entries:
            slug = unquote(entry["slug"])
            items.append({
                "text": entry["title_zh"],
                "link": f"/zh/{section_key}/{slug}",
            })

        # Build English sidebar items for this section
        en_items = []
        en_entries = get_en_entries(entries, repo_root)
        for en_entry in en_entries:
            slug = unquote(en_entry["slug"])
            en_items.append({
                "text": en_entry["title_en"],
                "link": f"/en/{section_key}/{slug}",
            })

        if section_key == "nmpa/guidance":
            groups = group_nmpa_guidance(entries)
            sidebar_items = [
                {"text": "<- NMPA 概览", "link": "/zh/nmpa/"},
                {"text": "指导原则索引", "link": "/zh/nmpa/guidance"},
            ]
            for group_name, group_entries in groups.items():
                if not group_entries:
                    continue
                children = []
                for e in sorted(group_entries, key=lambda x: x["title_zh"]):
                    s = unquote(e["slug"])
                    children.append({"text": e["title_zh"], "link": f"/zh/nmpa/guidance/{s}"})
                sidebar_items.append({
                    "text": f"{group_name} ({len(group_entries)})",
                    "collapsed": True,
                    "items": children,
                })
            sidebar["/zh/nmpa/guidance/"] = sidebar_items

        elif section_key == "nmpa/regulations":
            sorted_items = sorted(items, key=lambda x: x["text"])
            sidebar["/zh/nmpa/regulations/"] = [
                {"text": "<- NMPA 概览", "link": "/zh/nmpa/"},
                {"text": "法规规章索引", "link": "/zh/nmpa/regulations"},
                {
                    "text": f"法规全文 ({len(entries)})",
                    "collapsed": False,
                    "items": sorted_items,
                },
            ]

        elif section_key.startswith("insights/"):
            if "/zh/insights/" not in sidebar:
                sidebar["/zh/insights/"] = [
                    {"text": "法规解读", "link": "/zh/insights/"},
                ]
            sub_title = SECTION_MAP.get(section_key, ("", section_key, "", True))[1]
            sidebar["/zh/insights/"].append({
                "text": f"{sub_title} ({len(entries)})",
                "collapsed": True,
                "items": items,
            })

            # English insights sidebar
            if en_items:
                if "/en/insights/" not in en_sidebar:
                    en_sidebar["/en/insights/"] = [
                        {"text": "Regulatory Insights", "link": "/en/insights/"},
                    ]
                # Map Chinese section titles to English
                en_section_titles = {
                    "NMPA 合规动态": "NMPA Updates",
                    "EU MDR 合规动态": "EU MDR Updates",
                    "FDA 合规动态": "FDA Updates",
                    "法规解读分析": "Regulatory Analysis",
                    "临床评价方法论": "Clinical Evaluation",
                }
                en_sub_title = en_section_titles.get(sub_title, sub_title)
                en_sidebar["/en/insights/"].append({
                    "text": f"{en_sub_title} ({len(en_items)})",
                    "collapsed": True,
                    "items": en_items,
                })

    out_path = repo_root / "docs" / ".vitepress" / "sidebar.ts"
    if dry_run:
        print(f"  [DRY] Would write {out_path}")
        return

    ts_content = "// Auto-generated by scripts/generate_docs_index.py — DO NOT EDIT\n"
    ts_content += "export default " + json.dumps(sidebar, ensure_ascii=False, indent=2) + "\n"
    out_path.write_text(ts_content, encoding="utf-8")

    # Write English sidebar if there are English entries
    if en_sidebar:
        en_out_path = repo_root / "docs" / ".vitepress" / "sidebar-en.ts"
        en_ts_content = "// Auto-generated by scripts/generate_docs_index.py — DO NOT EDIT\n"
        en_ts_content += "export default " + json.dumps(en_sidebar, ensure_ascii=False, indent=2) + "\n"
        if not dry_run:
            en_out_path.write_text(en_ts_content, encoding="utf-8")
        print(f"  Generated {en_out_path.relative_to(repo_root)}")

    # Clean up old sidebar.json if it exists
    old_json = repo_root / "docs" / ".vitepress" / "sidebar.json"
    if old_json.exists():
        old_json.unlink()

    print(f"  Generated {out_path.relative_to(repo_root)}")


def main():
    parser = argparse.ArgumentParser(description="Generate VitePress docs index from data layer")
    parser.add_argument("--output-root", default=".",
                        help="Repo root directory (default: current directory)")
    parser.add_argument("--regulation", default=None,
                        help="Only process a specific regulation (nmpa, eu_mdr, fda, shared)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be generated without writing files")
    args = parser.parse_args()

    repo_root = Path(args.output_root).resolve()
    print(f"\nGenerating docs index pages from {repo_root}")
    if args.dry_run:
        print("[DRY RUN MODE]\n")

    total_entries = 0
    total_pages = 0
    total_synced = 0
    all_section_entries: Dict[str, List[dict]] = {}

    for section_key, (docs_page_path, section_title, regulation, sync_content) in SECTION_MAP.items():
        if args.regulation and regulation != args.regulation:
            continue

        data_dir = repo_root / section_key
        entries = get_doc_entries(data_dir, section_key)

        if not entries:
            continue

        if sync_content:
            # Sync full content files into docs/zh/ for VitePress rendering
            synced = sync_content_to_docs(section_key, entries, repo_root, dry_run=args.dry_run)
            total_synced += synced
            # Sync English content files into docs/en/ for VitePress rendering
            en_synced = sync_en_content_to_docs(section_key, entries, repo_root, dry_run=args.dry_run)
            total_synced += en_synced
            all_section_entries[section_key] = entries

        generate_section_page(
            section_key, docs_page_path, section_title,
            entries, repo_root, dry_run=args.dry_run
        )
        total_entries += len(entries)
        total_pages += 1

    # Generate dynamic sidebar config
    if all_section_entries:
        generate_sidebar_json(all_section_entries, repo_root, dry_run=args.dry_run)

    print(f"\nDone: {total_pages} index pages updated, {total_entries} entries, {total_synced} content files synced")


if __name__ == "__main__":
    main()
