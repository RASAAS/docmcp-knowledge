---
id: eu_mdr-endnote导入和导出
title:
  zh: Endnote导入和导出
  en: EndNote Import and Export
regulation: eu_mdr
category: insights/clinical-evaluation
status: active
source_url: https://docs.team-ra.org/zh/insights/clinical-evaluation/endnote-import-export
source_url_verified: '2026-02-23'
source_format: html
translation: ai-assisted
last_verified: '2026-02-23'
contributor: RASAAS
effective_date: '2025-08-11'
---

# EndNote Import and Export

Locate the **.nbib** and **.ris** files exported from the databases (see [Search Strategy](./search-strategy)), and double-click each to import into EndNote.

## Create a Project

In EndNote X9, click **File → New** to create a **.enl** file to store and manage all references for this project.

## Import References

Double-click the **.nbib** file; all PubMed references will be automatically imported. In **My Groups**, create a group named **PubMed #1** and drag all imported references into it.

![](/images/eu_mdr-mdcg/image-1024x498.png) ![](/images/eu_mdr-mdcg/image-1-1024x500.png)

Double-click the **.ris** file; all Embase references will be automatically imported. Create a group named **Embase #2** and drag all imported references into it.

![](/images/eu_mdr-mdcg/image-2-1024x459.png) ![](/images/eu_mdr-mdcg/image-3-1024x479.png)

## Deduplication

From the top menu, select **References → Find Duplicates**. Confirm duplicates in the dialog and retain one copy of each.

![](/images/eu_mdr-mdcg/image-6-1024x586.png)

## Export

Select all references, then go to **File → Export**. Set the file type to **Text File (*.txt)** and export in **Author + Title + Abstract** format for subsequent AI-assisted screening.

![](/images/eu_mdr-mdcg/image-7-1024x743.png)

Open the exported **.txt** file in a text editor to view the complete reference list.

![](/images/eu_mdr-mdcg/image-8-1024x909.png)

**Note**: To use this export format, create a new Output Style in EndNote. Name it (e.g., "Export Author-Year-Title-Abstract") and configure the **Bibliography → Templates** for the Generic reference type using:

```
Author. Year. TITLE: Title. ABSTRACT: Abstract
```

In **Bibliography → Layout**, set the numbering style:

```
Bibliography Number.
```

End each reference with a carriage return.

> Note: The above applies to EndNote X9. Other versions may require adjustments.
