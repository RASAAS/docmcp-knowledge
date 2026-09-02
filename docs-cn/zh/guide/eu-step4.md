# 文献筛选 (Step 4)

## 概述

Step 4 对文献检索结果进行自动筛选（Title/Abstract Screening），根据 Step 3 中定义的纳入/排除标准判定每篇文献的相关性。

## 上传检索结果

在执行 Step 4 前，需先上传各数据库导出的文献文件：

1. 在 Step 4 面板中点击「Upload / 上传」
2. 选择对应数据库来源
3. 上传文件：
   - **PubMed**：上传 `.nbib` 格式文件
   - **Embase / Cochrane / ScienceDirect**：上传 `.ris` 格式文件
4. 系统自动解析、统计文献数量和去重结果

## 操作流程

1. **自动批次处理**：AI 按批次自动筛选文献
2. **进度监控**：实时显示筛选进度和统计
3. **审阅结果**：查看各文献的筛选判定和理由
4. **批准**：确认筛选结果

## 伦理禁忌声明（可选）

如果目标适应症存在伦理限制，无法开展随机对照试验 (RCT)，可在执行前勾选「Ethical Contraindications」选项并填写具体适应症说明。启用后，AI 在筛选时将不以缺少 RCT 作为排除依据，而是优先保留观察性研究和同类器械的临床经验数据。

## 批次处理机制

由于文献数量可能较多（几十到上千篇），Step 4 采用分批次处理：

- 每批处理一组文献
- 批次间自动延续（Auto-continue 模式）
- 可暂停自动模式改为手动逐批确认
- 处理完成后自动合并所有批次结果

### Auto-continue 模式

- 默认开启，自动执行下一批
- 进度条实时显示处理进度
- 点击「Pause / 暂停」可切换为手动模式
- 出错时自动暂停供用户检查

## 筛选输出

每篇文献的筛选结果包括：
- **Relevant (相关)**：纳入后续全文评审
- **Irrelevant (不相关)**：排除并记录排除理由

合并统计信息：
- 总检索量
- 去重后数量
- 纳入数量
- 排除数量（按排除理由分类）

## 用 ArticleFetcher 批量下载全文 {#af-fetch}

筛选完成后，在相关文献表上方可以导出 DOI 列表，并用 **ArticleFetcher v0.5.1** 批量下载开放获取全文。请使用 Step 4 工具栏里的 **Windows** / **macOS** 链接下载最新版（窗口标题为 `Article Fetcher v0.5.1`）。已下载过旧版的，请重新下载替换。

1. 点击 **导出 DOI**，保存 CSV（含序号、标题、DOI、建议文件名）。
2. 点击 **PDF 批量下载工具** 旁的 Windows 或 macOS，下载并打开 ArticleFetcher。
3. 打开 **Fetch** 页：
   - **DOI CSV**：选择刚导出的 DOI 列表
   - **Output dir**：选择保存 PDF 的文件夹
   - **Email (API ID)**：填写用于 Unpaywall 的邮箱
   - 如遇 VPN/代理干扰，勾选 **Bypass system proxy**
4. 点击 **Start Download**。完成后同一文件夹会生成 `download_report.csv`。
5. 回到 Step 4，点击 **导入批量结果**，导入 `download_report.csv`，自动标记哪些文献已有全文。

![ArticleFetcher Fetch：选择 DOI CSV 与输出目录后开始下载](/guide/af/fetch.png)

付费墙或下载失败的文献，仍可在表格中手动标记全文状态。归档纳入/排除 PDF 请到 [Step 7](./eu-step7.html#af-organize) 使用 Organize 页。

## 下一步

→ [安全数据 (Step 5)](./eu-step5)
