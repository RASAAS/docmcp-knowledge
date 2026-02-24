#!/usr/bin/env python3
"""
JSON to Markdown Generator — Single Source of Truth Pipeline

Reads JSON data files from the data layer (eu_mdr/, fda/, nmpa/, _shared/)
and generates bilingual (EN + ZH) Markdown files for the VitePress docs site.

Usage:
    python scripts/json_to_markdown.py                    # Generate all
    python scripts/json_to_markdown.py --section standards # Standards only
    python scripts/json_to_markdown.py --dry-run           # Preview without writing
    python scripts/json_to_markdown.py --verify            # Check JSON→MD sync status

Architecture:
    JSON data layer (eu_mdr/standards/*.json)  ← Single Source of Truth
        ↓  json_to_markdown.py
    docs/zh/eu_mdr/standards/*.md  (Chinese display layer)
    docs/en/eu_mdr/standards/*.md  (English display layer)
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent
DOCS_ZH = ROOT / "docs" / "zh"
DOCS_EN = ROOT / "docs" / "en"

# ---------------------------------------------------------------------------
# Category display name & GSPR mapping for standards
# ---------------------------------------------------------------------------
STANDARDS_GSPR_MAP = {
    "biocompatibility": {"gspr": "GSPR 10.4", "gspr_zh": "生物相容性", "gspr_en": "Biocompatibility"},
    "clinical_investigation": {"gspr": "GSPR 1, 8, 14", "gspr_zh": "临床调查", "gspr_en": "Clinical investigation"},
    "connectors": {"gspr": "GSPR 14.2(d)", "gspr_zh": "小口径连接器", "gspr_en": "Small-bore connectors"},
    "electrical_safety": {"gspr": "GSPR 14", "gspr_zh": "电气安全", "gspr_en": "Electrical safety"},
    "labelling": {"gspr": "GSPR 23", "gspr_zh": "标签", "gspr_en": "Labelling"},
    "medical_gloves": {"gspr": "GSPR 10.4", "gspr_zh": "医用手套", "gspr_en": "Medical gloves"},
    "patient_handling": {"gspr": "GSPR 9, 14", "gspr_zh": "患者搬运", "gspr_en": "Patient handling"},
    "processing": {"gspr": "GSPR 11.7", "gspr_zh": "器械处理", "gspr_en": "Device processing"},
    "quality_management": {"gspr": "GSPR 全盘", "gspr_zh": "质量管理", "gspr_en": "Quality management"},
    "risk_management": {"gspr": "GSPR 全盘", "gspr_zh": "风险管理", "gspr_en": "Risk management"},
    "software": {"gspr": "GSPR 17, 5", "gspr_zh": "软件与可用性", "gspr_en": "Software & usability"},
    "sterilization": {"gspr": "GSPR 11", "gspr_zh": "灭菌与包装", "gspr_en": "Sterilization & packaging"},
    "surgical_implants": {"gspr": "GSPR 10, 14", "gspr_zh": "非有源外科植入物", "gspr_en": "Non-active surgical implants"},
    "surgical_textiles": {"gspr": "GSPR 10, 11", "gspr_zh": "手术衣物与口罩", "gspr_en": "Surgical textiles & masks"},
}

# Editorial notes that cannot be derived from JSON — keyed by category slug
STANDARDS_EDITORIAL_ZH = {
    "biocompatibility": (
        '\n> **重要说明**：以下常用标准**目前不在**协调标准列表中，使用时不产生合规推定效力，'
        '但仍是行业公认的评价方法：EN ISO 10993-1（评价框架）、EN ISO 10993-3（遗传毒性）、'
        'EN ISO 10993-5（细胞毒性）、EN ISO 10993-6（植入）、EN ISO 10993-7（EO残留物）、'
        'EN ISO 10993-11（全身毒性）、EN ISO 10993-13（聚合物）。'
        '\n\n## 生物相容性评价框架（基于 ISO 10993-1:2018）\n\n'
        '材料表征 → 危害识别 → 暴露评估 → 毒理学风险评估 → 生物相容性结论\n\n'
        'EU MDR 下，**化学表征优先**：先进行毒理学风险评估（TRA），仅在TRA不足以得出结论时才进行动物试验。'
    ),
    "biocompatibility_en": (
        '\n> **Important**: The following widely-used standards are **not** on the EU MDR harmonised '
        'standards list and do not create a presumption of conformity: EN ISO 10993-1 (evaluation '
        'framework), EN ISO 10993-3 (genotoxicity), EN ISO 10993-5 (cytotoxicity), EN ISO 10993-6 '
        '(implantation), EN ISO 10993-7 (EO residuals), EN ISO 10993-11 (systemic toxicity), '
        'EN ISO 10993-13 (polymers). They remain industry-accepted evaluation methods but must be '
        'justified separately in the technical file.'
        '\n\n## Biocompatibility Evaluation Framework\n\n'
        'Material characterisation → Hazard identification → Exposure assessment → '
        'Toxicological risk assessment → Biocompatibility conclusion\n\n'
        'Under EU MDR, **chemical characterisation takes priority**: toxicological risk assessment (TRA) '
        'is performed first; animal testing is only conducted when TRA is insufficient to reach a conclusion.'
    ),
    "software": (
        '\n> **重要说明**：EN IEC 62304和EN IEC 62366-1**不在**EU MDR协调标准列表（CID 2021/1182）中。'
        '它们不产生合规推定效力，但是证明GSPR 17（软件）和GSPR 5（可用性）合规性的行业公认方法，'
        '必须在技术文件中以"其他方法"加以证明。'
        '\n\n## EN IEC 62304 — 软件安全分类\n\n'
        '| 安全类别 | 定义 | 要求级别 |\n'
        '|----------|------|----------|\n'
        '| **A类** | 软件故障不会导致伤害 | 基本要求 |\n'
        '| **B类** | 软件故障可能导致轻微伤害 | 中等要求 |\n'
        '| **C类** | 软件故障可能导致死亡或严重伤害 | 全面要求 |\n'
        '\n## EN IEC 62366-1 — 可用性工程过程\n\n'
        '1. 预期用途规范：用户、使用环境、用户界面\n'
        '2. 用户界面规范：用户界面设计要求\n'
        '3. 总结性可用性评估：与代表性用户进行测试\n'
        '4. 可用性总结报告'
    ),
    "software_en": (
        '\n> **Important**: EN IEC 62304 and EN IEC 62366-1 are **not** on the EU MDR harmonised '
        'standards list (CID 2021/1182). They do not create a presumption of conformity, but are '
        'industry-accepted methods for demonstrating GSPR 17 (software) and GSPR 5 (usability) '
        'compliance and must be justified as "other methods" in the technical file.'
        '\n\n## EN IEC 62304 — Software Safety Classification\n\n'
        '| Safety Class | Definition | Requirements Level |\n'
        '|--------------|-----------|-------------------|\n'
        '| **Class A** | No contribution to hazardous situation | Basic requirements |\n'
        '| **Class B** | Non-serious injury possible | Moderate requirements |\n'
        '| **Class C** | Death or serious injury possible | Full requirements |\n'
        '\n## EN IEC 62366-1 — Usability Engineering Process\n\n'
        '1. Use specification: users, use environment, user interface\n'
        '2. User interface specification: UI design requirements\n'
        '3. Summative usability evaluation: testing with representative users\n'
        '4. Usability engineering summary report'
    ),
}

# Related pages for each standards category
STANDARDS_RELATED_ZH = {
    "biocompatibility": [
        ("附件I — GSPR", "../regulations/annex-i-gspr"),
        ("协调标准 — 灭菌与包装", "./sterilization"),
    ],
    "clinical_investigation": [
        ("附件XV — 临床调查", "../regulations/annex-xv-clinical-investigations"),
        ("附件XIV — 临床评价", "../regulations/annex-xiv-clinical-evaluation"),
    ],
    "electrical_safety": [
        ("附件I — GSPR", "../regulations/annex-i-gspr"),
        ("协调标准 — 软件与可用性", "./software"),
    ],
    "software": [
        ("附件I — GSPR", "../regulations/annex-i-gspr"),
        ("协调标准 — 电气安全与EMC", "./electrical-safety"),
    ],
    "sterilization": [
        ("附件I — GSPR", "../regulations/annex-i-gspr"),
        ("协调标准 — 生物相容性", "./biocompatibility"),
    ],
    "risk_management": [
        ("附件I — GSPR", "../regulations/annex-i-gspr"),
        ("协调标准 — 质量管理体系", "./quality-management"),
    ],
    "quality_management": [
        ("附件I — GSPR", "../regulations/annex-i-gspr"),
        ("协调标准 — 风险管理", "./risk-management"),
    ],
}

STANDARDS_RELATED_EN = {
    "biocompatibility": [
        ("Annex I — GSPR", "../regulations/annex-i-gspr"),
        ("Harmonised Standards — Sterilization and Packaging", "./sterilization"),
    ],
    "clinical_investigation": [
        ("Annex XV — Clinical Investigations", "../regulations/annex-xv-clinical-investigations"),
        ("Annex XIV — Clinical Evaluation", "../regulations/annex-xiv-clinical-evaluation"),
    ],
    "electrical_safety": [
        ("Annex I — GSPR", "../regulations/annex-i-gspr"),
        ("Harmonised Standards — Software and Usability", "./software"),
    ],
    "software": [
        ("Annex I — GSPR", "../regulations/annex-i-gspr"),
        ("Harmonised Standards — Electrical Safety & EMC", "./electrical-safety"),
    ],
    "sterilization": [
        ("Annex I — GSPR", "../regulations/annex-i-gspr"),
        ("Harmonised Standards — Biocompatibility", "./biocompatibility"),
    ],
    "risk_management": [
        ("Annex I — GSPR", "../regulations/annex-i-gspr"),
        ("Harmonised Standards — Quality Management", "./quality-management"),
    ],
    "quality_management": [
        ("Annex I — GSPR", "../regulations/annex-i-gspr"),
        ("Harmonised Standards — Risk Management", "./risk-management"),
    ],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_entries(data: dict) -> list:
    """Get entries from JSON data, handling both 'entries' and 'standards' keys."""
    return data.get("entries", data.get("standards", []))


def get_title_str(title, lang: str = "en") -> str:
    """Get title string, handling both string and dict formats."""
    if isinstance(title, dict):
        return title.get(lang, title.get("en", ""))
    return str(title) if title else ""


def write_md(path: Path, content: str, dry_run: bool = False) -> bool:
    """Write markdown file. Returns True if content changed."""
    if path.exists():
        old = path.read_text(encoding="utf-8")
        if old.strip() == content.strip():
            return False
    if dry_run:
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Standards sub-page generators
# ---------------------------------------------------------------------------
def generate_standards_subpage_zh(category_slug: str, data: dict, index_data: dict) -> str:
    """Generate a Chinese standards sub-page from JSON data."""
    cat_info = index_data.get("categories", {}).get(category_slug, {})
    cat_name_zh = cat_info.get("name", {}).get("zh", category_slug)
    entries = get_entries(data)
    count = data.get("count", data.get("standards_count", len(entries)))
    gspr_info = STANDARDS_GSPR_MAP.get(category_slug, {})
    latest_amend = index_data.get("latest_amendment", "")
    latest_amend_url = index_data.get("latest_amendment_url", "")

    # Determine if these are harmonised or non-harmonised standards
    is_non_harmonised = category_slug == "software"
    list_type = "广泛适用标准（非协调标准）" if is_non_harmonised else f"协调标准列表（{count}条）"
    h1_prefix = "" if is_non_harmonised else "协调标准 — "

    lines = []
    lines.append("---")
    if is_non_harmonised:
        lines.append(f'title: {cat_name_zh} — EU MDR相关标准')
    else:
        lines.append(f'title: 协调标准 — {cat_name_zh}')
    desc = (f'"EU MDR 2017/745 协调标准：{cat_name_zh}（{count}条入官方公报标准），'
            f'适用于{gspr_info.get("gspr", "")}。基于 CID (EU) 2021/1182 及修正案 {latest_amend}。"')
    if is_non_harmonised:
        desc = (f'"EN IEC 62304和EN IEC 62366-1不在EU MDR协调标准列表中。'
                f'它们广泛作为\\"其他方法\\"用于证明{gspr_info.get("gspr", "")}合规性。"')
    lines.append(f'description: {desc}')
    lines.append("regulation: EU MDR 2017/745")
    lines.append(f"category: {cat_info.get('name', {}).get('en', category_slug)}")
    lines.append("---")
    lines.append("")

    if is_non_harmonised:
        lines.append(f"# {cat_name_zh} — EU MDR相关标准")
    else:
        lines.append(f"# 协调标准 — {cat_name_zh}")
    lines.append("")
    lines.append(
        f"**官方来源**：[EC Health — Harmonised Standards]"
        f"(https://health.ec.europa.eu/medical-devices-topics-interest/harmonised-standards_en)"
        f" | 基于 CID (EU) 2021/1182（合并版）及修正案 "
        f"[CID (EU) {latest_amend}]({latest_amend_url})"
    )
    lines.append("")
    lines.append(f"## {list_type}")
    lines.append("")
    lines.append("| 标准号 | 标题摘要 | GSPR对应 | 状态 |")
    lines.append("|--------|---------|---------|------|")

    for entry in entries:
        number = entry.get("number", "")
        title = get_title_str(entry.get("title", ""), "zh")
        # Shorten title for table display
        if " - " in title:
            title = title.split(" - ", 1)[1]
        elif " — " in title:
            title = title.split(" — ", 1)[1]

        amendments = entry.get("amendments", [])
        if amendments:
            number = f"{number} + {amendments[-1].split(':')[-1] if ':' in amendments[-1] else amendments[-1]}"

        gspr_ref = gspr_info.get("gspr", "")
        gspr_desc = gspr_info.get("gspr_zh", "")

        status_zh = "现行有效" if entry.get("status") == "active" else "已废止"
        label = "广泛适用（非协调标准）" if is_non_harmonised else status_zh

        lines.append(f"| **{number}** | {title} | {gspr_ref}（{gspr_desc}） | {label} |")

    # Editorial notes
    editorial = STANDARDS_EDITORIAL_ZH.get(category_slug, "")
    if editorial:
        lines.append(editorial)

    # Related pages
    lines.append("")
    lines.append("## 相关页面")
    lines.append("")
    related = STANDARDS_RELATED_ZH.get(category_slug, [("附件I — GSPR", "../regulations/annex-i-gspr")])
    for label, link in related:
        lines.append(f"- [{label}]({link})")

    # Data layer source
    lines.append("")
    lines.append("## 数据层源文件")
    lines.append("")
    json_file = cat_info.get("file", f"standards-{category_slug}.json")
    lines.append(
        f"[eu_mdr/standards/{json_file}]"
        f"(https://github.com/RASAAS/docmcp-knowledge/tree/main/eu_mdr/standards/{json_file})"
    )
    lines.append("")

    return "\n".join(lines)


def generate_standards_subpage_en(category_slug: str, data: dict, index_data: dict) -> str:
    """Generate an English standards sub-page from JSON data."""
    cat_info = index_data.get("categories", {}).get(category_slug, {})
    cat_name_en = cat_info.get("name", {}).get("en", category_slug)
    entries = get_entries(data)
    count = data.get("count", data.get("standards_count", len(entries)))
    gspr_info = STANDARDS_GSPR_MAP.get(category_slug, {})
    latest_amend = index_data.get("latest_amendment", "")
    latest_amend_url = index_data.get("latest_amendment_url", "")

    is_non_harmonised = category_slug == "software"
    list_type = "Widely-Used Standards (Non-Harmonised)" if is_non_harmonised else f"Harmonised Standards List ({count} standards)"

    lines = []
    lines.append("---")
    if is_non_harmonised:
        lines.append(f'title: {cat_name_en} — EU MDR Related Standards')
    else:
        lines.append(f'title: Harmonised Standards — {cat_name_en}')
    desc = (f'"EU MDR 2017/745 harmonised standards: {cat_name_en} ({count} standards in the OJ list), '
            f'applicable to {gspr_info.get("gspr", "")}. Based on CID (EU) 2021/1182 and amendment {latest_amend}."')
    if is_non_harmonised:
        desc = (f'"EN IEC 62304 and EN IEC 62366-1 are not on the EU MDR harmonised standards list. '
                f'They are widely used as \\"other methods\\" to demonstrate {gspr_info.get("gspr", "")} compliance."')
    lines.append(f'description: {desc}')
    lines.append("regulation: EU MDR 2017/745")
    lines.append(f"category: {cat_name_en}")
    lines.append("---")
    lines.append("")

    if is_non_harmonised:
        lines.append(f"# {cat_name_en} — EU MDR Related Standards")
    else:
        lines.append(f"# Harmonised Standards — {cat_name_en}")
    lines.append("")
    lines.append(
        f"**Official Source**: [EC Health — Harmonised Standards]"
        f"(https://health.ec.europa.eu/medical-devices-topics-interest/harmonised-standards_en)"
        f" | Based on CID (EU) 2021/1182 (consolidated) and amendment "
        f"[CID (EU) {latest_amend}]({latest_amend_url})"
    )
    lines.append("")
    lines.append(f"## {list_type}")
    lines.append("")
    lines.append("| Standard | Title Summary | GSPR Reference | Status |")
    lines.append("|----------|--------------|---------------|--------|")

    for entry in entries:
        number = entry.get("number", "")
        title = get_title_str(entry.get("title", ""), "en")
        if " - " in title:
            title = title.split(" - ", 1)[1]
        elif " — " in title:
            title = title.split(" — ", 1)[1]

        amendments = entry.get("amendments", [])
        if amendments:
            number = f"{number} + {amendments[-1].split(':')[-1] if ':' in amendments[-1] else amendments[-1]}"

        gspr_ref = gspr_info.get("gspr", "")
        gspr_desc = gspr_info.get("gspr_en", "")

        status_en = "Current" if entry.get("status") == "active" else "Withdrawn"
        label = "Widely used (non-harmonised)" if is_non_harmonised else status_en

        lines.append(f"| **{number}** | {title} | {gspr_ref} ({gspr_desc}) | {label} |")

    # Editorial notes
    editorial = STANDARDS_EDITORIAL_ZH.get(f"{category_slug}_en", "")
    if editorial:
        lines.append(editorial)

    # Related pages
    lines.append("")
    lines.append("## Related Pages")
    lines.append("")
    related = STANDARDS_RELATED_EN.get(category_slug, [("Annex I — GSPR", "../regulations/annex-i-gspr")])
    for label, link in related:
        lines.append(f"- [{label}]({link})")

    # Data layer source
    lines.append("")
    lines.append("## Data Layer Source File")
    lines.append("")
    json_file = cat_info.get("file", f"standards-{category_slug}.json")
    lines.append(
        f"[eu_mdr/standards/{json_file}]"
        f"(https://github.com/RASAAS/docmcp-knowledge/tree/main/eu_mdr/standards/{json_file})"
    )
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main generation orchestrator
# ---------------------------------------------------------------------------
def generate_standards(dry_run: bool = False) -> list[str]:
    """Generate all EU MDR standards sub-pages. Returns list of changed files."""
    standards_dir = ROOT / "eu_mdr" / "standards"
    index_path = standards_dir / "_index.json"
    if not index_path.exists():
        print(f"  SKIP: {index_path} not found")
        return []

    index_data = load_json(index_path)
    changed = []

    for cat_slug, cat_info in index_data.get("categories", {}).items():
        json_file = cat_info.get("file")
        if not json_file:
            continue
        json_path = standards_dir / json_file
        if not json_path.exists():
            print(f"  WARN: {json_path} not found, skipping")
            continue

        data = load_json(json_path)

        # Determine output slug (e.g. "biocompatibility" -> "biocompatibility.md")
        slug = cat_slug.replace("_", "-")

        # Generate ZH
        zh_path = DOCS_ZH / "eu_mdr" / "standards" / f"{slug}.md"
        zh_content = generate_standards_subpage_zh(cat_slug, data, index_data)
        if write_md(zh_path, zh_content, dry_run):
            changed.append(str(zh_path.relative_to(ROOT)))
            print(f"  {'WOULD WRITE' if dry_run else 'WROTE'}: {zh_path.relative_to(ROOT)}")

        # Generate EN
        en_path = DOCS_EN / "eu_mdr" / "standards" / f"{slug}.md"
        en_content = generate_standards_subpage_en(cat_slug, data, index_data)
        if write_md(en_path, en_content, dry_run):
            changed.append(str(en_path.relative_to(ROOT)))
            print(f"  {'WOULD WRITE' if dry_run else 'WROTE'}: {en_path.relative_to(ROOT)}")

    return changed


def verify_sync() -> list[str]:
    """Check which Markdown files are out of sync with JSON data. Returns list of out-of-sync files."""
    out_of_sync = []

    # Check standards
    standards_dir = ROOT / "eu_mdr" / "standards"
    index_path = standards_dir / "_index.json"
    if not index_path.exists():
        print("  WARN: eu_mdr/standards/_index.json not found")
        return out_of_sync

    index_data = load_json(index_path)

    for cat_slug, cat_info in index_data.get("categories", {}).items():
        json_file = cat_info.get("file")
        if not json_file:
            continue
        json_path = standards_dir / json_file
        if not json_path.exists():
            continue

        data = load_json(json_path)
        slug = cat_slug.replace("_", "-")

        # Check ZH
        zh_path = DOCS_ZH / "eu_mdr" / "standards" / f"{slug}.md"
        zh_content = generate_standards_subpage_zh(cat_slug, data, index_data)
        if zh_path.exists():
            old = zh_path.read_text(encoding="utf-8")
            if old.strip() != zh_content.strip():
                out_of_sync.append(str(zh_path.relative_to(ROOT)))
        else:
            out_of_sync.append(str(zh_path.relative_to(ROOT)) + " (MISSING)")

        # Check EN
        en_path = DOCS_EN / "eu_mdr" / "standards" / f"{slug}.md"
        en_content = generate_standards_subpage_en(cat_slug, data, index_data)
        if en_path.exists():
            old = en_path.read_text(encoding="utf-8")
            if old.strip() != en_content.strip():
                out_of_sync.append(str(en_path.relative_to(ROOT)))
        else:
            out_of_sync.append(str(en_path.relative_to(ROOT)) + " (MISSING)")

    return out_of_sync


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Generate bilingual Markdown from JSON data layer"
    )
    parser.add_argument(
        "--section",
        choices=["standards", "all"],
        default="all",
        help="Which section to generate (default: all)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing files"
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Check sync status between JSON and Markdown"
    )
    args = parser.parse_args()

    if args.verify:
        print("Verifying JSON -> Markdown sync status...")
        out_of_sync = verify_sync()
        if out_of_sync:
            print(f"\nOut of sync ({len(out_of_sync)} files):")
            for f in out_of_sync:
                print(f"  - {f}")
            sys.exit(1)
        else:
            print("\nAll Markdown files are in sync with JSON data.")
            sys.exit(0)

    print(f"Generating Markdown from JSON data layer (dry_run={args.dry_run})...")
    changed = []

    if args.section in ("standards", "all"):
        print("\n[Standards]")
        changed.extend(generate_standards(dry_run=args.dry_run))

    print(f"\nTotal: {len(changed)} files {'would be' if args.dry_run else ''} changed")
    if changed:
        for f in changed:
            print(f"  {f}")

    return 0 if not changed or not args.dry_run else 0


if __name__ == "__main__":
    sys.exit(main())
