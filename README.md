# DocMCP Knowledge Base

> Open regulatory knowledge base for medical device compliance — EU MDR, FDA, NMPA regulations, standards, and guidance documents.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 简介 / Introduction

**中文** | [English](#english)

本仓库是一个开放的医疗器械合规知识库，收录全球主要法规体系（EU MDR、FDA、NMPA）下的法规文本、适用标准、指南文件及解读内容。

所有内容以结构化 Markdown + JSON 格式存储，可被 [DocMCP](https://github.com/RASAAS/docmcp) AI 合规助手直接消费，也可通过 [docs.team-ra.org](https://docs.team-ra.org) 在线浏览。

### 内容范围

| 目录 | 内容 | 语言 |
|------|------|------|
| `eu_mdr/` | EU MDR/IVDR 法规、协调标准、MDCG 指南、TEAM-NB 立场文件 | EN / ZH |
| `fda/` | FDA 法规、FDA 认可共识标准（AAMI/ASTM 等）、指南文件 | EN / ZH |
| `nmpa/` | NMPA 法规、GB/YY 中国标准、指导原则、注册申报要求 | ZH / EN |
| `_shared/` | 国际通用标准（ISO/IEC 等）、跨法规通用内容 | EN / ZH |

### 在线文档

访问 [docs.team-ra.org](https://docs.team-ra.org) 浏览完整内容（支持中英文切换、全文搜索）。

---

## English

This repository is an open regulatory knowledge base for medical device compliance, covering major regulatory frameworks (EU MDR, FDA, NMPA) including regulatory texts, applicable standards, guidance documents, and interpretations.

All content is stored in structured Markdown + JSON format, directly consumable by the [DocMCP](https://github.com/RASAAS/docmcp) AI compliance assistant, and browsable online at [docs.team-ra.org](https://docs.team-ra.org).

### Content Scope

| Directory | Content | Language |
|-----------|---------|----------|
| `eu_mdr/` | EU MDR/IVDR regulations, harmonised standards, MDCG guidance, TEAM-NB position papers | EN / ZH |
| `fda/` | FDA regulations, FDA-recognized consensus standards (AAMI/ASTM etc.), guidance documents | EN / ZH |
| `nmpa/` | NMPA regulations, GB/YY Chinese standards, guidance principles, registration requirements | ZH / EN |
| `_shared/` | International standards (ISO/IEC etc.), cross-regulatory content | EN / ZH |

### Online Documentation

Visit [docs.team-ra.org](https://docs.team-ra.org) to browse all content (supports Chinese/English toggle and full-text search).

---

## Repository Structure

```
docmcp-knowledge/
├── eu_mdr/
│   ├── regulations/        # EU MDR / IVDR regulation texts
│   ├── standards/          # Harmonised standards (OJ published)
│   ├── mdcg/               # MDCG guidance documents (full text)
│   ├── team_nb/            # TEAM-NB position papers
│   └── meta.json           # Regulation metadata
├── fda/
│   ├── regulations/        # FDA regulations (21 CFR etc.)
│   ├── standards/          # FDA-recognized consensus standards (AAMI, ASTM, etc.)
│   ├── guidance/           # FDA guidance documents
│   └── meta.json
├── nmpa/
│   ├── regulations/        # NMPA regulations and announcements
│   ├── standards/          # Chinese standards (GB/YY)
│   ├── guidance/           # Guidance principles (指导原则) by device category
│   ├── classification/     # Device classification catalog
│   └── meta.json
├── _shared/
│   ├── standards/          # International standards (ISO/IEC) not regulation-specific
│   ├── glossary/           # Cross-regulatory terminology
│   └── templates/          # Shared document templates
├── docs/                   # VitePress documentation site source
│   ├── .vitepress/
│   │   └── config.ts
│   ├── zh/                 # Chinese content
│   └── en/                 # English content
├── scripts/
│   ├── migrate_wordpress.py    # WordPress → Markdown migration
│   ├── validate_schema.py      # JSON schema validation
│   ├── fetch_updates.py        # Automated update fetching
│   └── verify_urls.py          # Source URL verification
├── schemas/
│   ├── regulation.schema.json
│   ├── standard.schema.json
│   └── guidance.schema.json
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Data Format

Each document entry consists of:
- A **Markdown file** (`.md`) with the full content in both Chinese and English
- A **JSON metadata file** (`_index.json`) with structured metadata for machine consumption

### JSON Metadata Example

```json
{
  "id": "nmpa-guidance-21-sw-cmde-2022-9",
  "title": {
    "zh": "医疗器械软件注册审查指导原则（2022年修订版）",
    "en": "Medical Device Software Registration Review Guidance (2022 Revision)"
  },
  "regulation": "nmpa",
  "category": "guidance/21-sw",
  "document_number": "CMDE-2022-9",
  "effective_date": "2022-03-09",
  "status": "active",
  "source_url": "https://www.cmde.org.cn/...",
  "source_url_verified": "2026-02-22",
  "source_format": "word",
  "content_zh": "guidance/21-sw/cmde-2022-9.zh.md",
  "content_en": "guidance/21-sw/cmde-2022-9.en.md",
  "translation": "ai-assisted",
  "last_verified": "2026-02-22",
  "contributor": "RASAAS"
}
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

## License

Content in this repository is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).

Scripts and tooling are licensed under [MIT License](LICENSE-MIT).

## Related Projects

- [DocMCP](https://github.com/RASAAS/docmcp) — AI-powered medical device compliance assistant (MCP server + LLM backend)
- [DocMCP Office Plugin](https://github.com/RASAAS/docmcp-office-plugin) — Microsoft Word add-in for regulatory document generation
- [ReguVerse](https://reguverse.com) — Regulatory compliance resources and services
