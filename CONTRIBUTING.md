# Contributing to DocMCP Knowledge Base

感谢您对医疗器械合规知识库的贡献！/ Thank you for contributing to the medical device regulatory knowledge base!

---

## 目录 / Table of Contents

- [贡献类型 / Contribution Types](#贡献类型--contribution-types)
- [内容规范 / Content Standards](#内容规范--content-standards)
- [数据格式 / Data Format](#数据格式--data-format)
- [文件命名规范 / File Naming](#文件命名规范--file-naming)
- [PR 提交流程 / PR Submission Process](#pr-提交流程--pr-submission-process)
- [URL 验证要求 / URL Verification](#url-验证要求--url-verification)
- [翻译规范 / Translation Guidelines](#翻译规范--translation-guidelines)
- [来源要求 / Source Requirements](#来源要求--source-requirements)

---

## 贡献类型 / Contribution Types

欢迎以下类型的贡献：

- **新增内容**：添加尚未收录的法规、标准、指南文件
- **内容更新**：更新已失效或已修订的文件
- **翻译**：为现有内容提供中英文互译
- **错误修正**：修正内容错误、链接失效、格式问题
- **URL 验证**：验证现有条目的来源链接有效性

Welcome contributions of the following types:

- **New content**: Add regulations, standards, or guidance not yet included
- **Content updates**: Update superseded or revised documents
- **Translation**: Provide Chinese/English translations for existing content
- **Error corrections**: Fix content errors, broken links, or formatting issues
- **URL verification**: Verify source links for existing entries

---

## 内容规范 / Content Standards

### 收录标准 / Inclusion Criteria

内容必须满足以下条件才能被收录：

1. **官方来源**：必须来自官方机构（NMPA、EU 官方公报、FDA、ISO、IEC、SAC 等）
2. **生效状态**：优先收录现行有效文件；已废止文件需标注 `status: "superseded"`
3. **可验证**：必须提供可验证的官方来源 URL
4. **完整性**：内容应完整，不得截断或选择性引用

### 各法规体系收录范围 / Scope by Regulatory Framework

#### EU MDR (`eu_mdr/`)
- **`regulations/`**: EU MDR (2017/745), EU IVDR (2017/746) 及修订条例
- **`standards/`**: EU 官方公报（OJ）发布的协调标准列表（Harmonised Standards）
- **`mdcg/`**: MDCG 指南文件全文（来源：ec.europa.eu/health/mdcg）
- **`team_nb/`**: TEAM-NB 立场文件（来源：team-nb.org）

#### FDA (`fda/`)
- **`regulations/`**: 21 CFR Part 800-900 系列及相关法规
- **`standards/`**: FDA 认可的共识标准（AAMI、ASTM、ANSI 等，来源：FDA 认可标准数据库）
- **`guidance/`**: FDA 指南文件（来源：fda.gov/medical-devices/guidance-documents-medical-devices）

#### NMPA (`nmpa/`)
- **`regulations/`**: NMPA 发布的法规、规章、公告
- **`standards/`**: GB/YY 医疗器械相关国家/行业标准（来源：SAC、NMPA）
- **`guidance/`**: 注册审查指导原则（来源：CMDE，按 NMPA 器械分类编号组织）
- **`classification/`**: 医疗器械分类目录

#### 国际通用 (`_shared/`)
- **`standards/`**: ISO/IEC 国际标准（不专属于单一法规体系的）
  - 例：ISO 14971（风险管理）、ISO 13485（QMS）、IEC 62304（软件）
- **`glossary/`**: 跨法规体系术语对照

---

## 数据格式 / Data Format

每个文档条目由两个文件组成：

### 1. Markdown 内容文件

```
{category}/{document-id}.zh.md   # 中文版
{category}/{document-id}.en.md   # 英文版
```

Markdown 文件头部必须包含 YAML front matter：

```yaml
---
id: nmpa-guidance-21-sw-cmde-2022-9
title:
  zh: 医疗器械软件注册审查指导原则（2022年修订版）
  en: Medical Device Software Registration Review Guidance (2022 Revision)
regulation: nmpa
category: guidance/21-sw
document_number: CMDE-2022-9
effective_date: "2022-03-09"
status: active  # active | superseded | draft
source_url: "https://www.cmde.org.cn/..."
source_url_verified: "2026-02-22"
source_url_status: ok  # ok | archived | broken
source_format: word  # html | pdf | word
translation: ai-assisted  # original | ai-assisted | human-reviewed
last_verified: "2026-02-22"
contributor: your-github-username
---
```

### 2. 目录索引文件

每个分类目录下维护一个 `_index.json`：

```json
{
  "category": "nmpa/guidance/21-sw",
  "title": { "zh": "21 医用软件", "en": "21 Medical Software" },
  "last_updated": "2026-02-22",
  "entries": [
    {
      "id": "nmpa-guidance-21-sw-cmde-2022-9",
      "title": {
        "zh": "医疗器械软件注册审查指导原则（2022年修订版）",
        "en": "Medical Device Software Registration Review Guidance (2022 Revision)"
      },
      "effective_date": "2022-03-09",
      "status": "active",
      "source_url": "https://www.cmde.org.cn/...",
      "source_url_verified": "2026-02-22"
    }
  ]
}
```

---

## 文件命名规范 / File Naming

- 使用小写字母、数字、连字符（`-`），不使用空格或下划线
- 语言后缀：`.zh.md`（中文）、`.en.md`（英文）

| 类型 | 示例文件名 | 说明 |
|------|-----------|------|
| NMPA 指导原则 | `cmde-2022-9.zh.md` | 文号-年份-序号 |
| NMPA 法规 | `order-2021-47.zh.md` | 令-年份-序号 |
| EU MDR 协调标准 | `en-iso-13485-2016.en.md` | 标准编号 |
| MDCG 指南 | `mdcg-2019-16.en.md` | MDCG-年份-序号 |
| FDA 指南 | `fda-guidance-sw-2023.en.md` | 描述性名称 |
| ISO 标准 | `iso-14971-2019.en.md` | 标准编号-年份 |

---

## PR 提交流程 / PR Submission Process

1. **Fork** 本仓库
2. 创建功能分支：`git checkout -b add/nmpa-guidance-21-sw-xxxx`
3. 按规范添加/修改内容
4. 运行验证脚本：`python scripts/validate_schema.py`
5. 运行 URL 验证：`python scripts/verify_urls.py --changed-only`
6. 提交 PR，使用以下标题格式：
   - 新增：`feat(nmpa): add guidance CMDE-2022-9 medical device software`
   - 更新：`update(eu_mdr): update harmonised standards list 2026-01`
   - 修正：`fix(fda): correct broken source URL for 21 CFR 820`

### PR Labels

| Label | 含义 |
|-------|------|
| `new-content` | 新增文档 |
| `update` | 更新现有文档 |
| `translation` | 翻译内容 |
| `needs-review` | 格式复杂，需要人工审核 |
| `url-unverified` | 来源 URL 未能自动验证 |
| `nmpa` / `eu_mdr` / `fda` / `shared` | 法规体系标签 |

---

## URL 验证要求 / URL Verification

**所有来源 URL 必须在提交前验证有效性。**

- URL 必须指向**官方机构**的页面或文件
- 对于 NMPA Word 文档下载链接，需验证文件可下载且内容与标题一致
- 若官方 URL 已失效，请提供**官方存档链接**或标注 `source_url_status: "archived"`
- 不接受非官方镜像或第三方转载链接作为主要来源

### NMPA 文档特殊说明

NMPA 发布的指导原则通常以 Word 文档（.doc/.docx）形式提供下载。处理流程：

1. 从 CMDE 官网（cmde.org.cn）或 NMPA 官网获取官方下载链接
2. 下载并用 python-docx 解析章节结构
3. 按 Heading 样式（标题1/2/3）或中文编号模式（一、二、（一））提取章节
4. 对格式混乱的文档，在 PR 中添加 `needs-review` label
5. 在元数据中标注 `source_format: "word"`

---

## 翻译规范 / Translation Guidelines

| `translation` 字段值 | 含义 |
|---------------------|------|
| `original` | 原文（无需翻译） |
| `ai-assisted` | AI 辅助翻译，未经人工审核 |
| `human-reviewed` | 人工审核过的翻译 |

- **专业术语**：使用行业通用译法（参考 `_shared/glossary/`）
- **法规引用**：保留原文法规编号，括号内附中文/英文译名
- **不翻译**：标准编号（ISO 14971）、文号（CMDE-2022-9）、机构缩写（NMPA、FDA）

---

## 来源要求 / Source Requirements

| 法规体系 | 可接受来源 |
|---------|----------|
| EU MDR/IVDR | EUR-Lex (eur-lex.europa.eu), EC Health (ec.europa.eu/health) |
| 协调标准 | EU 官方公报 (OJ), CEN (cen.eu) |
| MDCG 指南 | EC MDCG 页面 (ec.europa.eu/health/mdcg) |
| TEAM-NB | team-nb.org |
| FDA 法规 | eCFR (ecfr.gov), FDA.gov |
| FDA 指南 | FDA.gov/medical-devices |
| FDA 认可标准 | accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards |
| NMPA 法规 | NMPA 官网 (nmpa.gov.cn) |
| NMPA 指导原则 | CMDE 官网 (cmde.org.cn) |
| GB/YY 标准 | SAC (sac.gov.cn), NMPA |
| ISO/IEC 标准 | ISO.org, IEC.ch（注：全文需购买，仅收录摘要和适用范围） |

---

如有疑问，请提交 [Issue](https://github.com/RASAAS/docmcp-knowledge/issues) 或联系维护者。

For questions, please open an [Issue](https://github.com/RASAAS/docmcp-knowledge/issues) or contact the maintainers.
