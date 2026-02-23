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
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)


# Mapping: data layer dir -> docs/zh/ page path + section title
SECTION_MAP = {
    "nmpa/guidance":        ("docs/zh/nmpa/guidance.md",        "NMPA 注册审查指导原则",   "nmpa"),
    "nmpa/regulations":     ("docs/zh/nmpa/regulations.md",     "NMPA 法规规章",           "nmpa"),
    "nmpa/classification":  ("docs/zh/nmpa/classification.md",  "NMPA 医疗器械分类",       "nmpa"),
    "nmpa/standards":       ("docs/zh/nmpa/standards.md",       "NMPA 标准",               "nmpa"),
    "eu_mdr/mdcg":          ("docs/zh/eu_mdr/mdcg.md",          "MDCG 指南文件",           "eu_mdr"),
    "eu_mdr/team_nb":       ("docs/zh/eu_mdr/team_nb.md",       "Team-NB 立场文件",        "eu_mdr"),
    "eu_mdr/ivdr":          ("docs/zh/eu_mdr/ivdr.md",          "EU IVDR",                 "eu_mdr"),
    "eu_mdr/standards":     ("docs/zh/eu_mdr/standards.md",     "EU MDR 协调标准",         "eu_mdr"),
    "eu_mdr":               ("docs/zh/eu_mdr/regulations.md",   "EU MDR 法规",             "eu_mdr"),
    "fda/guidance":         ("docs/zh/fda/guidance.md",         "FDA 指南文件",            "fda"),
    "fda/regulations":      ("docs/zh/fda/regulations.md",      "FDA 法规",                "fda"),
    "fda/standards":        ("docs/zh/fda/standards.md",        "FDA 认可标准",            "fda"),
    "_shared":              ("docs/zh/shared/index.md",         "通用资源",                "shared"),
    "insights/nmpa-updates":    ("docs/zh/insights/nmpa-updates.md",    "NMPA 合规动态",   "insights"),
    "insights/eu-mdr-updates":  ("docs/zh/insights/eu-mdr-updates.md",  "EU MDR 合规动态", "insights"),
    "insights/fda-updates":     ("docs/zh/insights/fda-updates.md",     "FDA 合规动态",    "insights"),
    "insights/analysis":        ("docs/zh/insights/analysis.md",        "法规解读分析",    "insights"),
}

# Category grouping for NMPA guidance (by device category prefix in slug)
NMPA_GUIDANCE_GROUPS = {
    "software": "软件与数字健康",
    "ai": "人工智能",
    "clinical": "临床评价",
    "cer": "临床评价",
    "biocompat": "生物相容性",
    "steriliz": "灭菌",
    "implant": "植入器械",
    "orthopedic": "骨科器械",
    "cardiovascular": "心血管器械",
    "ophthalm": "眼科器械",
    "dental": "口腔器械",
    "imaging": "影像器械",
    "diagnostic": "诊断器械",
    "ventilat": "呼吸器械",
    "respirat": "呼吸器械",
    "infusion": "输液护理器械",
    "wound": "伤口护理",
    "dressing": "伤口护理",
    "collagen": "生物材料",
    "qms": "质量管理体系",
    "gmp": "质量管理体系",
    "registration": "注册申报",
    "submission": "注册申报",
    "innovative": "创新医疗器械",
    "priority": "优先审批",
}


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
    """Group NMPA guidance entries by device category."""
    groups: Dict[str, List[dict]] = {"其他": []}

    for entry in entries:
        slug = entry["slug"].lower()
        title = entry["title_zh"].lower()
        matched = False
        for key, group_name in NMPA_GUIDANCE_GROUPS.items():
            if key in slug or key in title:
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
        dest_file = dest_dir / (entry["slug"] + ".md")
        if dry_run:
            print(f"    [DRY] sync {src_file.relative_to(repo_root)} -> {dest_file.relative_to(repo_root)}")
            synced += 1
            continue
        content = src_file.read_text(encoding="utf-8")
        # Rewrite image paths: /assets/images/ -> /images/ (VitePress public dir)
        content = content.replace("](/assets/images/", "](/images/")
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
    slug = entry["slug"]
    link = f"/zh/{section_key}/{slug}"

    title_cell = f"[{title}]({link})"
    doc_num_cell = f"`{doc_num}`" if doc_num else ""
    date_cell = date

    return f"| {title_cell} | {doc_num_cell} | {date_cell} |"


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

    for section_key, (docs_page_path, section_title, regulation) in SECTION_MAP.items():
        if args.regulation and regulation != args.regulation:
            continue

        data_dir = repo_root / section_key
        entries = get_doc_entries(data_dir, section_key)

        if not entries:
            continue

        # Sync full content files into docs/zh/ for VitePress rendering
        synced = sync_content_to_docs(section_key, entries, repo_root, dry_run=args.dry_run)
        total_synced += synced

        generate_section_page(
            section_key, docs_page_path, section_title,
            entries, repo_root, dry_run=args.dry_run
        )
        total_entries += len(entries)
        total_pages += 1

    print(f"\nDone: {total_pages} index pages updated, {total_entries} entries, {total_synced} content files synced")


if __name__ == "__main__":
    main()
