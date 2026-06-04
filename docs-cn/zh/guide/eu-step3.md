# 文献检索策略 (Step 3)

## 概述

Step 3 定义系统性文献检索策略，包括数据库选择、检索词、纳入/排除标准等。AI 自动生成符合 MEDDEV 2.7/1 Rev.4 要求的系统性检索策略。

## 操作流程

1. **自动生成**：AI 根据设备信息和预期用途，生成系统性的检索策略
2. **选择数据库**：确认默认数据库（PubMed + Embase），可选添加 Cochrane Library 或 ScienceDirect
3. **审阅**：检查检索词和纳入/排除标准是否合理
4. **批准**：确认检索策略

::: info 注意
文献文件的上传在 Step 4（文献筛选）中进行，不在本步骤操作。
:::

## 生成内容包括

- 检索数据库列表
- 检索词策略 (含 MeSH terms 和自由文本)
- 纳入标准 (Inclusion criteria)
- 排除标准 (Exclusion criteria)
- 检索时间范围
- 文献类型限定

## 支持的文献数据库

| 数据库 | 类型 | 说明 |
|--------|------|------|
| PubMed | 默认 | 生物医学核心数据库 |
| Embase | 默认 | 药学与医疗器械文献 |
| Cochrane Library | 可选 | 系统评价与临床试验 |
| ScienceDirect | 可选 | 综合科技文献 |

::: tip
可在生成检索策略前勾选「Additional Databases」添加 Cochrane Library 和 ScienceDirect。
:::

## 下一步

检索策略批准后，在各数据库执行检索并导出文件，然后在 Step 4 中上传并进行文献筛选。

→ [文献筛选 (Step 4)](./eu-step4)
