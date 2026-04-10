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
  <li><strong>法规知识库</strong> -- 插件新增"法规库"标签页，支持浏览和搜索 EU MDR、FDA、NMPA 法规文档全文。可按法规框架、分类逐级浏览，内置全文阅读器。</li>
  <li><strong>测试环境</strong> -- 新增独立测试环境 (VPS-test)，所有新功能先在测试环境验证后再部署到生产环境，确保用户使用更稳定。</li>
</ul>

<h3>改进</h3>
<ul>
  <li><strong>前端托管迁移</strong> -- 插件前端现从 Cloudflare Pages (<code>app.team-ra.org</code>) 加载，取代之前的后端服务器托管，加快加载速度并确保用户始终使用最新版本。</li>
  <li><strong>安装包更新</strong> -- 下载安装包已更新为指向 Cloudflare 托管的前端，加载更快，自动获取最新界面。</li>
</ul>

<h3>已有用户注意事项</h3>

<div class="callout callout-warning">
  <strong>已安装用户需要操作</strong>
  <p>如果您在此更新之前安装了插件，可能看不到新的"法规库"标签页，因为本地 manifest 文件仍指向后端服务器上的旧版前端。</p>
  <p><strong>解决方法：</strong></p>
  <ol>
    <li>从<a href="/zh/contact">联系我们</a>页面重新下载最新安装包</li>
    <li>再次运行安装脚本（会自动覆盖旧的 manifest 文件）</li>
    <li>重启 Word</li>
  </ol>
  <p>您的账户、项目和所有数据均存储在服务器上，不会受到影响。此操作仅更新本地插件配置文件。</p>
</div>
</div>

<div class="section-block">
<h2>v0.2.0 <span class="release-date">2026-04-02</span></h2>

<h3>功能</h3>
<ul>
  <li><strong>临床评价工作流</strong> -- 8 步 AI 辅助临床评价流程（SSE 流式生成），包括文献搜索、筛选、评审和差距分析。</li>
  <li><strong>文档生成</strong> -- CEP、CER、DCR 文档生成并直接插入 Word。</li>
  <li><strong>用户注册与订阅</strong> -- 多路径注册（国内/国际、个人/企业）、订阅管理与支付集成。</li>
  <li><strong>AI 工具</strong> -- 按套餐等级可见的 AI 工具集合。</li>
  <li><strong>两步验证 (TOTP)</strong> -- 可选 2FA 及恢复码，增强账户安全。</li>
  <li><strong>实名认证（国内）</strong> -- 国内个人用户三要素实名认证。</li>
  <li><strong>企业认证与签约</strong> -- 统一社会信用代码校验、合同生成与管理员审核流程。</li>
</ul>
</div>

<div class="section-block">
<h2>v0.1.0 <span class="release-date">2026-03-15</span></h2>

<h3>首次发布</h3>
<ul>
  <li>Word 插件任务面板界面</li>
  <li>MCP Standards Server 法规数据查询</li>
  <li>LLM Proxy 多模型路由</li>
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
