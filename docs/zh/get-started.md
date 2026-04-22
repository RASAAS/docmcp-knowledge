---
layout: page
title: 快速开始
---

<div class="getstarted-page">

<div class="getstarted-hero">
  <h1>快速开始</h1>
  <p class="hero-tagline">AI 驱动的医疗器械法规智能平台</p>
</div>

<div class="section-block" style="border-color: var(--vp-c-brand-1); border-width: 2px;">
<h2>网页版 -- 无需安装，浏览器直接使用</h2>
<p>无需安装任何插件，打开浏览器即可使用全部功能。生成的文档支持一键下载为标准 Word 格式（.docx），排版与 Word 插件效果完全一致。</p>
<div style="text-align:center; margin: 1.25rem 0 0.5rem;">
  <a class="download-btn btn-cn" href="https://app.reguverse.com" target="_blank" style="font-size:1.05rem; padding: 0.75rem 2.5rem;">立即使用网页版</a>
  <a class="download-btn" href="https://app.team-ra.org" target="_blank" style="font-size:1.05rem; padding: 0.75rem 2.5rem; margin-left: 0.75rem;">International Version</a>
</div>
<p style="text-align:center; font-size:0.85rem; color:var(--vp-c-text-3); margin-top:0.25rem;">推荐使用 Chrome、Edge 或 Safari 浏览器</p>
</div>

<div class="section-block">
<h2>Word 插件下载</h2>

<p>安装 Word 插件后，您可以直接在 Word 中使用全部功能：AI 生成内容一键插入当前文档、使用翻译等 AI 工具处理文档内容，以及后续即将推出的对 Word 中选中内容进行智能分析和处理等高级功能。这些与 Word 深度集成的能力在网页版中无法实现。</p>

<div class="callout callout-warning">
  <strong>系统要求</strong>
  <p>Word 插件需要 <strong>Microsoft 365（Office 365）</strong> 或 <strong>Word 2016 及以上版本</strong>。旧版 Office（2013 及更早）不支持 Web 加载项。如果您的 Office 版本较低或未安装 Word，请直接使用上方网页版。</p>
</div>

<p>请根据您的所在地区和操作系统选择对应安装包。两个版本使用相同的后端服务，您的账户在两个版本之间通用。</p>

<div class="download-grid">

<div class="download-card card-cn">
  <div class="card-badge badge-cn">推荐</div>
  <h3>国内版</h3>
  <p>适合中国大陆用户使用。</p>
  <div class="dl-os-btns">
    <a href="/downloads/ReguverseAssistant-CN-Windows.zip" class="download-btn btn-cn" onclick="try{navigator.sendBeacon('https://llm.team-ra.org/api/v1/track/download',new Blob([JSON.stringify({event:'download',source:'installer',version:'cn',os:'windows',lang:'zh',ts:Date.now()})],{type:'text/plain'}))}catch(e){}">Windows 下载</a>
    <a href="/downloads/ReguverseAssistant-CN-macOS.zip" class="download-btn btn-cn-outline" onclick="try{navigator.sendBeacon('https://llm.team-ra.org/api/v1/track/download',new Blob([JSON.stringify({event:'download',source:'installer',version:'cn',os:'macos',lang:'zh',ts:Date.now()})],{type:'text/plain'}))}catch(e){}">macOS 下载</a>
  </div>
</div>

<div class="download-card">
  <div class="card-badge">International</div>
  <h3>国际版</h3>
  <p>适合中国大陆以外的用户。</p>
  <div class="dl-os-btns">
    <a href="/downloads/ReguverseAssistant-Windows.zip" class="download-btn" onclick="try{navigator.sendBeacon('https://llm.team-ra.org/api/v1/track/download',new Blob([JSON.stringify({event:'download',source:'installer',version:'intl',os:'windows',lang:'zh',ts:Date.now()})],{type:'text/plain'}))}catch(e){}">Windows 下载</a>
    <a href="/downloads/ReguverseAssistant-macOS.zip" class="download-btn download-btn-outline" onclick="try{navigator.sendBeacon('https://llm.team-ra.org/api/v1/track/download',new Blob([JSON.stringify({event:'download',source:'installer',version:'intl',os:'macos',lang:'zh',ts:Date.now()})],{type:'text/plain'}))}catch(e){}">macOS 下载</a>
  </div>
</div>

</div>

<span class="download-version">当前版本: v0.4.0 (2026-04-22) &middot; <a href="/zh/changelog">查看更新日志</a></span>
</div>

<div class="section-block">
<h2>安装步骤</h2>

<h3>第一步：解压安装包 (Windows)</h3>
<p>下载完成后，右键点击压缩包选择 <strong>"全部解压缩"</strong>，解压后打开文件夹，您将看到如下文件：</p>
<div class="guide-img"><img src="/images/install-guide/00-win-unzip.png" alt="解压后的安装文件"></div>
<p>其中 <strong>install.bat</strong> 为安装脚本，<strong>cleanup-old-install.bat</strong> 用于清理旧版本安装。</p>

<h3>第二步：运行安装程序</h3>
<ol>
  <li>双击 <strong>install.bat</strong> 运行安装程序，系统将弹出 cmd 黑色窗口</li>
  <li>等待安装完成，看到 "Installation complete!" 提示后按任意键关闭窗口</li>
</ol>
<div class="guide-img"><img src="/images/install-guide/01-install-bat.png" alt="install.bat 运行界面"></div>
<div class="callout callout-warning">
  <strong>重要</strong>
  <p>安装完成后，必须<strong>关闭所有 Word 窗口</strong>，然后重新打开 Word。</p>
</div>

<h3>第三步：在 Word 中打开 Reguverse Assistant</h3>
<ol>
  <li>打开 Word，点击 <strong>Home（开始）</strong> 标签页</li>
  <li>在功能区最右侧找到 <strong>Add-ins（加载项）</strong> 按钮，点击它</li>
  <li>在下拉面板中，找到 <strong>Developer Add-ins</strong> 区域下的 <strong>Reguverse...</strong> 图标</li>
  <li>点击 Reguverse 图标即可打开助手侧边栏</li>
</ol>
<div class="guide-img"><img src="/images/install-guide/02-home-addins-button.png" alt="Home 标签页的 Add-ins 按钮"></div>

<p style="margin-top:1.2rem;">如果在 Home 标签页找不到 Add-ins 按钮，需要手动启用 Add-ins 标签页：</p>
<ol>
  <li>点击 <strong>文件 (File)</strong> &gt; <strong>选项 (Options)</strong></li>
</ol>
<div class="guide-img"><img src="/images/install-guide/03-file-options.png" alt="打开 Word 选项"></div>

<ol start="2">
  <li>在弹出的窗口中左侧选择 <strong>自定义功能区 (Customize Ribbon)</strong>，在右侧列表中找到 <strong>加载项 (Add-ins)</strong> 并勾选</li>
</ol>
<div class="guide-img"><img src="/images/install-guide/04-customize-ribbon.png" alt="选择自定义功能区"></div>

<ol start="3">
  <li>点击 <strong>确定 (OK)</strong> 保存设置</li>
  <li>现在功能区会出现 <strong>Add-ins</strong> 标签页，点击它就能看到 <strong>Reguverse Assistant</strong> 按钮，点击后会加载到工具栏内，同时打开插件面板</li>
</ol>
<div class="guide-img"><img src="/images/install-guide/05-addins-tab.png" alt="Add-ins 标签页中的 Reguverse Assistant"></div>

<h3>macOS 用户安装</h3>
<p>找到安装包目录（如 <code>reguverse-assistant-cn</code>），右键并在弹出菜单中选择 <strong>"新建位于文件夹位置的终端窗口"</strong></p>
<div class="guide-img"><img src="/images/install-guide/06-macos.png" alt="macOS 打开终端"></div>

<p>运行命令：</p>
<p><code>bash install.sh</code></p>
<div class="guide-img"><img src="/images/install-guide/07-command.png" alt="运行安装命令"></div>

<p>安装后打开 Word，加载项按钮通常会自动出现在 Home 标签页功能区的 Add-ins。如未出现，参考上述 Word 加载项的设置。</p>

<div class="callout callout-info">
  <strong>从旧版本升级或切换版本</strong>
  <p>如果您之前安装过旧版本的插件，请先运行压缩包中的 <code>cleanup-old-install.bat</code> 清理旧安装，然后再运行新版本的 <code>install.bat</code>。</p>
  <ol>
    <li>双击运行 <code>cleanup-old-install.bat</code>（位于压缩包根目录）</li>
    <li>关闭所有 Word 窗口</li>
    <li>运行新版本文件夹中的 <code>install.bat</code></li>
    <li>重新打开 Word</li>
  </ol>
</div>
</div>

<div class="section-block">
<h2>常见问题</h2>

<h3>安装后插件未出现 (Windows)</h3>
<ol>
  <li>确认已<strong>关闭所有</strong> Office 应用（Word、Excel、Outlook 等）后再重新打开</li>
  <li>如仍未出现，运行 <code>cleanup-old-install.bat</code> 清理所有旧安装残留</li>
  <li>重新运行 <code>install.bat</code>，关闭并重新打开 Word</li>
</ol>

<h3>插件显示旧版本</h3>
<ol>
  <li>关闭所有 Word 窗口</li>
  <li>打开文件资源管理器，定位到：<br><code>%LOCALAPPDATA%\Microsoft\Office\16.0\Wef\</code></li>
  <li>删除 <code>webextensions</code> 文件夹（如果存在）</li>
  <li>重新运行安装脚本并重启 Word</li>
</ol>

<h3>macOS: 插件未出现</h3>
<p>确认以下目录存在：</p>
<p><code>~/Library/Containers/com.microsoft.Word/Data/Documents/wef/</code></p>
<p>如不存在，请重新运行安装脚本。</p>
</div>

<div class="section-block">
<h2>系统要求</h2>
<ul>
  <li><strong>Microsoft Word</strong>：桌面版（Windows 或 macOS），需 Microsoft 365 或 Office 2016 及以上版本。</li>
  <li><strong>网络连接</strong>：AI 功能和法规数据访问需要联网。</li>
  <li>暂不支持 Word 网页版。</li>
</ul>
</div>

<div class="section-block">
<h2>免费试用</h2>
<p>所有用户注册后即可获得 <strong>1 个月免费试用</strong>，体验全部功能，无需邀请码。网页版和 Word 插件均可使用。</p>
<p>试用期满后可在<a href="/zh/contact">套餐方案</a>页面选择合适的套餐升级。</p>
</div>

</div>

<style>
.getstarted-page {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
}

.getstarted-hero {
  text-align: center;
  margin-bottom: 3rem;
  padding: 2rem 0;
}

.getstarted-hero h1 {
  font-size: 2.5rem;
  font-weight: 700;
  line-height: 1.3;
  margin-bottom: 0.75rem;
  background: linear-gradient(135deg, var(--vp-c-brand-1), var(--vp-c-brand-2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-tagline {
  font-size: 1.15rem;
  color: var(--vp-c-text-2);
}

.section-block {
  margin-bottom: 2.5rem;
  padding: 1.5rem 2rem;
  background: var(--vp-c-bg-soft);
  border-radius: 12px;
  border: 1px solid var(--vp-c-divider);
}

.section-block h2 {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: var(--vp-c-text-1);
  border-bottom: 2px solid var(--vp-c-brand-1);
  padding-bottom: 0.5rem;
}

.section-block h3 {
  font-size: 1.15rem;
  font-weight: 600;
  margin-top: 1.25rem;
  margin-bottom: 0.5rem;
}

.section-block p,
.section-block li {
  color: var(--vp-c-text-2);
  line-height: 1.7;
}

.section-block code {
  background: var(--vp-c-bg-mute);
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 0.9em;
}

.download-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.25rem;
  margin: 1.5rem 0;
}

.download-card {
  background: var(--vp-c-bg);
  border: 2px solid var(--vp-c-divider);
  border-radius: 12px;
  padding: 1.75rem;
  text-align: center;
  position: relative;
}

.download-card h3 {
  margin-top: 0.5rem;
}

.card-badge {
  display: inline-block;
  background: var(--vp-c-brand-1);
  color: white;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 3px 12px;
  border-radius: 10px;
}

.badge-cn {
  background: #e74c3c;
}

.card-cn {
  border-color: #e74c3c;
}

.download-btn {
  display: inline-block;
  padding: 0.7rem 1.75rem;
  background: var(--vp-c-brand-1);
  color: white !important;
  font-size: 1rem;
  font-weight: 700;
  border-radius: 8px;
  text-decoration: none !important;
  transition: background 0.2s, box-shadow 0.2s;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  margin: 1rem 0 0.5rem;
}

.download-btn:hover {
  background: var(--vp-c-brand-2);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

.btn-cn {
  background: #e74c3c;
}

.btn-cn:hover {
  background: #c0392b;
}

.download-btn-outline {
  background: transparent !important;
  color: var(--vp-c-brand-1) !important;
  border: 2px solid var(--vp-c-brand-1);
  box-shadow: none;
}
.download-btn-outline:hover {
  background: var(--vp-c-brand-1) !important;
  color: white !important;
}

.btn-cn-outline {
  background: transparent !important;
  color: #e74c3c !important;
  border: 2px solid #e74c3c;
  box-shadow: none;
}
.btn-cn-outline:hover {
  background: #e74c3c !important;
  color: white !important;
}

.dl-os-btns {
  display: flex;
  gap: 8px;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 0.5rem;
}
.dl-os-btns .download-btn {
  font-size: 0.9rem;
  padding: 0.55rem 1.25rem;
  margin: 0;
}

.download-meta {
  display: block;
  font-size: 0.8rem;
  color: var(--vp-c-text-3);
  margin-top: 0.25rem;
}

.download-version {
  display: block;
  text-align: center;
  font-size: 0.85rem;
  color: var(--vp-c-text-3);
  margin-top: 0.5rem;
}

.download-version a {
  color: var(--vp-c-brand-1);
  text-decoration: none;
}

.download-version a:hover {
  text-decoration: underline;
}

.callout {
  margin: 1rem 0;
  padding: 1rem 1.25rem;
  border-radius: 8px;
  border-left: 4px solid;
}

.callout-info {
  background: rgba(59, 130, 246, 0.08);
  border-color: #3b82f6;
}

.callout strong {
  display: block;
  margin-bottom: 0.5rem;
  color: var(--vp-c-text-1);
}

.callout p {
  color: var(--vp-c-text-2);
  line-height: 1.6;
  margin: 0.4rem 0;
}

.callout ol {
  margin: 0.5rem 0;
  padding-left: 1.25rem;
}

.callout li {
  color: var(--vp-c-text-2);
  line-height: 1.6;
}

.guide-img {
  margin: 1rem 0 1.5rem;
  text-align: center;
}
.guide-img img {
  max-width: 100%;
  border-radius: 8px;
  border: 1px solid var(--vp-c-divider);
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.callout-warning {
  background: rgba(234, 179, 8, 0.08);
  border-color: #eab308;
}

@media (max-width: 640px) {
  .download-grid {
    grid-template-columns: 1fr;
  }
}
</style>
