---
layout: page
title: 更新日志
---

<div class="changelog-page">

<div class="changelog-hero">
  <h1>更新日志</h1>
  <p class="hero-tagline">Reguverse 助手版本更新记录与注意事项</p>
</div>

<div class="section-block">
<h2>v0.3.0 <span class="release-date">2026-04-10</span></h2>

<h3>新功能</h3>
<ul>
  <li><strong>法规知识库</strong> -- 新增"法规库"标签页，支持浏览和搜索 EU MDR、FDA、NMPA 法规文档全文，内置全文阅读器。</li>
  <li><strong>性能优化</strong> -- 提升插件加载速度，界面响应更流畅。</li>
</ul>

<h3>已有用户注意事项</h3>

<div class="callout callout-warning">
  <strong>已安装用户需要操作</strong>
  <p>如果更新后未看到"法规库"标签页，请重新下载安装包并运行安装脚本：</p>
  <ol>
    <li>从<a href="/zh/contact">联系我们</a>页面下载最新安装包</li>
    <li>运行安装脚本（自动覆盖旧配置）</li>
    <li>重启 Word</li>
  </ol>
  <p>您的账户和数据不受影响。</p>
</div>
</div>

<div class="section-block">
<h2>v0.2.0 <span class="release-date">2026-04-02</span></h2>

<h3>功能</h3>
<ul>
  <li><strong>临床评价工作流</strong> -- AI 辅助临床评价，涵盖文献搜索、筛选、评审和差距分析。</li>
  <li><strong>文档生成</strong> -- 支持 CEP、CER、DCR 文档生成并直接插入 Word。</li>
  <li><strong>用户与订阅管理</strong> -- 注册、订阅和支付功能。</li>
  <li><strong>AI 工具</strong> -- 内置 AI 辅助工具集。</li>
  <li><strong>账户安全</strong> -- 两步验证 (TOTP)、实名认证（国内用户）。</li>
  <li><strong>企业认证与签约</strong> -- 企业资质验证与合同签约流程。</li>
</ul>
</div>

<div class="section-block">
<h2>v0.1.0 <span class="release-date">2026-03-15</span></h2>

<h3>首次发布</h3>
<ul>
  <li>Word 插件基础界面</li>
  <li>法规与标准数据查询</li>
  <li>GSPR 合规分析</li>
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
  margin-bottom: 3rem;
  padding: 2rem 0;
}

.changelog-hero h1 {
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
