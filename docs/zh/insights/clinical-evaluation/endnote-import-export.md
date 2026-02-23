---
id: eu_mdr-endnote导入和导出
title:
  zh: Endnote导入和导出
  en: ''
regulation: eu_mdr
category: eu_mdr/mdcg
status: active
source_url: https://reguverse.com/documentation/clinical-evaluation/literature-search-and-appraisal/endnote-import-export/
source_url_verified: '2026-02-23'
source_url_status: migrated
source_format: html
translation: original
last_verified: '2026-02-23'
contributor: RASAAS
migrated_from: wordpress
wordpress_id: 3735
effective_date: '2025-08-11'
---

# Endnote导入和导出

找到[**检索方法**](<https://reguverse.com/documentation/lit-search-and-review/search-strategy/>)中导出的包含所有文献的**.nbib** 文件和**.ris** 文件，逐个双击导入到Endnote中，步骤如下：

## 创建项目

以Endnote X9为例，点击 File -> New 创建一个**.enl** 文件，用来存储和管理本项目中所有的文献。

## 导入文献

双击**.nbib** 文件，此时PubMed中检索到的全部文献将会自动导入到当前已创建的项目中。在左侧My Groups中创建一个组，命名为PubMed #1，将本次导入的文献全选并拖入。

[图示] [图示]

完成PubMed文献导入后双击**.ris** 文件，此时Embase中检索到的全部文献将会自动导入到当前已创建的项目中。在左侧My Groups中创建另一个组，命名为Embase #2，将本次导入的文献全选并拖入。

[图示] [图示]

## 去重

顶部菜单中选择 References -> Find Duplicates，在弹出的窗口中确认重复文献并保留其中的一篇。

[图示]

## 导出

完成所有重复文献去重后，选择全部文献，之后在顶部菜单中选择 File -> Export，保存类型选择 **Text File（*.txt）** 按照**作者+标题+摘要** 的形式进行结构化导出，以便于后续使用AI工具进行筛选。

[图示]

使用记事本打开导出的**.txt** 文件，可以看到全部文献（以**作者+标题+摘要** 的形式）的清单。

[图示]

注：使用上述导出格式需要在Endnote中新建一个Output Style。在关于此样式(About this style)中将其进行命名，例如：导出作者-年份-标题-摘要，之后根据需要进行其他设置。

为了在导出时以上述**编号-作者/年代-标题-摘要** 的形式导出，需要设置**Bibliography** 中的**Templates** 选项，在Reference Types中选择Generic，然后通过Insert Field填入对应的内容，或直接使用如下格式：
    
    
    Author. Year. TITLE: Title. ABSTRACT: Abstract

然后在**Bibliography** 中的**Layout** 选项中设置序号样式，可直接使用如下格式：

Start each reference with: 
    
    
    Bibliography Number. 

End each reference with: 直接输入一个回车

注意：上述设置适用于EndNote X9，其他版本可能需要根据实际情况进行调整。
