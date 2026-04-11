---
layout: page
title: Get Started
---

<div class="getstarted-page">

<div class="getstarted-hero">
  <h1>Get Started</h1>
  <p class="hero-tagline">Download and install Reguverse Assistant for Microsoft Word</p>
</div>

<div class="section-block">
<h2>Download</h2>

<p>Choose the version that matches your region for optimal speed. Both versions connect to the same backend and your account works on either.</p>

<div class="download-grid">

<div class="download-card">
  <div class="card-badge">International</div>
  <h3>International Version</h3>
  <p>Hosted on US servers. Best for users outside mainland China.</p>
  <a href="/downloads/ReguverseAssistant-Installer.zip" class="download-btn" onclick="try{navigator.sendBeacon('https://llm.team-ra.org/api/v1/track/download',new Blob([JSON.stringify({event:'download',source:'installer',version:'intl',lang:'en',ts:Date.now()})],{type:'text/plain'}))}catch(e){}">Download (International)</a>
  <span class="download-meta">Frontend: app.team-ra.org</span>
</div>

<div class="download-card card-cn">
  <div class="card-badge badge-cn">China Optimized</div>
  <h3>China Version</h3>
  <p>Hosted on Alibaba Cloud (Hangzhou). Best for mainland China users.</p>
  <a href="/downloads/ReguverseAssistant-CN-Installer.zip" class="download-btn btn-cn" onclick="try{navigator.sendBeacon('https://llm.team-ra.org/api/v1/track/download',new Blob([JSON.stringify({event:'download',source:'installer',version:'cn',lang:'en',ts:Date.now()})],{type:'text/plain'}))}catch(e){}">Download (China)</a>
  <span class="download-meta">Frontend: app.reguverse.com</span>
</div>

</div>

<span class="download-version">Current version: v0.3.0 (2026-04-10) &middot; <a href="/en/changelog">View changelog</a></span>
</div>

<div class="section-block">
<h2>Installation</h2>

<h3>Windows</h3>
<ol>
  <li>Unzip the downloaded file</li>
  <li>Double-click <code>install.bat</code> (or right-click <code>install.ps1</code> and select "Run with PowerShell")</li>
  <li><strong>Close ALL Word windows</strong>, then re-open Word</li>
  <li>Go to <strong>Home &gt; Add-ins</strong> (or <strong>Insert &gt; My Add-ins</strong>)</li>
  <li>Click the <strong>"SHARED FOLDER"</strong> tab at the top</li>
  <li>Select <strong>"Reguverse Assistant"</strong> and click <strong>"Add"</strong></li>
</ol>

<h3>macOS</h3>
<ol>
  <li>Unzip the downloaded file</li>
  <li>Open Terminal, navigate to the unzipped folder</li>
  <li>Run: <code>bash install.sh</code></li>
  <li><strong>Close ALL Word windows</strong>, then re-open Word</li>
  <li>Go to <strong>Insert &gt; My Add-ins</strong></li>
  <li>Select <strong>"Reguverse Assistant"</strong></li>
</ol>

<div class="callout callout-info">
  <strong>Switching Versions</strong>
  <p>To switch between International and China versions:</p>
  <ol>
    <li>Run the <strong>uninstall</strong> script from your current version's folder</li>
    <li>Close ALL Word windows</li>
    <li>Run the <strong>install</strong> script from the new version's folder</li>
    <li>Re-open Word</li>
  </ol>
</div>
</div>

<div class="section-block">
<h2>Troubleshooting</h2>

<h3>"SHARED FOLDER" tab is empty (Windows)</h3>
<ol>
  <li>Close <strong>ALL</strong> Office applications (Word, Excel, Outlook, etc.)</li>
  <li>Run the installer again</li>
  <li>Re-open Word and check the Add-ins dialog</li>
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
<p>All users get a <strong>72-hour free trial</strong> with full feature access upon registration. No invite code required.</p>
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
