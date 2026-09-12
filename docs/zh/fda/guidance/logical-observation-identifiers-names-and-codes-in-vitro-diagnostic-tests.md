---
title: "体外诊断检测的逻辑观察标识符名称与代码(LOINC)：行业与FDA工作人员指南"
description: "Logical Observation Identifiers Names and Codes for In Vitro Diagnostic Tests : Guidance for Industry and Food and Drug Administration Staff"
published: 2018-06-15
---

# 体外诊断检测的逻辑观察标识符名称与代码(LOINC)：行业与FDA工作人员指南

**Logical Observation Identifiers Names and Codes for In Vitro Diagnostic Tests : Guidance for Industry and Food and Drug Administration Staff**

**发布日期**：2018-06-15

**状态**：Final（最终）
**类型**：Guidance Document
**类别**：数字健康与网络安全
**主题**：Labeling、Laboratory Tests、IVDs (In Vitro Diagnostic Devices)、Digital Health
**案卷号**：FDA-2017-D-6982

::: tip 官方来源
https://www.fda.gov/regulatory-information/search-fda-guidance-documents/logical-observation-identifiers-names-and-codes-in-vitro-diagnostic-tests
PDF：https://www.fda.gov/media/113967/download
:::

::: info
本内容由英文原文机器辅助翻译，并经结构校对。如有歧义，以英文官方文本为准。
:::

<!-- fulltext-start -->

---

## 官方文件全文

本指南代表美国食品药品监督管理局（FDA或FDA）对该主题的当前观点。它不赋予任何个人任何权利，对FDA或公众不具有约束力。如果您采用的替代方法满足适用法律法规的要求，则可以采用该替代方法。如需讨论替代方法，请联系本指南标题页所列的负责FDA工作人员或办公室。
## I. 简介
美国食品药品监督管理局（FDA或FDA）认识到，随着电子健康记录（EHR）的日益实施，对体外诊断（IVD）检测编码方式进行标准化的需求也在增加。协调并标准化在电子医疗系统中采集与存储的信息，对公共卫生具有重要意义，包括加快医疗服务提供者获取患者诊断信息、减轻实验室将新诊断系统接入实验室信息系统（LIS）的负担，以及便于将医疗信息用于决策支持工具等，还有更多潜在用途。
IVD检测信息在全部EHR中占有相当大的比例。实验室通常会为实验室开展的每项检测关联一个LOINC®（逻辑观察标识符名称与代码；由Regenstrief研究所拥有、开发并维护）¹代码。对于每项IVD检测，LOINC提供与检测属性相关的唯一数字代码，用于识别IVD检测类型，例如组分、属性、时间、系统、标度与方法。²
目前，LOINC是临床实验室和EHR中使用最广泛的IVD编码系统，也是美国卫生与公众服务部（HHS）国家卫生信息技术协调办公室（ONC）作为有意义使用（meaningful use）重要组成部分所推荐的IVD编码标准。LOINC是部分获FDA认可的共识标准，该认可仅限于IVD检测。要查阅目前未被FDA认可的LOINC类别，请参见FDA认可共识标准数据库网站。
³
重要的是区分LOINC代码与唯一器械标识符（UDI）。LOINC编码系统识别所进行的实验室检测类型，而UDI识别特定制造商生产的受监管实验室器械的具体型号/版本。⁴ 本指南既不涉及也不影响与受监管器械UDI分配相关的要求。
FDA指南文件（包括本指南）不确立具有法律强制执行力的责任。相反，指南描述FDA对某一主题的当前观点，且除非援引具体的法规或法定要求，否则应仅视为建议。在FDA指南中使用“应当（should）”一词，表示某事项被建议或推荐，但并非强制要求。同样，本指南中使用“不应当（should not）”并不暗示或创设独立的法律禁止，而表示一种推荐做法。
## II. 背景
语义互操作性在医疗信息技术中的关键作用已得到充分认识。⁵ 第13410号行政令将互操作性定义为“在不同环境中与不同的信息技术系统、软件应用和网络准确、有效、安全且一致地通信和交换数据的能力，并以保留且不改变数据的临床或操作目的与含义的方式交换数据。”⁶ FDA的《研究数据技术符合性指南》进一步将语义互操作性定义为“系统共享的信息能够被理解的能力，从而使非数值数据可由接收系统处理。语义互操作性是一个多层次概念，其程度取决于对数据内容术语及其他因素的一致程度。语义互操作性程度越高，所需人工处理越少，从而降低数据分析中的错误与低效。受控术语和一致定义的元数据支持语义互操作性。”⁷
实验室检测的明确且一致的表示，对于实现电子健康记录的许多潜在益处至关重要。语义互操作性对于开发能够访问并无缝汇总来自多个系统的数据的决策支持算法至关重要。例如，在传染病背景下，语义可互操作的EHR系统可通过提供来自多个地理位置、可评估的实时IVD检测信息，更高效地追踪疫情或重大公共卫生威胁。一致的表示还允许使用EHR数据库研究诊断检测，而无需针对各现场不同的编码方案进行调整。使用EHR数据库的研究示例可能包括：评估快速核酸检测是否需常规继以传统确证方法的上市后研究，或评估IVD在不同临床环境中性能的研究。对标准化数据的潜在分析，有望为获取可用于未来监管行动的真实世界证据提供途径。在EHR中对IVD检测进行明确且一致的表示，还可尽量减少信息在系统间传输时的潜在错误（例如，确保始终保持检测结果的正确单位），从而在系统日益互联的情况下帮助降低患者风险。
语义互操作性应视为一般互操作性的具体应用。FDA支持为IVD检测采用统一的LOINC编码系统，这与FDA在促进医疗器械互操作性其他方面的努力相一致。
⁸
## III. 范围
在FDA寻求鼓励IVD检测编码一致性的背景下，本指南回应有关IVD检测制造商向用户（主要是临床实验室和软件供应商）分发LOINC代码的问题。本指南仅限于针对特定类型IVD检测适当使用LOINC代码，不涉及检测结果的互操作性编码，例如通过在SNOMED-CT（医学系统命名法—临床术语）或LOINC等编码系统中使用应答集。本指南亦不涉及唯一器械标识（UDI），UDI按法规要求识别单个器械。⁹
## IV. IVD的LOINC编码
### A. FDA是否强制要求对IVD检测进行LOINC编码？
否。LOINC或任何类似的IVD检测编码系统均为自愿性，并非FDA所要求。¹⁰
然而，FDA强烈鼓励使用共识标准对IVD检测进行编码，并特别认可LOINC在此用途上的实用价值。¹¹
### B. 制造商是否应在器械标签中列入LOINC代码？
如果信息准确且与器械已批准或已获准的适应证一致，FDA支持在标签中自愿列入IVD检测的LOINC代码。
FDA不打算对制造商可能选择向临床实验室或其他用户提供的LOINC代码进行上市前审查。但是，器械标签一般仍须遵守《联邦食品、药品和化妆品法》的其他要求，包括贴错标签与掺假相关规定。
制造商可选择在印刷标签中列入LOINC代码，或列入指向标签之外列出或以其他方式提供该IVD检测LOINC代码的位置的引用。例如，标签可包含指向列有与制造商检测相关的LOINC代码表的网站超链接。直接纳入器械的LOINC代码——例如，与直接传输至LIS等外部系统的器械输出一并包含的LOINC代码——可能须遵守适用于该器械的质量体系要求。
### C. FDA对制造商为未获准或未批准预期用途提供LOINC代码有何观点？
一般而言，制造商提供的LOINC代码应与该IVD检测经FDA批准或FDA获准的预期用途一致。制造商通过例如列入印刷标签或制造商网站等方式传播某LOINC代码，若该代码暗示未批准或未获准的预期用途，可被视为新预期用途的证据，并可能导致该器械依据《FD&C法》被视为掺假和/或贴错标签。
¹²
但是，FDA理解临床实验室或其他人员可能就特定未获准或未批准预期用途的LOINC代码向制造商提出个别、未经请求的询问。在此情况下，若制造商的答复为请求中所述特定情形提供适当的LOINC编码，或指出需要新的LOINC代码以应对请求中提及的临床使用，则FDA不打算将该答复视为企业意图将该产品用于未批准或未获准用途的证据。¹³
本指南不改变IVD检测何时需提交新的上市前通知（510(k)）或新的上市前批准申请（PMA）的要求。
此外，本指南不影响临床实验室在其他现行法律法规下适用的要求。
### D. FDA是否推荐分发LOINC代码的特定格式？
否。FDA没有推荐分发LOINC代码的特定格式。FDA承认，LOINC代码可以表格形式的简单文本显示，或以JavaScript对象表示法（JSON）或可扩展标记语言（XML）等结构化格式显示。
但是，FDA强烈鼓励使用FDA认可的共识标准，作为向实验室或其他终端用户沟通或传播由制造商或其他方（例如Regenstrief研究所）提供的LOINC代码的机制。面向IVD的LOINC传输文件（LIVD）标准是由IVD行业互联互通联盟专门为此目的制定的一种通信标准。
¹⁴ 标准化格式可便于实验室采用新的LOINC代码、纳入对现有LOINC代码的更新或变更，并维护适用于本地使用的LOINC代码数据库。FDA建议制造商关注该领域的发展，因为电子传输推荐LOINC代码的标准可能被修改或扩展，或出现新标准，这些都可能进一步促进实验室内部及实验室之间更大程度的语义互操作性。

---

## 脚注

[^1]: 见 http://loinc.org/

[^2]: https://loinc.org/get-started/loinc-term-basics/

[^3]: 见 LOINC 的认可共识标准页面：https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfstandards/detail.cfm?id=32889。

[^4]: 见 http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/UniqueDeviceIdentification/。

[^5]: 见全国共享互操作性路线图：https://www.healthit.gov/sites/default/files/hie-interoperability/nationwide-interoperability-roadmap-final-version-1.0.pdf。

[^6]: 见第13410号行政令《促进联邦政府管理或赞助的医疗保健项目中的优质高效医疗》。

[^7]: 见《研究数据技术符合性指南》：https://www.fda.gov/downloads/ForIndustry/DataStandards/StudyDataStandards/UCM384744.pdf

[^8]: 见“医疗器械互操作性”：http://www.fda.gov/medicaldevices/digitalhealth/ucm512245.htm。

[^9]: 见 http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/UniqueDeviceIdentification/。

[^10]: 如前所述，本指南既不涉及也不影响UDI要求。

[^11]: 见 LOINC 的认可共识标准页面：https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfstandards/detail.cfm?standardidentification_no=32889。

[^12]: 见《FD&C法》第501(f)(1)、502(o)、513(f)(1)和515条（21 U.S.C. 351(f)(1)、352(o)、360c(f)(1)和360e）。另见FDA行业指南《药品和器械制造商与付费方、处方集委员会及类似实体的沟通——问答》。

[^14]: 见 http://ivdconnectivity.org/livd/
