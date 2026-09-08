# Step 4：文献筛选

Step 4 按 Step 3 的纳入/排除标准做标题/摘要筛选，并按检索类型归档。输出是相关 / 不相关，还不是全文评分，也还不是 D1 / D2(a) / D2(b)。

## 这一步在法规上完成什么

系统评价必须先有可追溯的筛选记录，DCR 的识别、去重和筛选计数都来自本步。去重按篇，不按库把同一研究算两次。筛选在合并去重后的文献池上进行，因此不能再按单个数据库去「按比例拆」纳入数。

## 在助手中怎么操作

![Step 4 示意：按库上传、批次筛选、相关/不相关表](/guide/ce/ce-ui-step4.png)

*界面示意，不是真截图。*

1. 按数据库上传导出文件：PubMed 用 `.nbib`，Embase / Cochrane / ScienceDirect 用 `.ris`。每个检索类型都应有对应文件；某类没有上传时，识别表的原始命中、去重、去重后三列均为 0。
2. 核对解析出的原始命中与去重后数量。Embase 导出常常没有摘要字段，这是导出限制，不是解析失败。
3. 若适应症存在伦理上无法做 RCT 的情形，勾选 **Ethical prohibition against controlled trials** 并写明适应症。此后不得仅因缺少 RCT 而排除。
4. 点击开始筛选。文献多时按批进行：默认自动继续下一批，进度条显示当前批；可 **Pause**，再 **Continue Screening** 或恢复自动。出错时会停住，便于你查看后再继续。
5. 审阅相关 / 不相关判定和理由。不要在本步给 D/A/P/R 分。
6. 全部批次完成后，系统合并去重并给出累计统计。**Approve**。
7. 需要补传新检索文件时 **Reopen**，新批次追加到已有结果之后，不要 Redo 除非你要作废全部筛选。

等同优先时，本步第一波只处理 Equivalent + DUE 的上传与筛选。Gate 在第一波全文评价之后，不在本步。

## 用 ArticleFetcher 批量下载全文 {#af-fetch}

筛选完成后，可在相关文献表导出 DOI 列表，用 **ArticleFetcher v0.5.1** 批量下载开放获取全文。请使用窗口标题为 `Article Fetcher v0.5.1` 的版本。

- Windows：[国内](https://app.reguverse.com/downloads/ArticleFetcher-Windows.zip) · [国际](https://app.team-ra.org/downloads/ArticleFetcher-Windows.zip)
- macOS：[国内](https://app.reguverse.com/downloads/ArticleFetcher-macOS-GUI.zip) · [国际](https://app.team-ra.org/downloads/ArticleFetcher-macOS-GUI.zip)

也可在本步工具栏「PDF 批量下载工具」旁选择 Windows / macOS。

1. 点击 **导出 DOI**，保存 CSV（序号、标题、DOI、建议文件名）。
2. 打开 ArticleFetcher 的 **Fetch** 页：选择该 CSV、输出文件夹，填写用于 Unpaywall 的邮箱；如遇代理干扰，勾选 **Bypass system proxy**。
3. **Start Download**。完成后同一文件夹会有 `download_report.csv`。
4. 回到 Step 4，**导入批量结果**，导入该报告，标记哪些文献已有全文。

![ArticleFetcher Fetch](/guide/af/fetch.png)

付费墙或失败的条目仍可在表中手工标记。纳入/排除 PDF 的归档到 [Step 7](./eu-step7.html#af-organize) 使用 Organize 页。

## 审阅什么

- 相关文献是否真与 Step 1 的适应症和器械有关。
- 排除理由是否可写入 DCR，而不是「不相关」三个字。
- 去重后数量是否合理；不要为了凑数把明显重复的记录再纳入。

## 常见失败

- 未上传某一检索类型却以为「没有就是空」，识别表必须显示 0 而不是空白。
- 在本步做全文评价或来源打标（那是 Step 7）。
- 批次未完成就 Approve，后续统计与 DCR B.6 对不上。

## 下一步

Step 5 / Step 6 的警戒工作不绑文献分叉，可与 Step 4 / Step 7 并行。全文评价见 [Step 7](./eu-step7)。
