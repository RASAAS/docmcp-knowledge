---
layout: page
title: 快速开始
---

<div class="getstarted-page">

<div class="getstarted-hero">
  <h1>快速开始</h1>
  <p class="hero-tagline">下载并安装 Reguverse 助手 Microsoft Word 插件</p>
</div>

<div class="section-block">
<h2>下载</h2>

<p>请根据您的所在地区选择对应版本以获得最佳访问速度。两个版本使用相同的后端服务，您的账户在两个版本之间通用。</p>

<div class="download-grid">

<div class="download-card card-cn">
  <div class="card-badge badge-cn">推荐</div>
  <h3>国内版</h3>
  <p>适合中国大陆用户使用。</p>
  <a href="/downloads/ReguverseAssistant-CN-Installer.zip" class="download-btn btn-cn" onclick="try{navigator.sendBeacon('https://llm.team-ra.org/api/v1/track/download',new Blob([JSON.stringify({event:'download',source:'installer',version:'cn',lang:'zh',ts:Date.now()})],{type:'text/plain'}))}catch(e){}">下载国内版</a>
</div>

<div class="download-card">
  <div class="card-badge">International</div>
  <h3>国际版</h3>
  <p>适合中国大陆以外的用户。</p>
  <a href="/downloads/ReguverseAssistant-Installer.zip" class="download-btn" onclick="try{navigator.sendBeacon('https://llm.team-ra.org/api/v1/track/download',new Blob([JSON.stringify({event:'download',source:'installer',version:'intl',lang:'zh',ts:Date.now()})],{type:'text/plain'}))}catch(e){}">下载国际版</a>
</div>

</div>

<span class="download-version">当前版本: v0.3.0 (2026-04-10) &middot; <a href="/zh/changelog">查看更新日志</a></span>
</div>

<div class="section-block">
<h2>安装步骤</h2>

<h3>Windows</h3>
<ol>
  <li>解压下载的压缩包</li>
  <li>双击运行 <code>install.bat</code>（或右键 <code>install.ps1</code> 选择"使用 PowerShell 运行"）</li>
  <li><strong>关闭所有 Word 窗口</strong>，然后重新打开 Word</li>
  <li>点击 <strong>开始 &gt; 加载项</strong>（或 <strong>插入 &gt; 我的加载项</strong>）</li>
  <li>点击顶部的 <strong>"共享文件夹"</strong> 标签</li>
  <li>选择 <strong>"Reguverse Assistant"</strong>，点击 <strong>"添加"</strong></li>
</ol>

<h3>macOS</h3>
<ol>
  <li>解压下载的压缩包</li>
  <li>打开终端 (Terminal)，进入解压后的文件夹</li>
  <li>运行: <code>bash install.sh</code></li>
  <li><strong>关闭所有 Word 窗口</strong>，然后重新打开 Word</li>
  <li>点击 <strong>插入 &gt; 我的加载项</strong></li>
  <li>选择 <strong>"Reguverse Assistant"</strong></li>
</ol>

<div class="callout callout-info">
  <strong>切换版本</strong>
  <p>如需在国内版和国际版之间切换：</p>
  <ol>
    <li>运行当前版本文件夹中的 <strong>卸载脚本</strong>（uninstall）</li>
    <li>关闭所有 Word 窗口</li>
    <li>运行新版本文件夹中的 <strong>安装脚本</strong>（install）</li>
    <li>重新打开 Word</li>
  </ol>
</div>
</div>

<div class="section-block">
<h2>常见问题</h2>

<h3>"共享文件夹" 标签页为空 (Windows)</h3>
<ol>
  <li>关闭 <strong>所有</strong> Office 应用（Word、Excel、Outlook 等）</li>
  <li>重新运行安装脚本</li>
  <li>打开 Word 并再次检查加载项对话框</li>
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
<p>所有用户注册后即可获得 <strong>72 小时免费试用</strong>，体验全部功能，无需邀请码。</p>
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

@media (max-width: 640px) {
  .download-grid {
    grid-template-columns: 1fr;
  }
}
</style>
