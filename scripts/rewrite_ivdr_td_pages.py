#!/usr/bin/env python3
"""Rewrite EU IVDR TD knowledge pages with curated ZH/EN BPG checklists (#232).

Source: Team-NB Position Paper BPG-IVDR V2 (2025-09-03).
Usability pages intentionally omit MDR/FDA/NMPA comparison (training-only).
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / "docs" / "zh" / "eu_ivdr" / "td"
EN = ROOT / "docs" / "en" / "eu_ivdr" / "td"

# slug -> (zh_markdown, en_markdown)
PAGES: dict[str, tuple[str, str]] = {}


def add(slug: str, zh: str, en: str) -> None:
    PAGES[slug] = (zh.strip() + "\n", en.strip() + "\n")


# ---------------------------------------------------------------------------
# index
# ---------------------------------------------------------------------------
add(
    "index",
    """# EU IVDR 技术文件（Team-NB BPG-IVDR V2）

本目录依据 **Team-NB Position Paper — Best Practice Guidance for the Submission of Technical Documentation under Annexes II and III of In Vitro Diagnostic Medical Devices Regulation (EU) 2017/746（BPG-IVDR V2，2025-09-03）** 整理，对应 IVDR 附件二 / 附件三提交通用期望。

## 章节导航

| 章节 | 页面 |
|------|------|
| 器械描述与规格 | [device-description](./device-description) |
| 制造商提供的信息 | [information-supplied](./information-supplied) |
| 设计与制造信息 | [design-manufacturing](./design-manufacturing) |
| GSPR 检查表 | [gspr](./gspr) |
| 受益-风险与风险管理 | [risk-management](./risk-management) |
| 产品验证与确认 (V&V) | [verification-validation](./verification-validation) |
| 性能评价 (PEP/PER) | [performance-evaluation](./performance-evaluation) |
| PMPF | [pmpf](./pmpf) |
| SSP | [ssp](./ssp) |
| PMS | [pms](./pms) |
| 伴随诊断 | [companion-diagnostics](./companion-diagnostics) |
| TD 封面 / 提交通则 | [cover-letter](./cover-letter) |

## Reguverse 使用提示

- IVDR 项目须先完成并批准 **器械描述（DD）**，再进入性能评价 / GSPR 等下游任务。
- 条款编号一律使用 **IVDR**（勿混用 MDR GSPR / 分类编号）。
- 临床证据邻居是 **性能评价（PEP/PER）与 PMPF**，不是 MDR CER。
""",
    """# EU IVDR Technical Documentation (Team-NB BPG-IVDR V2)

This section follows **Team-NB Position Paper — Best Practice Guidance for the Submission of Technical Documentation under Annexes II and III of IVDR (EU) 2017/746 (BPG-IVDR V2, 2025-09-03)**.

## Section map

| Topic | Page |
|------|------|
| Device description & specifications | [device-description](./device-description) |
| Information supplied by manufacturer | [information-supplied](./information-supplied) |
| Design & manufacturing | [design-manufacturing](./design-manufacturing) |
| GSPR checklist | [gspr](./gspr) |
| Benefit-risk & risk management | [risk-management](./risk-management) |
| Product verification & validation | [verification-validation](./verification-validation) |
| Performance evaluation (PEP/PER) | [performance-evaluation](./performance-evaluation) |
| PMPF | [pmpf](./pmpf) |
| SSP | [ssp](./ssp) |
| PMS | [pms](./pms) |
| Companion diagnostics | [companion-diagnostics](./companion-diagnostics) |
| TD cover / submission | [cover-letter](./cover-letter) |

## Reguverse notes

- IVDR projects require an approved **Device Description (DD)** before PE / GSPR.
- Use **IVDR** clause numbering only.
- Evidence neighbour is **performance evaluation (PEP/PER) and PMPF**, not an MDR CER.
""",
)

# ---------------------------------------------------------------------------
# device-description (expanded)
# ---------------------------------------------------------------------------
add(
    "device-description",
    """# 器械描述与规格（IVDR）

**IVDR 参考：** 附件二，第 1 节  
**BPG 参考：** Team-NB BPG-IVDR V2（2025-09-03）Device Description & Specifications（约第 7–10 页）  
**文件代码：** AII-S1  
**责任方：** 制造商  
**服务模式：** 协助（Reguverse：**执行 PE / GSPR 前的强制前置**）

## 一致性总则

- [ ] 器械名称、预期用途/预期目的在 TD、IFU、标签、性能评价、风险管理、促销材料中一致
- [ ] 若存在不可避免差异：在主技术文件中说明差异及为何仍适用于本次 IVDR 评审范围
- [ ] 申请文件上的器械名称与语言与 TD 一致

## 1.1 器械描述与规格细节

### (a) 名称、一般描述与预期用途 / 使用者

- [ ] 器械或商品名称 + 一般描述（含预期用途/预期目的）
- [ ] 变体/型号/配置/组件/附件清单表：标识符（目录号/型号/条码/UDI 等）+ 名称/描述
- [ ] EMDN 编码详情
- [ ] 适用 IVDR NANDO 编码（(EU) 2017/2185）；一次性/多次使用说明
- [ ] 一般描述足以理解设计、包装、灭菌、组合使用、组件与附件
- [ ] 伴随诊断：关联药品及 INN；注明药品经 EMA 集中程序或成员国主管当局程序
- [ ] 预期用途足够具体，符合 IVDR 第 2 条医学目的
- [ ] 预期使用者（实验室专业人员 / 医护人员 / 外行）由临床性能评价、风险管理与可用性文件支持

### (b) Basic UDI-DI

- [ ] 按附件六 C 部分分配的 Basic UDI-DI
- [ ] 全套 TD 中 Basic UDI-DI 一致
- [ ] 同一 Basic UDI-DI 下多器械：说明差异及同组理由（参见 MDCG 2018-1）

### (c) 预期用途要素（附件二 1.1(c)）

- [ ] (i) 检测和/或测量对象（analyte / measurand）
- [ ] (ii) 功能：筛查、监测、诊断、辅助诊断、预后、预测、伴随诊断等
- [ ] (iii) 拟检测/界定/区分的疾病、状况或风险因素
- [ ] (iv) 是否自动化
- [ ] (v) 定性 / 半定量 / 定量
- [ ] (vi) 所需标本类型
- [ ] (vii) 适用时的检测人群
- [ ] (viii) 预期使用者
- [ ] (ix) 伴随诊断：相关目标人群与关联药品（含 INN）
- [ ] 预期患者/检测人群写入 TD；若无特定人群，须理解无限制使用，并在 IFU 中写明防误用限制（如“非一线筛查”）
- [ ] 预期用途变更时，评估对 TD 各章节的影响
- [ ] 使用者与使用环境描述清晰，并由临床性能评价结果支持

### (d) 检测方法 / 仪器工作原理

- [ ] 检测方法原理或仪器工作原理的详细描述

### (e) 作为 IVD 的定性

- [ ] 按 IVDR 第 2 条论证产品为 IVD（软件尤其注意 MDR/IVDR 边界，参见 MDCG 2019-11）
- [ ] 明确排除：一般实验室用品 / 仅供研究（RUO，除非制造商特别指定用于体外诊断）、侵入性取样产品、国际认证参考物质 / 外部质评材料
- [ ] 标本容器视为 IVD

### (f) 风险等级与分类规则（附件八）

- [ ] 分类由制造商规定的预期用途决定（标签、IFU、性能评价、促销材料）
- [ ] 给出 A/B/C/D 类别及附件八规则逐点论证
- [ ] 多规则适用时列出全部，取最严（最高类别）
- [ ] 同时论证为何某些规则不适用
- [ ] 多检测项目分别分类，整机取最高类别
- [ ] 参考 MDCG 2020-16；独立软件参考 MDCG 2019-11

### (g) 组件与反应性成分

- [ ] 组件描述；适用时描述抗体、抗原、核酸引物等反应性成分

### (h)–(m) 新颖性、组合使用、标本、仪器、软件、配置、附件

- [ ] 新颖特征描述及对安全/性能影响，或明确声明无新颖特征
- [ ] 与其他器械/产品组合使用的描述及兼容性证据
- [ ] 随附或推荐的标本采集/运输材料及分析前要求（如分析物稳定性）
- [ ] 自动化仪器：与适用/专用检测的兼容性证据（作为性能评价一部分）
- [ ] 自动化检测：适用仪器特征/应用表
- [ ] 一并使用或推荐的软件描述及版本
- [ ] 拟上市全部配置/变体完整清单
- [ ] 附件及其他非器械产品（缓冲液、提取试剂盒等）；若附件属 MDR 器械，提供证书/DoC

## 1.2 既往代次与类似器械

- [ ] 制造商既往代次概览（如存在）
- [ ] IVDR 初始申请：是否曾按 IVDD 自我宣告或 NB 认证上市；相对 IVDD 认证版本的变更
- [ ] 市场历史（欧盟及其他地区）；全新器械明确声明从未上市
- [ ] 欧盟或国际市场上类似器械概览及关键规格对比（如存在）

## NB 常见不足

- 预期用途要素不完整或与 IFU / 性能评价不一致
- 变体/附件/UDI/DoC/标签不一致
- 缺少 IVDD→IVDR 变更或市场历史
- 分类仅写结论而无“不适用规则”论证

## 相关页面

- [制造商提供的信息](./information-supplied)
- [设计与制造](./design-manufacturing)
- [性能评价](./performance-evaluation)
""",
    """# Device Description & Specifications (IVDR)

**IVDR reference:** Annex II, Section 1  
**BPG reference:** Team-NB BPG-IVDR V2 (2025-09-03), Device Description & Specifications (approx. pp. 7–10)  
**Document code:** AII-S1  
**Owner:** Manufacturer  
**Service mode:** Assisted (Reguverse: **mandatory before PE / GSPR**)

## Consistency rule

- [ ] Device name and intended purpose/use are consistent across TD, IFU, labels, performance evaluation, risk management and promotional materials
- [ ] Any unavoidable differences are explained in the main technical document
- [ ] Device name/language matches the application form

## 1.1 Device description and specification details

### (a) Name, general description, intended purpose / users

- [ ] Device or trade name and general description including intended purpose
- [ ] Table of each variant/model/configuration/component/accessory in scope with identifiers and descriptions
- [ ] EMDN code details
- [ ] Applicable IVDR NANDO codes ((EU) 2017/2185); single-use / multiple-use
- [ ] Description sufficient to understand design, packaging, sterilisation, combination use, components and accessories
- [ ] Companion diagnostics: associated medicinal product(s) with INN; note EMA centralised vs national CA procedure
- [ ] Intended purpose detailed enough for IVDR Article 2 medical purpose
- [ ] Intended users (lab professionals / HCPs / lay persons) substantiated by clinical performance evaluation, RM and usability

### (b) Basic UDI-DI

- [ ] Basic UDI-DI per Annex VI Part C
- [ ] Consistency across the full TD
- [ ] Devices under one Basic UDI-DI: differences and grouping rationale (MDCG 2018-1)

### (c) Intended purpose elements (Annex II 1.1(c))

- [ ] (i) what is detected and/or measured
- [ ] (ii) function (screening, monitoring, diagnosis, aid to diagnosis, prognosis, prediction, CDx, …)
- [ ] (iii) disorder, condition or risk factor of interest
- [ ] (iv) automated or not
- [ ] (v) qualitative / semi-quantitative / quantitative
- [ ] (vi) specimen type(s)
- [ ] (vii) testing population where applicable
- [ ] (viii) intended user
- [ ] (ix) for CDx: target population and associated medicinal product(s) including INN
- [ ] Intended testing population documented; if unrestricted, include IFU limitations against foreseeable misuse
- [ ] Intended-use changes reviewed for impact across the file
- [ ] User and use environment supported by clinical performance evaluation

### (d)–(f) Principle, qualification, classification

- [ ] Detailed assay method principle or instrument operating principle
- [ ] Qualification as an IVD under Article 2 (software borderline: MDCG 2019-11)
- [ ] Exclusions addressed (general lab / RUO, invasive sampling devices, certified reference materials / EQA materials); specimen receptacles are IVDs
- [ ] Class A/B/C/D with Annex VIII rule-by-rule rationale; strictest rule wins; N/A rules explained; multi-analyte: classify each, highest applies overall (MDCG 2020-16)

### (g)–(m) Components, novelty, combination, specimens, instruments, software, configurations, accessories

- [ ] Components and reactive ingredients (antibodies, antigens, primers, …) as applicable
- [ ] Novel features and impact on safety/performance, or explicit “no novel features”
- [ ] Combination use and compatibility evidence
- [ ] Specimen collection/transport materials and pre-analytical requirements
- [ ] Instrument compatibility (part of performance evaluation) and instrument characteristics table where automated
- [ ] Software used with the device and versioning
- [ ] Complete list of configurations/variants to be placed on the market
- [ ] Accessories and non-device products; MDR accessories: certificate/DoC

## 1.2 Previous generations and similar devices

- [ ] Previous generations overview
- [ ] IVDD legacy (self-declaration and/or NB certificate) and changes vs IVDD-certified version
- [ ] Market history (EU and other regions); totally new devices stated explicitly
- [ ] Similar devices overview with key specification comparison where available

## Common NB gaps

- Incomplete intended-purpose elements vs IFU / performance evaluation
- Variant / accessory / UDI / DoC / label inconsistencies
- Missing IVDD→IVDR change history
- Classification conclusion without non-applicable-rule reasoning

## Related pages

- [Information supplied](./information-supplied)
- [Design & manufacturing](./design-manufacturing)
- [Performance evaluation](./performance-evaluation)
""",
)

# ---------------------------------------------------------------------------
# information-supplied
# ---------------------------------------------------------------------------
add(
    "information-supplied",
    """# 制造商提供的信息（IVDR）

**IVDR 参考：** 第 10(10) 条、附件一 GSPR 20、第 18 条；DoC：第 17 条 / 附件四  
**BPG 参考：** Team-NB BPG-IVDR V2（约第 11–12 页）  
**文件代码：** AII-S2

## 总则

- [ ] 每台器械随附识别器械与制造商所需信息，以及与使用者相关的安全与性能信息（可在器械本体、包装或 IFU 上）
- [ ] 制造商如有网站，应在网站提供并保持更新（第 10(10) 条）

## 标签

- [ ] 提供所有变体最终批准版标签（打印版式）：器械标签、无菌包装、单支包装、销售包装、运输包装（适用层级）
- [ ] 各级包装标签清晰可读，代表成品形态，含全部符号
- [ ] 尽可能提供包装配置图（标签位置）与标签规格（布局、尺寸）
- [ ] 成品上标签位置清晰；无菌包装标签明确标识
- [ ] 包装上印刷的用户信息/示意图一并提供
- [ ] 按 GSPR 20.2 与第 18 条验证标签内容
- [ ] 满足适用协调标准或通用规范（CS）对标签的额外要求
- [ ] 含危险物质/混合物：适用 CLP (EC) No 1272/2008 危险象形图与标签要求
- [ ] 维持无菌状态的包装需额外信息；自测与床旁检测标签需额外信息
- [ ] C/D 类：在标签或 IFU 说明 SSP 可获得位置（第 29 条；EUDAMED 未全面可用时）

## 使用说明书 / 操作手册

- [ ] 按执行符合性评估的 NB 所要求语言提供 IFU
- [ ] TD 中列明拟销售国家并摘要翻译流程；上市前完成目标市场所需语言翻译，初次提交可仅一种 NB 要求语言（翻译程序有效为前提）
- [ ] IFU 中预期用途、适应证、禁忌证、警告等与风险管理、性能评价、可用性等章节一致
- [ ] IFU 含 GSPR 20.4 与第 18 条全部适用信息
- [ ] 满足相关标准/CS 对 IFU 的特定要求
- [ ] 仪器：提供用户手册、安装与维修手册（如适用）
- [ ] 监督评审：提交全部已售国家清单及全部翻译标签/IFU
- [ ] 自测器械 IFU 需额外信息，并需针对外行人群的附加验证

## 电子说明书 (e-IFU)

- [ ] 若使用 e-IFU：器械或随附传单上的电子标签信息
- [ ] 电子标签相关风险管理引用/详情

## 安全数据表 (SDS)

- [ ] 若提供 SDS：SDS 作为 TD 一部分，按成员国要求提供相应译文
- [ ] 标签或 IFU 说明如何获取 SDS
- [ ] 适用 REACH (EC) No 1907/2006 与 CLP；除非相关信息已完整出现在 IFU

## 宣传材料与 DoC

- [ ] 仅需提交提及符合 CE 要求或含 CE 标志的营销材料
- [ ] 营销声明与 IFU 一致，并与 TD 其他部分一致
- [ ] EU DoC（第 17 条 / 附件四最低信息）可用；持续更新并译为官方联盟语言（适用时）

## 关键标准挂钩

- EN ISO 15223（符号，已协调至 IVDR）
- EN ISO 18113、EN ISO 20417（标签/说明书内容指引）

## 相关页面

- [器械描述与规格](./device-description)
- [SSP](./ssp)
- [GSPR](./gspr)
""",
    """# Information Supplied by Manufacturer (IVDR)

**IVDR reference:** Art. 10(10), Annex I GSPR 20, Art. 18; DoC Art. 17 / Annex IV  
**BPG reference:** Team-NB BPG-IVDR V2 (approx. pp. 11–12)  
**Document code:** AII-S2

## General

- [ ] Each device is accompanied by information needed to identify the device and manufacturer and by safety/performance information for the user (on device, packaging or IFU)
- [ ] If the manufacturer has a website, information is available and kept up to date (Art. 10(10))

## Labelling

- [ ] Final approved labels for all variants and applicable packaging levels (device, sterile, unit, sales, transport)
- [ ] Legible finished-form labels showing all symbols
- [ ] Packaging configuration drawings (label placement) and label specifications where possible
- [ ] Clear label positions; sterile-pack labels identified
- [ ] User information printed on packaging provided
- [ ] Label content verified per GSPR 20.2 and Art. 18
- [ ] Harmonised standards / CS labelling requirements addressed
- [ ] Dangerous substances/mixtures: CLP pictograms/labelling ((EC) No 1272/2008)
- [ ] Extra particulars for sterile packaging; self-testing and near-patient testing labels
- [ ] Class C/D: where SSP is available stated on label or IFU (Art. 29; without full EUDAMED)

## Instructions for use / manuals

- [ ] IFU in the language required by the NB assessing conformity
- [ ] TD lists intended sales countries and summarises translation process
- [ ] IFU intended purpose / indications / contraindications / warnings aligned with RM, performance evaluation and usability
- [ ] IFU contains all applicable GSPR 20.4 and Art. 18 information
- [ ] Standards/CS-specific IFU requirements addressed
- [ ] Instruments: user, installation and service manuals where applicable
- [ ] Surveillance: list of countries sold + all translated labelling/IFU
- [ ] Self-testing IFU: additional information and lay-user validation

## e-IFU, SDS, promotional materials, DoC

- [ ] e-IFU: electronic labelling information on device/leaflet + RM reference
- [ ] SDS (if provided) in TD with required translations; how to obtain SDS on label/IFU; REACH/CLP apply unless fully covered in IFU
- [ ] Only CE-claim / CE-mark promotional materials required; claims consistent with IFU/TD
- [ ] EU DoC (Art. 17 / Annex IV minimum content) available and kept updated

## Related standards

- EN ISO 15223; EN ISO 18113; EN ISO 20417

## Related pages

- [Device description](./device-description)
- [SSP](./ssp)
- [GSPR](./gspr)
""",
)

# More pages continue in rewrite_ivdr_td_pages_body.py via exec
_BODY = Path(__file__).with_name("rewrite_ivdr_td_pages_body.py")
if _BODY.exists():
    exec(_BODY.read_text(encoding="utf-8"), {"add": add, "PAGES": PAGES})


def main() -> None:
    for slug, (zh, en) in sorted(PAGES.items()):
        rel = Path(slug + ".md")
        zh_path = ZH / rel
        en_path = EN / rel
        zh_path.parent.mkdir(parents=True, exist_ok=True)
        en_path.parent.mkdir(parents=True, exist_ok=True)
        zh_path.write_text(zh, encoding="utf-8")
        en_path.write_text(en, encoding="utf-8")
        print("wrote", slug)
    print("done", len(PAGES), "pages")


if __name__ == "__main__":
    main()
