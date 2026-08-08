# Exec'd by rewrite_ivdr_td_pages.py — defines remaining pages via add()

add(
    "design-manufacturing",
    """# 设计与制造信息（IVDR）

**IVDR 参考：** 附件二，第 3 节  
**BPG 参考：** Team-NB BPG-IVDR V2（约第 13–14 页）  
**文件代码：** AII-S3

## 场所与关键外包方

- [ ] 关键外包生产/服务：名称、地址；与其提供产品/服务相关的证书
- [ ] 关键分包商/供应商若未持有 NB 颁发的有效质量体系证书：向 NB 提供充分证据（如额外供应商审核）
- [ ] 证明采购的关键产品/服务满足规定要求（如 EN ISO 13485 证书、检验/放行记录、协议）
- [ ] 申请文件中包含场所与分包商信息；NB 据此评估是否需现场审核
- [ ] 说明制造商采购控制流程（含受控采购程序引用）

## 设计阶段信息

- [ ] 设计阶段的描述，足以理解设计应用于该器械的方式
- [ ] 设计输入/输出、设计评审、设计验证与设计确认的证据链（或等效 QMS 记录引用）
- [ ] 设计变更控制：变更评估是否引入新危险或影响性能评价结论
- [ ] 软件设计（如适用）：生命周期过程引用（见软件 V&V 页）

## 制造信息

- [ ] 制造工艺概述（含关键工艺步骤、过程控制、特殊过程）
- [ ] 灭菌工艺（如适用）：方法、验证状态、无菌屏障系统
- [ ] 批放行准则与关键质量检验
- [ ] 与标签/包装过程接口清晰

## 供应与可追溯

- [ ] 关键供应商清单及控制程度
- [ ] 可追溯性安排（与 UDI / 批号体系一致）

## NB 常见不足

- 仅列供应商名称而无控制证据
- 设计输出与 IFU/性能声明脱节
- 关键过程（灭菌、冻干、生物原材料）缺少验证引用

## 相关页面

- [器械描述与规格](./device-description)
- [产品验证与确认](./verification-validation)
- [GSPR](./gspr)
""",
    """# Design & Manufacturing Information (IVDR)

**IVDR reference:** Annex II, Section 3  
**BPG reference:** Team-NB BPG-IVDR V2 (approx. pp. 13–14)  
**Document code:** AII-S3

## Sites and critical outsourced parties

- [ ] Name/address of critical outsourced production/services and related certificates
- [ ] Where critical subcontractors/suppliers lack a valid NB QMS certificate: satisfactory evidence for the NB (e.g. additional supplier audits)
- [ ] Evidence that purchased critical products/services meet specified requirements (e.g. EN ISO 13485 certificates, inspection/release records, agreements)
- [ ] Sites and subcontractors included in the application; NB assesses need for on-site audit
- [ ] Description of purchasing controls and controlled procedures

## Design-stage information

- [ ] Description of design stages sufficient to understand how design is applied to the device
- [ ] Design inputs/outputs, reviews, verification and validation evidence chain (or controlled QMS references)
- [ ] Design change control: assessment of new hazards / impact on performance evaluation
- [ ] Software design lifecycle references where applicable

## Manufacturing information

- [ ] Manufacturing process overview (critical steps, process controls, special processes)
- [ ] Sterilisation (if applicable): method, validation status, sterile barrier system
- [ ] Batch release criteria and critical QC
- [ ] Clear interface to labelling/packaging processes

## Supply and traceability

- [ ] Critical supplier list and degree of control
- [ ] Traceability arrangements consistent with UDI / lot systems

## Related pages

- [Device description](./device-description)
- [Verification & validation](./verification-validation)
- [GSPR](./gspr)
""",
)

add(
    "gspr",
    """# GSPR 合规清单（IVDR）

**IVDR 参考：** 附件一（一般安全与性能要求）  
**BPG 参考：** Team-NB BPG-IVDR V2（约第 15 页）  
**文件代码：** AII-S4

## 清单结构要求

- [ ] 对附件一 **每一条**适用 GSPR 给出符合性论证；含分节的 GSPR 须**独立**处理各分节
- [ ] 明确每条适用 GSPR 的符合性证明方法（标准、CS、其他方法、内部规范等）
- [ ] 精确标识证明符合性的受控文件（文件名/编号/版本/日期），并交叉引用其在完整 TD 中的位置
- [ ] 适用标准与 CS 列表；部分采用或偏离时提供摘要/差距分析与正当理由
- [ ] 不适用 GSPR：给出不适用理由（与预期用途/技术特征一致）

## 建议列（示例）

| GSPR | 适用? | 符合方法 | 适用标准/CS | 证据文件位置 | 备注 |
|------|-------|----------|-------------|--------------|------|
| … | Y/N | … | … | … | … |

## 证据邻居（IVDR）

- [ ] 证据指向 **PER / 分析性能 / 临床性能 / RM / V&V / 标签 IFU**，而非 MDR CER
- [ ] Applied Standards 与 Complying Documents 按 IVD 语境填写（含性能评价相关）

## Reguverse 工作流提示

- 使用 `eu_ivdr` 的 Annex I 全文数据生成 checklist（条款号为 IVDR）
- 勿混用 MDR GSPR 编号

## 相关页面

- [风险管理](./risk-management)
- [性能评价](./performance-evaluation)
- [产品验证与确认](./verification-validation)
""",
    """# GSPR Checklist (IVDR)

**IVDR reference:** Annex I (General Safety and Performance Requirements)  
**BPG reference:** Team-NB BPG-IVDR V2 (approx. p. 15)  
**Document code:** AII-S4

## Checklist structure

- [ ] Conformity demonstration for **each** applicable Annex I GSPR; sub-sections addressed independently
- [ ] Method(s) used to demonstrate conformity for each applicable GSPR
- [ ] Precise identity of controlled documents offering evidence, with location cross-references in the full TD
- [ ] List of applicable standards and CS; partial application / deviations justified (summary or gap analysis)
- [ ] Non-applicable GSPRs justified consistently with intended purpose / technology

## Suggested columns

| GSPR | Applicable? | Method | Standard/CS | Evidence location | Notes |
|------|-------------|--------|-------------|-------------------|-------|

## Evidence neighbour (IVDR)

- [ ] Evidence points to **PER / analytical & clinical performance / RM / V&V / labelling IFU**, not an MDR CER

## Reguverse notes

- Generate checklist from `eu_ivdr` Annex I data (IVDR clause numbers only)

## Related pages

- [Risk management](./risk-management)
- [Performance evaluation](./performance-evaluation)
- [Verification & validation](./verification-validation)
""",
)

add(
    "risk-management",
    """# 受益-风险分析与风险管理（IVDR）

**IVDR 参考：** 附件一 GSPR 1–8 等；与性能评价结论一致  
**BPG 参考：** Team-NB BPG-IVDR V2（约第 16–18 页）  
**文件代码：** AII-S5  
**过程标准：** EN ISO 14971（及适用时 ISO/TR 24971）

## 程序与生命周期

- [ ] 提供风险管理程序副本（含所用评级系统定义）
- [ ] 风险管理作为全生命周期连续迭代过程的证据
- [ ] 覆盖器械全部零件/组件
- [ ] 生命周期管理概念证据（上市后信息反馈更新风险分析）

## 风险管理计划

- [ ] 与该器械关联的风险管理计划
- [ ] 范围、职责、可接受性准则、风险控制策略
- [ ] 与可用性、性能评价、PMS/PMPF 的接口

## 安全概念与使用错误

- [ ] 按附件一第 4 节应用安全概念的证据
- [ ] 使用错误相关风险降低覆盖附件一第 5 节要求
- [ ] 建议提供器械使用流程图（便于评审）

## 风险分析与控制

- [ ] 风险分析证明：识别全部已知与可合理预见的危险
- [ ] 每一危险实施风险控制措施（引用实现文件）
- [ ] 风险控制措施有效性已验证（引用验证文件）
- [ ] 设计变更评估是否引入新危险/影响受益-风险
- [ ] IVD 特有危险示例（非穷尽）：假阴性/假阳性后果、标本处理、交叉污染、校准失效、软件失效、自测误用、CDx 用药决策错误等

## 风险管理报告与受益-风险

- [ ] 风险管理报告：剩余风险可接受；受益-风险结论与性能评价一致
- [ ] 制造商对受益与风险的权衡清晰可辨（参见附件七 4.5.4 精神）
- [ ] 风险管理结果为性能评价适当性提供信息

## 相关页面

- [GSPR](./gspr)
- [可用性](./vv/usability)
- [性能评价](./performance-evaluation)
""",
    """# Benefit-Risk Analysis & Risk Management (IVDR)

**IVDR reference:** Annex I GSPR 1–8 et al.; aligned with performance evaluation conclusions  
**BPG reference:** Team-NB BPG-IVDR V2 (approx. pp. 16–18)  
**Document code:** AII-S5  
**Process standard:** EN ISO 14971 (and ISO/TR 24971 where used)

## Procedures and lifecycle

- [ ] Risk management procedure(s) including rating system definitions
- [ ] Evidence of continuous iterative lifecycle risk management
- [ ] Coverage of all parts/components of the device
- [ ] Lifecycle management (post-market information feeds updates)

## Risk management plan

- [ ] Device-specific RMP: scope, responsibilities, acceptability criteria, control strategy
- [ ] Interfaces to usability, performance evaluation, PMS/PMPF

## Safety concept and use error

- [ ] Safety concept per Annex I Section 4
- [ ] Use-error risk reduction covers Annex I Section 5
- [ ] Use flow-chart recommended for reviewability

## Analysis, controls, benefit-risk

- [ ] All known and reasonably foreseeable hazards addressed (IVD examples: false negative/positive consequences, specimen handling, cross-contamination, calibration failure, software failure, self-test misuse, CDx treatment decision errors, …)
- [ ] Risk controls implemented per hazard with document references
- [ ] Effectiveness of controls verified with document references
- [ ] Design changes assessed for new hazards / benefit-risk impact
- [ ] RMR: residual risks acceptable; benefit-risk aligned with performance evaluation

## Related pages

- [GSPR](./gspr)
- [Usability](./vv/usability)
- [Performance evaluation](./performance-evaluation)
""",
)

add(
    "verification-validation",
    """# 产品验证与确认（V&V）（IVDR）

**IVDR 参考：** 附件二相关条款；与附件一 GSPR 及性能评价接口  
**BPG 参考：** Team-NB BPG-IVDR V2（约第 19–30 页，含软件专章）  
**文件代码：** AII-S6（V&V 集合）

## 总览要求

- [ ] V&V 证据支持声称的分析性能、安全与适用 GSPR
- [ ] 方案/报告受控：目的、方法、接受准则、结果、偏差、结论
- [ ] 接受准则事先定义；禁止事后编造
- [ ] 与风险管理、IFU 声明、性能评价声称一致

## 专题页面

| 主题 | 页面 |
|------|------|
| V&V 总览 | [vv/](./vv/) |
| 稳定性（试剂） | [稳定性](./vv/stability) |
| 计量溯源 | [计量溯源](./vv/metrological-traceability) |
| 可用性/人因工程 | [可用性](./vv/usability) |
| 化学/物理/生物特性 | [化学物理生物](./vv/chemical-physical-biological) |
| 软件与网络安全 | [软件](./vv/software) |

## 相关页面

- [设计与制造](./design-manufacturing)
- [性能评价](./performance-evaluation)
- [风险管理](./risk-management)
""",
    """# Product Verification & Validation (IVDR)

**IVDR reference:** Annex II interfaces; Annex I GSPRs; performance evaluation  
**BPG reference:** Team-NB BPG-IVDR V2 (approx. pp. 19–30, including software)  
**Document code:** AII-S6 (V&V set)

## Overview requirements

- [ ] V&V evidence supports claimed analytical performance, safety and applicable GSPRs
- [ ] Controlled protocols/reports: objective, methods, acceptance criteria, results, deviations, conclusions
- [ ] Acceptance criteria predefined — never invented after the fact
- [ ] Consistency with risk management, IFU claims and performance evaluation claims

## Topic pages

| Topic | Page |
|------|------|
| V&V overview | [vv/](./vv/) |
| Stability (reagents) | [stability](./vv/stability) |
| Metrological traceability | [metrological-traceability](./vv/metrological-traceability) |
| Usability / human factors | [usability](./vv/usability) |
| Chemical / physical / biological | [chemical-physical-biological](./vv/chemical-physical-biological) |
| Software & cybersecurity | [software](./vv/software) |

## Related pages

- [Design & manufacturing](./design-manufacturing)
- [Performance evaluation](./performance-evaluation)
- [Risk management](./risk-management)
""",
)

add(
    "vv/index",
    """# V&V 总览（IVDR）

本页汇总 IVDR 技术文件中产品验证与确认的常见专题。具体检查表见各子页。

## 必备接口

- [ ] V&V 范围覆盖声称性能与适用 GSPR
- [ ] 与风险管理危险/控制措施可追溯
- [ ] 与 IFU / 性能评价声称一致
- [ ] 关键供应商/外包测试的资质与协议

## 子页

- [稳定性（试剂）](./stability)
- [计量溯源](./metrological-traceability)
- [可用性/人因工程](./usability)
- [化学/物理/生物特性](./chemical-physical-biological)
- [软件与网络安全](./software)
""",
    """# V&V Overview (IVDR)

This page summarises product verification & validation topics commonly expected in IVDR technical documentation. Detailed checklists are in the child pages.

## Mandatory interfaces

- [ ] V&V scope covers claimed performance and applicable GSPRs
- [ ] Traceability to risk-management hazards/controls
- [ ] Consistency with IFU / performance-evaluation claims
- [ ] Qualification of critical outsourced testing

## Child pages

- [Stability (reagents)](./stability)
- [Metrological traceability](./metrological-traceability)
- [Usability / human factors](./usability)
- [Chemical / physical / biological](./chemical-physical-biological)
- [Software & cybersecurity](./software)
""",
)

add(
    "vv/stability",
    """# 稳定性（试剂）（IVDR）

**BPG 参考：** Team-NB BPG-IVDR V2（V&V — Stability，约第 19–21 页）  
**相关：** 货架期、开瓶/机载稳定性、运输模拟、使用中稳定性

## 要求清单

- [ ] 稳定性研究支持声称的货架期（实时和/或经正当理由的加速数据）
- [ ] 开瓶稳定性 / 机载稳定性（适用时）有方案与报告
- [ ] 运输稳定性 / 挑战条件（温湿度、震动等）与标签储存条件一致
- [ ] 校准品、质控品、试剂分别说明稳定性（如适用）
- [ ] 接受准则与分析方法事先定义；结果统计处理透明
- [ ] 稳定性结论反馈至 IFU 储存/使用说明与风险管理
- [ ] 多配置/多包装规格：覆盖代表性或最差情形并说明外推理由

## NB 常见不足

- 仅有加速数据而无实时计划/正当性
- 开瓶稳定性缺失但 IFU 声称多日使用
- 运输条件与标签储存条件矛盾
""",
    """# Stability (Reagents) (IVDR)

**BPG reference:** Team-NB BPG-IVDR V2 (V&V — Stability, approx. pp. 19–21)  
**Covers:** shelf-life, open-vial/on-board stability, transport simulation, in-use stability

## Checklist

- [ ] Stability studies support claimed shelf-life (real-time and/or justified accelerated data)
- [ ] Open-vial / on-board stability protocols and reports where claimed
- [ ] Transport stability / challenge conditions aligned with labelled storage
- [ ] Calibrators, controls and reagents addressed separately where applicable
- [ ] Predefined acceptance criteria; transparent statistics
- [ ] Conclusions reflected in IFU storage/use statements and risk management
- [ ] Multiple configurations/pack sizes: representative or worst-case coverage with extrapolation rationale

## Common NB gaps

- Accelerated data only without real-time plan/justification
- Missing open-vial data despite multi-day IFU claims
- Transport conditions contradict labelled storage
""",
)

add(
    "vv/metrological-traceability",
    """# 计量溯源（IVDR）

**BPG 参考：** Team-NB BPG-IVDR V2（Metrological traceability，约第 21–22 页）  
**相关：** 校准层级、参考物质/程序、单位、不确定度

## 要求清单

- [ ] 说明测量结果如何溯源至适当参考（参考物质、参考测量程序或国际约定）
- [ ] 校准品赋值方法与层级文件化
- [ ] 单位与换算（如适用）在 IFU 与性能评价中一致
- [ ] 无更高阶参考时：说明制造商内部参考体系与维持方法
- [ ] 与分析性能（正确度/偏倚、互换性）证据衔接
- [ ] 软件/算法参与结果计算时：说明对溯源的影响

## 相关页面

- [稳定性](./stability)
- [性能评价](../performance-evaluation)
""",
    """# Metrological Traceability (IVDR)

**BPG reference:** Team-NB BPG-IVDR V2 (Metrological traceability, approx. pp. 21–22)

## Checklist

- [ ] Explain how results are traceable to an appropriate reference (reference material, reference measurement procedure, or international convention)
- [ ] Calibrator value assignment and hierarchy documented
- [ ] Units/conversions consistent across IFU and performance evaluation
- [ ] Where no higher-order reference exists: describe the manufacturer’s internal reference system and maintenance
- [ ] Link to analytical performance (trueness/bias, commutability)
- [ ] If software/algorithms contribute to results: impact on traceability described

## Related pages

- [Stability](./stability)
- [Performance evaluation](../performance-evaluation)
""",
)

add(
    "vv/usability",
    """# 可用性 / 人因工程（IVDR）

**过程主标准：** IEC 62366-1:2015+A1:2020  
**IVDR 挂钩：** 附件一 GSPR 5（使用错误）；自测/床旁相关信息要求（GSPR 19–20 等）；与性能评价（第 56 条 / 附件十三）及说明书一致  
**BPG 参考：** Team-NB BPG-IVDR V2（Usability，约第 23 页）

## 要求清单

- [ ] 建立可用性工程文件（UEF）：使用规范、危险相关使用场景、用户界面评价计划
- [ ] 识别并控制与使用错误相关的危险（GSPR 5），结果反馈风险管理
- [ ] 形成性评价与总结性评价（或正当化的等效路径）记录完整
- [ ] 预期使用者（实验室专业人员 / 医护 / 外行）与使用环境在 UEF 中明确
- [ ] IFU、标签、培训材料作为用户界面的一部分纳入评价
- [ ] 自测 / 床旁检测：针对外行或近患者用户的额外可用性验证
- [ ] 可用性结论与临床性能评价、剩余风险可接受性一致
- [ ] 接受准则事先定义；缺失数据标记为待制造商完成，禁止编造

## Reguverse 内置 UEF Harness

可在证据 / V&V 域 `usability` 应用 **Usability UEF harness** 生成结构化方案/报告骨架。代码拼装结构；AI 仅填充产品叙事。

## 相关页面

- [风险管理](../risk-management)
- [制造商提供的信息](../information-supplied)
- [性能评价](../performance-evaluation)
""",
    """# Usability / Human Factors (IVDR)

**Primary process standard:** IEC 62366-1:2015+A1:2020  
**IVDR hooks:** Annex I GSPR 5 (use error); self-testing / near-patient information requirements (GSPR 19–20 et al.); consistency with performance evaluation (Art. 56 / Annex XIII) and IFU  
**BPG reference:** Team-NB BPG-IVDR V2 (Usability, approx. p. 23)

## Checklist

- [ ] Usability Engineering File (UEF): use specification, hazard-related use scenarios, UI evaluation plan
- [ ] Use-error-related hazards identified and controlled (GSPR 5); results feed risk management
- [ ] Formative and summative evaluation records (or justified equivalent path)
- [ ] Intended users (lab professionals / HCPs / lay persons) and use environment defined in the UEF
- [ ] IFU, labels and training materials evaluated as part of the user interface
- [ ] Self-testing / near-patient testing: additional usability validation for lay or near-patient users
- [ ] Usability conclusions aligned with clinical performance evaluation and residual-risk acceptability
- [ ] Acceptance criteria predefined; missing data marked for manufacturer completion — never invented

## Reguverse UEF Harness

Apply the **Usability UEF harness** in the evidence / V&V `usability` domain for structured protocol/report skeletons. Structure is code-assembled; AI fills product narrative only.

## Related pages

- [Risk management](../risk-management)
- [Information supplied](../information-supplied)
- [Performance evaluation](../performance-evaluation)
""",
)

add(
    "vv/chemical-physical-biological",
    """# 化学 / 物理 / 生物特性（IVDR）

**BPG 参考：** Team-NB BPG-IVDR V2（Chemical, physical and biological properties，约第 23–25 页）  
**相关 GSPR：** 附件一材料、污染、微生物、生物学等适用条款

## 要求清单

- [ ] 识别与使用者/患者/标本接触的材料与残留物风险
- [ ] 生物相容性评价（当存在身体接触或合理可预见接触时）按适用标准策划并出报告
- [ ] 化学表征 / 浸提物与残留（适用时）支持风险管理结论
- [ ] 微生物状态：生物负荷、无菌、内毒素等按产品类型适用
- [ ] 交叉污染、携带污染（carry-over）控制验证（自动化系统尤其重要）
- [ ] 危险试剂的 SDS / CLP 信息与标签一致
- [ ] 动物/人源材料：来源控制、病毒安全与可追溯（适用时）

## 相关页面

- [器械描述与规格](../device-description)
- [风险管理](../risk-management)
- [稳定性](./stability)
""",
    """# Chemical / Physical / Biological Properties (IVDR)

**BPG reference:** Team-NB BPG-IVDR V2 (Chemical, physical and biological properties, approx. pp. 23–25)

## Checklist

- [ ] Materials and residue risks for user/patient/specimen contact identified
- [ ] Biocompatibility planned and reported where bodily contact is reasonably foreseeable
- [ ] Chemical characterisation / extractables & residuals support RM conclusions where applicable
- [ ] Microbial status (bioburden, sterility, endotoxin) as applicable to product type
- [ ] Cross-contamination / carry-over controls verified (critical for automated systems)
- [ ] SDS/CLP information for hazardous reagents aligned with labelling
- [ ] Materials of animal/human origin: source control, viral safety and traceability where applicable

## Related pages

- [Device description](../device-description)
- [Risk management](../risk-management)
- [Stability](./stability)
""",
)

add(
    "vv/software",
    """# 软件与网络安全（IVDR）

**BPG 参考：** Team-NB BPG-IVDR V2（Software，约第 26–30 页）  
**过程标准：** IEC 62304；网络安全参见 MDCG 2019-16 精神及适用指南  
**定性/分类：** MDCG 2019-11

## 要求清单

- [ ] 软件定性为 IVD（相对 MDR）的论证完整
- [ ] IEC 62304 安全类别与软件开发生命周期文件（计划、需求、架构、详设、单元/集成/系统测试）
- [ ] 软件版本策略、配置管理与已知异常清单（bug list）受控
- [ ] 软件验证与确认证据覆盖声称功能与风险控制
- [ ] 网络安全：威胁建模、安全控制、更新/补丁策略、SBOM（适用时）、残留风险沟通（IFU）
- [ ] SOUP / 第三方组件清单与评估
- [ ] 与仪器/试剂组合使用时的兼容性矩阵与回归策略
- [ ] 性能评价中软件相关分析/临床性能声称有对应测试支持

## 相关页面

- [器械描述与规格](../device-description)
- [GSPR](../gspr)
- [可用性](./usability)
""",
    """# Software & Cybersecurity (IVDR)

**BPG reference:** Team-NB BPG-IVDR V2 (Software, approx. pp. 26–30)  
**Process standard:** IEC 62304; cybersecurity per applicable guidance (incl. MDCG 2019-16 spirit)  
**Qualification/classification:** MDCG 2019-11

## Checklist

- [ ] Qualification as IVD software (vs MDR) documented
- [ ] IEC 62304 safety class and SDLC documentation (plans, requirements, architecture, detailed design, unit/integration/system tests)
- [ ] Versioning, configuration management and known anomaly list controlled
- [ ] Software V&V covers claimed functions and risk controls
- [ ] Cybersecurity: threat modelling, controls, update/patch strategy, SBOM where applicable, residual-risk communication in IFU
- [ ] SOUP / third-party component inventory and assessment
- [ ] Compatibility matrix and regression strategy when used with instruments/reagents
- [ ] Software-related analytical/clinical performance claims supported in performance evaluation

## Related pages

- [Device description](../device-description)
- [GSPR](../gspr)
- [Usability](./usability)
""",
)

add(
    "performance-evaluation",
    """# 性能评价（PEP / PER）（IVDR）

**IVDR 参考：** 第 56 条；附件十三；科学有效性、分析性能、临床性能  
**BPG 参考：** Team-NB BPG-IVDR V2（Performance Evaluation，约第 31–36 页）  
**文件代码：** 性能评价成套文件  
**服务模式：** Reguverse 核心工作流（含上市后 **Performance Evaluation Update**）

## 总则

- [ ] 性能评价计划（PEP）与性能评价报告（PER）受控、版本清晰
- [ ] 评价范围与器械描述中的预期用途、分类、变体范围一致
- [ ] 科学有效性、分析性能、临床性能三者均覆盖（或正当化不适用）
- [ ] 文献、研究、常规诊断使用数据等证据来源透明；检索策略可复现
- [ ] 受益-风险与风险管理结论一致；剩余不确定性进入 PMPF

## 科学有效性

- [ ] 分析物与临床状况/生理状态关联的科学论证
- [ ] 支持预期用途声明的文献或其他证据

## 分析性能

- [ ] 分析性能参数按声称覆盖（如正确度/偏倚、精密度、灵敏度/特异性分析层面、检测限、线性/量程、钩状效应、干扰、交叉反应、矩阵效应等适用项）
- [ ] 方案、接受准则、样本类型与声称一致
- [ ] 计量溯源与校准层级衔接

## 临床性能

- [ ] 临床性能研究 / 等效证据支持预期用途与目标人群
- [ ] 诊断灵敏度/特异度、预测值、似然比等适用指标及置信区间
- [ ] 自测/床旁：外行或近患者使用条件下的性能证据
- [ ] 伴随诊断：与关联药品临床决策相关的性能证据及与药品授权信息一致

## 计划、报告与更新

- [ ] PEP：目标、方法、统计、伦理/监管、里程碑
- [ ] PER：汇总证据、缺口、结论、对 IFU 的影响
- [ ] 上市后：性能评价更新与 PMPF/PMS 数据接口（见 PMPF / PMS 页）

## Reguverse 提示

- 初始 PE 与 **performance_evaluation_update** 均为正式任务；更新任务可重复
- DD 为强制前置；勿在 PE 中重新发明与 DD 冲突的预期用途

## 相关页面

- [器械描述与规格](./device-description)
- [PMPF](./pmpf)
- [PMS](./pms)
- [伴随诊断](./companion-diagnostics)
""",
    """# Performance Evaluation (PEP / PER) (IVDR)

**IVDR reference:** Art. 56; Annex XIII; scientific validity, analytical performance, clinical performance  
**BPG reference:** Team-NB BPG-IVDR V2 (Performance Evaluation, approx. pp. 31–36)  
**Service mode:** Reguverse core workflow (including post-market **Performance Evaluation Update**)

## General

- [ ] Controlled PEP and PER with clear versioning
- [ ] Scope consistent with intended purpose, classification and variants in the Device Description
- [ ] Scientific validity, analytical performance and clinical performance covered (or justified N/A)
- [ ] Transparent evidence sources; reproducible literature search strategy
- [ ] Benefit-risk aligned with RM; residual uncertainties feed PMPF

## Scientific validity / analytical / clinical performance

- [ ] Scientific link between analyte and clinical condition/physiological state
- [ ] Analytical performance parameters as claimed (trueness/bias, precision, LoD, linearity/range, hook effect, interference, cross-reactivity, matrix effects, …)
- [ ] Protocols, acceptance criteria and specimen types aligned with claims; metrological traceability linked
- [ ] Clinical performance evidence for intended purpose and target population (sensitivity/specificity, predictive values, likelihood ratios as applicable)
- [ ] Self-testing / near-patient: performance under intended user conditions
- [ ] CDx: performance relevant to medicinal-product decision-making; consistency with drug authorisation information

## Planning, reporting, updates

- [ ] PEP: objectives, methods, statistics, ethics/regulatory, milestones
- [ ] PER: evidence synthesis, gaps, conclusions, IFU impact
- [ ] Post-market: PE updates interfacing with PMPF/PMS

## Reguverse notes

- Initial PE and **performance_evaluation_update** are both formal tasks; update is repeatable
- DD is a mandatory prerequisite — do not reinvent a conflicting intended purpose inside PE

## Related pages

- [Device description](./device-description)
- [PMPF](./pmpf)
- [PMS](./pms)
- [Companion diagnostics](./companion-diagnostics)
""",
)

add(
    "pmpf",
    """# PMPF 计划与报告（IVDR）

**IVDR 参考：** 附件十三 Part B；与第 56 条性能评价持续更新相关  
**BPG 参考：** Team-NB BPG-IVDR V2 中与上市后性能随访相关的期望  
**文件代码：** PMPF

## 要求清单

- [ ] PMPF 计划：目标、方法、数据源、指标、统计、里程碑、职责
- [ ] 计划与 PER 中识别的剩余不确定性 / 知识缺口对应
- [ ] 数据源可包括：常规诊断使用数据、登记、文献、投诉/vigilance、专项研究等
- [ ] PMPF 报告：结果、对性能评价与 IFU/RM 的影响、后续行动
- [ ] 与 PMS 计划接口清晰；避免重复但确保覆盖
- [ ] C/D 类及高风险声称：PMPF 强度与风险相称

## 相关页面

- [性能评价](./performance-evaluation)
- [PMS](./pms)
- [SSP](./ssp)
""",
    """# PMPF Plan & Report (IVDR)

**IVDR reference:** Annex XIII Part B; continuous update of performance evaluation (Art. 56)  
**Document code:** PMPF

## Checklist

- [ ] PMPF plan: objectives, methods, data sources, metrics, statistics, milestones, responsibilities
- [ ] Plan addresses residual uncertainties / knowledge gaps from the PER
- [ ] Data sources may include routine diagnostic use, registries, literature, complaints/vigilance, dedicated studies
- [ ] PMPF report: results, impact on PE / IFU / RM, follow-up actions
- [ ] Clear interface with the PMS plan
- [ ] Intensity proportionate to risk (notably class C/D and high-risk claims)

## Related pages

- [Performance evaluation](./performance-evaluation)
- [PMS](./pms)
- [SSP](./ssp)
""",
)

add(
    "ssp",
    """# 安全与性能摘要 SSP（IVDR）

**IVDR 参考：** 第 29 条  
**适用：** 主要 C/D 类（及法规规定的其他情形）  
**BPG / 实施：** EUDAMED 未全面可用时，标签或 IFU 须说明 SSP 可获得位置

## 要求清单

- [ ] SSP 内容覆盖法规要求的安全与性能关键信息，与 PER / IFU 一致
- [ ] 语言与公开可及性安排符合要求
- [ ] 标签或 IFU 指明 SSP 获取途径（EUDAMED 或替代安排）
- [ ] 变更控制：性能/安全结论重大变更时更新 SSP
- [ ] 与 DoC、Basic UDI-DI、器械识别信息一致

## 相关页面

- [制造商提供的信息](./information-supplied)
- [性能评价](./performance-evaluation)
- [PMS](./pms)
""",
    """# Summary of Safety and Performance (SSP) (IVDR)

**IVDR reference:** Art. 29  
**Applicability:** primarily class C/D (and other cases required by the Regulation)  
**Implementation note:** while EUDAMED is not fully available, label or IFU must state where the SSP is available

## Checklist

- [ ] SSP covers required safety and performance information and is consistent with PER / IFU
- [ ] Language and public accessibility arrangements meet requirements
- [ ] Label or IFU indicates how to obtain the SSP (EUDAMED or alternative)
- [ ] Change control: update SSP when safety/performance conclusions change materially
- [ ] Consistent with DoC, Basic UDI-DI and device identification

## Related pages

- [Information supplied](./information-supplied)
- [Performance evaluation](./performance-evaluation)
- [PMS](./pms)
""",
)

add(
    "pms",
    """# 上市后监督 PMS（IVDR）

**IVDR 参考：** 第 78–81 条等；附件三  
**相关文件：** PMS 计划；定期更新（如适用类别的 PSUR 等）

## 要求清单

- [ ] PMS 计划：数据源、方法、指标、阈值、职责、报告路径
- [ ] 主动与被动收集：投诉、vigilance、文献、数据库、PMPF、真实世界数据等
- [ ] 与风险管理、性能评价更新、纠正预防措施（CAPA）闭环
- [ ] 趋势分析与信号检测方法文件化
- [ ] 报告义务与时限（严重事件、FSCA 等）程序就绪
- [ ] 输出反馈至 IFU/标签、DD、PER、GSPR 证据维护

## 相关页面

- [PMPF](./pmpf)
- [性能评价](./performance-evaluation)
- [风险管理](./risk-management)
""",
    """# Post-Market Surveillance (PMS) (IVDR)

**IVDR reference:** Arts. 78–81 et al.; Annex III  
**Related documents:** PMS plan; periodic updates (e.g. PSUR where applicable)

## Checklist

- [ ] PMS plan: data sources, methods, metrics, thresholds, responsibilities, reporting pathways
- [ ] Active and passive collection: complaints, vigilance, literature, databases, PMPF, real-world data, …
- [ ] Closed loop with RM, performance-evaluation updates and CAPA
- [ ] Trend analysis and signal detection methods documented
- [ ] Reporting obligations and timelines (serious incidents, FSCA, …) procedurally ready
- [ ] Outputs feed IFU/labels, DD, PER and GSPR evidence maintenance

## Related pages

- [PMPF](./pmpf)
- [Performance evaluation](./performance-evaluation)
- [Risk management](./risk-management)
""",
)

add(
    "companion-diagnostics",
    """# 伴随诊断 CDx（IVDR）

**IVDR 参考：** 第 2 条定义；分类与符合性评估中与药品主管当局/EMA 咨询相关的要求  
**BPG 参考：** Device Description 中 CDx 专段；性能评价对关联药品的要求

## 要求清单

- [ ] 明确为伴随诊断：关联药品通用名/INN、治疗决策语境、目标人群
- [ ] 说明药品授权路径（EMA 集中程序或成员国主管当局）以便 NB 咨询
- [ ] 预期用途 1.1(c)(ix) 要素完整写入 DD 与 IFU
- [ ] 临床性能证据支持与药品标签/授权一致的选择或排除患者用途
- [ ] 风险管理覆盖错误分型导致的用药伤害情景
- [ ] 标签/IFU 清晰提示须与指定药品联合解读
- [ ] 变更（药品标签或试剂性能）影响评估与沟通路径

## 相关页面

- [器械描述与规格](./device-description)
- [性能评价](./performance-evaluation)
- [风险管理](./risk-management)
""",
    """# Companion Diagnostics (CDx) (IVDR)

**IVDR reference:** Art. 2 definition; conformity assessment consultation with medicines authorities / EMA as applicable  
**BPG reference:** CDx notes under Device Description; performance evaluation expectations for associated medicinal products

## Checklist

- [ ] CDx identification: associated medicinal product INN, decision context, target population
- [ ] Medicinal product authorisation path (EMA centralised vs national CA) stated for NB consultation
- [ ] Annex II 1.1(c)(ix) elements complete in DD and IFU
- [ ] Clinical performance evidence supports patient selection/exclusion consistent with drug labelling/authorisation
- [ ] Risk management covers harm scenarios from incorrect biomarker classification
- [ ] Labelling/IFU clearly state joint interpretation with the specified medicinal product
- [ ] Change impact assessment when drug label or assay performance changes

## Related pages

- [Device description](./device-description)
- [Performance evaluation](./performance-evaluation)
- [Risk management](./risk-management)
""",
)

add(
    "cover-letter",
    """# TD 封面信 / 提交通则（IVDR）

**BPG 参考：** Team-NB BPG-IVDR V2 开篇与提交通用期望（约第 1–6 页及全文结构）  
**文件代码：** Sec.00 / Cover

## 要求清单

- [ ] 封面信标明制造商、器械名称、Basic UDI-DI、风险类别、符合性评估路径、NB 申请范围
- [ ] 文件清单（索引）覆盖附件二/三要求章节，含版本与页码/节号
- [ ] 明确提交语言；翻译控制说明
- [ ] 标明是否含既往 IVDD 证书/自我宣告历史及主要变更摘要
- [ ] 关键外包场所与证书索引
- [ ] 保密/电子提交格式符合 NB 指示
- [ ] 申请范围与 DD 变体清单一致

## 相关页面

- [器械描述与规格](./device-description)
- [技术文件目录首页](./)
""",
    """# TD Cover Letter / Submission Generalities (IVDR)

**BPG reference:** Team-NB BPG-IVDR V2 introductory and submission expectations (approx. pp. 1–6 and overall structure)  
**Document code:** Sec.00 / Cover

## Checklist

- [ ] Cover letter identifies manufacturer, device name, Basic UDI-DI, risk class, conformity assessment route and NB application scope
- [ ] Document index covering Annex II/III sections with versions and locations
- [ ] Submission language stated; translation control described
- [ ] IVDD legacy (certificate/self-declaration) and key changes summarised where applicable
- [ ] Critical outsourced sites and certificates indexed
- [ ] Confidentiality / electronic submission format per NB instructions
- [ ] Application scope matches the DD variant list

## Related pages

- [Device description](./device-description)
- [TD index](./)
""",
)

# Soft-retire crosswalk pages: point to usability only (training contrast removed from TD nav)
add(
    "vv/usability-crosswalk",
    """# 说明

本页原用于培训中的法规对照，**不属于 IVDR 技术文件提交通用清单**。

请使用：[可用性 / 人因工程（IVDR）](./usability)
""",
    """# Note

This page previously held training-only regulatory comparisons and is **not** part of the IVDR TD submission checklist.

Please use: [Usability / Human Factors (IVDR)](./usability)
""",
)
