#!/usr/bin/env python3
"""
Generate VitePress markdown pages for the full NMPA classification catalog.

Reads classification_catalog.json and produces:
  - docs/zh/nmpa/classification.md  (index with L1 summary + links)
  - docs/zh/nmpa/classification/*.md (one page per L1, full L2/L3 tree)
  - docs/en/nmpa/classification.md  (English index)
  - docs/en/nmpa/classification/*.md (English per-L1 pages)

Also generates VitePress sidebar config snippet for config.mts.
"""

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CATALOG_PATH = REPO / "nmpa" / "classification" / "classification_catalog.json"
ZH_OUT = REPO / "docs" / "zh" / "nmpa" / "classification"
EN_OUT = REPO / "docs" / "en" / "nmpa" / "classification"

L1_EN_NAMES = {
    "01": "Active Surgical Instruments",
    "02": "Passive Surgical Instruments",
    "03": "Neurovascular Surgical Instruments",
    "04": "Orthopedic Surgical Instruments",
    "05": "Radiation Therapy Equipment",
    "06": "Medical Imaging Equipment",
    "07": "Medical Diagnostic & Monitoring Instruments",
    "08": "Respiratory, Anesthesia & Emergency Equipment",
    "09": "Physical Therapy Equipment",
    "10": "Transfusion, Dialysis & Extracorporeal Circulation Equipment",
    "11": "Medical Sterilization & Disinfection Equipment",
    "12": "Active Implantable Devices",
    "13": "Passive Implantable Devices",
    "14": "Infusion, Nursing & Protective Equipment",
    "15": "Patient Transfer Equipment",
    "16": "Ophthalmic Devices",
    "17": "Dental Devices",
    "18": "Obstetric, Gynecologic, Assisted Reproduction & Contraceptive Devices",
    "19": "Medical Rehabilitation Devices",
    "20": "Traditional Chinese Medicine Devices",
    "21": "Medical Software",
    "22": "Clinical Laboratory Instruments",
}


def load_catalog():
    with open(CATALOG_PATH, encoding="utf-8") as f:
        return json.load(f)


def build_tree(catalog):
    """Build {l1_code: {l2_code: [items]}} structure."""
    tree = {}
    for item in catalog.get("items", []):
        l1 = item.get("l1_code", "")
        l2 = item.get("l2_code", "")
        if not l1 or not l2:
            continue
        tree.setdefault(l1, {}).setdefault(l2, []).append(item)
    return tree


def generate_zh_index(catalog, tree):
    l1s = catalog["l1_categories"]
    lines = [
        "---",
        "title: NMPA 分类目录",
        "---",
        "",
        "# 医疗器械分类目录",
        "",
        "中国医疗器械分类基于**风险程度**，采用三级分类目录体系。",
        "",
        "## 分类规则",
        "",
        "- **第一类** -- 低风险，一般控制，备案管理",
        "- **第二类** -- 中等风险，特殊控制，省级注册",
        "- **第三类** -- 高风险，上市前审批，国家注册",
        "",
        "## 分类目录（2017版，含后续修订）",
        "",
        f"共 **22** 个一级目录、**{catalog['l2_count']}** 个二级目录、**{catalog['l3_count']}** 个三级产品类别。",
        "",
        "| 编码 | 子目录名称 | 二级目录 | 三级类别 |",
        "|------|----------|---------|---------|",
    ]
    for l1 in l1s:
        c = l1["code"]
        n = l1["name"]
        l2count = len(tree.get(c, {}))
        l3count = sum(len(v) for v in tree.get(c, {}).values())
        lines.append(f"| [{c}](./classification/{c}) | {n} | {l2count} | {l3count} |")

    lines += [
        "",
        "## 分类判定",
        "",
        "对于管理类别不明确或存在争议的产品，NMPA 通过 **分类界定通知** 发布判定结果。",
        "",
        "::: tip 来源",
        "- [NMPA 医疗器械分类目录（2017版）](https://www.nmpa.gov.cn/ylqx/ylqxfgwj/ylqxgfxwj/20180808173901137.html)",
        "- [NMPA 分类目录修订公告](https://www.nmpa.gov.cn/ylqx/ylqxfgwj/ylqxgfxwj/)",
        ":::",
        "",
    ]
    return "\n".join(lines)


def generate_en_index(catalog, tree):
    l1s = catalog["l1_categories"]
    lines = [
        "---",
        "title: NMPA Device Classification",
        "---",
        "",
        "# NMPA Medical Device Classification Catalog",
        "",
        "China's medical device classification uses a three-level catalog based on **risk level**.",
        "",
        "## Classification Rules",
        "",
        "- **Class I** -- Low risk, general controls, filing",
        "- **Class II** -- Moderate risk, special controls, provincial registration",
        "- **Class III** -- High risk, premarket approval, national registration",
        "",
        "## Classification Catalog (2017 Edition, with Amendments)",
        "",
        f"Total: **22** L1 categories, **{catalog['l2_count']}** L2 subcategories, **{catalog['l3_count']}** L3 product groups.",
        "",
        "| Code | Category | L2 | L3 |",
        "|------|----------|-----|-----|",
    ]
    for l1 in l1s:
        c = l1["code"]
        en_name = L1_EN_NAMES.get(c, l1["name"])
        l2count = len(tree.get(c, {}))
        l3count = sum(len(v) for v in tree.get(c, {}).values())
        lines.append(f"| [{c}](./classification/{c}) | {en_name} | {l2count} | {l3count} |")

    lines += [
        "",
        "## Classification Determination",
        "",
        "For products with unclear classification, NMPA issues **Classification Determination Notices**.",
        "",
        "::: tip Source",
        "- [NMPA Classification Catalog (2017)](https://www.nmpa.gov.cn/ylqx/ylqxfgwj/ylqxgfxwj/20180808173901137.html)",
        ":::",
        "",
    ]
    return "\n".join(lines)


def generate_zh_l1_page(l1_code, l1_name, l2_dict):
    """Generate a page for one L1 category with all L2/L3 items."""
    l2_sorted = sorted(l2_dict.keys())
    l2_count = len(l2_sorted)
    l3_count = sum(len(l2_dict[k]) for k in l2_sorted)

    lines = [
        "---",
        f"title: \"{l1_code} {l1_name}\"",
        "---",
        "",
        f"# {l1_code} {l1_name}",
        "",
        f"共 **{l2_count}** 个二级目录、**{l3_count}** 个三级产品类别。",
        "",
    ]
    for l2_code in l2_sorted:
        items = sorted(l2_dict[l2_code], key=lambda x: x.get("code", ""))
        first_name = items[0].get("name", "") if items else ""
        lines.append(f"## {l2_code} {first_name}")
        lines.append("")
        lines.append("| 编码 | 产品类别 | 管理类别 | 品名举例 |")
        lines.append("|------|---------|---------|---------|")
        for it in items:
            code = it.get("code", "")
            name = it.get("name", "")
            dc = it.get("device_class", "")
            ex = it.get("exemption_product_name", "")
            if ex:
                ex = ex.replace("|", "/")[:60]
            lines.append(f"| {code} | {name} | {dc} | {ex} |")
        lines.append("")

    lines.append(f"[<< 返回分类目录](../classification)")
    lines.append("")
    return "\n".join(lines)


def generate_en_l1_page(l1_code, l1_name, l2_dict):
    en_name = L1_EN_NAMES.get(l1_code, l1_name)
    l2_sorted = sorted(l2_dict.keys())
    l2_count = len(l2_sorted)
    l3_count = sum(len(l2_dict[k]) for k in l2_sorted)

    lines = [
        "---",
        f"title: \"{l1_code} {en_name}\"",
        "---",
        "",
        f"# {l1_code} {en_name}",
        "",
        f"**{l2_count}** L2 subcategories, **{l3_count}** L3 product groups.",
        "",
    ]
    for l2_code in l2_sorted:
        items = sorted(l2_dict[l2_code], key=lambda x: x.get("code", ""))
        first_name = items[0].get("name", "") if items else ""
        lines.append(f"## {l2_code} {first_name}")
        lines.append("")
        lines.append("| Code | Product Group | Class | Example Products |")
        lines.append("|------|---------------|-------|------------------|")
        for it in items:
            code = it.get("code", "")
            name = it.get("name", "")
            dc = it.get("device_class", "")
            ex = it.get("exemption_product_name", "")
            if ex:
                ex = ex.replace("|", "/")[:60]
            lines.append(f"| {code} | {name} | {dc} | {ex} |")
        lines.append("")

    lines.append(f"[<< Back to Classification Catalog](../classification)")
    lines.append("")
    return "\n".join(lines)


def main():
    catalog = load_catalog()
    tree = build_tree(catalog)

    ZH_OUT.mkdir(parents=True, exist_ok=True)
    EN_OUT.mkdir(parents=True, exist_ok=True)

    # Index pages (overwrite existing classification.md)
    zh_index_path = ZH_OUT.parent / "classification.md"
    en_index_path = EN_OUT.parent / "classification.md"
    zh_index_path.write_text(generate_zh_index(catalog, tree), encoding="utf-8")
    en_index_path.write_text(generate_en_index(catalog, tree), encoding="utf-8")
    print(f"[written] {zh_index_path}")
    print(f"[written] {en_index_path}")

    # Per-L1 pages
    for l1 in catalog["l1_categories"]:
        c = l1["code"]
        n = l1["name"]
        l2_dict = tree.get(c, {})
        if not l2_dict:
            continue

        zh_path = ZH_OUT / f"{c}.md"
        en_path = EN_OUT / f"{c}.md"
        zh_path.write_text(generate_zh_l1_page(c, n, l2_dict), encoding="utf-8")
        en_path.write_text(generate_en_l1_page(c, n, l2_dict), encoding="utf-8")
        print(f"[written] {zh_path}")
        print(f"[written] {en_path}")

    # Print sidebar config for config.mts
    print("\n=== VitePress sidebar items (paste into config.mts) ===")
    print("// ZH sidebar for /zh/nmpa/classification/")
    print("{")
    print("  text: '分类目录', link: '/zh/nmpa/classification',")
    print("  collapsed: true,")
    print("  items: [")
    for l1 in catalog["l1_categories"]:
        c = l1["code"]
        n = l1["name"]
        print(f"    {{ text: '{c} {n}', link: '/zh/nmpa/classification/{c}' }},")
    print("  ],")
    print("},")

    print(f"\nGenerated {len(catalog['l1_categories'])} L1 pages (ZH + EN)")


if __name__ == "__main__":
    main()
