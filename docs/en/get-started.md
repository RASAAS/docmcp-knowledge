---
layout: page
title: Get Started
---

<div class="getstarted-page">

<div class="getstarted-hero">
  <h1>Get Started</h1>
  <p class="hero-tagline">AI-powered regulatory intelligence platform for medical devices</p>
</div>

<div class="section-block" style="border-color: var(--vp-c-brand-1); border-width: 2px;">
<h2>Web Version -- No Installation Required</h2>
<p>Use all features directly in your browser without installing any plugin. Generated documents can be downloaded as standard Word files (.docx) with formatting identical to the Word plugin output.</p>
<div style="text-align:center; margin: 1.25rem 0 0.5rem;">
  <a class="download-btn" href="https://app.team-ra.org" target="_blank" style="font-size:1.05rem; padding: 0.75rem 2.5rem;">Use Web Version</a>
  <a class="download-btn btn-cn" href="https://app.reguverse.com" target="_blank" style="font-size:1.05rem; padding: 0.75rem 2.5rem; margin-left: 0.75rem;">China Version</a>
</div>
<p style="text-align:center; font-size:0.85rem; color:var(--vp-c-text-3); margin-top:0.25rem;">Recommended: Chrome, Edge, or Safari</p>
</div>

<div class="section-block">
<h2>Word Plugin Download</h2>

<p>Install the Word plugin for deep integration with Microsoft Word: insert AI-generated content directly into your document, use AI tools (such as translation) to process document content, and access upcoming features for intelligent analysis and processing of selected text within Word -- capabilities not available in the web version.</p>

<div class="callout callout-warning">
  <strong>System Requirement</strong>
  <p>The Word plugin requires <strong>Microsoft 365 (Office 365)</strong> or <strong>Word 2016 or later</strong>. Older Office versions (2013 and earlier) do not support Web Add-ins. If your Office version is too old or you don't have Word installed, use the web version above.</p>
</div>

<p>Choose the version that matches your region and operating system. Both versions connect to the same backend and your account works on either.</p>

<div class="download-grid">

<div class="download-card">
  <div class="card-badge">International</div>
  <h3>International Version</h3>
  <p>Best for users outside mainland China.</p>
  <div class="dl-os-btns">
    <a href="/downloads/ReguverseAssistant-Windows.zip" class="download-btn" onclick="try{navigator.sendBeacon('https://llm.team-ra.org/api/v1/track/download',new Blob([JSON.stringify({event:'download',source:'installer',version:'intl',os:'windows',lang:'en',ts:Date.now()})],{type:'text/plain'}))}catch(e){}">Windows</a>
    <a href="/downloads/ReguverseAssistant-macOS.zip" class="download-btn download-btn-outline" onclick="try{navigator.sendBeacon('https://llm.team-ra.org/api/v1/track/download',new Blob([JSON.stringify({event:'download',source:'installer',version:'intl',os:'macos',lang:'en',ts:Date.now()})],{type:'text/plain'}))}catch(e){}">macOS</a>
  </div>
</div>

<div class="download-card card-cn">
  <div class="card-badge badge-cn">China Optimized</div>
  <h3>China Version</h3>
  <p>Best for mainland China users.</p>
  <div class="dl-os-btns">
    <a href="/downloads/ReguverseAssistant-CN-Windows.zip" class="download-btn btn-cn" onclick="try{navigator.sendBeacon('https://llm.team-ra.org/api/v1/track/download',new Blob([JSON.stringify({event:'download',source:'installer',version:'cn',os:'windows',lang:'en',ts:Date.now()})],{type:'text/plain'}))}catch(e){}">Windows</a>
    <a href="/downloads/ReguverseAssistant-CN-macOS.zip" class="download-btn btn-cn-outline" onclick="try{navigator.sendBeacon('https://llm.team-ra.org/api/v1/track/download',new Blob([JSON.stringify({event:'download',source:'installer',version:'cn',os:'macos',lang:'en',ts:Date.now()})],{type:'text/plain'}))}catch(e){}">macOS</a>
  </div>
</div>

</div>

<span class="download-version">Current version: v0.4.0 (2026-04-22) &middot; <a href="/en/changelog">View changelog</a></span>
</div>

<div class="section-block">
<h2>Installation</h2>

<h3>Step 1: Extract the Installation Package (Windows)</h3>
<p>After downloading, right-click the ZIP file and select <strong>"Extract All"</strong>. Open the extracted folder and you will see the following files:</p>
<div class="guide-img"><img src="/images/install-guide/00-win-unzip.png" alt="Extracted installation files"></div>
<p><strong>install.bat</strong> is the installer script, and <strong>cleanup-old-install.bat</strong> is used to remove previous installations.</p>

<h3>Step 2: Run the Installer</h3>
<ol>
  <li>Double-click <strong>install.bat</strong> to run the installer. A cmd window will appear</li>
  <li>Wait for installation to complete. Press any key to close the window after seeing "Installation complete!"</li>
</ol>
<div class="guide-img"><img src="/images/install-guide/01-install-bat.png" alt="install.bat running"></div>
<div class="callout callout-warning">
  <strong>Important</strong>
  <p>After installation, you must <strong>close ALL Word windows</strong> and then re-open Word.</p>
</div>

<h3>Step 3: Open Reguverse Assistant in Word</h3>
<ol>
  <li>Open Word, click the <strong>Home</strong> tab</li>
  <li>Find the <strong>Add-ins</strong> button on the far right of the ribbon and click it</li>
  <li>In the dropdown panel, find <strong>Reguverse...</strong> under the <strong>Developer Add-ins</strong> section</li>
  <li>Click the Reguverse icon to open the assistant sidebar</li>
</ol>
<div class="guide-img"><img src="/images/install-guide/02-home-addins-button.png" alt="Add-ins button on the Home tab"></div>

<p style="margin-top:1.2rem;">If you can't find the Add-ins button on the Home tab, you need to enable the Add-ins tab manually:</p>
<ol>
  <li>Click <strong>File</strong> &gt; <strong>Options</strong></li>
</ol>
<div class="guide-img"><img src="/images/install-guide/03-file-options.png" alt="Open Word Options"></div>

<ol start="2">
  <li>In the left panel select <strong>Customize Ribbon</strong>, then check <strong>Add-ins</strong> in the right-side list</li>
</ol>
<div class="guide-img"><img src="/images/install-guide/04-customize-ribbon.png" alt="Customize Ribbon settings"></div>

<ol start="3">
  <li>Click <strong>OK</strong> to save</li>
  <li>Now the <strong>Add-ins</strong> tab will appear in the ribbon. Click it to see the <strong>Reguverse Assistant</strong> button, which will load the add-in into the toolbar and open the panel</li>
</ol>
<div class="guide-img"><img src="/images/install-guide/05-addins-tab.png" alt="Reguverse Assistant in the Add-ins tab"></div>

<h3>macOS Installation</h3>
<p>Locate the installer folder (e.g. <code>reguverse-assistant</code>), right-click and select <strong>"New Terminal at Folder"</strong></p>
<div class="guide-img"><img src="/images/install-guide/06-macos.png" alt="Open terminal on macOS"></div>

<p>Run the command:</p>
<p><code>bash install.sh</code></p>
<div class="guide-img"><img src="/images/install-guide/07-command.png" alt="Run install command"></div>

<p>After installation, open Word. The Add-ins button usually appears automatically on the Home tab. If not, follow the Add-ins tab setup instructions above.</p>

<div class="callout callout-info">
  <strong>Upgrading or Switching Versions</strong>
  <p>If you have a previous version installed, run <code>cleanup-old-install.bat</code> (included in the ZIP root) first to remove old installations, then run the new version's <code>install.bat</code>.</p>
  <ol>
    <li>Double-click <code>cleanup-old-install.bat</code> (in the ZIP root folder)</li>
    <li>Close ALL Word windows</li>
    <li>Run <code>install.bat</code> from the new version's folder</li>
    <li>Re-open Word</li>
  </ol>
</div>
</div>

<div class="section-block">
<h2>Troubleshooting</h2>

<h3>Add-in not appearing after install (Windows)</h3>
<ol>
  <li>Close <strong>ALL</strong> Office applications (Word, Excel, Outlook, etc.)</li>
  <li>Run <code>cleanup-old-install.bat</code> to remove any old installation remnants</li>
  <li>Run the installer again</li>
  <li>Re-open Word and check <strong>Home &gt; Add-ins</strong></li>
</ol>

<h3>Add-in shows old version</h3>
<ol>
  <li>Close ALL Word windows</li>
  <li>Open File Explorer and navigate to:<br><code>%LOCALAPPDATA%\Microsoft\Office\16.0\Wef\</code></li>
  <li>Delete the <code>webextensions</code> folder if it exists</li>
  <li>Run the installer again and restart Word</li>
</ol>

<h3>macOS: add-in not appearing</h3>
<p>Make sure the <code>wef</code> directory exists:</p>
<p><code>~/Library/Containers/com.microsoft.Word/Data/Documents/wef/</code></p>
<p>If not, re-run the install script.</p>
</div>

<div class="section-block">
<h2>System Requirements</h2>
<ul>
  <li><strong>Microsoft Word</strong>: Desktop version (Windows or macOS). Microsoft 365 or Office 2016+.</li>
  <li><strong>Internet connection</strong>: Required for AI features and regulatory data access.</li>
  <li>Word for the web is not currently supported.</li>
</ul>
</div>

<div class="section-block">
<h2>Free Trial</h2>
<p>All users get a <strong>1-month free trial</strong> with full feature access upon registration. No invite code required. Both the web version and Word plugin are available during the trial.</p>
<p>After the trial, choose a plan on the <a href="/en/contact">pricing page</a>.</p>
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
