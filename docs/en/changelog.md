---
layout: page
title: Changelog
---

<div class="changelog-page">

<div class="changelog-hero">
  <h1>Changelog</h1>
  <p class="hero-tagline">Reguverse Assistant release history and update notes</p>
</div>

<div class="section-block">
<h2>v0.3.0 <span class="release-date">2026-04-10</span></h2>

<h3>New Features</h3>
<ul>
  <li><strong>Regulatory Knowledge Base</strong> -- New "Regulations" tab in the plugin with full-text browsing and search across EU MDR, FDA, and NMPA regulatory documents. Browse by framework, category, and individual documents with built-in full-text reader.</li>
  <li><strong>Test Environment</strong> -- Added a staging environment (VPS-test) for feature validation before production deployment, ensuring higher stability for all users.</li>
</ul>

<h3>Improvements</h3>
<ul>
  <li><strong>Frontend hosting migration</strong> -- Plugin frontend now loads from Cloudflare Pages (<code>app.team-ra.org</code>) instead of the backend server, improving load times and ensuring users always get the latest version.</li>
  <li><strong>Installer updated</strong> -- The download package now points to the Cloudflare-hosted frontend for faster loading and automatic updates.</li>
</ul>

<h3>Important Notes for Existing Users</h3>

<div class="callout callout-warning">
  <strong>Action Required for Existing Users</strong>
  <p>If you installed the plugin before this update, the "Regulations" tab may not appear because your local manifest still points to an older frontend version hosted on the backend server.</p>
  <p><strong>To fix this:</strong></p>
  <ol>
    <li>Download the latest installer from the <a href="/en/contact">Contact page</a></li>
    <li>Run the installer again (it will overwrite the old manifest)</li>
    <li>Restart Word</li>
  </ol>
  <p>Your account, projects, and all data are stored on the server and will not be affected. This is only a local manifest update.</p>
</div>
</div>

<div class="section-block">
<h2>v0.2.0 <span class="release-date">2026-04-02</span></h2>

<h3>Features</h3>
<ul>
  <li><strong>Clinical Evaluation workflow</strong> -- 8-step AI-assisted clinical evaluation with SSE streaming, including literature search, screening, appraisal, and gap analysis.</li>
  <li><strong>Document generation</strong> -- CEP, CER, and DCR document generation with Word insertion.</li>
  <li><strong>User registration & subscription</strong> -- Multi-path registration (CN/international, personal/enterprise), subscription management, and payment integration.</li>
  <li><strong>AI Tools</strong> -- Curated AI tools with tier-based visibility.</li>
  <li><strong>Two-factor authentication (TOTP)</strong> -- Optional 2FA with recovery codes for account security.</li>
  <li><strong>Identity verification (CN)</strong> -- Three-element real-name verification for CN personal users.</li>
  <li><strong>Enterprise verification & contract signing</strong> -- USCC validation, contract generation, and admin review workflow.</li>
</ul>
</div>

<div class="section-block">
<h2>v0.1.0 <span class="release-date">2026-03-15</span></h2>

<h3>Initial Release</h3>
<ul>
  <li>Word Add-in with task pane interface</li>
  <li>MCP Standards Server for regulatory data queries</li>
  <li>LLM Proxy with multi-provider routing</li>
  <li>GSPR compliance analysis</li>
</ul>
</div>

</div>

<style>
.changelog-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
}

.changelog-hero {
  text-align: center;
  margin-bottom: 2.5rem;
  padding: 1.5rem 0;
}

.changelog-hero h1 {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  background: linear-gradient(135deg, var(--vp-c-brand-1), var(--vp-c-brand-2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-tagline {
  font-size: 1.1rem;
  color: var(--vp-c-text-2);
}

.section-block {
  margin-bottom: 2rem;
  padding: 1.5rem 2rem;
  background: var(--vp-c-bg-soft);
  border-radius: 12px;
  border: 1px solid var(--vp-c-divider);
}

.section-block h2 {
  font-size: 1.4rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: var(--vp-c-text-1);
  border-bottom: 2px solid var(--vp-c-brand-1);
  padding-bottom: 0.5rem;
  display: flex;
  align-items: baseline;
  gap: 0.75rem;
}

.release-date {
  font-size: 0.85rem;
  font-weight: 400;
  color: var(--vp-c-text-3);
}

.section-block h3 {
  font-size: 1.05rem;
  font-weight: 600;
  margin-top: 1rem;
  margin-bottom: 0.5rem;
  color: var(--vp-c-text-1);
}

.section-block ul, .section-block ol {
  padding-left: 1.25rem;
}

.section-block li {
  color: var(--vp-c-text-2);
  line-height: 1.7;
  margin-bottom: 0.3rem;
}

.callout {
  margin: 1rem 0;
  padding: 1rem 1.25rem;
  border-radius: 8px;
  border-left: 4px solid;
}

.callout-warning {
  background: rgba(234, 179, 8, 0.08);
  border-color: #eab308;
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
</style>
