#!/usr/bin/env python3
"""Generate EU IVDR TD knowledge pages from Team-NB BPG IVDR V2 PDF.

Source: reference/global_regulations/ivdr/Team-NB-PositionPaper-BPG-IVDR-V2-20250903.pdf
Adoption: 2025-09-03, Version V2
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import fitz
except ImportError:
    print("PyMuPDF (fitz) required", file=sys.stderr)
    sys.exit(1)

REPO = Path(__file__).resolve().parents[1]
PDF_CANDIDATES = [
    Path("/Users/michael/Library/CloudStorage/OneDrive-个人/coding/reference/global_regulations/ivdr/Team-NB-PositionPaper-BPG-IVDR-V2-20250903.pdf"),
    REPO.parent / "reference/global_regulations/ivdr/Team-NB-PositionPaper-BPG-IVDR-V2-20250903.pdf",
]

BPG_REF = "Team-NB Position Paper BPG-IVDR V2 (2025-09-03)"
IVDR_REF = "IVDR (EU) 2017/746, Annex II & III"


def find_pdf() -> Path:
    for p in PDF_CANDIDATES:
        if p.exists():
            return p
    raise FileNotFoundError("IVDR BPG PDF not found")


def page_text(doc: fitz.Document, start: int, end: int) -> str:
    """1-based inclusive page range."""
    parts = []
    for i in range(start - 1, min(end, doc.page_count)):
        t = doc.load_page(i).get_text("text")
        # drop running headers/footers noise
        lines = []
        for line in t.splitlines():
            s = line.strip()
            if not s:
                continue
            if s.startswith("TEAM-NB"):
                continue
            if s.startswith("Ref.: Team-NB"):
                continue
            if re.match(r"^Page \d+/\d+$", s):
                continue
            lines.append(s)
        parts.append("\n".join(lines))
    return "\n\n".join(parts)


def bullets_from_text(text: str, limit: int = 40) -> list[str]:
    """Turn BPG expectation lines into checklist items."""
    items: list[str] = []
    for raw in text.splitlines():
        s = raw.strip()
        if not s or len(s) < 12:
            continue
        # skip TOC dotted leaders
        if "...." in s:
            continue
        # prefer expectation / requirement style lines
        if s.startswith(("-", "•", "✓", "*")):
            s = s.lstrip("-•✓* ").strip()
        elif re.match(r"^\([a-z]\)\s", s):
            s = s
        elif re.match(r"^\d+\.\s", s):
            s = s
        else:
            # keep sentences that look like requirements
            low = s.lower()
            if not any(k in low for k in (
                "provide", "include", "describe", "evidence", "shall", "must",
                "should", "demonstrate", "reference", "list", "confirm",
                "提交", "提供", "描述", "证据", "应", "需",
            )):
                continue
        s = re.sub(r"\s+", " ", s)
        if s not in items:
            items.append(s)
        if len(items) >= limit:
            break
    return items


def md_checklist(items: list[str]) -> str:
    if not items:
        return "- [ ] （见原文 BPG 对应章节）\n"
    return "\n".join(f"- [ ] {i}" for i in items) + "\n"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    print("wrote", path.relative_to(REPO))


def page_zh(doc: fitz.Document) -> None:
    base = REPO / "docs/zh/eu_ivdr"

    write(base / "index.md", f"""# EU IVDR 概述

EU IVDR (EU) 2017/746 规范体外诊断医疗器械（IVD）在欧盟的上市与全生命周期合规。

本知识库的**技术文件（TD）**章节按 **{BPG_REF}** 组织，对齐 IVDR **附件二（技术文件）**与**附件三（上市后监督技术文件）**，并补充性能评价（第 56 条 / 附件十三）相关交付物。

## 快速入口

- [技术文件总览（BPG IVDR V2）](./td/)
- [器械描述与规格](./td/device-description) — 建议作为项目首个强制交付
- [性能评价（PEP / PER / PMPF / SSP）](./td/performance-evaluation)
- [GSPR 检查表](./td/gspr)

## 与 EU MDR 的关系

| 主题 | MDR | IVDR |
|------|-----|------|
| 法规 | (EU) 2017/745 | (EU) 2017/746 |
| 核心评价 | 临床评价（CEP/CER） | **性能评价**（科学有效性 / 分析性能 / 临床性能 → PER） |
| 上市后临床/性能 | PMCF | **PMPF** |
| 安全性能摘要 | SSCP | **SSP** |
| GSPR | 附件一（编号不同） | 附件一（IVDR 条款号） |

> 可用性工程过程可共用 IEC 62366-1，但 GSPR 条款号与证据邻居（PER vs CER）不同。见 [可用性（IVDR）](./td/vv/usability)。

## 参考文献

- {IVDR_REF}
- {BPG_REF}
""")

    # Extract sections
    gen = page_text(doc, 5, 6)
    dd = page_text(doc, 7, 10)
    info = page_text(doc, 11, 12)
    dm = page_text(doc, 13, 14)
    gspr = page_text(doc, 15, 15)
    rm = page_text(doc, 16, 18)
    vv = page_text(doc, 19, 21)
    stab = page_text(doc, 22, 22)
    metro = page_text(doc, 23, 23)
    chem = page_text(doc, 24, 25)
    soft = page_text(doc, 26, 30)
    pe = page_text(doc, 31, 33)
    pmpf = page_text(doc, 34, 34)
    pms = page_text(doc, 35, 35)
    cdx = page_text(doc, 36, 36)

    write(base / "td/index.md", f"""# EU IVDR 技术文件

EU IVDR (EU) 2017/746 的技术文件（TD）要求定义在**附件二**（技术文件）和**附件三**（上市后监督技术文件）中。本指南遵循 **{BPG_REF}** 的结构，这是业界通知机构（NB）对 IVD TD 提交的统一最佳实践期望。

## 文件结构（附件二 + 附件三 + 性能评价）

### 附件二 -- 技术文件

| 章节 | 文件 | 代码 | 阶段 |
|------|------|------|------|
| 1 | [器械描述与规格](./device-description) | AII-S1 | 1 |
| 2 | [制造商提供的信息](./information-supplied) | AII-S2 | 1 |
| 3 | [设计与制造信息](./design-manufacturing) | AII-S3 | 1 |
| 4 | [GSPR 合规清单](./gspr) | AII-S4 | 1+4 |
| 5 | [受益-风险与风险管理](./risk-management) | AII-S5 | 1+4 |
| 6 | [产品验证与确认](./verification-validation) | AII-S6-VV | 2 |
| 6.* | [性能评价（PEP / PER）](./performance-evaluation) | AII-S6-PE | 2+3 |
| 6.* | [PMPF 计划与报告](./pmpf) | AII-S6-PMPF | 3+5 |
| 6.* | [SSP](./ssp) | AII-S6-SSP | 3 |

### 附件三 -- 上市后监督技术文件

| 章节 | 文件 | 代码 | 阶段 |
|------|------|------|------|
| — | [PMS 计划与报告](./pms) | AIII-PMS | 3+5 |

### 特殊主题

| 文件 | 代码 | 阶段 |
|------|------|------|
| [伴随诊断（CDx）](./companion-diagnostics) | AII-CDX | 视适用 |
| [TD 封面信 / 提交通则](./cover-letter) | AII-COVER | 最终 |

## 分阶段交付工作流（建议）

| 阶段 | 名称 | 关键文件 |
|------|------|----------|
| **阶段0** | 项目启动与差距分析 | 启动会、器械描述审查、初步差距分析、RMP 框架 |
| **阶段1** | 器械特性化 | AII-S1、AII-S2、AII-S3、RMP、GSPR 差距分析 |
| **阶段2** | V&V 与性能规划 | AII-S6-VV、**PEP**、分析/临床性能数据收集 |
| **阶段3** | 性能评价与 PMS | **PER**、PMPF 计划、PMS 计划、SSP |
| **阶段4** | 整合与定稿 | RMR 定稿、GSPR 最终版（含证据引用）、TD 封面信 |
| **阶段5** | 认证后生命周期 | PMPF 报告、**PER 更新**、PMS/PSUR 类监督支持 |

> **注意：** 阶段依赖为推荐顺序。Reguverse 中 **器械描述（DD）** 应为执行 PE / GSPR 等任务前的强制前置。

## 关键参考文献

- {IVDR_REF}
- {BPG_REF}
- Article 29（SSP）、Article 56 / Annex XIII（性能评价）

## 提交通则（摘自 BPG）

{md_checklist(bullets_from_text(gen, 18))}
""")

    write(base / "td/device-description.md", f"""# 器械描述与规格（IVDR）

**IVDR 参考：** 附件二，第 1 节  
**{BPG_REF}：** Device Description & Specifications（约第 7–10 页）  
**文件代码：** AII-S1  
**责任方：** 制造商  
**服务模式：** 协助（Reguverse 建议作为项目强制首任务）

## 要求清单

### 1. 器械描述与规格细节

{md_checklist(bullets_from_text(dd, 45))}

### 2. 既往代次与类似器械

- [ ] 提供制造商既往代次器械概览（如存在）；IVDR 初始申请说明是否曾按 IVDD 自我宣告/NB 认证上市及相对变更
- [ ] 提供市场历史（含欧盟及其他地区批准时间线）；全新器械需明确声明从未上市
- [ ] 提供欧盟或国际市场上已识别类似器械概览及关键规格对比（如存在）

## NB 常见不足

- 预期用途要素不完整（分析物、标本、人群、用途语境）
- 配置/变体/附件清单与标签、DoC、UDI 不一致
- 缺少 IVDD→IVDR 过渡变更说明或市场历史

## 相关页面

- [制造商提供的信息](./information-supplied)
- [设计与制造](./design-manufacturing)
- [性能评价](./performance-evaluation)
""")

    write(base / "td/information-supplied.md", f"""# 制造商提供的信息（IVDR）

**IVDR 参考：** 第 10(10) 条、附件一 GSPR 20、第 18 条；DoC 见第 17 条 / 附件四  
**{BPG_REF}：** Information to be supplied by manufacturer（约第 11–12 页）  
**文件代码：** AII-S2

## 要求清单

{md_checklist(bullets_from_text(info, 40))}

## 关键标准 / 法规挂钩

- EN ISO 15223（符号，已协调至 IVDR）
- EN ISO 18113、EN ISO 20417（标签/说明书内容指引）
- CLP (EC) No 1272/2008；REACH (EC) No 1907/2006（SDS）
- C/D 类：标签或 IFU 说明 SSP 可获得位置（Art. 29，EUDAMED 未全面可用时）

## 相关页面

- [器械描述与规格](./device-description)
- [SSP](./ssp)
- [GSPR](./gspr)
""")

    write(base / "td/design-manufacturing.md", f"""# 设计与制造信息（IVDR）

**IVDR 参考：** 附件二，第 3 节  
**{BPG_REF}：** Design & Manufacturing Information（约第 13–14 页）  
**文件代码：** AII-S3

## 要求清单

{md_checklist(bullets_from_text(dm, 40))}

## 相关页面

- [器械描述与规格](./device-description)
- [风险管理](./risk-management)
- [产品验证与确认](./verification-validation)
""")

    write(base / "td/gspr.md", f"""# GSPR 合规清单（IVDR）

**IVDR 参考：** 附件一（一般安全与性能要求）  
**{BPG_REF}：** General Safety & Performance Requirements (GSPRs)（约第 15 页）  
**文件代码：** AII-S4

## 要求清单

{md_checklist(bullets_from_text(gspr, 35))}

## Reguverse 工作流提示

- 使用 `eu_ivdr` 的 Annex I 全文数据生成 checklist（条款号为 IVDR，勿混用 MDR 编号）
- 证据位置应引用 **PER / 分析与临床性能 / RM / V&V**，而非 MDR CER
- Applied Standards 与 Complying Documents 类别按 IVD 语境填写（含 Performance Evaluation 相关）

## 相关页面

- [风险管理](./risk-management)
- [性能评价](./performance-evaluation)
- [产品验证与确认](./verification-validation)
""")

    write(base / "td/risk-management.md", f"""# 受益-风险分析与风险管理（IVDR）

**IVDR 参考：** 附件一 GSPR 1–8 等；与性能评价结论一致  
**{BPG_REF}：** Benefit Risk Analysis and Risk Management（约第 16–18 页）  
**文件代码：** AII-S5

## 要求清单

{md_checklist(bullets_from_text(rm, 40))}

## 相关页面

- [GSPR](./gspr)
- [性能评价](./performance-evaluation)
- [PMS](./pms)
""")

    write(base / "td/verification-validation.md", f"""# 产品验证与确认（IVDR）

**IVDR 参考：** 附件二第 6 节及适用 GSPR  
**{BPG_REF}：** Product Verification and Validation（约第 19 页起）  
**文件代码：** AII-S6-VV

IVDR 的 V&V 以**性能特征**为核心（分析性能、临床性能相关验证），并按器械类型覆盖稳定性、计量溯源、可用性、软件、化学/生物材料等。

## 子主题

| 主题 | 页面 |
|------|------|
| 性能特征（总览） | [V&V 总览](./vv/) |
| 稳定性（试剂） | [稳定性](./vv/stability) |
| 计量溯源 | [计量溯源](./vv/metrological-traceability) |
| 可用性 | [可用性](./vv/usability) |
| 化学/物理/生物特性 | [化学物理生物](./vv/chemical-physical-biological) |
| 软件与网络安全 | [软件 V&V](./vv/software) |

## 本页摘录要求

{md_checklist(bullets_from_text(vv, 35))}

## 相关页面

- [性能评价（PEP/PER）](./performance-evaluation)
- [器械描述](./device-description)
""")

    write(base / "td/vv/index.md", f"""# IVDR V&V 总览

本页索引 **{BPG_REF}** 中 Product Verification and Validation 及其子主题。

| 子主题 | 链接 | BPG 约页 |
|--------|------|----------|
| 性能特征 / 分析性能等 | 见 [V&V 主页](../verification-validation) | 19–21 |
| 稳定性（试剂） | [stability](./stability) | 22 |
| 计量溯源 | [metrological-traceability](./metrological-traceability) | 23 |
| 可用性 / 人因 | [usability](./usability) | 23 |
| 化学/物理/生物 | [chemical-physical-biological](./chemical-physical-biological) | 24–25 |
| 软件与网络安全 | [software](./software) | 26–30 |

> 可用性过程标准见 [usability](./usability)；与 MDR 对照见 [usability-crosswalk](./usability-crosswalk)。
""")

    write(base / "td/vv/stability.md", f"""# 稳定性（试剂）（IVDR）

**{BPG_REF}：** Stability (applicable to reagents)（约第 22 页）

## 要求清单

{md_checklist(bullets_from_text(stab, 30))}

## 相关页面

- [V&V 总览](./)
- [性能评价](../performance-evaluation)
""")

    write(base / "td/vv/metrological-traceability.md", f"""# 计量溯源（IVDR）

**{BPG_REF}：** Metrological Traceability（约第 23 页）

## 要求清单

{md_checklist(bullets_from_text(metro, 25))}

## 相关页面

- [V&V 总览](./)
- [性能评价](../performance-evaluation)
""")

    write(base / "td/vv/chemical-physical-biological.md", f"""# 化学、物理与生物特性（IVDR）

**{BPG_REF}：** Chemical, Physical and Biological properties（约第 24–25 页）  
含危险物质/CMR/内分泌干扰、灭菌、生物材料、与环境相互作用、测量功能、辐射防护等适用项。

## 要求清单

{md_checklist(bullets_from_text(chem, 40))}

## 相关页面

- [V&V 总览](./)
- [风险管理](../risk-management)
""")

    write(base / "td/vv/software.md", f"""# 软件与软件确认 / 网络安全（IVDR）

**{BPG_REF}：** Software & Software Validation（约第 26–30 页）  
过程可参考 IEC 62304；网络安全期望与风险、可用性、性能评价一致。

## 要求清单

{md_checklist(bullets_from_text(soft, 45))}

## 相关页面

- [可用性](./usability)
- [V&V 总览](./)
""")

    # Keep existing usability content but prepend BPG citation block if file exists
    usability_path = base / "td/vv/usability.md"
    existing_u = usability_path.read_text(encoding="utf-8") if usability_path.exists() else ""
    if "BPG-IVDR V2" not in existing_u:
        write(usability_path, f"""# 可用性 / 人因工程（IVDR）

**过程主标准：** IEC 62366-1:2015+A1:2020  
**IVDR 挂钩：** 附件一 GSPR 5（使用错误）；自测/床旁相关 GSPR 19–20；与性能评价（第 56 条 / 附件十三）及说明书一致。  
**{BPG_REF}：** Usability（约第 23 页）

## 与 MDR 可用性的关系

可用性工程**过程**共用 IEC 62366-1。IVDR 下主要变化：

| 主题 | IVDR 侧重点 |
|------|-------------|
| 制度 | 体外诊断医疗器械（`eu_ivdr`） |
| GSPR 编号 | 使用错误条款为 IVDR **GSPR 5**（IVDR 技术文档勿写 MDR 条款号） |
| 证据邻居 | PER / 分析与临床性能，而非 MDR CER |
| 自测 / 床旁 | 额外信息与验证要求 |

另见：[MDR↔IVDR 可用性对照](./usability-crosswalk.md) 与 MDR 页 [可用性 / HFE](../../../eu_mdr/td/vv/usability.md)。

## 内置 UEF Harness

可在证据 / V&V 域 `usability` 应用 **Usability UEF harness** 生成结构化方案/报告骨架。代码拼装结构；AI 仅填充产品叙事。缺失数据标记 `[TO BE COMPLETED]`，禁止编造接受准则。

## 中国特殊说明（非平行主路径）

- NMPA 2024 可用性指导原则主要面向医疗器械，**不适用于体外诊断试剂**。
- 中低使用风险路径在部分中国申报中可用**使用错误评估报告**替代完整 UEF——属管辖区特殊情形，不能替代声称 IVDR CE 时的欧盟 UEF 要求。
""")

    write(base / "td/performance-evaluation.md", f"""# 性能评价（PEP / PER）（IVDR）

**IVDR 参考：** 第 56 条、附件十三  
**{BPG_REF}：** Performance Evaluation（含 SSP 与标签相关说明；约第 31–33 页）  
**文件代码：** AII-S6-PE

性能评价是**持续过程**：科学有效性、分析性能、临床性能 → 形成 PER，并由 **PMPF** 驱动生命周期更新（C/D 类必要时至少每年更新）。

## 要求清单（PEP / 支柱 / PER）

{md_checklist(bullets_from_text(pe, 45))}

## Reguverse 任务映射

| 产品任务 | 说明 |
|----------|------|
| Performance Evaluation | 初始认证阶段 |
| Performance Evaluation Update | 上市后 / PMPF 驱动，可重复版本化 |
| PER 文档 | 代码拼装 + AI 辅助叙事；Word 下载带 AI 页眉标识 |

## 相关页面

- [PMPF](./pmpf)
- [SSP](./ssp)
- [GSPR](./gspr)
- [V&V](./verification-validation)
""")

    write(base / "td/pmpf.md", f"""# PMPF 计划与评价报告（IVDR）

**IVDR 参考：** 附件十三 B 部分  
**{BPG_REF}：** Post Market Performance Follow Up（约第 34 页）  
**文件代码：** AII-S6-PMPF

## 要求清单

{md_checklist(bullets_from_text(pmpf, 35))}

## 与 MDR PMCF 的对照

| MDR | IVDR |
|-----|------|
| PMCF Plan / Evaluation Report | **PMPF** Plan / Evaluation Report |
| 更新 CER | 更新 **PER** |

## 相关页面

- [性能评价](./performance-evaluation)
- [PMS](./pms)
- [SSP](./ssp)
""")

    write(base / "td/ssp.md", f"""# 安全与性能摘要 SSP（IVDR）

**IVDR 参考：** 第 29 条  
**{BPG_REF}：** Summary of Safety and Performance (SSP)（约第 34 页）  
**文件代码：** AII-S6-SSP

> 注意：IVDR 使用 **SSP**，不是 MDR 的 SSCP。

## 要求清单

{md_checklist(bullets_from_text(pmpf, 20))}

（BPG 将 SSP 与 PMPF 同页阐述；提交时需单独成文并与标签/IFU 中的可获得性声明一致。）

## 相关页面

- [制造商提供的信息](./information-supplied)
- [性能评价](./performance-evaluation)
""")

    write(base / "td/pms.md", f"""# 上市后监督 PMS（IVDR）

**IVDR 参考：** 附件三等  
**{BPG_REF}：** Post Market Surveillance（约第 35 页）  
**文件代码：** AIII-PMS

## 要求清单

{md_checklist(bullets_from_text(pms, 30))}

## 相关页面

- [PMPF](./pmpf)
- [性能评价更新（产品内任务）](./performance-evaluation)
""")

    write(base / "td/companion-diagnostics.md", f"""# 伴随诊断 Companion Diagnostics（IVDR）

**{BPG_REF}：** Companion Diagnostics（约第 36 页）  
**文件代码：** AII-CDX

## 要求清单

{md_checklist(bullets_from_text(cdx, 25))}

## 相关页面

- [性能评价](./performance-evaluation)
- [器械描述](./device-description)
""")

    write(base / "td/cover-letter.md", f"""# TD 封面信 / 提交通则（IVDR）

**{BPG_REF}：** General Considerations（约第 5–6 页）  
**文件代码：** AII-COVER

封面信与行政信息用于减少 NB 审查延误（不完整提交、结构混乱是最常见原因）。

## 建议清单

{md_checklist(bullets_from_text(gen, 25))}

## 相关页面

- [技术文件总览](./)
- [器械描述](./device-description)
""")


def page_en(doc: fitz.Document) -> None:
    base = REPO / "docs/en/eu_ivdr"

    write(base / "index.md", f"""# EU IVDR Overview

EU IVDR (EU) 2017/746 governs in vitro diagnostic medical devices (IVDs) in the Union across the full lifecycle.

This knowledge base organises **Technical Documentation (TD)** around **{BPG_REF}**, aligned with IVDR **Annex II** and **Annex III**, plus performance evaluation deliverables (Article 56 / Annex XIII).

## Quick links

- [TD overview (BPG IVDR V2)](./td/)
- [Device description & specification](./td/device-description) — recommended mandatory first deliverable
- [Performance evaluation (PEP / PER / PMPF / SSP)](./td/performance-evaluation)
- [GSPR checklist](./td/gspr)

## Relationship to EU MDR

| Topic | MDR | IVDR |
|-------|-----|------|
| Regulation | (EU) 2017/745 | (EU) 2017/746 |
| Core evaluation | Clinical evaluation (CEP/CER) | **Performance evaluation** → PER |
| Post-market follow-up | PMCF | **PMPF** |
| Safety & performance summary | SSCP | **SSP** |

## References

- {IVDR_REF}
- {BPG_REF}
""")

    gen = page_text(doc, 5, 6)
    dd = page_text(doc, 7, 10)
    info = page_text(doc, 11, 12)
    dm = page_text(doc, 13, 14)
    gspr = page_text(doc, 15, 15)
    rm = page_text(doc, 16, 18)
    vv = page_text(doc, 19, 21)
    stab = page_text(doc, 22, 22)
    metro = page_text(doc, 23, 23)
    chem = page_text(doc, 24, 25)
    soft = page_text(doc, 26, 30)
    pe = page_text(doc, 31, 33)
    pmpf = page_text(doc, 34, 34)
    pms = page_text(doc, 35, 35)
    cdx = page_text(doc, 36, 36)

    write(base / "td/index.md", f"""# EU IVDR Technical Documentation

Technical documentation under IVDR (EU) 2017/746 is defined in **Annex II** and **Annex III**. This guide follows **{BPG_REF}**, the Team-NB unified best-practice expectation for IVD TD submissions.

## Document structure

### Annex II -- Technical Documentation

| Section | Document | Code | Phase |
|---------|----------|------|-------|
| 1 | [Device Description & Specification](./device-description) | AII-S1 | 1 |
| 2 | [Information Supplied by Manufacturer](./information-supplied) | AII-S2 | 1 |
| 3 | [Design & Manufacturing](./design-manufacturing) | AII-S3 | 1 |
| 4 | [GSPR Checklist](./gspr) | AII-S4 | 1+4 |
| 5 | [Benefit-Risk & Risk Management](./risk-management) | AII-S5 | 1+4 |
| 6 | [Product Verification & Validation](./verification-validation) | AII-S6-VV | 2 |
| 6.* | [Performance Evaluation (PEP / PER)](./performance-evaluation) | AII-S6-PE | 2+3 |
| 6.* | [PMPF Plan & Report](./pmpf) | AII-S6-PMPF | 3+5 |
| 6.* | [SSP](./ssp) | AII-S6-SSP | 3 |

### Annex III -- PMS Documentation

| Document | Code | Phase |
|----------|------|-------|
| [PMS Plan & Reports](./pms) | AIII-PMS | 3+5 |

### Special / administrative

| Document | Code |
|----------|------|
| [Companion Diagnostics](./companion-diagnostics) | AII-CDX |
| [TD Cover Letter / Submission Practices](./cover-letter) | AII-COVER |

## Phased delivery (recommended)

| Phase | Focus | Key outputs |
|-------|-------|-------------|
| 0 | Kick-off / gap | DD review, RMP framework |
| 1 | Characterisation | AII-S1/S2/S3, RMP, GSPR gap |
| 2 | V&V + PE planning | VV, **PEP**, analytical/clinical data |
| 3 | PE + PMS | **PER**, PMPF plan, PMS, SSP |
| 4 | Integration | RMR final, GSPR final, cover letter |
| 5 | Lifecycle | PMPF report, **PER updates**, PMS |

> In Reguverse, **Device Description (DD)** should be the mandatory gate before PE / GSPR tasks.

## References

- {IVDR_REF}
- {BPG_REF}

## Submission practices (from BPG)

{md_checklist(bullets_from_text(gen, 18))}
""")

    pages = {
        "td/device-description.md": ("Device Description & Specification (IVDR)", "Annex II §1", "pp. 7–10", dd, 45),
        "td/information-supplied.md": ("Information Supplied by Manufacturer (IVDR)", "Art. 10(10), GSPR 20, Art. 18; DoC Art. 17 / Annex IV", "pp. 11–12", info, 40),
        "td/design-manufacturing.md": ("Design & Manufacturing Information (IVDR)", "Annex II §3", "pp. 13–14", dm, 40),
        "td/gspr.md": ("GSPR Checklist (IVDR)", "Annex I", "p. 15", gspr, 35),
        "td/risk-management.md": ("Benefit-Risk & Risk Management (IVDR)", "Annex I GSPRs + PE alignment", "pp. 16–18", rm, 40),
        "td/verification-validation.md": ("Product Verification & Validation (IVDR)", "Annex II §6", "from p. 19", vv, 35),
        "td/vv/stability.md": ("Stability (reagents) (IVDR)", "BPG Stability", "p. 22", stab, 30),
        "td/vv/metrological-traceability.md": ("Metrological Traceability (IVDR)", "BPG Metrological Traceability", "p. 23", metro, 25),
        "td/vv/chemical-physical-biological.md": ("Chemical, Physical & Biological Properties (IVDR)", "BPG Chemical/Physical/Biological", "pp. 24–25", chem, 40),
        "td/vv/software.md": ("Software Validation & Cybersecurity (IVDR)", "BPG Software & Software Validation", "pp. 26–30", soft, 45),
        "td/performance-evaluation.md": ("Performance Evaluation — PEP / PER (IVDR)", "Art. 56 / Annex XIII", "pp. 31–33", pe, 45),
        "td/pmpf.md": ("PMPF Plan & Evaluation Report (IVDR)", "Annex XIII Part B", "p. 34", pmpf, 35),
        "td/pms.md": ("Post-Market Surveillance (IVDR)", "Annex III", "p. 35", pms, 30),
        "td/companion-diagnostics.md": ("Companion Diagnostics (IVDR)", "BPG Companion Diagnostics", "p. 36", cdx, 25),
        "td/cover-letter.md": ("TD Cover Letter / Submission Practices (IVDR)", "BPG General Considerations", "pp. 5–6", gen, 25),
    }

    for rel, (title, ivdr, pages_s, text, lim) in pages.items():
        overview = "../" if "/vv/" in rel else "./"
        write(base / rel, f"""# {title}

**IVDR reference:** {ivdr}  
**{BPG_REF}:** {pages_s}  

## Checklist

{md_checklist(bullets_from_text(text, lim))}

## See also

- [TD overview]({overview})
""")

    # fix see-also clumsiness for nested vv pages - rewrite key ones cleanly
    write(base / "td/vv/index.md", f"""# IVDR V&V Overview

Index of Product Verification and Validation topics from **{BPG_REF}**.

| Topic | Link | Approx. pages |
|-------|------|----------------|
| Performance characteristics | [VV main](../verification-validation) | 19–21 |
| Stability (reagents) | [stability](./stability) | 22 |
| Metrological traceability | [metrological-traceability](./metrological-traceability) | 23 |
| Usability / HFE | [usability](./usability) | 23 |
| Chemical / physical / biological | [chemical-physical-biological](./chemical-physical-biological) | 24–25 |
| Software & cybersecurity | [software](./software) | 26–30 |
""")

    write(base / "td/ssp.md", f"""# Summary of Safety and Performance — SSP (IVDR)

**IVDR reference:** Article 29  
**{BPG_REF}:** SSP (approx. p. 34)

> IVDR uses **SSP**, not MDR SSCP.

## Checklist

{md_checklist(bullets_from_text(pmpf, 20))}

## See also

- [Information supplied](./information-supplied)
- [Performance evaluation](./performance-evaluation)
""")

    usability_path = base / "td/vv/usability.md"
    existing_u = usability_path.read_text(encoding="utf-8") if usability_path.exists() else ""
    if "BPG-IVDR V2" not in existing_u:
        write(usability_path, f"""# Usability / Human Factors (IVDR)

**Process standard:** IEC 62366-1:2015+A1:2020  
**IVDR hooks:** Annex I GSPR 5 (use error); self-testing / near-patient GSPRs 19–20; consistency with performance evaluation (Art. 56 / Annex XIII) and IFU.  
**{BPG_REF}:** Usability (approx. p. 23)

## Relationship to MDR usability

The **process** is shared (IEC 62366-1). Under IVDR:

| Topic | IVDR emphasis |
|-------|----------------|
| Regime | In vitro diagnostic devices (`eu_ivdr`) |
| GSPR numbering | Use-error clause is IVDR **GSPR 5** |
| Evidence neighbours | PER / analytical & clinical performance (not MDR CER) |
| Self-test / NPT | Additional information and validation expectations |

See also: [MDR↔IVDR usability crosswalk](./usability-crosswalk.md) and [MDR usability](../../../eu_mdr/td/vv/usability.md).

## Built-in UEF Harness

Apply the **Usability UEF harness** in Evidence / V&V domain `usability` to generate structured plan/report skeletons. Code assembles structure; AI fills product narrative only. Missing data must be `[TO BE COMPLETED]`.
""")


def main() -> None:
    pdf = find_pdf()
    doc = fitz.open(pdf)
    print("PDF", pdf, "pages", doc.page_count)
    page_zh(doc)
    page_en(doc)
    print("done")


if __name__ == "__main__":
    main()
