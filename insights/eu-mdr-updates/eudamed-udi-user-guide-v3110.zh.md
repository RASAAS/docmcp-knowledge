---
id: insights-eudamed-udi-user-guide-v3110
title:
  zh: 官方指南：EUDAMED UDI/器械模块操作详解
  en: ''
type: insight
subcategory: eu-mdr-updates
category: insights/eu-mdr-updates
status: active
published_date: '2025-04-24'
source_url: https://reguverse.com/eu-mdr-update/eudamed-udi-user-guide-v3110/
source_format: html
translation: original
contributor: RASAAS
migrated_from: wordpress
wordpress_id: 4244
excerpt:
  zh: 欧盟委员会发布的关于如何在 EUDAMED（欧洲医疗器械数据库）的 UDI/器械模块（特指 Playground 测试环境 v3.11.0）中进行操作的用户指南EUDAMED
    user guide UDI Devices Playground v 3.11.0 2025 。尽管这是针对测试环境的指南，但它详细揭示了 EUDAMED
    中 UDI/器械注册和管理的核心流程、数据要求和系统功能，具有非常
  en: ''
---

# 官方指南：EUDAMED UDI/器械模块操作详解

> 欧盟委员会发布的关于如何在 EUDAMED（欧洲医疗器械数据库）的 UDI/器械模块（特指 Playground 测试环境 v3.11.0）中进行操作的用户指南EUDAMED user guide UDI Devices Playground v 3.11.0 2025 。尽管这是针对测试环境的指南，但它详细揭示了 EUDAMED 中 UDI/器械注册和管理的核心流程、数据要求和系统功能，具有非常

欧盟委员会发布的关于如何在 EUDAMED（欧洲医疗器械数据库）的 UDI/器械模块（特指 Playground 测试环境 v3.11.0）中进行操作的用户指南EUDAMED user guide UDI Devices Playground v 3.11.0 2025 。尽管这是针对测试环境的指南，但它详细揭示了 EUDAMED 中 UDI/器械注册和管理的核心流程、数据要求和系统功能，具有非常高的实践指导价值和可操作性。

## **文件核心目的与适用范围**

  * **目的：** 指导制造商等经济运营商如何在 EUDAMED 的 UDI/器械模块中注册和管理医疗器械（包括 IVD）的唯一器械标识（UDI）信息 。这些信息旨在供所有人（包括公众、主管当局、公告机构）访问。
  * **适用范围：** 本指南详细描述了在 EUDAMED UDI/器械模块中注册符合 MDR (EU) 2017/745 和 IVDR (EU) 2017/746 的“法规器械”(Regulation Devices) 以及系统和手术包 (System or Procedure Packs, SPP) 的流程，还包括后续的数据管理、搜索和查看功能 。
  * **重要警示：** EUDAMED 系统本身并不包含法规、指南和良好实践中的所有约束条件。因此，能在 EUDAMED 中技术上实现的操作，不代表其在法规上是被允许的 。RA 人员必须确保所有操作和数据录入都完全符合 MDR/IVDR 及相关指南的要求。

## **关键解读与行动建议**

**1\. 访问 EUDAMED 与用户管理**

  * **核心要求：**
    * 需要一个与注册制造商关联的专业邮箱注册的 EU Login 账户 。
    * 制造商必须首先在 EUDAMED 中注册为“经济运营商”(Actor)。
    * 用户需要在 EUDAMED 中注册，并根据需要申请特定模块的权限 。
    * UDI/器械模块有不同用户权限：Viewer（默认，仅查看）、Proposer（创建和删除草稿）、Confirmer（包含 Proposer 权限，外加提交和作废记录）。
    * 申请 Proposer 或 Confirmer 权限需要由该制造商账户的本地管理员（LAA 或 LUA）批准 。
  * **建议：**
    * **确保账户与权限：** RA 需确保公司已在 EUDAMED 完成 Actor 注册。负责 EUDAMED 操作的相关人员必须拥有有效的 EU Login 账户。
    * **建立内部管理机制：** 明确公司内部谁担任 LAA/LUA 角色，负责批准用户访问请求 。建立清晰的内部流程，根据职责分配 EUDAMED 用户权限（谁负责录入草稿 Proposer，谁负责最终审核提交 Confirmer）。
    * **及时审批：** LAA/LUA 需及时处理内部用户的权限升级请求，避免延误数据录入工作 。

**2\. 注册“法规器械”(Regulation Devices) 的流程与数据要求**

  * **核心流程与概念：**
    * **标识符：** 核心标识符包括 Basic UDI-DI、UDI-DI，以及适用的包装 UDI-DI (Package UDI-DI) 。这些标识符对于特定的器械或 SPP 必须是唯一的 。
    * **注册基础：** 必须先注册 Basic UDI-DI，并且总是需要同时注册至少一个关联的 UDI-DI 。
    * **主要步骤 (以首次注册 Basic UDI-DI + UDI-DI 为例):**
      * **步骤 1: Basic UDI-DI 识别信息 ：**
        * 选择法规 (MDR/IVDR) 。
        * 选择签发机构 (Issuing Entity) 并输入 Basic UDI-DI 码（系统会校验格式和唯一性）。
        * 指明特殊器械类型（如：软件、试剂盒、SPP、需要 Master UDI-DI 的隐形眼镜等）。
        * 非欧盟制造商需选择授权代表 (AR) 。
        * 选择风险等级 。
        * 输入器械型号 (Device model) 和/或器械名称 (Device name) 。
      * **步骤 2: 证书信息 (如适用) ：**
        * 适用性取决于风险等级和器械特性（如 MDR Class III, IIb；IVDR Class D, C, 及 B 类自测/近患检测器械）。
        * 需提供公告机构 (NB) 信息，以及证书编号（如果已知）。
        * 此信息需要关联的 NB 在 EUDAMED 证书模块中确认后，器械状态才能变为“Registered” 。
      * **步骤 3: UDI-DI 识别信息 ：**
        * 选择签发机构并输入 UDI-DI 码（校验格式和唯一性，除非用于关联 Legacy Device）。注意 GS1 码需补齐至 14 位 。
        * 输入次要 UDI-DI (Secondary UDI-DI) (如适用) 。
        * 输入 EMDN 代码 (欧洲医疗器械命名法) 。
        * 输入商品名 (Trade name) 。
        * 输入参考号/目录号 (Reference/Catalogue number) (Master UDI-DI 可输入 ‘many’) 。
        * 指明是否直接打码 (Direct Marking) 。
        * 输入使用单元 DI (Unit of Use DI, UoU DI) (如适用，且基础数量 > 1) 。
        * 输入器械数量（每个 UDI-DI 的基础包装单位数量，Master UDI-DI 输入最大数量）。
        * 选择 UDI-PI 的类型 。
        * 输入附加信息及 URL 。
        * 选择 UDI-DI 状态（如：在欧盟市场、不打算投放欧盟市场、已不再投放欧盟市场）。
      * **步骤 4: UDI-DI 特性 ：**
        * 临床尺寸 。
        * 是否一次性使用及最大复用次数 。
        * 是否含乳胶 (仅 MDR) 。
        * CMR/内分泌干扰物信息 (仅 MDR，可输入 EC# 或 CAS#) 。
        * 存储/操作条件 。
        * 关键警告或禁忌症 。
      * **步骤 5: 器械信息 ：**
        * 是否为复处理一次性器械 (仅 MDR) 。
        * 是否有非医疗预期用途 (MDR Annex XVI) 。
        * 原始制造商信息（如非本制造商，可通过 SRN 搜索或手动输入）。
        * 临床研究参考信息 。
        * 组织/细胞/物质信息 (MDR/IVDR 有别) 。
        * 是否为“新”器械 (仅 IVDR) 。
        * 首次投放欧盟市场的成员国，以及计划投放的成员国（对于非 Class I/A 且状态为“在欧盟市场”的器械是强制性的）。
      * **步骤 6: 包装容器信息 ：**
        * 为更高层级的包装（如中包装、外箱）添加包装 UDI-DI 和相应的数量 。
        * 每个包装层级都需要唯一的 UDI-DI 。
        * 包装状态通常需单独选择，但若基础 UDI-DI 状态为“不投放”或“已停止投放”，则包装状态自动跟随 。
  * **建议：**
    * **数据收集是核心工作：** RA 必须牵头，在开始注册前，完整、准确地收集上述 6 个步骤所需的所有数据点 。这需要与研发、生产、市场、临床、供应链等多个部门协作。将本指南作为数据收集的检查清单。
    * **理解并管理 UDI 码：** 深刻理解 Basic UDI-DI 与 UDI-DI 的层级关系，以及 Package UDI-DI、UoU DI、Direct Marking DI 的概念。确保从选定的签发机构获取正确的、符合格式要求的 UDI 码（例如，遵守 GS1 的补零规则 ）。
    * **关注强制字段和条件要求：** 识别所有标记为强制的字段 。理解某些字段的要求是基于其他字段的选择（如风险等级决定证书要求 ，器械状态和风险等级决定市场信息要求 ）。
    * **协调 NB 工作：** 对于需要证书的器械，RA 需与 NB 紧密协调，确保 NB 及时在 EUDAMED 中录入并确认证书信息，否则器械无法获得“Registered”状态 。
    * **处理 Legacy Device 关联：** 如果新注册的 Regulation Device 使用了已注册 Legacy Device 的 UDI-DI，系统会尝试自动链接 。RA 需确保两个记录的关键属性不冲突，否则无法链接 。需要规划好新旧产品 UDI 的过渡策略。
    * **数据准确性至上：** 反复核对录入数据的准确性，特别是各种代码（UDI 码、EMDN 码 ）、物质标识符（EC#/CAS# ）、原始制造商 SRN 等。错误可能导致记录需要被作废 (Discard)，代价高昂 。
    * **特殊类型器械的额外关注：** 对于软件 、试剂盒 、SPP 、以及使用 Master UDI-DI 的器械（如隐形眼镜 ），注意其特定的数据字段和规则。

**3\. 注册系统和手术包 (SPP)**

  * **核心要点：**
    * 此流程仅适用于在 EUDAMED 中注册为“SPP 生产商”的经济运营商 。
    * SPP 仅适用于 MDR 法规 。
    * 注册流程与常规器械类似，但有 SPP 特定的字段，例如 SPP 的风险等级由其包含的最高风险等级的器械决定 ，需要填写 SPP 的医疗预期用途 ，以及关于灭菌的特定问题 。
  * **建议：**
    * 如果公司生产 SPP， 必须确保公司 Actor 类型正确，并遵循此特定注册路径 。
    * 理解 SPP 风险等级的确定规则 ，并准备好 SPP 特定的数据。

**4\. 管理已注册的器械/SPP 信息**

  * **核心功能：**
    * **查看数据：** 查看已注册或草稿状态的 Basic UDI-DI 和 UDI-DI 的详细信息 。
    * **删除草稿：** 删除处于草稿状态的记录 。
    * **更新记录（创建新版本）：** 对已注册的记录进行修改会创建新版本，保留历史记录 。Basic UDI-DI 和 UDI-DI 码本身通常不可更改。
    * **独立更新特定部分：** 市场信息 、原始制造商信息（有限制 ）、包装容器信息 可以独立于 UDI-DI 主记录进行更新，并产生各自的版本历史。
    * **作废记录 (Discard)：** 对已注册的 UDI-DI 进行最终停用操作，使其在公开网站不可见 。通常用于纠正无法通过更新解决的严重错误 。作废最后一个 UDI-DI 会同时作废其关联的 Basic UDI-DI 。
    * **关联/解除关联 Legacy Device：** 手动将 Regulation Device 与 Legacy Device 关联（如果 UDI-DI 不同或自动链接失败），或解除已有的关联 。关联时系统会检查数据兼容性 。
    * **查看历史版本：** 查看 Basic UDI-DI、UDI-DI 及相关实体（市场信息、包装等）的所有历史版本 。
  * **建议：**
    * **建立严格的变更控制：** RA 必须制定公司内部对 EUDAMED 数据变更的严格控制流程。明确哪些变更需要分配新的 UDI (Basic 或 UDI-DI)，哪些只需在现有记录上创建新版本（需参考 MDR/IVDR UDI 分配规则）。
    * **理解版本管理：** 熟悉 EUDAMED 的版本控制机制 。确保内部文档与 EUDAMED 中的数据版本保持一致。
    * **制定错误纠正策略：** 规划如何处理录入错误。小错误可通过创建新版本修正，重大错误可能需要“Discard”并重新注册 。理解“Discard”操作的后果（主要是公开可见性丧失 ）。
    * **善用管理功能：** 培训相关人员使用“Manage your Basic UDI-DIs” 和“Manage your device details” (或对应 SPP 的管理入口 ) 进行日常数据维护和更新。
    * **管理 Legacy 关联：** 主动管理 Regulation Device 和 Legacy Device 之间的链接状态 。

**5\. 搜索与查看功能**

  * **核心功能：**
    * 提供强大的搜索功能，可通过多种过滤器查找已注册（或对 CA/NB 可见的其他状态）的器械和 SPP 。
    * 可以查看搜索结果的详细信息 。
    * 可以专门搜索处于特定“子状态”(Sub-status) 的器械，这些子状态通常与警戒模块中的现场安全通知 (FSN) / 现场安全纠正措施 (FSCA) 相关联（如“已启动现场安全纠正措施”、“已召回”）。
    * 可以搜索并查看记录的历史版本 。
    * 制造商可以批量下载**自己** 的器械/SPP 数据为 XML 文件，但需注意是按搜索结果页面下载 。
  * **建议：**
    * **利用搜索进行核查与监督：** 应利用搜索功能定期检查公司在 EUDAMED 中注册数据的准确性、完整性和状态 。也可用于了解公开的竞争对手产品信息。
    * **关注与警戒活动的联动：** 密切关注器械因 FSN/FSCA 而产生的“子状态” 。需与负责警戒的同事紧密协作，确保信息一致。
    * **数据备份与分析：** 使用 XML 下载功能 进行数据备份、内部存档或离线分析。了解其按页下载的限制 。

**总结**

  1. **EUDAMED 是法规强制要求，数据准确性是生命线：** 企业必须将 EUDAMED UDI/器械注册视为一项核心合规任务，确保数据的完整、准确和及时更新。
  2. **事前准备是成功的关键：** 在进入 EUDAMED 系统操作前，必须完成所有必要数据的收集、核对和 UDI 码的正确分配 。
  3. **熟悉系统操作与数据字段：** 相关操作人员必须熟练掌握本指南描述的各项操作（注册、更新、查询等），并深刻理解每个数据字段的含义和要求。
  4. **内部流程与权限管理：** 必须建立清晰的内部职责分工、审批流程（特别是 LAA/LUA ）和变更控制程序，以支持 EUDAMED 的有效管理。
  5. **理解标识符体系和状态逻辑：** 准确区分 Basic UDI-DI, UDI-DI, Package UDI-DI 等概念 ，并理解记录的不同状态（Draft, Submitted, Registered, Discarded ）及其含义。
  6. **关注与其他模块的联动：** UDI/器械模块与 Actor 注册、证书、警戒等模块紧密相关，RA 需要有全局视角，协调跨模块的信息一致性（如 NB 确认证书 ，FSCA 引发子状态 ）。
  7. **技术操作服从法规要求：** 牢记 EUDAMED 的技术可能性不等于法规允许性 。所有操作的最终依据是 MDR/IVDR 法规本身。

这份指南是理解和操作 EUDAMED UDI/器械模块不可或缺的工具。建议将其作为内部培训和操作规程（SOP）制定的重要参考。
