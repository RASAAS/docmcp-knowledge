---
title: Principles and Practices for Medical Device Cybersecurity
---

# Principles and Practices for Medical Device Cybersecurity

**文件编号**: IMDRF/CYBER WG/N60FINAL:2020

::: tip 官方来源
[https://www.imdrf.org/documents/principles-and-practices-medical-device-cybersecurity](https://www.imdrf.org/documents/principles-and-practices-medical-device-cybersecurity)
:::

::: info
This content has been machine-translated from the English original.
:::

<!-- fulltext-start -->

---

## 全文

# 医疗器械网络安全原则和实践

**Document Number**: IMDRF/CYBER WG/N60FINAL:2020

**Source**: [https://www.imdrf.org/documents/principles-and-practices-medical-device-cybersecurity](https://www.imdrf.org/documents/principles-and-practices-medical-device-cybersecurity)

---

**IMDRF/CYBER WG/N60FINAL:2020**

**最终文档**

****

**标题：** 医疗器械网络安全原则和实践

**编写组：** 医疗器械网络安全工作组

**日期：** 2020年3月18日

Dr Choong May Ling, Mimi, IMDRF 负责人

本文件由国际医疗器械监管论坛制作。对本文件的复制或使用没有限制；然而，将本文件（部分或全部）纳入其他文件，或将其翻译成其他语言，并不代表国际医疗器械监管论坛的认可。

© 2020年 国际医疗器械监管论坛 版权所有。

**目录**

1.0 简介 5

2.0 范围 5

3.0 定义 6

4.0 总体原则 9

4.1 全球协调

4.2 整个产品生命周期 9

4.3 共同责任 10

4.4 信息共享 10

5.0 医疗器械网络安全预上市考虑 10

5.1 安全要求和架构设计 10

5.2 针对整个产品生命周期的风险管理原则 13

5.3 安全测试 15

5.4 整个产品生命周期网络安全管理计划 16

5.5 标签和客户安全文档 16

5.5.1 标签 16

5.5.2 客户安全文档 17

5.6 提交给监管机构的文档 18

5.6.1 设计文档 18

5.6.2 风险管理文档 18

5.6.3 安全测试文档 18

5.6.4 TPLC 网络安全管理规划文档 19

5.6.5 标签和客户安全文档 19

6.0 医疗器械网络安全后的市场考量 19

6.1 在预期使用环境中运行设备 19

6.1.1 医疗机构和患者 19

6.1.2 医疗器械制造商 20

6.2 信息共享 20

6.2.1 关键原则 21

6.2.2 关键利益相关者 21

6.2.3 信息类型 22

6.2.4 可信的通信 23

6.3 有效信息披露 23

6.3.1 医疗器械制造商 23

6.3.2 监管机构 24

6.3.3 漏洞发现者（包括安全研究人员和其他人） 25

6.4 漏洞修复 25

6.4.1 医疗器械制造商 25

6.4.2 医疗机构和患者 27

6.4.3 监管机构 30

6.5 事故响应 32

6.5.1 医疗器械制造商 32

6.5.2 医疗机构 33

6.5.3 医疗器械监管机构 34

6.6 遗留医疗器械 34

6.6.1 医疗器械制造商 35

6.6.2 医疗机构 37

7.0 参考文献 38

7.1 IMDRF 文档 38

7.2 标准 38

7.3 监管指导 39

7.4 其他资源和参考资料 40

8.0 附录 42

8.1 附录 A：事件响应角色（基于 ISO/IEC 27035） 43

8.2 附录 B：协调漏洞披露的管辖区资源 45

**前言**

本文件由国际医疗器械监管论坛 (IMDRF) 制作，IMDRF 是一组来自世界各地的医疗器械监管者的自愿团体。 本文件在开发过程中接受了广泛的咨询。

本文件不受任何限制，可以复制、分发或使用；但是，将本文件（或其任何部分）包含在其他文件中，或将其翻译成其他语言，并不代表国际医疗器械监管论坛的任何形式认可。

# 简介

随着无线、互联网和网络连接设备的日益使用，确保医疗设备功能和安全所需的有效网络安全变得越来越重要。网络安全事件导致医疗设备和医院网络无法使用，从而中断了医疗机构内的患者护理。 这样的事件可能导致因诊断和/或治疗干预的延迟和/或错误等原因，对患者造成损害。

在医疗保健领域，所有利益相关者都有共同的责任，即医疗设备网络安全。 本指南旨在帮助所有利益相关者更好地了解他们在支持主动网络安全方面的作用，从而保护和安全地保护医疗设备，以应对未来的攻击、问题或事件。

为了确保患者安全和医疗设备性能，需要全球医疗保健网络安全原则和实践的融合。 然而，目前各国不同的法规缺乏实现医疗设备网络安全所需的全球一致性。

本 IMDRF 指导文件旨在提供一般原则和最佳实践，以促进医疗器械网络安全领域的国际监管协调。文件结构如下：文件范围在第 2 节中定义，然后是第 3 节中定义的术语。第 4 节概述了医疗器械网络安全的通用原则，而第 5 节和第 6 节则为利益相关者提供了关于医疗器械网络安全在上市前和上市后管理中的最佳实践的若干建议。虽然上市前部分主要针对医疗器械制造商，但上市后部分包括所有利益相关者的建议。

这是第一个专门关注医疗器械网络安全的 IMDRF 指导文件。然而，还有其他相关的 IMDRF 文件，在一般安全考虑方面应予以注意。IMDRF/GRRP WG/N47 FINAL:2018 提供了一致的基本原则，这些原则应在医疗器械和体外诊断医疗器械的设计和制造中得到满足[1]。这些基本原则应在医疗器械的整个生命周期中与本指导文件一起考虑。IMDRF/SaMD WG/N12 FINAL:2014 描述了与安全考虑相关的信息安全的重要性，具体在第 9.3 节中阐述，并说明了影响软件作为医疗器械（SaMD）的信息安全的一些具体因素。

# 范围

这份文档旨在为所有相关利益相关者提供具体的建议，关于医疗器械网络安全（包括体外诊断（IVD）医疗器械）的通用原则和最佳实践。它为医疗器械制造商、医疗服务提供者、监管机构和用户提供了建议，以：最大限度地减少因使用该设备以其预期用途而产生的网络安全风险；并确保设备的安全性、性能和持续性。为了本文的目的，医疗服务提供者包括医疗服务提供机构。

本文考虑了医疗器械的网络安全，这些器械要么包含软件，包括固件和可编程逻辑控制器（例如：心脏起搏器、输液泵），要么仅为软件（例如：软件为医疗器械（SaMD））。需要注意的是，由于大多数监管机构对医疗器械的安全性、性能具有管辖权，因此本文的医疗器械网络安全指南的范围仅限于考虑患者可能遭受的危害。例如，影响性能、损害临床运营或导致诊断或治疗错误的网络安全风险，均属于本文的范围。虽然与数据隐私泄露相关的其他危害也很重要，但它们不在本文的范围内。此外，本文承认网络安全对制造商的企业的重要性，但本文的范围不包括制造商的企业网络安全。要获取与制造商企业网络安全相关的更多最佳实践，NIST网络安全框架是一个重要的资源。

本文旨在：

* 采用基于风险的方法来设计和开发具有适当网络安全保护的医疗器械；

* 确保医疗器械和相关的医疗基础设施的安全、性能和安全性；

* 认识到网络安全是所有利益相关者共同的责任，包括但不限于医疗器械制造商、医疗服务提供者、用户、监管机构和漏洞发现者；

* 向这些利益相关者提供建议，以帮助最大限度地降低产品生命周期内患者受到伤害的风险；

* 保持术语的一致性，并描述实现医疗器械网络安全的当前最佳实践；

* 推广关于网络安全事件、威胁和漏洞的广泛信息共享政策，以提高透明度并加强应对。

需要注意的是，不同类型的医疗器械和监管辖区之间的差异，可能会导致需要考虑的特定情况。

# 定义

对于本文档，以下术语和定义适用：IMDRF/GRRP WG/N47 FINAL:2018。

1. _资产:_ 对个人、组织或政府有价值的物理或数字实体 (ISO/IEC JTC 1/SC 41 N0317, 2017-11-12)

2. _攻击:_ 尝试破坏、暴露、修改、禁用、窃取或未经授权访问或使用资产 (ISO/IEC 27000:2018)

3. _身份验证:_ 提供有关实体声称的特征是否正确保证 (ISO/IEC 27000:2018)

4. _真实性：_ 实体与其声称的性质相符（ISO/IEC 27000:2018）

5. _授权：_ 授予权限，包括授予访问数据和功能的权限（ISO 27789:2013）

注意：根据 ISO 7498-2 规定，这包括基于访问权限的访问权限授予。

1. _可用性：_ 实体在授权实体按需访问和使用的属性（ISO/IEC 27000:2018）

2. _补偿性风险控制措施（同义词：补偿性控制）：_ 一种在替代或缺少作为设备设计的一部分实施的风险控制措施的特定类型（AAMI TIR97:2019）

注意：补偿性风险控制措施可以是永久性的或临时性的（例如，直到制造商能够提供包含额外风险控制措施的更新）。

1. _保密性：_ 信息不会被未授权的个人、实体或流程访问或披露（ISO/IEC 27000:2018）

2. _协调性漏洞披露（CVD）：_ 研究人员和其他相关方与制造商合作，以寻找减少与漏洞披露相关的风险的解决方案的过程（AAMI TIR97:2019）

注意：此过程包括报告、协调和发布有关漏洞及其解决方案的信息。

1. _网络安全：_ 信息和系统免受未经授权的活动（如访问、使用、披露、中断、修改或破坏）的保护，使得与机密性、完整性和可用性相关的风险在整个生命周期内保持在可接受的水平。（ISO 81001-1）

2. _产品生命周期结束 (EOL):_ 产品生命周期的起始阶段，即制造商不再销售该产品，且该产品已通过正式的 EOL 流程，包括通知用户，该产品已达到制造商定义的生命周期结束。

3. _停止支持 (EOS):_ 产品生命周期的起始阶段，即制造商终止所有服务支持活动，且在此之后不再提供服务支持。

4. _基本性能:_ 临床功能，除了与基本安全相关的功能之外，如果因性能损失或退化超过制造商规定的限制，会导致不可接受的风险（IEC 60601-1:2005+AMD1:2012）

5. _利用:_ 通过利用漏洞，以定义的手段来破坏信息系统的安全（ISO/IEC 27039:2015）

6. _完整性:_ 数据在创建、传输或存储后，未被未经授权的方式修改的属性（ISO/IEC 29167-19:2016）

7. _遗留医疗器械 (同义词: 遗留设备):_ 无法合理地保护免受当前网络安全威胁的医疗器械

8. _不可否认性:_ 证明声称发生的事件或行为以及其发起方的能力（ISO/IEC 27000:2018）

9. _患者伤害:_ 患者的身体损伤或健康损害（改编自 ISO/IEC Guide 51:2014）

10. _隐私:_ 在个人生活或事务中，由于对个人数据的过度或非法收集和使用而造成的侵入，个人免受这种侵入（ISO/TS 27799:2009）
  11. _威胁:_ 安全可能被违反的可能性，当存在可能破坏安全并造成损害的情况、能力、行动或事件时（ISO/IEC 指南 120）
  12. _威胁建模:_ 一种探索性的过程，旨在揭示任何可能对系统造成损害（如破坏、数据泄露、数据修改或拒绝服务）的情况或事件（改编自 ISO/IEC/IEEE 24765-2017）
  13. _更新:_ 对医疗器械软件的纠正、预防、适应性或完善修改

注意 1: 来源于 ISO/IEC 14764:2006 中描述的软件维护活动。

注意 2: 更新可能包括补丁和配置更改

注意 3: 适应性和完善性修改是软件的增强。这些修改不是医疗器械的设计规范。

1. _验证:_ 通过提供客观证据，确认特定用途或应用的需要已得到满足（ISO 9000:2015）

注意 1: “已验证”一词用于指定相应的状态。

注意 2: 验证的适用条件可以是真实的或模拟的。

1. _验证:_ 通过提供客观证据，确认已指定的要求已得到满足（ISO/IEC 指南 63）

注意 1: 验证所需的客观证据可以是检查的结果或其它形式的确定，例如进行替代计算或审查文件。

说明 2：用于验证的活动有时被称为“合格性过程”。

说明 3：使用“已验证”一词来指定相应的状态。

1. _漏洞：_资产或控制措施的弱点，可被一个或多个威胁利用（ISO/IEC 27000:2018）

# 总体原则

本部分提供医疗器械网络安全的一般指导原则，适用于所有利益相关者在开发、监管、使用和监控医疗器械时应考虑的内容。 这些主题，贯穿于本指南文件中，对于全球医疗器械网络安全水平的提高至关重要，并且在遵循这些原则时，预计将对患者安全产生积极影响。

## 全球协调

医疗器械网络安全是一个全球性问题。 安全事件有可能威胁全球医疗保健系统中的患者安全，例如，通过导致诊断或治疗错误、通过损害设备的正常运行、通过影响临床操作或通过阻止患者获得关键护理。 为了确保在鼓励创新并确保患者及时获得安全有效的医疗器械的同时，维护患者安全，需要全球医疗保健网络安全方面的努力实现协调。 鼓励所有利益相关者在整个医疗器械的生命周期范围内，协调其网络安全方法。 这包括在产品设计、设备生命周期的各个阶段进行风险管理活动、设备标签、监管提交要求、信息共享以及上市后活动等方面进行协调。

## 整个产品生命周期

[Glossary - 使用这些精确的翻译时:]
  差距分析 -> Gap Analysis
  test_zh -> test_en

风险与网络安全威胁和漏洞应贯穿医疗器械的整个生命周期，从最初的概念到最终支持（EOS）。为了有效地管理网络安全风险的动态性，应在整个产品生命周期（TPLC）中应用风险管理，其中在设计、制造、测试和上市后监测等各个阶段对网络安全风险进行评估和缓解。

认识到需要平衡安全和安全。在整合网络安全控制和缓解措施时，医疗器械制造商必须确保医疗器械的安全性和基本性能得到维护。

## 共同责任

医疗器械的网络安全是制造商、医疗机构、用户、监管机构和漏洞发现者等利益相关者共同承担的责任。所有利益相关者必须了解自己的责任，并与其他的利益相关者密切合作，持续监测、评估、缓解、沟通和应对整个医疗器械生命周期的潜在网络安全风险和威胁。

## 信息共享

网络安全信息共享是 TPLC 应对安全可靠医疗器械的基本原则。所有利益相关者都应积极采用预上市和上市后的网络安全信息共享方法。及时获取信息，使所有相关方能够更好地识别威胁、评估相关风险并采取相应措施。因此，所有相关利益相关者应积极参与信息共享分析组织（ISAOs），以促进网络安全事件、威胁和漏洞的协作和沟通，这些漏洞可能影响医疗器械和相关的医疗基础设施的安全性、性能、完整性和安全性。这些努力有助于提高透明度。协调的漏洞披露也是一种鼓励采用的最佳实践的信息共享机制。此外，生态系统将受益于进一步发展信息共享政策，这些政策不仅适用于制造商，还应包括医疗服务提供者以及医疗器械的使用者。监管机构也应与其他监管机构共享信息，以在全球范围内保护和维护患者安全。

# 医疗器械的网络安全——上市前考虑

虽然医疗器械网络安全应在整个产品生命周期中加以考虑，但在产品上市之前，制造商应在设计和开发阶段解决一些重要的方面。这些预上市方面包括：将安全功能融入产品；应用已接受的风险管理策略；进行安全测试；为用户提供有用的信息，以便安全地操作设备；以及制定用于上市后的活动计划。对于上述预上市方面，制造商应考虑预期使用环境以及合理可预见的误用场景。以下部分旨在介绍这些概念，并为制造商在产品生命周期的预上市阶段提供建议。请注意，医疗器械软件的生命周期活动已在 IEC 62304:2006/AMD 1:2015 中指定。

## 安全要求和架构设计

在设计阶段主动应对网络安全威胁（例如，通过威胁建模等措施）比仅进行上市后的反应性活动更能有效降低对患者的潜在危害。这些设计输入可以来自产品生命周期的各个阶段，例如需求捕获、设计验证测试或预上市和上市后的风险管理活动。

安全要求也应在产品生命周期的设计过程的“需求捕获”阶段中确定。 一些安全要求和安全风险控制措施可以在AAMI TIR57:2016、IEC TR 80001-2-2、IEC TR 80001-2-8、ISO 27000系列以及NIST（如NIST的Secure Software Development Framework (SSDF)、OWASP（如Security by Design原则）和美国医疗保健与公共卫生部门协调委员会（HPH SCC）联合网络安全工作组（JCWG）（如联合安全计划）发布的资源中找到。

虽然下表 1 并非详尽的清单，但它概述了医疗器械制造商在设计其产品时应考虑的设计原则。

**设计原则** | **描述**
---|---
安全通信 | 制造商应考虑设备如何与其他设备或网络进行交互。 接口可能包括硬线连接和/或无线通信。 接口方法示例包括 Wi-Fi、以太网、蓝牙、USB 等。
制造商应考虑验证所有输入（不仅是外部输入）的设计特征，并考虑到与仅支持不安全通信的设备和环境（例如，连接到家庭网络的设备或旧设备）的通信。
制造商应考虑如何安全地传输设备上的数据，以防止未经授权的访问、修改或重放。 例如，制造商应确定：设备/系统之间的通信将如何互相验证；是否需要加密；如何防止先前传输的命令或数据的未经授权重放；以及在预定义的时间后终止通信会话是否合适。
数据保护 | 制造商应考虑，如果存储在设备上或从设备传输的数据与安全相关，是否需要某种级别的保护，例如加密。 例如，密码应存储为加密安全的哈希。
制造商应考虑，是否需要控制措施来保护通信协议中的消息控制/序列化字段，或防止加密密钥材料被泄露。
设备完整性 | 制造商应评估系统级别的架构，以确定是否需要设计特征来确保数据不可否认（例如，支持审计日志功能）。
制造商应考虑设备完整性的风险，例如未经授权地修改设备软件。
制造商应考虑控制措施，例如反恶意软件，以防止病毒、间谍软件、勒索软件和其他形式的恶意代码在设备上执行。
用户身份验证 | 制造商应考虑用户访问控制，以验证谁可以使用设备或授予不同用户角色权限，或允许用户在紧急情况下访问。 此外，相同的凭据不应在设备和客户之间共享。 身份验证或访问授权的示例包括密码、硬件密钥或生物识别，或无法由其他设备产生的意图信号。
软件维护 | 制造商应建立并沟通定期更新的实施和部署流程。
制造商应考虑如何更新操作系统软件、第三方软件或开源软件。 制造商还应计划如何应对超出其控制范围的软件更新或过时的操作系统环境（例如，在不安全的操作系统版本上运行的医疗设备软件）。
制造商应考虑如何更新设备，以使其免受新发现的网络安全漏洞的影响。 例如，可以考虑更新是否需要用户干预，或者由设备启动，以及如何验证更新，以

##### 表 1：医疗器械设计中应考虑的设计原则

安全开发原则是安全设备设计的内在组成部分。 许多当前的软件开发生命周期模型或标准默认不包含这些原则。 对于开发医疗器械软件的设备制造商来说，将这些安全原则融入到软件开发中至关重要。 这需要制造商采取全面的设备网络安全方法，并在产品生命周期的各个阶段评估风险和缓解措施。

## TPLC 的风险管理原则

健全的风险管理原则，应贯穿医疗器械的整个生命周期，并解决安全和安全领域。 任何影响设备安全和基本性能、损害临床操作或导致诊断或治疗错误的网络安全风险，也应在医疗器械的风险管理过程中加以考虑。 制造商应使用 ISO 14971:2019 中描述的风险管理，以及（例如，AAMI TIR57:2016；AAMI TIR97:2019 中描述的网络安全风险管理，作为其风险管理过程的一部分，采取以下步骤：

* 识别任何网络安全漏洞；

* 估算和评估相关的风险；

* 将这些风险控制在可接受的水平；

* 评估和监控风险控制的有效性；以及

* 通过协调的方式向关键利益相关者沟通风险。

图 1 显示了 AAMI TIR57:2016 中的安全风险管理流程。这可以是一个专门的风险管理流程，作为整体风险管理的一部分执行，也可以是与 ISO 14971:2019 风险管理流程的有机组成部分，并对漏洞、威胁和其他与安全相关的术语进行适当的映射。请参阅 ISO/TR 24971:2020 第 F 附件，了解可能的映射。

##### 图 1：安全风险管理流程的示意图（基于 AAMI TIR57:2016 的授权。）

在医疗器械监管中，与网络安全相关的风险分析应侧重于评估患者可能遭受的危害，并考虑：1) 网络安全漏洞的可利用性，以及 2) 如果该漏洞被利用，患者可能遭受的危害程度。这些分析还应纳入对弥补控制和风险缓解措施的考虑。

风险评估与产品设计、威胁建模、患者安全、缓解措施和测试相关联。因此，至关重要的是建立一个安全的设计架构，以便能够充分管理风险。在本次评估中，可以采用多种工具和方法，包括但不限于安全风险评估、威胁建模和漏洞评分。

* **安全风险评估**：制造商应在产品整个生命周期中考虑网络安全风险、威胁和控制措施。如果适用，应将网络安全要求与特定设备的网络安全威胁和漏洞进行交叉引用，如果这些要求是针对已识别危害的缓解措施。

* **威胁建模**：威胁建模是一种识别、列举和缓解潜在威胁的流程，这些威胁与设备和系统相关。具体而言，威胁建模包括考虑风险，包括但不限于与供应链（例如，系统组件）、设计、生产、部署（例如，进入医院环境）和维护相关的风险。此外，创建足够详细的系统图表有助于理解网络安全设计元素如何融入设备，从而进一步有助于威胁建模。根据 OWASP 的指导，在生成威胁模型时，设备制造商应考虑回答以下四个基本问题，这些问题与网络安全相关：

1. 我们在做什么？

2. 哪些可能出错？（例如，如何攻击？）

3. 我们将如何处理这些问题？

4. 我们做得足够好吗？

这些问题可以在应用架构、运营数据流程或更广泛的系统级别威胁建模的背景下提出。在确定威胁建模中可能出现的问题时，制造商应考虑软件和硬件的意外或恶意配置（例如，将未设计用于连接网络的设备连接到互联网）。

* **漏洞评分**：漏洞评分提供了一种对网络安全漏洞的可利用性和严重程度进行描述和评估的方法。在设计和开发过程中识别的已知常见漏洞和暴露（CVE）应使用一致的漏洞评分方法（例如，通用漏洞评分系统（CVSS）或任何未来广泛采用的漏洞评分系统）进行分析和评估。网络安全风险、漏洞评分和控制措施可用于为新的产品和其他非网络安全相关的风险评估工具（例如，失效模式和影响分析（FMEA））提供威胁建模和安全风险评估的信息。

在将安全风险管理过程整合到现有的ISO 14971:2019风险管理过程中时，应考虑与安全相关的活动，例如威胁建模和漏洞评分。

## 安全测试

[术语表 - 在这些术语出现时，请使用这些确切的翻译:]
  差距分析 -> Gap Analysis
  test_zh -> test_en

在设计和开发过程中，在验证和确认阶段，制造商应采用各种类型的安全测试，以确保代码中不存在重大已知的漏洞，并且安全控制措施已得到有效实施。测试应考虑到设备的用途和部署环境。建议采用软件验证技术，以确保软件符合规范，并最大限度地减少异常。此外，还应确保医疗设备经过测试，以识别可能被利用的已知漏洞。为此，医疗设备应进行安全评估或验收检查（例如，软件测试、攻击模拟等）。安全测试是安全开发框架的一部分，关于测试考虑的更多细节可以在第 5.1 节提供的标准和资源中找到。以下是针对医疗设备制造商的一些高层考虑：

* 在开发过程中，对软件组件/模块进行目标搜索，以查找已知的漏洞或软件弱点。例如，定期安全测试可能包括：静态代码分析、动态分析、鲁棒性测试、漏洞扫描或软件组合分析。

* 进行技术安全分析（例如，渗透测试）。这包括通过模糊测试等方法识别未知的漏洞；或检查替代入口点，例如通过读取隐藏文件、配置、数据流或硬件寄存器。

* 完成漏洞评估。这包括对漏洞对其他内部产品的影响分析（即变体分析）、识别对策，以及修复或缓解漏洞。

## TPLC 网络安全管理计划

鉴于网络安全威胁将持续演变，制造商应主动监测、识别和解决漏洞和利用，作为其在产品生命周期内的网络安全管理计划的一部分。 该计划应在产品开发的预市场阶段制定，并理想情况下在制造商的整个组织中保持。 该计划应涵盖：

* **TPLC 预警**：主动监测和识别新发现的网络安全漏洞，评估其威胁，并采取适当的应对措施。

* **漏洞披露**：一种正式的过程，用于从漏洞发现者获取信息，制定缓解和修复策略，并披露漏洞及其缓解或修复方法，向利益相关者。

* **更新和修复**：一份计划，说明如何更新软件，或如何应用其他修复措施，以保持设备的持续安全和性能，无论是定期还是针对已识别的漏洞。

* **恢复**：一份恢复计划，适用于制造商、用户或两者，以在发生网络安全事件后将设备恢复到正常运行状态。

* **信息共享**：参与信息共享分析组织（ISAOs）或信息共享和分析中心（ISACs），这些组织促进有关安全威胁和漏洞的最新信息的沟通和共享。

## 标签和客户安全文档

### 标签

标签向最终用户传达相关的安全信息，同时考虑到相对的网络安全风险。 标签应包含以下元素：

* 与推荐的、适用于预期使用环境的网络安全控制相关的设备说明和产品规格（例如，反恶意软件软件、网络连接配置、防火墙的使用）。

* 备份和恢复功能和程序的描述，用于恢复配置。

* 预期接收和/或发送数据的网络端口和其他接口的列表，以及端口功能和端口是入站还是出站的描述（注意：未使用的端口应禁用）。

* 足够详细的系统图表，供最终用户使用。

### 客户安全文档

除了使用说明，制造商编写的关于设备安装、配置以及其运行环境的技术文档，对于用户安全可靠的使用尤为重要。它应包括以下内容：

* 针对用户，提供明确的关于支持基础设施要求的指导，以便设备能够按照预期运行。

* 描述如何通过安全的配置来保护设备。安全的配置可能包括终端保护，如反恶意软件、防火墙/防火墙规则、白名单、安全事件参数、日志参数、物理安全检测等。

* 在适当的情况下，提供技术指导，以实现安全的网络（连接）部署和维护，以及用户在检测到网络安全漏洞或事件时的应对方法。

* 描述设备或相关系统在检测到异常条件（即安全事件）时，如何通知用户（如果可行）。安全事件类型可能包括配置更改、网络异常、登录尝试、异常流量（例如，向未知实体发送请求）。

* 描述经过认证的特权用户如何保留和恢复设备配置的方法。

* 在适当的情况下，描述安全配置或使用环境的变更所带来的安全风险和后果。描述经过授权用户从制造商下载和安装更新的系统性程序。

* 如果已知，提供关于设备网络安全支持结束的信息（参见第 6.6 节，遗留医疗设备）。

* 软件材料清单 (SBOM) 用于向操作人员提供有关医疗器械中使用的商业、开源或标准软件组件的网络安全信息，并提供支持。SBOM 通过列出每个软件组件的名称、来源、版本和构建，创建必要的透明度。SBOM 使设备操作人员（包括患者和医疗服务提供者）能够有效地管理其资产和相关风险，了解已识别的漏洞对设备（以及连接的系统）的潜在影响，并采取措施以保持设备的安全性及其基本性能。设备操作人员可以使用 SBOM 来协助与设备制造商合作，识别可能存在漏洞的软件、更新要求以及进行适当的安全风险管理。SBOM 还可以帮助采购决策，为潜在买方提供有关应用程序中使用的组件的可见性，并确定潜在的安全风险。制造商应采用 SBOM 的格式、语法和标记的最佳实践。由于 SBOM 揭示了关于医疗设备的敏感信息，因此鼓励通过可信的沟通渠道进行分发。制造商将确定可信的沟通 SBOM 的方式。

## 提交文件

除了前几部分中概述的活动之外，医疗器械制造商应明确记录和总结其与网络安全相关的活动。根据该设备的风险等级，监管机构可能会要求制造商提供此类文档，以评估医疗器械，以便在进入市场之前，或在产品生命周期的后期阶段进行评估。如果需要用于上市前授权，制造商应提交清晰的文档，描述该设备的设计特征、风险管理活动、测试、标签以及在产品生命周期的整个过程中，监测和应对新兴威胁的计划，特别是与网络安全相关的，例如：访问控制、加密、安全更新、日志记录、物理安全等措施的选择理由和假设。以下段落提供了有关上述各项的更多详细信息。

### 设计文档

描述该设备，包括任何接口或通信路径或组件（硬件和软件），以及所有纳入设计特征，以减轻与患者安全相关的网络安全风险，例如前述第 5.1 部分中概述的措施（特别是关于访问控制、加密、安全更新、日志记录、物理安全等的选择理由和假设）。

### 风险管理文档

[术语表 - 在这些术语出现时，请使用这些确切的翻译：]
  差距分析 -> Gap Analysis
  test_zh -> test_en

包含清晰描述网络安全威胁和漏洞的文档，对相关的风险进行估算，描述已采取的控制措施以减轻这些风险，以及证明这些控制措施已充分测试的证据。制造商应考虑在最大化设备网络安全的同时，不会过度影响其他安全控制的风险控制。具体而言，向监管机构提交的网络安全风险管理相关文档应清晰，并使用网络安全风险管理标准（例如：AAMI TIR57:2016、AAMI TIR97:2019）作为指导。结果应与ISO 14971:2019的总体要求保持一致，以确保输出可作为整体风险管理的一般输入。网络安全相关的风险管理文档可能包括：

* 完整的风险管理文档，例如风险管理报告或安全风险管理报告，应包含任何威胁建模和已识别的网络安全威胁。

* 讨论安全风险缓解措施对其他风险管理的影响。

### 安全测试文档

总结对验证设备和任何安全控制有效性的所有测试的测试报告。例如，可以从第5.3节中找到关于特定测试的详细信息，例如，将软件组件或子系统与已知的漏洞数据库进行交叉引用，但所有测试文档都应包含：

* 测试方法、结果和结论的描述；

* 安全风险、安全控制和测试之间的可追溯矩阵，以验证这些控制；以及

* 任何使用的标准和内部SOP/文档的引用。

### TPLC 网络安全管理规划文档

[术语表 - 在这些术语出现时，请使用这些确切的翻译:]
  差距分析 -> Gap Analysis
  test_zh -> test_en

一份关于医疗器械的维护计划的总结，描述制造商打算通过市场后流程来确保该设备在其整个生命周期内持续安全和性能。 如第 5.4 节所述，这些计划流程可能包括：TPLC 监测、计划或纠正更新、协调的漏洞披露政策以及信息共享。

### 标签和客户安全文档

所有用户文档，其中包含与第 5.5 节中概述的相关信息，以便用户能够在设备的使用环境中有效地管理风险。

# 医疗器械网络安全后的考量

随着漏洞随时间变化，在市场前设计的和实施的控制可能不足以维持可接受的风险水平；因此，需要采取市场后方法，多个利益相关者将发挥作用。 这种市场后方法涵盖各种要素，包括：设备在预期环境中的运行、信息共享、协调的漏洞披露、漏洞修复、事件响应以及旧设备。 以下部分旨在介绍这些概念，并为产品生命周期的市场后阶段的所有关键利益相关者提供建议。

## 在预期使用环境中运行设备

### 医疗保健提供者和患者

#### 医疗机构应采用的最佳网络安全实践

医疗器械的网络安全是共享责任，需要所有利益相关者的参与，包括医疗机构。 医疗机构应考虑采用风险管理流程，以应对与医疗器械相关的安全、性能和网络安全方面，这些医疗器械连接到其IT基础设施。 这种流程应在以下环节应用：

* IT基础设施的初始开发；

* 将新的医疗器械集成到现有IT网络；以及

* 操作系统、IT网络或医疗器械（软件和固件）的更新或修改。

为了实施上述风险管理流程，医疗机构可以参考相关的标准，例如：IEC 80001-1、ISO 31000以及特别是ISO 27799，以便采用。《医疗行业网络安全实践：管理威胁和保护患者》文档也可以作为另一个资源。

除了采用风险管理系统外，医疗机构还应遵循以下通用网络安全最佳实践（这并非详尽的清单），以维护医疗机构的整体安全态势：

* 良好的物理安全，以防止未经授权的物理访问医疗器械或网络访问点；

* 访问控制措施（例如基于角色的访问控制），以确保只有授权人员才能访问网络元素、存储的信息、服务和应用程序；

* 采用配置管理，以识别所有当前资产并跟踪未来的配置更改；

* 采用制造商推荐的配置和保护措施；

* 网络访问控制，以限制医疗设备之间的通信；

* 更新管理实践，以确保及时进行安全更新；

* 恶意软件防护，以防止攻击；以及

* 会话超时，以防止无人照看的设备被未经授权访问。

实施这些最佳实践应结合医疗设备的临床使用。例如，遵守这些最佳实践在医疗紧急情况下可能不可行。上述许多实践都描述在 NIST 网络安全框架中。

#### 为所有用户提供培训/教育

最后，医疗机构应采取全面的方法，以防止在他们的机构中发生网络安全事件。因此，他们应鼓励提供基本网络安全培训，以提高所有用户（例如医生、护士、生物医学工程师、技术人员等）的安全意识，并介绍网络安全行为。这包括培训如何以安全的方式使用医疗设备（例如，仅将设备连接到安全的网络），以及如何发现和报告任何异常设备行为（例如，随机关闭/重启、安全软件已禁用）。此类培训也应扩展到患者，如果连接的医疗设备（例如，用于家庭使用的设备，如连续血糖监测仪或胰岛素泵）是供患者自行操作的，则应进行。

### 医疗设备制造商

除了产品标签和客户安全文档中包含的信息外，制造商应尽可能与医疗机构、分销商和其产品的消费者合作，以确保其设备的最佳部署和配置。

## 信息共享

信息共享是管理全球经济各个领域的网络安全威胁和漏洞的关键工具。在医疗保健之外的行业，已经制定并实施了情报和威胁共享的标准和最佳实践；因此，鼓励医疗器械领域的利益相关者采用其他行业的经过验证的工具，以加强全球医疗器械生态系统的安全性。

由于利益相关者在资源获取、方法和成熟度水平方面存在差异，因此信息共享也存在多种有效方法。此外，网络安全最佳实践仍在不断发展，并受到多种因素的影响，包括设备类型、连接基础设施、组织规模和成熟度，以及威胁级别。因此，本文件并未偏向任何特定方法。相反，它阐述了关于信息共享的原则。示例并非旨在指定要求，而是作为说明。

### 关键原则

* 关于医疗器械安全的信息应与任何需要这些信息的人共享，以确保该医疗器械能够安全使用（例如：用户、患者、其他制造商、分销商、医疗服务提供者、安全研究人员和公众）。

* 分享的信息应保持平衡，以便对不同利益相关者具有意义、可理解和可操作性（例如：关于更安全的芯片组的信息可能对所有制造商都重要，但对于设备的使用者可能没有任何益处）。

* 应以适当的方式，自由且诚实地共享信息，旨在提高患者安全，无论是否有商业利益。

* 尽可能在全球范围内，在适当的情况下，实现信息同步共享，以便不同地区的利益相关者能够相应地做出反应。

### 关键利益相关者

医疗器械行业受到监管，并且具有全球性。因此，针对不同地区的利益相关者，信息共享的本地或管辖范围内的建议可能不足以满足向多个市场供应医疗器械的制造商的需求。与医疗器械安全相关的信息共享策略需要具有全球性。因此，利益相关者可能需要参与多个网络，认识到某些网络可能具有国际性。

#### 监管机构

* 是与医疗器械安全相关信息的重要接收方，并且通常参与信息传播。

* 应致力于建立鼓励及时披露与医疗器械网络安全相关信息的过程。 这包括监管机构之间共享信息，以促进全球协调的响应。

#### 医疗器械制造商

* 应识别、评估并分享来自任何来源的漏洞信息。 制造商应分享任何有助于监管机构管理预期并满足监管要求的信息。

* 应致力于与所有分发受影响产品的监管机构同步通知，以确保全球一致的信息，并在适当情况下，实现全球一致的响应。

* 应使用适合目标用户的语言，以清晰简洁的方式传达关于医疗器械网络安全漏洞和威胁的行动性信息。 这可能需要包含关于部署更新的临床益处和风险，或在更新可用之前所需的替代控制的信息。

#### 医疗服务提供者

* 通常负责采取行动或促进行动。 因此，他们应能够访问任何需要实施建议所需的信息，并确保患者的安全。

* 也是重要信息生成者，因为他们与医疗器械在实践中，可以提供关于哪些设备受到影响以及在实际环境中实施修复或缓解措施的便利性和有效性的反馈。

#### 用户（例如：临床医生、患者、照护者和消费者）

* 通常是决定是否采取更新或其他纠正措施的最终决策者。因此，他们需要清晰且有意义的信息，以便做出明智的决定。

#### 其他利益相关者，包括政府和信息共享实体

* 执法部门、国家安全机构和其他政府机构可能需要共享医疗设备网络安全威胁和漏洞信息，以保护医疗保健和其他关键基础设施。

* 收集或共享信息、提供安全建议或专家的实体，也可以是重要的安全信息和支持资源的来源。这些可能包括政府或私营组织。例如，信息共享网络（如ISAO、ISAC）、传播机构（如计算机应急响应团队（CERT））和其他实体。这些利益相关者可能在不同司法管辖区和市场中有所不同。

### 信息类型

网络安全漏洞可能对多个产品组件（包括软件和硬件、以及第一方或第三方组件）构成威胁。为了保护患者，共享的信息可能包括但不限于：

* 关于受漏洞影响的产品以及它们如何受到影响的信息；

* 关于其他产品中使用的组件的漏洞信息；

* 关于可能影响医疗设备安全的信息技术设备；

* 关于攻击、潜在攻击以及漏洞代码的可利用性信息；

* 事故确认（例如：“您也看到了吗？”）；

* 提供补丁和其他安全缓解措施，例如补偿控制；以及

* 关于医疗设备使用和集成的附加说明，作为临时措施

信息共享还应包括可能减轻威胁的实践和方法，例如，如何配置IT设备以缓解影响医疗设备的漏洞，或如何应对已知的漏洞。

### 可信通信

应建立信息共享网络，并达成书面协议（如果需要），明确表示信息共享是为了提高安全性和患者安全，并且共享的信息不得用于获取商业利益。 鼓励信息共享的一种方式是提供匿名共享。

## 有序漏洞披露

透明度是网络安全的重要基础，因为只有了解才能有效防御。 有序漏洞披露（CVD）是增强透明度的一个机制。 CVD 建立正式流程，用于获取网络安全漏洞信息、评估漏洞、制定缓解措施和补偿控制，并将这些信息告知各种利益相关者，包括客户、同行业公司、政府监管机构、网络安全信息共享组织以及公众。

采用CVD政策和程序是一种主动的方法，使受到影响的技术的使用者能够就采取哪些措施来更好地保护其医疗设备、健康IT基础设施和患者做出更明智的决定。

参与CVD（产品安全验证）是一种负责任的做法，旨在提高对安全问题的认识，并且应被视为制造商在持续质量改进和风险管理方面的成熟表现，正如在其他行业领域所见。

尽管积极参与CVD是一种主动和负责任的企业行为，但一些医疗器械制造商因采用这一最佳实践而遭受负面宣传。作为最佳实践，CVD应被视为常态，而不是例外，并鼓励医疗器械相关方向制造商询问其CVD政策，以进一步促进采用。

### 医疗设备制造商

随着医疗器械生态系统的不断成熟，行为透明化的益处将得到更充分的认识。这种披露对于在多个上市产品中，主动保护公众免受潜在危害至关重要。制造商也直接受益于透明行为，这有助于改进新产品的安全设计。医疗机构和患者应了解，来自制造商、以及由CERT（计算机应急响应技术团队）或政府监管机构等计算机响应团队的CVD，是有关漏洞的权威信息来源。在CVD方面，监管机构的沟通方式可能存在管辖范围差异。然而，制造商应在评估后，及时通过客户公告、通知或其他方式发布信息。制造商应了解关于及时沟通的具体管辖要求。

[术语表 - 在这些术语出现时，请使用这些确切的翻译:]
  差距分析 -> Gap Analysis
  test_zh -> test_en

任何使用软件的医疗设备都无法完全消除漏洞，因此，进行 CVD（漏洞评估和披露）应成为常规实践的一部分。 制造商的网络安全态势，与其漏洞的数量，而与其漏洞的频率和及时性。 因此，CVD 应该成为制造商主动的网络安全实践的一部分，因为它有助于改善患者的健康和安全。 在主动进行 CVD 的情况下，制造商应：

* 监控网络安全信息来源，以识别和检测网络安全漏洞和风险。

* 采用协调的漏洞披露政策和实践（ISO/IEC 29147:2014：信息技术 – 安全技术 – 漏洞披露）。 这包括在指定的时间范围内，向发现漏洞的人确认收到初始漏洞报告。

* 建立并沟通漏洞接收和处理流程（ISO/IEC 30111:2013：信息技术 – 安全技术 – 漏洞处理流程）。 这些流程应清晰、一致且可重复，无论漏洞的来源（例如，安全研究人员或医疗服务提供者等）如何。

* 根据既定的安全（例如，CVSS）和临床（例如，ISO 14971:2019）风险评估方法评估报告的漏洞。

* 如果可能，制定修复方案。 如果无法修复，则制定适当的漏洞缓解和/或补偿控制，并建立报告部署失败和回滚更改的机制。

* 在需要时与监管机构沟通，以便他们了解即将披露的漏洞。

* 向相关方告知漏洞的描述，包括范围、影响、基于制造商当前理解的风险评估，并描述漏洞的缓解措施和/或替代控制。相关方应根据情况的变化进行更新。

除了与客户的沟通外，制造商应鼓励在全球范围内协调披露漏洞。计算机应急响应团队（CERT）和其他类似组织通常与漏洞发现者和制造商在漏洞披露（CVD）过程中进行协作。特别是，CERT通常在通过全球和区域CERT公告进行公开披露，并将这些公告翻译成当地语言。有关CVD的更多信息，请参见CERT®关于协调漏洞披露指南。

### 监管机构

监管机构可以协助制造商和漏洞发现者之间的漏洞评估/评估、影响分析和缓解/修复过程的协调，从而最终促进更及时的向公众沟通，以降低被利用的风险。这种沟通包括根据需要进行全球范围内的沟通，因为CVD被认为是最佳实践。

### 漏洞发现者（包括安全研究人员和其他）

漏洞一旦发现，应直接向相关制造商或协调第三方（例如，适当的政府机构）报告。制造商随后与发现漏洞的人协调并沟通，直至完成评估和修复。最后，漏洞发现者和制造商应协调公开披露漏洞。借鉴美国国家电信与信息管理局（NTIA）/美国商务部《漏洞披露态度和行动：NTIA意识和采用小组的研究报告》（2016年12月），只要制造商对发现者负责，并且没有证据表明该漏洞已被用于未经授权的攻击，则协调披露意味着，在修复或其他缓解措施可用之前，漏洞发现者不会公开披露该漏洞。如果发现者在修复之前公开披露该漏洞，那么发现者和制造商至少应协调，描述一系列可能的缓解措施，从而使用户（包括医疗保健提供者和/或患者）能够以最有利的方式安全地使用其设备。

## 漏洞修复

与漏洞修复相关的行动对于降低患者伤害的风险至关重要。修复措施可能包括各种行动，包括通知患者。因此，多个利益相关者群体在这一过程中发挥着关键作用，并且这些作用将在下面进行更详细的描述。

### 医疗设备制造商

#### 风险管理

任何针对医疗器械网络安全漏洞的响应的第一部分是风险评估。根据ISO 14971:2019，风险管理是医疗器械领域的成熟且完善的做法。这种做法应用于评估漏洞的网络安全风险，然后由制造商和监管机构共同确定，通过建立与风险管理相关的网络安全风险管理流程来确定对患者安全的潜在影响。然后可以制定并达成一致的修复策略。为了提高这种方法的有效性，监管机构和制造商之间应共享信息，尤其是在关于感知到的风险和适当的行动理由方面。由于风险评估的结果会影响修复的优先级和时间安排，因此制造商和监管机构不太可能就适当的修复策略达成一致，如果他们对风险的看法差异很大。

制造商和监管机构还需要考虑其他利益相关者的风险认知，这些利益相关者可能不太熟悉风险管理、质量管理和法规。这可能导致对制造商应如何响应安全漏洞以及在什么时间范围内响应存在不同的期望。同样，一些利益相关者可能不理解可以部署的补偿控制，例如，这些控制可以充分保护易受攻击的设备，从而将患者伤害的风险降低到可接受的水平。如果提供不准确的信息，夸大对患者的风险，可能会在医疗技术领域引发信任危机。

所有利益相关者都需要认识到，与医疗器械相关的其他风险一样，网络安全漏洞的管理应与它们对患者和用户的潜在风险相称。

#### 第三方组件

第三方组件是医疗器械供应链的关键组成部分，无论它们是软件还是硬件。这些组件可能会带来自身的风险，制造商通过风险管理、质量管理和设计选择来管理这些风险。制造商应管理其软件和硬件组件的网络安全影响。同样，与第三方组件相关的售后问题也可能影响医疗器械的安全性，制造商需要管理这些风险。用户期望制造商了解底层组件（如操作系统或处理器）中的安全漏洞如何影响医疗器械。

制造商对第三方组件漏洞的响应应与对第一方漏洞的响应相同，即持续的风险管理和向客户和用户共享信息。虽然制造商可能无法控制第三方漏洞的解决时间（例如，更新的可用性），但仍应采取措施以降低对患者和用户的风险。

#### 沟通

如前文所述，向需要相关信息以进行风险管理的各方提供清晰简洁的沟通至关重要。此外，还应了解负责风险管理的技术专长水平。沟通应包括以下关键信息：漏洞解决的时间表（例如，修复将在何时可用）；解决机制（例如，补丁部署将如何进行）；漏洞评分（例如，CVSS评分）；可利用性指数（例如，低技能水平）和方法（例如，远程）以及临时风险缓解措施（例如，应采取哪些行动，包括在等待更永久性解决方案时使用补偿控制）。

#### 纠正措施

利益相关方的行动将取决于多种因素，包括设备类型、监管管辖区、对用户/患者安全的风险以及预期用途。因此，本文件并未详细说明所有设备都应采取的具体行动。然而，以下原则应指导所有漏洞修复行动：

* 遵守当地监管要求；

* 遵循安全和基本性能的原则；

* 与利益相关者共享信息，以降低对患者和用户的风险；

* 利益相关者合作，以实现已达成的修复目标；以及

* 及时修复，与风险相符。

当设备缺乏足够的基本或内在保护措施，且无法进行更新时，应采用补偿性控制措施以降低风险。例如，可以安装设备与医疗IT网络之间的防火墙，或将设备从医疗IT网络中移除。这些补偿性控制通常由医疗机构根据制造商提供的信息实施。

监管机构在各自管辖区的法律框架下运作，这意味着在对医疗设备进行修复之前，他们可能会实施特定的要求。制造商在制定漏洞修复行动时，需要考虑这一点。制造商应尽早通知监管机构，以免阻碍或延误制造商的修复活动。尽早通知监管机构，可以为启动任何监管程序或所需行动提供充足的时间，同时支持快速修复，并协助管理利益相关者及其期望（例如：用户、媒体、公众）。

关于安全漏洞的信息在全球经济中传播迅速，并且利用安全漏洞的攻击可以在几秒钟内传播到世界各地。因此，需要制定一个全球和协调的策略来修复漏洞。如果在一个司法管辖区修复并披露了漏洞，但在另一个司法管辖区未解决，则会给对手带来优势，并使患者以及整个医疗保健领域暴露于攻击之中。

向多个市场供应的制造商应协调信息发布和修复工作，以尽量减少时间差。制造商的协调应包括与所有相关监管机构进行主动沟通，特别是对于受影响的产品。

所有利益相关者都需要认识到，立即更新可能不可行或不可取，并且在确保患者安全方面，临时措施可能至关重要。这在那些需要利益相关者（包括制造商和监管机构之外的）实施措施时尤其重要。例如，某些行动只能由医院的IT部门执行。修复策略的成功执行通常取决于有效的信息共享和利益相关者管理（包括用户和媒体）。需要注意的是，虽然修复是理想的，但并非总是可以实现，在这种情况下，应采取适当的风险缓解和补偿控制措施。

### 医疗保健提供者和患者

#### 更新

[术语表 - 在这些术语出现时，请使用这些精确的翻译:]
差距分析 -> Gap Analysis
test_zh -> test_en

患者在专业的医疗机构和家庭医疗环境中接受医疗服务，并且每个使用环境都与更新相关的独特考虑因素。[2] 例如，在家庭医疗环境中，用户可能是患者、照护者、值得信赖的邻居或家庭成员。本部分提供关于更新的一般指导，后续部分描述了针对每个使用环境的具体考虑因素。

IEC 62304:2006 +AMD1:2015 的第 6.2.5 子条款，《医疗器械软件 — 软件生命周期流程》，要求制造商告知用户和监管机构，已发布医疗软件中存在的问题以及如何获取和安装更改。制造商识别并经当地监管机构批准的特定医疗器械用户，应按照相关的安装说明，实施制造商提供的更新。这些用户应遵循制造商的指导，访问服务公告和其他通常在网页上提供的信息。

当无法在合理的时间内应用更新时，制造商可能会建议采取补偿措施（例如，分割医疗 IT 网络）或更改医疗器械的可编程设置。为了降低某些类型的漏洞对患者造成的危害，当地监管机构可能会要求制造商禁用医疗器械、附件或支持生态系统的特定功能（例如，软件更新服务器）。无论哪种情况，用户应遵循制造商的指导，并在适当的情况下，评估与他们的使用环境相关的风险。[3]

[术语表 - 在这些术语出现时，请使用这些确切的翻译:]
  差距分析 -> Gap Analysis
  test_zh -> test_en

表 2 的内容改编自联合安全计划中记录的补丁方法。[4] 表的最右一列描述了由医疗设备制造商批准的更新的主要责任人。

**更新方法**| **摘要描述**| **用户责任**
---|---|---
远程更新| 通过制造商提供的安全授权的远程服务和支持平台进行更新。| 确保根据制造商提供的说明进行远程连接。
用户管理| 客户可以从指定来源（包括直接从提供产品或组件的第三方下载）获取和安装经过批准的更新。| 按照制造商提供的说明获取和安装更新。
服务访问| 本地服务机构管理网络安全更新（包括现场服务）。请注意，此方法适用于在出现明显且严重的故障更新的情况下，可能需要本地服务人员进行解决的情况。| 将医疗设备提供给服务机构，支持现场服务访问，或前往专业医疗机构。

##### 表 2：更新方法和实施的用户责任

请注意，对于服务访问，用户负责与合格的专业人员进行更新安装。

#### 就医疗机构环境的考虑

在医疗机构，患者由合格的医疗专业人员（例如，护士、医生）提供护理，这些专业人员可能因当地法规要求而获得或不获得执照。 预计患者将遵循医疗提供者的指示，包括与安全相关的指示，以确保其医疗设备的安全有效运行。

IEC 80001-1:2010 第 3.2 条：“对包含医疗设备的 IT 网络进行风险管理的应用 — 第 1 部分：角色、责任和活动”，描述了“负责组织”的风险管理责任，包括维护在医疗 IT 网络中部署的医疗设备。负责组织可能与患者的直接医疗服务提供者不同。更新是一种风险控制措施，第 4.4.4.3 条提供了具体指导：

_“医疗设备内部的风险控制措施应仅由医疗设备制造商或负责组织按照使用说明或在医疗设备制造商的书面授权下实施…… 负责组织在未经医疗设备制造商书面授权的情况下对医疗设备进行的任何更改均不建议。”_

这些建议旨在确保对医疗 IT 网络的有效和安全管理。不得允许非专业人士安装连接到医疗 IT 网络的医疗设备的更新。

如 IEC 80001-1 所强调的，责任协议是确保所有相关方了解在医疗 IT 网络中共同管理设备的一种选择。如果制造商被要求禁用医疗设备中的某些功能，那么医疗服务提供者应评估其临床工作流程，以确保患者安全得到维护。

#### 家庭医疗环境的考虑

家庭医疗环境可以容纳各种潜在用户，如 FDA 相关的指导“为家庭使用设备的设计考虑”中所述：

_"使用家用设备的个体与通常在医疗机构中操作医疗设备的医疗专业人员不同。家用设备的使用者可能具有广泛的生理、感觉和认知能力以及残疾，以及需要考虑的情感差异。因此，在设计家用设备时，应充分考虑这些因素。"_

在家庭医疗环境中，更新方法的适用性取决于多种因素，包括医疗设备风险分类、资源需求（例如，高速互联网连接）和可用性。由于用户能力范围广泛，许多家用设备需要采用表 1 中列出的“服务访问”更新方法。对于植入式医疗设备的更新安装，可能需要与患者的医疗服务提供者进行面对面的互动。

某些家用设备，尤其是被归类为SaMD（软件为医疗器械）的产品，可以支持远程更新或由用户自行进行的修复方法。远程更新需要最少的用户交互，但通常需要根据医疗服务提供商确定的流程获得患者的同意。无论采用哪种更新方法，患者都应遵循其医疗服务提供商和（如果适用）医疗设备制造商提供的说明。

如果患者计划进行国际旅行，则应与其医疗服务提供商或医疗设备制造商沟通，了解其设备上的软件维护选项。

### 监管机构

#### 市场后更新

威胁行为者不断适应和改进利用技术。因此，经常进行软件维护活动通常是必要的，以增强设备的网络安全防御能力（“网络安全卫生”），修复漏洞或减轻无法修复的漏洞带来的风险。如果对“仅为了加强网络安全”所做的每次更改都进行最高级别的监管审查，那么由此产生的审查负担将很快使大多数监管机构不堪重负。

在网络安全方面，监管机构应确定两个基本问题，以确定软件更改是否需要在发布前获得批准：

1. 更改的目的是仅为了加强网络安全，并且已确定该更改不会对软件或设备产生任何其他影响吗？

制造商应评估其系统，以确保此类变更不会影响设备的安全性或性能，通过进行必要的分析、验证和/或验证。如果制造商发现变更对软件或设备的其他方面产生任何意外或间接影响，则监管机构可能会决定，对拟议的修改进行预部署审查是适当的。

1. 变更是否旨在消除或降低与患者伤害相关的不可接受的残留风险相关的漏洞？

上市后漏洞风险评估应基于对可利用性和潜在患者伤害的严重程度的评估，并用于确定残留风险是否可接受或不可接受。请注意，“患者伤害”的定义是“伤害”的子集，该“伤害”已定义在ISO 14971:2019《医疗器械——医疗器械风险管理应用》中[5]。“患者伤害”的狭义定义，实际上是为了优先审查那些必要的变更，以保护公共健康。

表 3 呈现了一个监管机构在考虑各种软件维护活动所需的监管监督框架的建议框架。需要注意的是，本表中呈现的级别并非强制性的，而是提供了一种关于推荐的监管监督级别指南。

**更新目的** | **拟定的监管要求级别** | **示例**
---|---|---
增强安全性 (“网络安全”) | 低 | 一种软件为医疗设备 (SaMD) 应用程序 (“app”) 的制造商，了解到主机操作系统更新，该更新增加了安全控制，以支持多层次防御策略。该 SaMD 应用程序需要修改，以便与主机操作系统的低层接口更改兼容。与该 SaMD 应用程序相关的修改与已知的任何漏洞无关。
针对无法修复的漏洞的漏洞修复或风险降低策略 | 适当的患者伤害风险 | 中 | 一家制造商收到用户投诉，称一种血气分析仪感染了恶意软件，并且存在恶意软件可能修改设备数据的担忧。制造商的调查和影响评估证实了恶意软件的存在，并确定恶意软件不会导致存储和通过设备传输的未加密数据的篡改。该设备的安全性及其基本性能不受恶意软件的影响，制造商的风险评估确定，由于该漏洞，患者受到伤害的风险是可接受的。[6]
不可接受的患者伤害风险 | 高 | 制造商了解到存在未使用的通信端口。制造商承认已收到漏洞报告，并对漏洞查找者和后续分析表明，该设备的内置功能无法阻止未经授权的固件下载到设备，这可能会被用于损害设备的安全性及其基本性能。虽然没有报告与该漏洞相关的任何严重的不良事件或死亡，但风险评估得出结论，由于该漏洞，患者受到伤害的风险是不可接受的。[7]

##### 表 3：软件更新和建议的监管审查级别

如果拟议的软件变更影响多个漏洞，或者，作为替代，改善“网络安全”并影响至少一个漏洞，则制造商应考虑表 3 中列出的最高适用级别，以指导后续行动。例如，一个软件变更可以增强系统安全，降低漏洞 A（患者潜在伤害的容忍风险）、并修复漏洞 B（患者潜在伤害的不可接受风险）。在这种情况下，与漏洞 B 相关的“高”级别的监管要求将适用。

对于任何级别，监管机构可以根据自身判断，要求制造商提供证据，证明制造商正在遵循已建立的软件维护生命周期流程和其他监管要求，包括 IEC 62304:2006/AMD 1:2015 中规定的要求。

## 应急响应

### 医疗设备制造商

医疗器械制造商应为应对可能影响其产品和客户（包括患者）的网络安全事件和事件做好准备。因此，制造商应建立应急响应管理政策，并根据其产品组合建立应急响应团队。应急响应团队的目标是提供适当的容量，以评估、应对和从网络安全事件中学习，并提供必要的协调、管理、反馈和沟通，以便在下一次事件中及时有效地采取行动。

准备工作包括建立应急管理政策、制定详细的应急响应计划、建立应急响应团队、定期测试和演练应急响应，以及通过经验教训不断改进这一能力。

根据 ISO/IEC 27035 的定义，事件管理包括以下内容（参见“角色和职责”部分以获取更多详细信息）：计划和准备、检测和报告、评估和决策、响应和经验教训（参见附录 A 以获取项目描述）。

#### 角色和职责

事件响应团队可以分为以下小组：经理、规划、监控、响应、实施、分析，以及有时还会包括外部专家。每个小组都有不同的角色和职责。团队应根据成员的技能和知识，将成员分配到这些小组，并且某些职位可能由多名团队成员担任。被分配到相关小组的成员应负责相同或相似的工作。有关这些小组角色的更详细信息，请参见附录 A。

#### 沟通期望

客户应获得医疗器械制造商的联系方式，以便报告网络安全事件和事件，或通过常规客户支持渠道进行其他报告。事件响应团队应建立定期更新所有受事件影响的利益相关者的节奏，并尽快向客户提供有针对性的沟通（制造商应了解关于及时沟通的具体管辖要求）。制造商在事件期间及时、准确地向客户提供公告或通知的时间，可能取决于与客户的及时有效沟通。

医疗设备网络安全事件，如果对患者安全和隐私造成影响，必须按照法规的要求向相关监管机构报告。如果调查过程中发现了犯罪活动，应通知当地和适用的执法机构。应联系CERT和ISAO，以就全球网络安全攻击和事件进行进一步协调。

### 医疗机构

医疗机构应建立处理安全事件的政策，以及减轻或解决安全事件的机制，并向内部和外部利益相关者披露相关信息。为此，医疗机构应考虑制定计划和管理资源，以减轻设备漏洞。这可能包括确保在事件发生时，有足够的备用或额外设备。

#### 政策和角色

医疗机构应制定漏洞或安全事件处理政策和角色。这些政策应规定医疗机构如何接收和传播来自制造商披露文件（例如，医疗设备安全制造商披露声明（MDS2）、SBOM、漏洞/更新信息）以及信息共享机构或参与的ISAO的信息。为此，必须维护和定期验证联系人的清单，以便及时获取和提供信息。同样，在安装前制定的服务级别协议（SLA），以及定期审查，规定制造商和其他供应商在事件发生期间或应对事件时必须履行的义务。鼓励医疗机构建立自己的安全事件响应团队。

#### 角色培训

要求为每个相关角色建立并定期审查，以确定是否需要更新。负责评估安全事件证据的专家，除了需要具备安全取证分析的知识外，还应具备实际经验。参与事件响应过程的人员，应接受该过程和事件响应理论的培训，此外还应具备实际经验。应定期评估培训流程，并可以进行事件响应演习以进行评估。

#### 分析与响应

医疗服务提供者应评估任何事件或报告的漏洞的影响，并与相关方（包括医疗器械制造商）合作，提供调查结果的描述性信息。如果需要采取任何行动来解决问题，调查状态和时间表应包含在结果中。医疗服务提供者应向患者提供与安全相关的信息，包括最佳实践和缓解措施。如果解决方案包括修复，则在将修复应用于整个设施之前，必须进行验证，包括回归测试。这些测试应确保修复不会影响现有系统功能。医疗服务提供者应根据需要更新修复和缓解信息。

### 医疗器械监管机构

监管机构也应参与医疗器械网络安全事件的应对。如制造商响应部分中所述，监管机构应被告知网络安全事件，以便他们了解情况、请求额外的信息以进行监管决策，并在必要时采取进一步行动。根据需要，进一步行动可能包括但不限于评估患者安全影响、评估制造商提出的缓解措施的效益/风险、向利益相关者（包括非传统利益相关者，如网络安全研究人员）进行沟通，以及与其他政府机构和监管机构进行合作。

## 遗留医疗器械

为了本 IMDRF 指导的目的，如果医疗设备无法通过更新（以及/或补偿控制措施）来合理地保护其免受当前的网络安全威胁，则这些设备将被视为“老旧设备”。“老旧设备”状况对全球医疗生态系统的现状构成了尤其复杂的挑战，因为许多今天使用的设备，在最初的设备设计和维护中，可能并未充分考虑网络安全。 此外，随着医疗设备中数字技术的应用，这些设备的功能得到了扩展，而这些功能在较早的模拟设备中无法实现。 虽然这些技术对患者护理有益，但软件、硬件和网络连接的组合，给设备的使用寿命带来了新的要求，这些要求通常包括资本设备（例如扫描硬件）以及通用组件（例如服务器、工作站、数据库和操作系统）。 然而，需要注意的是，设备的使用年限并不是“老旧设备”的唯一决定因素。 换句话说，如果设备无法合理地保护其免受当前的网络安全威胁，该设备可能只有不到五年的使用年限；无论其使用年限如何，该设备仍然将被视为“老旧设备”。 另一方面，如果设备可以使用，并且能够维持其在当前网络安全威胁下的合理保护能力，则该设备将不被视为“老旧设备”。

随着从医疗器械设计和开发的最早阶段开始，针对医疗器械网络安全问题的努力不断推进，能够维持在整个使用寿命内对网络安全威胁具有合理保护能力的设备的可用性将越来越普遍，并且，与当前临床使用中大量老旧设备的失衡——这些设备对医疗机构及其网络构成安全威胁——将逐渐减少。以下 IMDRF 指导的子部分阐述了一个概念框架，旨在实现医疗器械网络安全的最佳未来状态，即，在医疗机构能够合理地保护其设备免受当前网络安全威胁影响的情况下，老旧设备（即无法合理地保护的设备）将被逐步淘汰，并向医疗机构发出适当的通知，以便进行业务连续性规划。（参见图 2）。

![A screenshot of a cell phone Description automatically generated](data:image/jpeg;base64,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iIgIiICIiD44FzSAS0kcx2LQMldE+G5Nx+qxpuIVVdWzsczXOGjTqN3HbmTbn610BEBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQFW5gwnx9gFdhRqpaVtXC6F00VtTQedr+jb2qyRBqGQOj3Duj+gqqeiqJqmSqkD5ZpgATYWAAHYLn3rb0RAREQEREBERAREQEREBERAREQEREBERAREQEUHEMYocMgdNV1MUUbebnvDQPaVpGIdMGX6VxZA+apI7YYiR7yQrETPJL2dFRcrj6a8LLwH0Vaxvfoaf4ArZMH6ScvYvI2KOuZHK7YRzAxuJ9F9j70mmYLw3BF4jmZK27HXXtRRERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAWjZ6z/TZZp+BAGzV0gvHFfYD853c37Vf5oxyHAMCqa6bcRsJ033ceQb7Tt71+YcRxCpxXEZ66skL55nanH7APQOS3RTdmqbMuLY1iGOVZqcRqXzP/JB2awdzRyCgKVR4dXYgJjRUc9RwWa5OFGXaG95sttoOjDGK/KUuNgujlDXPjonQniSNHaO6+9hb7V2vEOdplpCKXUYXiFJSR1VTQ1MNPI4sZJLEWtcRzAuoio3LKPSFiWXJ44aiSSqw+9jG43fGO9hP2HZfoHCMWpcZw+KspJWyRSN1Nc3tH/rs7F+TFv3RfmqTB8bbhk0n9Eq3WYHHZkvZ7DyPsXOunzhqmryfoRFy6s6Z6agrZ6SowKrbNBIY3jit5grB9/Kh/sSq/etXPRLeqHWEXJ/v5UP9iVX71qffyof7Eq/3rU0VGqHWEXJ/v5UP9iVX71qffyof7Eqv3rU0VGqHWEXJ/v5UP9iVX71qffyof7Eqv3rU0VGqHWEXJ/v5UP8AYlV+9an38qH+xKr961NFRqh1hFyf7+VD/YlV+9an38qH+xKr961NFRqh1hFyf7+VD/YlV+9an38qH+xKr961NFRqh1hFyf7+VD/YlV+9an38qH+xKr961NFRqh1hFoOWelCkzJiElIzD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H93L9ezV6N1E25qZKqKQOBZJTgGw9RI39N1PqMVo699c2pjnjjnkjkY6OznXa3Tvew3Hb3q58gXfXx8CeQLvr4+BKcpmqY0xT9u/uVZzKVTqmv79vZBdXUNdFisrxNHTuip2ADSXgtNr25HkvNLW0c7auK0raSDDuC0kgSO64JNuV7nkrDyBd9eHwJ5Au+vD4F03GavfR8x7z/Ln4jKWtr6eU+0fwp2YtSQiKlYyZ1G2nkge8gCQ6zcuAvbYgbJS4tR0UtDHC2d9PTyvle97QHOc5unYA2AHrVx5Au+vj4E8gXfXx8Cz4bNxN9P27+zU5nJTFtX39/b3a3QVVPDS1tNU8UMqGNAdGAS0tdfkSFAW5+QLvr4+BPIF318fAuU5HMzERNPL3ju6xtDKxMzFXP2ns0xFufkC76+PgTyBd9fHwLP0/M+n5ju19Sy3q+J7NMWei/Hqf9q37VtnkC76+PgXuHIzoZ45fDQdDg62jnYrVGQzEVRM0/Md2a9o5aaZiKviezc0RF+kfmBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREEKf6Wo/wBSX/apqhz/AErSfs5f9qmICIiAiIgIiICIiAiIgIiICIiAiIgIiIPL/wAG71FR8M+iqT9iz7ApLvmO9Si4X9FUn7Fn2IJaIiAiIgIiICIiAiIgIiICIiAiIgIiIChYhu+j/wAQ37HKaodd+Fov8QP5XIJiIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIghz/StJ+zl/2qYoc30rSfspf9qmICIiAiIgIiICIiAiIgIiICIiAiIgIiIPjvmn1KLhn0XS/sm/YpZ5FRML+iqX9k37EEtERAREQEREBERAREQEREBERAREQEREBRKz8PRD+//wBjlLUSr/GqAf35/wCm9BLREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREEOb6Vpf2Un2tUxQ5fpam/YyfaxTEBERAREQEREBERAREQEREBERAREQEREBQ8L+i6X9mFMUPCvoum/ZhBMRR62tpsOo5KurlbFBGLue71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NrdQMb2/KGzw3UAAdt78lBGGVoe14ezU03BMt19dhlc+QyOezWSSTxe9S8dS09EiHDKZtRTtkZUzslDjraNLTs6zeV9XVGy90+DQCKnlmZO4ybGK4ubsc5tjbnty39nJQvFNYAAHRixv+F7U8VVm3XZty+V5JeOpaeiVHhUUzIXHijWyNp4bR8ndpOp/o29HavjcJpXOYBJPsWNfZoNy6MuFrAkC4tffvUbxTWb9aPfY/K80GFVgNw6MH0SpeOpaeiHPEYKiSIixY4tIuDyPeFjU/wAUVXfF+8TxRVf3X7xa109U0z0QEU/xRVf3X7xPFFV/dfvE109TTPRART/FFV/dfvE8UVX91+8TXT1NM9G/Ze/8b9Yq+VFl4bSnsLjur1eN6RERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERBjmiEsZaVz7MWAvimfVUzLjnIwDl+kPQuiqNVUjahvc4ciFqmqaZvCVUxMWcdRbriuXIJXue5joZD+XG27T62/8ACoZMvVYJ4MsEwHc/SfcV6IxKZcJomFQisxgGIk7wsaO90jQPtWaPA44zerrGC3NkHXd/wtTXTHmkUVSq6enlqpmwwsL3u5ALZKXDmmPxbTniF5/pMo5H9EegKVRYfLIzgUUBp4HfOed3v9ZW0YbhcVBEA1o1dpXnrxNXCHamizHR4HR01O1gibsO5SPFdJ5pvuUxFzbQ/FdJ5pvuTxXSeab7lMRBD8V0nmm+5PFdJ5pvuUxEEPxXSeab7k8V0nmm+5TEQQ/FdJ5pvuTxXSeab7lMRBD8V0nmm+5PFdJ5pvuUxEEPxXSeab7k8V0nmm+5TEQQ/FdJ5pvuTxXSeab7lMRBjhgjgFo2gBZERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREHlzGvFnAEKHNhNLN85gU5EFOcvUhO7VIhwakhNxGCfSrBEHlkbIxZrQF6REBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQ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)

##### 图 2：产品生命周期内，老旧设备的概念框架，用于网络安全

### 医疗设备制造商

对医疗器械网络安全的关注应在设备设计和开发阶段开始，在商业发布之前，如图 2 所述。 按照 TPLC 框架，制造商应继续提供对医疗器械的全方位支持，以确保其能够对当前的网络安全威胁提供合理的保护，直至制造商发布的网络安全终生命日期（EOL）。 制造商的网络安全终生命日期标志着该医疗器械对全面网络安全支持的能力下降。 在接近网络安全终生命日期时，制造商应向其客户发布通知，告知他们在EOL之后剩余有限的支持，并明确说明该设备的网络安全终支持（EOS）日期。 不应期望在已确定的网络安全EOS日期之后，对任何医疗器械提供任何支持。

根据这个概念框架，当医疗设备达到其网络安全EOL日期时，它将被视为一种无法合理保护免受当前网络安全威胁的过时医疗设备，并应被报废。在此，维护设备安全和对其超出EOL日期的持续使用的风险承担责任将转移给客户，例如医疗机构。

重要的是要注意，虽然某些设备的某些设计更改可能不可行（例如，不再受支持且无法出于安全目的进行修补的过时操作系统），但补偿控制可能会提供一定程度的保护。在存在可用的且已成功部署的补偿控制的情况下，根据本框架，该医疗设备将不被视为过时设备。根据需要，监管机构可能会鼓励医疗设备制造商利用补偿控制来解决EOL日期后的当前设备安全挑战，以便为医疗机构提供充足的时间来进行EOL时的业务连续性规划，而无需制造商提供进一步的安全支持。设备设计、漏洞管理和客户沟通在解决设备网络安全挑战方面都发挥着重要作用。根据设备生命周期阶段，制造商的建议包括以下内容：

* 开发：

1. 考虑构成医疗设备的硬件和软件组件的生命周期。为了提供全面的医疗设备支持，制造商应能够从相应的硬件和软件供应商处获得支持，通过软件/固件更新来解决质量、性能和安全问题。制造商应预见到在产品使用期间支持产品的安全性，制造商应考虑第三方供应商对组件的支持可能在医疗服务提供者的设备预期使用寿命内结束，这可能会 adversely 影响制造商支持设备安全运行的能力。

2. 在安全开发框架下设计和开发设备，以最大限度地减少未来遗留设备的数量。这些设备至少应满足安全基准，并包括更新和补丁机制。

* 支持：

1. 监控存在不可接受风险的医疗设备，并提供最佳努力响应，并维护与设备整个生命周期相符的持续风险文档，作为风险管理的一部分。

2. 清晰地沟通关键生命周期里程碑，包括设备的安全终结日期（EOL），作为采购和安装流程的一部分，客户责任应在这些时间点集成到沟通中。

3. 主动通知客户第三方供应商对设备组件的支持结束。

4. 发布客户通知，表明在网络安全EOL日期之后，设备将不再提供支持，但仍会有限期内提供支持。 这种客户沟通的时间应在接近EOL日期时进行，以便为医疗机构提供设备停用/淘汰和业务连续性规划的提前通知。 明确地告知有助于医疗组织了解其责任以及设备风险，以便他们可以计划设备的退役和更换，并据此进行预算。

* 有限支持（EOL从这里开始）：

1. 继续沟通网络安全EOL日期的时间表，以便客户有充足的时间为EOL做好准备并承担相关的客户责任。

2. 继续执行上述支持生命周期阶段中的“a”和“c”项。

* 终结支持（遗留状态从这里开始）：

1. 制造商将全部责任转移给客户。 在设备正式的网络安全EOL之后，设备用户不应期望任何形式的支持。

### 医疗机构

许多医疗机构计划使用设备的时间比制造商在其发布的网络安全EOL中公布的设备寿命更长。 然而，随着时间的推移，威胁形势的变化以及新威胁的出现，使用过时技术的风险和成本会增加，必须通过制造商和医疗机构之间的共同责任来加以考虑。 以下建议，根据设备生命周期阶段，预计将有助于解决医疗机构与医疗设备的挑战，并提前计划在已定义的网络安全EOL日期：

* 支持：

1. 明确要求与设备制造商建立清晰的联系点和沟通流程，以确保产品生命周期规划、理解和透明度。

2. 请求 SBOM，因为具有最短支持生命周期的软件组件最终会影响这些设备的可用性和安全性。 获取 SBOM 有助于客户更好地了解影响设备生命周期的组件，并可以包含用于风险控制措施（如补偿控制）的额外硬件信息。

3. 在使用过程中，确保对医疗设备进行适当的支持和维护，可以通过医疗设备制造商、第三方服务代理或内部资源和控制来实现。 这包括对网络安全、资产安全、身份和访问管理以及安全运营的适当支持。

4. 评估其环境中的新和不断变化风险，并尽一切努力通过适当的缓解措施（包括但不限于网络分段、用户访问角色、风险评估、安全测试、网络监控等）来控制风险。

5. 提前计划制造商的网络安全EOL日期，以便无法停用（可能危及患者安全和医疗网络安全）的旧设备能够得到适当的淘汰和替换为安全的、可支持的医疗设备。

* 有限支持：

1. 继续执行“c”、“d”和“e”项，这些项在“设备生命周期”阶段中。

* 终结支持：

1. 承担管理设备安全并承担其在网络安全EOL日期之后持续使用的安全风险的责任，如果无法在不影响患者护理的情况下停用设备。

# 参考文献

## IMDRF 文档

1. 软件作为医疗设备：风险分类的可能框架及其相关考虑 IMDRF/SaMD WG/N12:2014 (2014年9月)

2. 医疗器械和体外诊断医疗器械的安全性与性能基本原则 IMDRF/GRRP WG/N47 最终版：2018（2018年11月）

## 标准

AAMI TIR57:2016 医疗器械安全——风险管理原则

AAMI TIR 97:2019，医疗器械安全——制造商的上市后风险管理

IEC 60601-1:2005+AMD1:2012，医疗电气设备 - 第 1 部分：基本安全和基本性能的通用要求

IEC 62304:2006/AMD 1:2015，医疗器械软件——软件生命周期流程

IEC 62366-1:2015，医疗器械 - 第 1 部分：将可用性工程应用于医疗器械

IEC 80001-1:2010，包含医疗器械的 IT 网络中的风险管理 - 第 1 部分：角色、责任和活动

IEC TR 80001-2-2:2012，包含医疗器械的 IT 网络中的风险管理 - 第 2-2 部分：关于披露和沟通医疗器械安全需求、风险和控制的指导

1. IEC TR 80001-2-8:2016，包含医疗器械的 IT 网络中的风险管理——第 2-8 部分：应用指导——关于 IEC 80001-2-2 中识别的安全能力的标准指导

ISO 13485:2016，医疗器械——质量管理系统——用于监管目的的要求

ISO 14971:2019，医疗器械——将风险管理应用于医疗器械

ISO/TR 80001-2-7:2015，包含医疗器械的 IT 网络中的风险管理——应用指导——第 2-7 部分：关于医疗保健提供机构（HDO）如何评估其符合 IEC 80001-1 的指导

ISO/IEC 27000 系列 - 信息安全管理系统

1. ISO/IEC 27035-1:2016，信息技术——安全技术——信息安全事件管理——第一部分：事件管理原则

2. ISO/IEC 27035-2:2016，信息技术——安全技术——信息安全事件管理——第二部分：事件响应规划和准备指南

3. ISO/IEC 29147:2018，信息技术——安全技术——漏洞披露

4. ISO/IEC 30111:2013，信息技术——安全技术——漏洞处理流程

ISO/TR 24971:2020，医疗器械——应用 ISO 14971 的指导

UL 2900-1:2017，适用于可连接网络的产品的软件网络安全标准，第1部分：通用要求

UL 2900-2-1:2017，适用于可连接网络的产品的软件网络安全标准，第2-1部分：医疗保健和健康系统可连接组件的特定要求

## 监管指导

1. ANSM (草案)：医疗器械在生命周期中集成软件的网络安全（2019年7月）

2. 中国：医疗器械网络安全注册的技术审查指导原则（2017年1月）

3. 欧盟委员会：2017/745号关于医疗器械的欧盟议会和理事会法规，于2017年4月5日通过，修订指令2001/83/EC、法规（EC）第178/2002和（EC）第1223/2009，并废除理事会指令90/385/EEC和93/42/EEC（2017年5月）

4. 欧盟委员会：2017/746号关于体外诊断医疗器械的欧盟议会和理事会法规，于2017年4月5日通过，并废除指令98/79/EC和委员会决定2010/227/EU（2017年5月）

5. FDA (草案)：用于管理医疗器械网络安全的前市场提交内容（2018年10月）

6. FDA：包含离线软件的网络医疗器械的网络安全（2005年1月）

7. FDA：为家用设备设计的设计考虑（2014年11月）

8. FDA：管理医疗器械网络安全后的市场管理（2016年12月）

9. 德国：网络连接医疗器械的网络安全要求（2018年11月）

10. 加拿大卫生部：医疗器械网络安全预上市要求 (2019年6月)
  11. 日本：确保医疗器械网络安全：PFSB/ELD/OMDE 通知第 0428-1 (2015年4月)
  12. 日本：关于确保医疗器械网络安全的指南：PSEHB/MDED-PSD 通知第 0724-1 (2018年7月)
  13. 新加坡标准委员会技术参考 67：医疗器械网络安全 (2018)
  14. TGA：医疗器械网络安全 - 消费者信息 (2019年7月)
  15. TGA：医疗器械网络安全行业指导 (2019年7月)
  16. TGA：医疗器械网络安全用户信息 (2019年7月)

## 其他资源和参考

1. CERT® 协调漏洞披露指南

<https://resources.sei.cmu.edu/asset_files/SpecialReport/2017_003_001_503340.pdf>

1. NIST 网络安全框架

<https://www.nist.gov/cyberframework>

1. NIST 的安全软件开发框架 (SSDF)

<https://csrc.nist.gov/CSRC/media/Publications/white-paper/2019/06/07/mitigating-risk-of-software-vulnerabilities-with-ssdf/draft/documents/ssdf-for-mitigating-risk-of-software-vulns-draft.pdf>

1. 医疗器械与健康信息技术联合安全计划 (2019年1月)

<https://healthsectorcouncil.org/wp-content/uploads/2019/01/HSCC-MEDTECH-JSP-v1.pdf>

1. MITRE 医疗器械网络安全 playbook (2018年10月)

<https://www.mitre.org/publications/technical-papers/medical-device-cybersecurity-regional-incident-preparedness-and>

1. MITRE CVSS 医疗领域指南

<https://www.mitre.org/publications/technical-papers/rubric-for-applying-cvss-to-medical-devices>

1. 医疗行业网络安全实践：管理威胁和保护患者 (HICP)

<https://www.phe.gov/Preparedness/planning/405d/Pages/hic-practices.aspx>

1. 开放网络应用程序安全项目 (OWASP)

<https://www.owasp.org/index.php/Main_Page>

1. 医疗器械安全制造商披露声明 (MDS2)

<https://www.nema.org/Standards/Pages/Manufacturer-Disclosure-Statement-for-Medical-Device-Security.aspx>

2. ECRI 将 NIST 框架应用于医疗器械的方法

<https://www.ecri.org/components/HDJournal/Pages/Cybersecurity-Risk-Assessment-for-Medical-Devices.aspx>

1. 美国国家电信与信息管理局 (NTIA) / 美国商务部，漏洞披露态度与行动：NTIA 意识与采用小组的研究报告

<https://www.ntia.doc.gov/files/ntia/publications/2016_ntia_a_a_vulnerability_disclosure_insights_report.pdf>

1. <https://republicans-energycommerce.house.gov/wp-content/uploads/2018/10/10-23-18-CoDis-White-Paper.pdf>

2. <https://resources.sei.cmu.edu/asset_files/SpecialReport/2017_003_001_503340.pdf>

# 附录

## 附录 A：事件响应角色 (基于 ISO/IEC 27035)

**事件管理 – ISO/IEC 27035**

---  
计划和准备 | 制定信息安全事件管理政策，组建事件响应团队等。
检测和报告 | 必须有人发现并报告“事件”，这些事件可能发展成事件。
评估和决策 | 必须评估情况，以确定是否确实发生了事件。
响应 | 在适当情况下，对事件进行遏制、清除、恢复和法证分析。
经验教训 | 作为因经历的事件而系统地改进组织的信息风险管理。
**事件响应团队**

---  
**角色** | **职责** | **主要行动**
经理 | 负责并就涉及网络安全事件响应的主要问题做出决策 | a) 承诺并支持事件响应，包括提供必要的资源（人力、财务和物料）；b) 审查和批准事件响应政策和计划，并监督实施；c) 审查和修订事件响应计划；d) 协调内部和外部团队。
计划小组 | 实施事件响应 | a) 制定和规划安全政策；b) 实施安全流程；c) 调整风险优先级；d) 与更高层级的组织和其他第三方组织沟通；e) 提供行政支持；f) 就目标组织的漏洞报告进行讨论/登记/批准；g) 按照经理指示执行其他活动。
监测小组 | 实施实时安全监测活动 | a) 每日监测和操作；b) 检测入侵、记录事件和初步响应；c) 执行安全更新；d) 实施安全政策和备份管理；e) 帮助台；f) 设施管理；g) 按照经理指示执行其他活动。
响应小组 | 提供如实时响应、技术支持等服务 | a) 传播和报告事件；b) 监测系统之间的相关性分析；c) 提供事件调查和恢复支持；d) 就目标事件进行漏洞分析；e) 按照经理指示执行其他活动。
实施小组 | 实施事件响应的全部行动 | a) 分析事件响应要求；b) 确定事件响应政策和级别；c) 实施事件响应政策和计划；d) 制定事件响应计划；e) 总结事件响应工作并撰写报告；f) 部署和使用事件响应资源；g) 按照经理指示执行其他活动。
分析小组 | 实施事件分析 | a) 为团队和制造部门制定漏洞分析计划；b) 改进安全分析工具和检查清单；c) 改进监测规则；d) 发布新闻通讯；e) 按照经理指示执行其他活动。

## 附录 B：协调漏洞披露的管辖区资源

**澳大利亚**

澳大利亚CERT

<https://www.cert.gov.au/>

AusCERT

<https://www.auscert.org.au/>

**巴西**

巴西所有CERT

<https://www.cert.br/csirts/brazil/>

**加拿大**

加拿大网络安全中心

<https://www.cyber.gc.ca/>

**欧洲**

欧盟CERT

<https://cert.europa.eu>

**法国**

ANSM

<https://ansm.sante.fr/>

<https://www.ansm.sante.fr/Declarer-un-effet-indesirable/Votre-declaration-concerne-un-dispositif-medical/Votre-declaration-concerne-un-dispositif-medical/(offset)/0>

法国卫生与团结部

<https://solidarites-sante.gouv.fr/soins-et-maladies/signalement-sante-gouv-fr/>

共享健康信息系统机构

<https://www.cyberveille-sante.gouv.fr/>

ANSSI - 国家信息系统安全机构

<https://www.ssi.gouv.fr/en/>

**德国**

德国CERT

<https://www.cert-bund.de/>

**意大利**

<https://www.csirt-ita.it/>

**日本**

日本计算机应急响应小组/协调中心 (JPCERT/CC)
<https://www.jpcert.or.jp/vh/top.html> 或 <https://www.jpcert.or.jp/english/>

**新加坡**

SingCERT

<https://www.csa.gov.sg/singcert/news/advisories-alerts>

**美国**

工业控制系统应急响应团队 (ICS-CERT)

<https://www.us-cert.gov/ics>

US CERT

<https://www.us-cert.gov/>

1. N47 第 5.8 节描述了重要的信息安全和网络安全要求，例如防止未经授权的访问。这些要求应在医疗器械的整个生命周期中与本指南一起考虑。 ↑

2. IEC 60601-1-11:2015，《医疗电气设备 — 第 1-11 部分：基本安全和基本性能的通用要求 — 附属标准：医疗电气设备和医疗电气系统的要求，用于家庭医疗环境》，将“家庭医疗环境”定义为“患者居住的场所或患者存在的其他场所，但不包括专业医疗机构环境……”。并列举了“在汽车、公共汽车、火车、船或飞机上，在轮椅上或在户外行走”等示例。 ↑

3. 承认，在某些情况下，用户无法充分评估风险。 ↑

4. 《医疗器械和健康信息技术联合安全计划》，由医疗与公共卫生领域协调委员会（HSCC）于2019年1月发布。请注意，前两列进行了轻微修改，以提高清晰度，并且“临时补丁”方法已被删除（仅考虑经过验证的补丁）。 ↑

5. ISO 14971:2019 将“危害”定义为“对人的身体或健康、财产或环境造成的物理伤害或损害”，而“患者危害”仅包括该定义的第一个短语。 ↑

6. 摘自《指导：医疗器械的网络安全事后管理——行业和食品药品监督管理局》，2016年12月。 ↑

7. Ibid. ↑


<!-- fulltext-end -->
