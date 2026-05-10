#!/usr/bin/env python3
"""
Generate VitePress markdown pages for the full NMPA standards library.

Reads standards.json and produces:
  - docs/zh/nmpa/standards.md  (index with stats + domain pages)
  - docs/zh/nmpa/standards/general.md  (general domain standards)
  - docs/zh/nmpa/standards/professional.md  (professional domain standards)
  - docs/en/nmpa/standards.md  (English index)
  - docs/en/nmpa/standards/general.md
  - docs/en/nmpa/standards/professional.md
"""

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STD_PATH = REPO / "nmpa" / "standards" / "master" / "standards.json"
ZH_OUT = REPO / "docs" / "zh" / "nmpa" / "standards"
EN_OUT = REPO / "docs" / "en" / "nmpa" / "standards"


def load_standards():
    with open(STD_PATH, encoding="utf-8") as f:
        return json.load(f)


def split_by_domain(stds):
    general = []
    professional = []
    for s in stds:
        d = s.get("dir_name", "")
        if "通用" in d:
            general.append(s)
        else:
            professional.append(s)
    return general, professional


def group_by_l1l2(stds):
    """Group standards by (l1, l2) categories."""
    groups = {}
    for s in stds:
        l1 = s.get("l1", "")
        l2 = s.get("l2", "")
        key = (l1, l2)
        groups.setdefault(key, []).append(s)
    return groups


def std_type(number):
    if number.startswith("GB/T"):
        return "GB/T"
    elif number.startswith("GB"):
        return "GB"
    elif number.startswith("YY/T"):
        return "YY/T"
    elif number.startswith("YY"):
        return "YY"
    return "Other"


def generate_zh_index(stds, general, professional):
    gb_count = sum(1 for s in stds if s.get("number", "").startswith("GB"))
    yy_count = len(stds) - gb_count
    active = sum(1 for s in stds if s.get("status") == "active")
    upcoming = sum(1 for s in stds if s.get("status") == "upcoming")

    return f"""---
title: NMPA 医疗器械标准
---

# 中国医疗器械标准（GB / YY）

中国医疗器械标准体系由国家标准和行业标准两部分组成：

| 标准代号 | 类型 | 说明 |
|----------|------|------|
| **GB** | 强制性国家标准 | 由 SAC（国家标准化管理委员会）发布 |
| **GB/T** | 推荐性国家标准 | 推荐采用，非强制 |
| **YY** | 强制性行业标准 | 由 NMPA 发布 |
| **YY/T** | 推荐性行业标准 | 推荐采用，非强制 |

## 标准库概况

| 统计项 | 数量 |
|--------|------|
| 标准总数 | **{len(stds):,}** |
| 其中 GB 系列 | {gb_count} |
| 其中 YY 系列 | {yy_count} |
| 现行有效 | {active} |
| 即将实施 | {upcoming} |

## 按领域浏览

- **[通用技术领域（{len(general)}项）](./standards/general)** -- 适用于大多数医疗器械的基础标准
- **[专业技术领域（{len(professional)}项）](./standards/professional)** -- 特定产品类别的专用标准

::: tip 数据来源
标准数据采集自 [NIFDC 医疗器械标准信息查询](https://app.nifdc.org.cn/biaogzx/qxqwk.do)（中检院），包含全量现行有效和即将实施标准。
:::
"""


def generate_en_index(stds, general, professional):
    gb_count = sum(1 for s in stds if s.get("number", "").startswith("GB"))
    yy_count = len(stds) - gb_count
    active = sum(1 for s in stds if s.get("status") == "active")
    upcoming = sum(1 for s in stds if s.get("status") == "upcoming")

    return f"""---
title: NMPA Medical Device Standards
---

# Chinese Medical Device Standards (GB / YY)

| Prefix | Type | Description |
|--------|------|-------------|
| **GB** | Mandatory national standard | Published by SAC |
| **GB/T** | Recommended national standard | Voluntary |
| **YY** | Mandatory industry standard | Published by NMPA |
| **YY/T** | Recommended industry standard | Voluntary |

## Overview

| Metric | Count |
|--------|-------|
| Total standards | **{len(stds):,}** |
| GB series | {gb_count} |
| YY series | {yy_count} |
| Currently active | {active} |
| Upcoming | {upcoming} |

## Browse by Domain

- **[General Technical Domain ({len(general)})](./standards/general)** -- Foundational standards
- **[Professional Technical Domain ({len(professional)})](./standards/professional)** -- Product-specific standards

::: tip Data Source
Collected from [NIFDC Medical Device Standards Query](https://app.nifdc.org.cn/biaogzx/qxqwk.do).
:::
"""


def generate_domain_page_zh(stds, domain_name, domain_key):
    groups = group_by_l1l2(stds)
    sorted_keys = sorted(groups.keys())

    lines = [
        "---",
        f"title: \"{domain_name}\"",
        "---",
        "",
        f"# {domain_name}",
        "",
        f"共 **{len(stds)}** 项标准。",
        "",
    ]

    for (l1, l2) in sorted_keys:
        items = groups[(l1, l2)]
        items.sort(key=lambda x: x.get("number", ""))
        header = f"{l1}" if not l2 else f"{l1} > {l2}"
        if header.strip():
            lines.append(f"## {header}")
        else:
            lines.append("## (未分类)")
        lines.append("")
        lines.append("| 标准编号 | 标准名称 | 状态 |")
        lines.append("|----------|---------|------|")
        for s in items:
            num = s.get("number", "")
            title = s.get("title_zh", "").replace("|", "/")
            status = "现行" if s.get("status") == "active" else "即将实施" if s.get("status") == "upcoming" else s.get("status_zh", "")
            lines.append(f"| {num} | {title} | {status} |")
        lines.append("")

    lines.append(f"[<< 返回标准库](../standards)")
    lines.append("")
    return "\n".join(lines)


def generate_domain_page_en(stds, domain_name, domain_key):
    groups = group_by_l1l2(stds)
    sorted_keys = sorted(groups.keys())

    lines = [
        "---",
        f"title: \"{domain_name}\"",
        "---",
        "",
        f"# {domain_name}",
        "",
        f"**{len(stds)}** standards in this domain.",
        "",
    ]

    for (l1, l2) in sorted_keys:
        items = groups[(l1, l2)]
        items.sort(key=lambda x: x.get("number", ""))
        header = f"{l1}" if not l2 else f"{l1} > {l2}"
        if header.strip():
            lines.append(f"## {header}")
        else:
            lines.append("## (Uncategorized)")
        lines.append("")
        lines.append("| Standard No. | Title | Status |")
        lines.append("|--------------|-------|--------|")
        for s in items:
            num = s.get("number", "")
            title = s.get("title_zh", "").replace("|", "/")
            status = "Active" if s.get("status") == "active" else "Upcoming" if s.get("status") == "upcoming" else s.get("status", "")
            lines.append(f"| {num} | {title} | {status} |")
        lines.append("")

    lines.append(f"[<< Back to Standards](../standards)")
    lines.append("")
    return "\n".join(lines)


def main():
    stds = load_standards()
    general, professional = split_by_domain(stds)

    print(f"Total: {len(stds)}, General: {len(general)}, Professional: {len(professional)}")

    ZH_OUT.mkdir(parents=True, exist_ok=True)
    EN_OUT.mkdir(parents=True, exist_ok=True)

    # Index pages
    zh_idx = ZH_OUT.parent / "standards.md"
    en_idx = EN_OUT.parent / "standards.md"
    zh_idx.write_text(generate_zh_index(stds, general, professional), encoding="utf-8")
    en_idx.write_text(generate_en_index(stds, general, professional), encoding="utf-8")
    print(f"[written] {zh_idx}")
    print(f"[written] {en_idx}")

    # Domain pages
    for (items, zh_name, en_name, key) in [
        (general, "通用技术领域标准", "General Technical Domain Standards", "general"),
        (professional, "专业技术领域标准", "Professional Technical Domain Standards", "professional"),
    ]:
        zh_p = ZH_OUT / f"{key}.md"
        en_p = EN_OUT / f"{key}.md"
        zh_p.write_text(generate_domain_page_zh(items, zh_name, key), encoding="utf-8")
        en_p.write_text(generate_domain_page_en(items, en_name, key), encoding="utf-8")
        print(f"[written] {zh_p}")
        print(f"[written] {en_p}")


if __name__ == "__main__":
    main()
