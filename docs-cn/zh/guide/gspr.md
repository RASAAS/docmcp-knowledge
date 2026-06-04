# GSPR 合规检查

::: info 适用套餐
Pro / Max / CRO
:::

## 概述

GSPR (General Safety and Performance Requirements) 合规检查工作流帮助您系统性地评估器械对 EU MDR Annex I 各条款的符合性，生成完整的 GSPR 合规检查表。

## 法规背景

EU MDR Annex I 定义了医疗器械的基本安全性和性能要求，共分为三章：

| 章节 | 条款范围 | 内容 |
|------|---------|------|
| Chapter I | GSPR 1-9 | 通用要求 |
| Chapter II Part A | GSPR 10-16 | 化学/物理/生物相关要求 |
| Chapter II Part B | GSPR 17-22 | 软件/网络安全/辐射相关要求 |
| Chapter III | GSPR 23 | 标签与说明书 |

## 工作流步骤

GSPR 合规检查分 5 步完成：

### Step 1: Chapter I (GSPR 1-9)

分析器械对通用安全性能要求的符合性：
- 风险管理基本原则
- 设计安全性
- 性能保证
- 产品供应链要求

### Step 2: Chapter II Part A (GSPR 10-16)

分析化学、物理、生物学相关要求：
- 化学和材料特性
- 感染与微生物污染控制
- 含动物/人体组织器械
- 辐射防护
- 电子可编程系统

### Step 3: Chapter II Part B (GSPR 17-22)

分析软件、网络安全等要求：
- 有源医疗器械要求
- 软件医疗器械要求
- 网络安全要求
- 辐射相关要求

### Step 4: Chapter III (GSPR 23)

分析标签和使用说明要求：
- 标识标签要求
- 使用说明书内容
- 安全信息

### Step 5: 文档组装

将所有步骤结果组装为完整的 GSPR 合规检查表文档。

## 智能特性

### 设备类型适用性分析

AI 会首先识别器械原型（SaMD / 软硬件组合 / 纯物理设备），然后根据原型判断各条款的适用性：

- **纯软件设备 (SaMD)**：材料/生物/化学相关条款自动标记为 N/A
- **纯物理设备**：软件/网络安全相关条款标记为 N/A
- **软硬件组合**：根据具体特征评估各条款适用性

### 交叉引用

如果项目中已有临床评价 (CE) 或风险管理 (RM) 任务的数据，GSPR 工作流会自动：
- 引用 CER 中的安全数据摘要
- 引用风险管理中的危害/控制措施/风险矩阵

## 输出文档

GSPR 检查表为多栏宽表格格式（横版 landscape 页面），包含：

| 列 | 说明 |
|----|------|
| GSPR No. | 条款编号 |
| General Requirement | Annex I 原文法条全文 |
| Comply (Y/NA) | Y = 符合，NA = 不适用 |
| Method of Demonstration | 符合性证明方法 |
| Document Reference | 引用文档编号 |

## 下一步

- [风险管理](./risk-management) -- 结合风险分析
- [生成文档](./eu-documents) -- 导出 GSPR 文档
