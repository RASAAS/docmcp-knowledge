# 安装插件

Reguverse 助手以 Microsoft Word 插件 (Office Add-in) 形式交付，支持 Windows 和 macOS 平台。此外还提供 Web 浏览器版本。

## 系统要求

| 平台 | 最低要求 |
|------|---------|
| Windows | Windows 10+，Microsoft 365 或 Office 2019+ |
| macOS | macOS 12+，Microsoft 365 for Mac |
| Web 版 | Chrome / Edge / Firefox / Safari 等现代浏览器 |

## 安装方式

### 方式一：自动安装（推荐）

从 [产品信息页](https://app.reguverse.com/info/) 下载对应平台的安装包，运行安装脚本即可自动完成配置。

**Windows 用户：**
1. 下载 `ReguverseAssistant-CN-Windows.zip`
2. 解压后双击运行 `install.bat`
3. 重启 Microsoft Word

**macOS 用户：**
1. 下载 `ReguverseAssistant-CN-macOS.zip`
2. 解压后双击运行 `install.command`（首次可能需右键 > 打开）
3. 重启 Microsoft Word

详细安装说明和下载链接请访问：
- 国内用户：https://app.reguverse.com/info/
- 国际用户：https://app.team-ra.org/info/

<!-- 截图占位：安装包解压后文件列表 -->

### 方式二：手动安装

如果自动安装失败，可手动安装：

**Windows：**
1. 打开文件资源管理器，地址栏输入：`%LOCALAPPDATA%\Microsoft\Office\16.0\Wef\`
2. 将 `manifest.xml` 复制到该目录
3. 重启 Word

**macOS：**
1. 打开 Finder，按 Cmd+Shift+G，输入：`~/Library/Containers/com.microsoft.Word/Data/Documents/wef/`
2. 将 `manifest.xml` 复制到该目录
3. 重启 Word

### 方式三：Web 浏览器版

无需安装任何插件，直接通过浏览器访问系统：

- 国内用户：https://app.reguverse.com/
- 国际用户：https://app.team-ra.org/

Web 版支持除「插入到 Word」之外的所有功能，生成的文档可直接下载为 Word 文件。

## 验证安装

安装成功后，在 Word 中应能看到「Reguverse」图标：

- **Windows/macOS**：在「Home / 开始」选项卡的右侧区域

点击图标即可打开 Reguverse 助手任务面板。

<!-- 截图占位：Word 中的 Reguverse 图标位置 -->

## 更新插件

插件会自动加载最新版本，通常无需手动更新。如果遇到功能异常：

1. 关闭 Word 所有窗口
2. 清除 Office 缓存：
   - Windows: 删除 `%LOCALAPPDATA%\Microsoft\Office\16.0\Wef\` 下的缓存文件
   - macOS: 删除 `~/Library/Containers/com.microsoft.Word/Data/Library/Caches/` 下的缓存
3. 重新打开 Word

## 常见问题

### 安装后看不到插件图标？

- 确认 Office 版本为 2019 或 Microsoft 365（不支持 Office 2016 及更早版本）
- 检查 manifest 文件是否放在正确目录
- 尝试完全退出 Word 并重新启动

### macOS 提示"无法验证开发者"？

右键点击安装脚本，选择「打开」，在弹出的对话框中再次点击「打开」即可。

### 插件加载缓慢？

首次加载可能需要几秒钟。如果持续缓慢，请检查网络连接是否正常。

## 下一步

- [注册与登录](./register) -- 在插件中创建账号
