#!/usr/bin/env python3
"""
Generate VitePress documentation pages for standards and regulations.

Reads from eu_mdr/{standards,other_standards,regulations}/ JSON data files
and generates corresponding Markdown pages in docs/{en,zh}/eu_mdr/.

Also updates _index.json files with correct counts.
"""

import json
import os
from pathlib import Path
from collections import OrderedDict

ROOT = Path(__file__).resolve().parent.parent
HS_DIR = ROOT / "eu_mdr" / "standards"
OS_DIR = ROOT / "eu_mdr" / "other_standards"
REG_DIR = ROOT / "eu_mdr" / "regulations"
DOCS_EN = ROOT / "docs" / "en" / "eu_mdr"
DOCS_ZH = ROOT / "docs" / "zh" / "eu_mdr"


def load_category_standards(base_dir: Path) -> dict:
    """Load all standards from category JSON files."""
    result = {}
    for f in sorted(base_dir.iterdir()):
        if f.name.startswith("standards-") and f.suffix == ".json":
            cat_key = f.stem.replace("standards-", "")
            with open(f) as fp:
                data = json.load(fp)
            result[cat_key] = data.get("standards", [])
    return result


def update_index_counts(base_dir: Path, categories_data: dict):
    """Update _index.json with correct category counts."""
    index_path = base_dir / "_index.json"
    with open(index_path) as f:
        index = json.load(f)

    total = 0
    cats = index.get("categories", {})
    for cat_key, stds in categories_data.items():
        count = len(stds)
        total += count
        if cat_key in cats:
            cats[cat_key]["count"] = count

    # Add missing categories
    for cat_key, stds in categories_data.items():
        if cat_key not in cats:
            cats[cat_key] = {
                "name": {"en": cat_key.replace("_", " ").title(), "zh": cat_key.replace("_", " ").title()},
                "count": len(stds),
                "file": f"standards-{cat_key}.json",
            }

    index["categories"] = dict(sorted(cats.items()))
    index["total_standards"] = total
    index["last_updated"] = "2026-05-04"

    with open(index_path, "w") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
        f.write("\n")

    return total


def generate_harmonised_standards_page(categories_data: dict):
    """Generate the main harmonised standards overview page (en + zh)."""
    total = sum(len(stds) for stds in categories_data.values())

    # English version
    en_lines = [
        "---",
        "title: EU MDR Harmonised Standards",
        "---",
        "",
        "# EU MDR Harmonised Standards",
        "",
        "Harmonised standards under EU MDR 2017/745 are published by the European Commission "
        "in the **Official Journal of the EU (OJ)**. Applying a harmonised standard creates a "
        "**presumption of conformity** with the corresponding GSPR requirements (EU MDR Article 8).",
        "",
        "::: info Data Source and Version",
        f"Data sourced from official EUR-Lex publications. Total: **{total}** harmonised standards across "
        f"**{len(categories_data)}** categories.",
        "- **Base Decision**: [CID (EU) 2021/1182](https://eur-lex.europa.eu/eli/dec_impl/2021/1182/oj)",
        "- **Latest Amendment**: [CID (EU) 2026/760](https://eur-lex.europa.eu/eli/dec_impl/2026/760/oj)",
        "- **EC Summary Page**: [health.ec.europa.eu](https://health.ec.europa.eu/medical-devices-topics-interest/harmonised-standards_en)",
        ":::",
        "",
    ]

    # Generate category tables
    for cat_key, stds in sorted(categories_data.items()):
        if not stds:
            continue
        cat_name = _get_cat_name_en(cat_key, stds)
        en_lines.append(f"## {cat_name}")
        en_lines.append("")
        en_lines.append("| Standard | Title | GSPR Reference |")
        en_lines.append("|----------|-------|----------------|")
        for s in stds:
            number = s.get("number", "")
            title_obj = s.get("title", {})
            title = title_obj.get("en", title_obj) if isinstance(title_obj, dict) else title_obj
            gsprs = s.get("applicable_gsprs", "")
            if isinstance(gsprs, list):
                gsprs = ", ".join(str(g) for g in gsprs[:5])
                if len(s.get("applicable_gsprs", [])) > 5:
                    gsprs += "..."
            source = s.get("source_url", "")
            number_link = f"[{number}]({source})" if source else number
            en_lines.append(f"| {number_link} | {title} | GSPR {gsprs} |")
        en_lines.append("")

    en_lines.extend([
        "---",
        "",
        "::: warning GSPR Applicability Note",
        "The GSPR correspondence above is a **general analysis**. Actual applicability depends on "
        "the specific device type, intended purpose and risk classification.",
        ":::",
    ])

    # Chinese version
    zh_lines = [
        "---",
        "title: EU MDR 协调标准",
        "---",
        "",
        "# EU MDR 协调标准",
        "",
        "EU MDR 2017/745 框架下的协调标准由欧盟委员会在**欧盟官方公报 (OJ)** 中发布。"
        "适用协调标准可产生对相应 GSPR 要求的**符合性推定**（EU MDR 第8条）。",
        "",
        "::: info 数据来源与版本",
        f"数据来源于 EUR-Lex 官方出版物。共 **{total}** 条协调标准，分布于 **{len(categories_data)}** 个类别。",
        "- **基础决定**: [CID (EU) 2021/1182](https://eur-lex.europa.eu/eli/dec_impl/2021/1182/oj)",
        "- **最新修正案**: [CID (EU) 2026/760](https://eur-lex.europa.eu/eli/dec_impl/2026/760/oj)",
        "- **EC 概览页面**: [health.ec.europa.eu](https://health.ec.europa.eu/medical-devices-topics-interest/harmonised-standards_en)",
        ":::",
        "",
    ]

    for cat_key, stds in sorted(categories_data.items()):
        if not stds:
            continue
        cat_name = _get_cat_name_zh(cat_key, stds)
        zh_lines.append(f"## {cat_name}")
        zh_lines.append("")
        zh_lines.append("| 标准编号 | 标题 | GSPR 参考 |")
        zh_lines.append("|----------|------|-----------|")
        for s in stds:
            number = s.get("number", "")
            title_obj = s.get("title", {})
            title = title_obj.get("zh", title_obj.get("en", title_obj)) if isinstance(title_obj, dict) else title_obj
            gsprs = s.get("applicable_gsprs", "")
            if isinstance(gsprs, list):
                gsprs = ", ".join(str(g) for g in gsprs[:5])
                if len(s.get("applicable_gsprs", [])) > 5:
                    gsprs += "..."
            source = s.get("source_url", "")
            number_link = f"[{number}]({source})" if source else number
            zh_lines.append(f"| {number_link} | {title} | GSPR {gsprs} |")
        zh_lines.append("")

    zh_lines.extend([
        "---",
        "",
        "::: warning GSPR 适用性说明",
        "以上 GSPR 对应关系为**一般性分析**。实际适用性取决于特定器械类型、预期用途和风险分类。",
        ":::",
    ])

    _write_page(DOCS_EN / "standards.md", "\n".join(en_lines))
    _write_page(DOCS_ZH / "standards.md", "\n".join(zh_lines))


def generate_other_standards_page(categories_data: dict):
    """Generate the other applicable standards page (en + zh)."""
    total = sum(len(stds) for stds in categories_data.values())

    en_lines = [
        "---",
        "title: Other Applicable Standards",
        "---",
        "",
        "# Other Applicable Standards (Non-Harmonised)",
        "",
        "Beyond harmonised standards, medical device manufacturers commonly apply the following "
        "international standards (ISO, IEC, ASTM, etc.) to demonstrate compliance with EU MDR GSPR. "
        "While these do not create a *presumption of conformity*, they represent accepted "
        "state-of-the-art practices.",
        "",
        f"::: info Total: **{total}** standards across **{len(categories_data)}** categories",
        ":::",
        "",
        "## Categories",
        "",
        "| Category | Standards | Key Standards |",
        "|----------|-----------|---------------|",
    ]

    for cat_key in sorted(categories_data.keys()):
        stds = categories_data[cat_key]
        cat_name = _get_cat_name_en(cat_key, stds)
        key_stds = ", ".join(s.get("number", "") for s in stds[:3])
        if len(stds) > 3:
            key_stds += "..."
        slug = cat_key.replace("_", "-")
        en_lines.append(f"| [{cat_name}](./other-standards/{slug}) | {len(stds)} | {key_stds} |")

    en_lines.extend(["", "---", ""])

    # Top standards by category detail pages will be generated separately
    en_lines.extend([
        "::: tip Navigation",
        "Click on a category above to see all standards in that category with their scope, "
        "applicable GSPRs, and official source links.",
        ":::",
    ])

    zh_lines = [
        "---",
        "title: 其他适用标准",
        "---",
        "",
        "# 其他适用标准（非协调标准）",
        "",
        "除协调标准外，医疗器械制造商通常还应用以下国际标准（ISO、IEC、ASTM 等）来证明"
        "符合 EU MDR GSPR 要求。虽然这些标准不产生*符合性推定*，但它们代表了公认的技术水平。",
        "",
        f"::: info 共 **{total}** 条标准，分布于 **{len(categories_data)}** 个类别",
        ":::",
        "",
        "## 标准分类",
        "",
        "| 类别 | 标准数量 | 代表性标准 |",
        "|------|----------|------------|",
    ]

    for cat_key in sorted(categories_data.keys()):
        stds = categories_data[cat_key]
        cat_name = _get_cat_name_zh(cat_key, stds)
        key_stds = ", ".join(s.get("number", "") for s in stds[:3])
        if len(stds) > 3:
            key_stds += "..."
        slug = cat_key.replace("_", "-")
        zh_lines.append(f"| [{cat_name}](./other-standards/{slug}) | {len(stds)} | {key_stds} |")

    zh_lines.extend(["", "---", ""])
    zh_lines.extend([
        "::: tip 导航提示",
        "点击上方类别名称可查看该类别下所有标准的适用范围、相关 GSPR 条款和官方来源链接。",
        ":::",
    ])

    _write_page(DOCS_EN / "other-standards.md", "\n".join(en_lines))
    _write_page(DOCS_ZH / "other-standards.md", "\n".join(zh_lines))


def generate_other_standards_category_pages(categories_data: dict):
    """Generate individual category pages for other standards."""
    os.makedirs(DOCS_EN / "other-standards", exist_ok=True)
    os.makedirs(DOCS_ZH / "other-standards", exist_ok=True)

    for cat_key, stds in sorted(categories_data.items()):
        if not stds:
            continue
        slug = cat_key.replace("_", "-")
        cat_name_en = _get_cat_name_en(cat_key, stds)
        cat_name_zh = _get_cat_name_zh(cat_key, stds)

        # English
        en_lines = [
            "---",
            f"title: \"{cat_name_en}\"",
            "---",
            "",
            f"# {cat_name_en}",
            "",
            f"**{len(stds)}** standards in this category.",
            "",
            "| Standard | Title | Scope | GSPR |",
            "|----------|-------|-------|------|",
        ]
        for s in stds:
            number = s.get("number", "")
            title_obj = s.get("title", {})
            title = title_obj.get("en", title_obj) if isinstance(title_obj, dict) else str(title_obj)
            title = title.replace("|", "/")
            scope_raw = s.get("scope", "")
            if isinstance(scope_raw, dict):
                scope_raw = scope_raw.get("en", "") or ""
            scope = (scope_raw or "")[:80].replace("|", "/").replace("\n", " ")
            if len(scope_raw or "") > 80:
                scope += "..."
            gsprs = s.get("applicable_gsprs", "")
            if isinstance(gsprs, list):
                gsprs = ", ".join(str(g) for g in gsprs[:4])
            source = s.get("source_url", "")
            number_link = f"[{number}]({source})" if source else number
            en_lines.append(f"| {number_link} | {title} | {scope} | {gsprs} |")

        en_lines.append("")
        _write_page(DOCS_EN / "other-standards" / f"{slug}.md", "\n".join(en_lines))

        # Chinese
        zh_lines = [
            "---",
            f"title: \"{cat_name_zh}\"",
            "---",
            "",
            f"# {cat_name_zh}",
            "",
            f"本类别共 **{len(stds)}** 条标准。",
            "",
            "| 标准编号 | 标题 | 适用范围 | GSPR |",
            "|----------|------|----------|------|",
        ]
        for s in stds:
            number = s.get("number", "")
            title_obj = s.get("title", {})
            title = title_obj.get("zh", title_obj.get("en", "")) if isinstance(title_obj, dict) else str(title_obj)
            title = title.replace("|", "/")
            scope_raw = s.get("scope", "")
            if isinstance(scope_raw, dict):
                scope_raw = scope_raw.get("zh", scope_raw.get("en", "")) or ""
            scope = (scope_raw or "")[:80].replace("|", "/").replace("\n", " ")
            if len(scope_raw or "") > 80:
                scope += "..."
            gsprs = s.get("applicable_gsprs", "")
            if isinstance(gsprs, list):
                gsprs = ", ".join(str(g) for g in gsprs[:4])
            source = s.get("source_url", "")
            number_link = f"[{number}]({source})" if source else number
            zh_lines.append(f"| {number_link} | {title} | {scope} | {gsprs} |")

        zh_lines.append("")
        _write_page(DOCS_ZH / "other-standards" / f"{slug}.md", "\n".join(zh_lines))


def generate_regulations_page():
    """Generate the EU regulations overview page (en + zh)."""
    index_path = REG_DIR / "_index.json"
    with open(index_path) as f:
        index = json.load(f)

    docs = [d for d in index.get("documents", []) if d.get("standard_type") == "eu_regulation"]
    core_docs = [d for d in index.get("documents", []) if d.get("id") in ("eu-mdr-2017-745", "eu-ivdr-2017-746", "eu-mdr-amendments")]

    # Check for fulltext availability
    fulltext_dir = REG_DIR / "fulltext"
    has_fulltext = set()
    if fulltext_dir.exists():
        for f in fulltext_dir.iterdir():
            if f.suffix == ".md":
                has_fulltext.add(f.stem)

    en_lines = [
        "---",
        "title: EU Regulations & Directives",
        "---",
        "",
        "# EU Regulations & Directives",
        "",
        "This section covers EU regulations and directives relevant to medical device compliance "
        "under the EU MDR framework. These include both the core MDR/IVDR and other cross-cutting "
        "EU legislation that medical device manufacturers must consider.",
        "",
        "## Core Regulations",
        "",
        "| Regulation | Title | Status | Application Date |",
        "|------------|-------|--------|-----------------|",
    ]

    for d in core_docs:
        title_obj = d.get("title", {})
        title = title_obj.get("en", "") if isinstance(title_obj, dict) else str(title_obj)
        source = d.get("source_url", "")
        number = d.get("number", d.get("id", ""))
        status = d.get("status", "")
        app_date = d.get("application_date", "")
        slug = d.get("slug", "")
        if slug and slug in has_fulltext:
            title_display = f"[{title}](./regulations/{slug})"
        elif source:
            title_display = f"[{title}]({source})"
        else:
            title_display = title
        en_lines.append(f"| {number} | {title_display} | {status} | {app_date} |")

    en_lines.extend([
        "",
        "## Related EU Regulations & Directives",
        "",
        "The following EU legislation intersects with MDR compliance requirements:",
        "",
        "| Regulation | Short Name | Relevance to Medical Devices | EUR-Lex |",
        "|------------|-----------|------------------------------|---------|",
    ])

    for d in docs:
        title_obj = d.get("title", {})
        title = title_obj.get("en", "") if isinstance(title_obj, dict) else str(title_obj)
        source = d.get("source_url", "")
        number = d.get("number", "")
        slug = d.get("slug", "")
        short_name = _extract_short_name(number)
        if slug and slug in has_fulltext:
            link = f"[Full Text](./regulations/{slug})"
        elif source:
            link = f"[EUR-Lex]({source})"
        else:
            link = ""
        en_lines.append(f"| {number} | {short_name} | {title} | {link} |")

    en_lines.extend([
        "",
        "---",
        "",
        "::: info Fulltext Availability",
        "Where available, regulation full texts are extracted from EUR-Lex and can be viewed "
        "directly. Click the \"Full Text\" link to access the complete regulatory text.",
        ":::",
    ])

    # Chinese
    zh_lines = [
        "---",
        "title: EU 法规与指令",
        "---",
        "",
        "# EU 法规与指令",
        "",
        "本节涵盖 EU MDR 框架下与医疗器械合规相关的欧盟法规和指令。包括核心的 MDR/IVDR "
        "以及医疗器械制造商必须考虑的其他相关欧盟立法。",
        "",
        "## 核心法规",
        "",
        "| 法规 | 标题 | 状态 | 适用日期 |",
        "|------|------|------|----------|",
    ]

    for d in core_docs:
        title_obj = d.get("title", {})
        title = title_obj.get("zh", title_obj.get("en", "")) if isinstance(title_obj, dict) else str(title_obj)
        source = d.get("source_url", "")
        number = d.get("number", d.get("id", ""))
        status = d.get("status", "")
        app_date = d.get("application_date", "")
        slug = d.get("slug", "")
        if slug and slug in has_fulltext:
            title_display = f"[{title}](./regulations/{slug})"
        elif source:
            title_display = f"[{title}]({source})"
        else:
            title_display = title
        zh_lines.append(f"| {number} | {title_display} | {status} | {app_date} |")

    zh_lines.extend([
        "",
        "## 相关 EU 法规与指令",
        "",
        "以下欧盟立法与 MDR 合规要求存在交叉：",
        "",
        "| 法规编号 | 简称 | 与医疗器械的关系 | EUR-Lex |",
        "|----------|------|------------------|---------|",
    ])

    for d in docs:
        title_obj = d.get("title", {})
        title = title_obj.get("zh", title_obj.get("en", "")) if isinstance(title_obj, dict) else str(title_obj)
        source = d.get("source_url", "")
        number = d.get("number", "")
        slug = d.get("slug", "")
        short_name = _extract_short_name(number)
        if slug and slug in has_fulltext:
            link = f"[全文](./regulations/{slug})"
        elif source:
            link = f"[EUR-Lex]({source})"
        else:
            link = ""
        zh_lines.append(f"| {number} | {short_name} | {title} | {link} |")

    zh_lines.extend([
        "",
        "---",
        "",
        "::: info 全文可用性",
        "部分法规全文已从 EUR-Lex 提取，可直接在线阅读。点击\"全文\"链接查看完整法规文本。",
        ":::",
    ])

    _write_page(DOCS_EN / "regulations.md", "\n".join(en_lines))
    _write_page(DOCS_ZH / "regulations.md", "\n".join(zh_lines))


def _extract_short_name(number: str) -> str:
    """Extract short name from regulation number string."""
    if "(" in number and ")" in number:
        # e.g. "Regulation (EU) 2023/1542 (Battery Regulation)" -> "Battery Regulation"
        parts = number.split("(")
        for p in reversed(parts):
            if ")" in p and not p.startswith("EU") and not p.startswith("EC"):
                return p.rstrip(")")
    return number.split(" - ")[0] if " - " in number else number


def _get_cat_name_en(cat_key: str, stds: list) -> str:
    """Get English category name from first standard's metadata or key."""
    # Look for name in _index.json-style data
    return cat_key.replace("_", " ").title()


def _get_cat_name_zh(cat_key: str, stds: list) -> str:
    """Get Chinese category name."""
    zh_names = {
        "active_implants": "有源植入物",
        "anaesthesia": "麻醉设备",
        "audiology": "听力学",
        "biocompatibility": "生物相容性",
        "biological_materials": "生物来源材料",
        "breathing_gas_pathways": "呼吸气路",
        "cardiology": "心血管",
        "clinical_investigation": "临床调查",
        "connectors": "小口径连接器",
        "cybersecurity": "网络安全",
        "dental": "牙科",
        "diagnostic_imaging": "诊断成像",
        "dialysis": "透析",
        "drug_device_combination": "药械组合",
        "electrical_safety": "电气安全与EMC",
        "endoscopy": "内窥镜",
        "environmental_testing": "环境测试",
        "general": "通用要求",
        "home_healthcare": "家用医疗",
        "implant_materials": "植入材料",
        "implant_testing": "植入物测试",
        "ivd": "体外诊断",
        "labelling": "标签与符号",
        "laser_surgery": "激光手术",
        "lithotripsy": "碎石术",
        "mechanical_testing": "机械测试",
        "medical_gloves": "医用手套",
        "mri_safety": "MRI 安全",
        "needles_syringes": "针头与注射器",
        "neonatal": "新生儿",
        "neurology": "神经学",
        "nuclear_medicine": "核医学",
        "ophthalmic": "眼科",
        "packaging": "包装",
        "patient_monitoring": "患者监护",
        "patient_handling": "患者搬运",
        "patient_warming": "患者加温",
        "phototherapy": "光疗",
        "physiotherapy": "物理治疗",
        "pms": "上市后监督",
        "ppe_barrier": "防护设备",
        "processing": "器械处理",
        "quality_management": "质量管理",
        "radiation_protection": "辐射防护",
        "regulatory_references": "法规参考",
        "reprocessing": "再处理",
        "risk_management": "风险管理",
        "software": "软件与可用性",
        "sterilization": "灭菌",
        "surgical_implants": "外科植入物",
        "surgical_textiles": "手术衣物",
        "therapeutic_ultrasound": "治疗超声",
        "usability": "可用性工程",
        "wound_care": "伤口护理",
        "hearing_aids": "助听器",
    }
    return zh_names.get(cat_key, cat_key.replace("_", " ").title())


def _write_page(path: Path, content: str):
    """Write a page file, creating directories as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
        if not content.endswith("\n"):
            f.write("\n")


def main():
    print("=== Phase 7: Generate Standards Documentation Pages ===")
    print()

    # 1. Load data
    print("Loading harmonised standards...")
    hs_data = load_category_standards(HS_DIR)
    print(f"  {sum(len(s) for s in hs_data.values())} standards in {len(hs_data)} categories")

    print("Loading other standards...")
    os_data = load_category_standards(OS_DIR)
    print(f"  {sum(len(s) for s in os_data.values())} standards in {len(os_data)} categories")

    # 2. Update _index.json counts
    print("\nUpdating _index.json counts...")
    hs_total = update_index_counts(HS_DIR, hs_data)
    os_total = update_index_counts(OS_DIR, os_data)
    print(f"  Harmonised: {hs_total}")
    print(f"  Other: {os_total}")

    # 3. Generate pages
    print("\nGenerating harmonised standards page...")
    generate_harmonised_standards_page(hs_data)
    print("  docs/en/eu_mdr/standards.md")
    print("  docs/zh/eu_mdr/standards.md")

    print("\nGenerating other standards overview page...")
    generate_other_standards_page(os_data)
    print("  docs/en/eu_mdr/other-standards.md")
    print("  docs/zh/eu_mdr/other-standards.md")

    print("\nGenerating other standards category pages...")
    generate_other_standards_category_pages(os_data)
    print(f"  {len(os_data)} category pages (en + zh)")

    print("\nGenerating regulations page...")
    generate_regulations_page()
    print("  docs/en/eu_mdr/regulations.md")
    print("  docs/zh/eu_mdr/regulations.md")

    print("\n=== Done! ===")
    print(f"Total pages generated: {2 + 2 + len(os_data)*2 + 2}")


if __name__ == "__main__":
    main()
