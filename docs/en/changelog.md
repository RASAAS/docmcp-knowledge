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
  <li><strong>Regulatory Knowledge Base</strong> -- New "Regulations" tab with full-text browsing and search across EU MDR, FDA, and NMPA regulatory documents, with built-in reader.</li>
  <li><strong>Performance improvements</strong> -- Faster plugin loading and smoother interface responsiveness.</li>
</ul>

<h3>Important Notes for Existing Users</h3>

<div class="callout callout-warning">
  <strong>Action Required for Existing Users</strong>
  <p>If the "Regulations" tab does not appear after updating, please re-download and re-install:</p>
  <ol>
    <li>Download the latest installer from the <a href="/en/contact">Contact page</a></li>
    <li>Run the installer (overwrites old configuration)</li>
    <li>Restart Word</li>
  </ol>
  <p>Your account and data are not affected.</p>
</div>
</div>

<div class="section-block">
<h2>v0.2.0 <span class="release-date">2026-04-02</span></h2>

<h3>Features</h3>
<ul>
  <li><strong>Clinical Evaluation workflow</strong> -- AI-assisted clinical evaluation covering literature search, screening, appraisal, and gap analysis.</li>
  <li><strong>Document generation</strong> -- CEP, CER, and DCR document generation with direct Word insertion.</li>
  <li><strong>User & subscription management</strong> -- Registration, subscription, and payment features.</li>
  <li><strong>AI Tools</strong> -- Built-in AI-powered tool suite.</li>
  <li><strong>Account security</strong> -- Two-factor authentication (TOTP) and identity verification (CN users).</li>
  <li><strong>Enterprise verification & contract signing</strong> -- Enterprise qualification verification and contract workflow.</li>
</ul>
</div>

<div class="section-block">
<h2>v0.1.0 <span class="release-date">2026-03-15</span></h2>

<h3>Initial Release</h3>
<ul>
  <li>Word Add-in interface</li>
  <li>Regulatory and standards data queries</li>
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
