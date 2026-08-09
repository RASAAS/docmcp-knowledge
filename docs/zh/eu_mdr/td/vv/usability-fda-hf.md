# FDA 人因工程 — 过程指南 vs 申报内容指南

Reguverse 将 **两份互补的 FDA 指南** 分开处理，且均 **不替代** 产品中以 IEC 62366-1 为骨干的可用性工程文件（UEF）过程。

## 1. 过程指南

**标题：** *Applying Human Factors and Usability Engineering to Medical Devices*  
**作用：** 说明如何在风险管理与设计控制中开展人因/可用性工程（用户、使用环境、UI、形成性评价、人因验证测试方法等）。  
**与 UEF 的典型对应：** Use Specification ↔ 用户/使用环境；critical tasks ↔ 入选总结性评价的危害相关使用情景；formative ↔ 条款 5.8；HF validation ↔ 总结性评价 5.9。

## 2. 申报内容指南（2026）

**标题：** *Content of Human Factors Information in Medical Device Marketing Submissions*  
**发布：** 2026-05-29  
**审评期望实施：** **2026-08-01** 及之后收到的申报  
**适用范围：** 510(k)、De Novo、PMA、HDE（CDRH 医疗器械）  
**不替代：** 风险管理 / 设计控制 / 实际开展 HFE — 仅规定 **申报应提交何种级别的人因信息**。  
**Town Hall：** 2026-07-22 CDRH（幻灯/实录见 CDRH Learn）。

### HF 申报类别（Submission Categories）

| 类别 | 何时（概要） | 通常提交什么 |
|------|--------------|--------------|
| **1** | 变更器械；UI/用户/用途/环境/培训/标签均无变化 | 结论 + 人因高阶摘要 |
| **2** | 无关键任务（新品）/无新增或受影响关键任务（变更），**或** Decision Point D 判定可不提交验证数据 | Cat1 内容 + 用户/UI/已知使用问题 + 论证 |
| **3** | 关键任务需要提交人因验证 | 完整 HFE/UE 报告（含初步分析、**URRA**、关键任务、最终设计人因验证） |

流程图：**A** 是否变更器械？→ **B** UI/用户/用途/环境/培训/标签是否变化？→ **C** 是否存在关键任务？→ **D** 是否应提交人因验证数据？  
**Decision Point D** 是关键：存在关键任务 **不等于** 必须按 Category 3 提交验证数据。

### URRA

使用相关风险分析（指南 Table 2）及 comparative URRA（Table 3）为活文档。典型列：任务、使用错误、危险处境、伤害、严重度、**关键任务 Y/N**、风险控制、控制有效性验证方法。

### eSTAR

更新后的 eSTAR 模板会引导选择 Category（“Guide Me”或自选）并定位支撑材料。

## 3. Reguverse 实现方式

| 层级 | 实现 |
|------|------|
| 过程 UEF | 内置 Usability Harness（`#231`）— IEC 62366-1 Document+Study |
| UE ↔ RM | `#233`–`#235`（同一危害表、Sync） |
| FDA 申报 Overlay | `#236` Path B — Category 向导 + **URRA 派生视图** + 按类别 Submission Pack Word 下载 |
| Feature Visibility | 继续挂 `evidence_registry`（不新增 feature key） |
| 当前范围 | **仅 MD**；组合产品排除；IVD eSTAR 延后 |

**过程侧 Summative 硬门禁：** EU/IVDR/NMPA 仍要求已选 HRUS + 实质 UI Spec 后才能创建总结性 Study（`#233` D10）。  
**FDA Cat 1/2 申报包：** 即使过程中已有 Summative Study，也可不纳入人因验证细节 — UI 会明确区分「过程」与「申报」。

## 相关页面

- [MDR 可用性](./usability)
- [IVDR 可用性](/zh/eu_ivdr/td/vv/usability)
