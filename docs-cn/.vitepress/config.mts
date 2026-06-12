import { defineConfig } from "vitepress";

export default defineConfig({
  title: "Reguverse 助手",
  description: "Reguverse 助手操作手册与使用指南",
  head: [["link", { rel: "icon", type: "image/png", href: "/branding-4f072eca.png" }]],

  locales: {
    zh: {
      label: "中文",
      lang: "zh-CN",
      link: "/zh/",
      themeConfig: {
        nav: [
          { text: "首页", link: "/zh/" },
          { text: "快速开始", link: "/zh/guide/get-started" },
          { text: "产品与定价", link: "/zh/guide/pricing" },
          { text: "反馈与建议", link: "/zh/feedback" },
          { text: "联系我们", link: "/zh/contact" },
        ],
        sidebar: {
          "/zh/guide/": [
            {
              text: "入门",
              items: [
                { text: "快速开始", link: "/zh/guide/get-started" },
                { text: "安装插件", link: "/zh/guide/install" },
                { text: "注册与登录", link: "/zh/guide/register" },
                { text: "套餐与定价", link: "/zh/guide/pricing" },
              ],
            },
            {
              text: "EU MDR 临床评价",
              items: [
                { text: "创建项目", link: "/zh/guide/eu-create-project" },
                { text: "设备信息 (Step 1)", link: "/zh/guide/eu-step1" },
                { text: "临床背景 (Step 2)", link: "/zh/guide/eu-step2" },
                { text: "文献检索 (Step 3)", link: "/zh/guide/eu-step3" },
                { text: "文献筛选 (Step 4)", link: "/zh/guide/eu-step4" },
                { text: "安全数据 (Step 5)", link: "/zh/guide/eu-step5" },
                { text: "安全分析 (Step 6)", link: "/zh/guide/eu-step6" },
                { text: "全文评审 (Step 7)", link: "/zh/guide/eu-step7" },
                { text: "文献综述 (Step 8)", link: "/zh/guide/eu-step8" },
                { text: "风险与差距 (Step 9-10)", link: "/zh/guide/eu-step9" },
                { text: "生成文档", link: "/zh/guide/eu-documents" },
              ],
            },
            {
              text: "EU MDR 其他工作流",
              items: [
                { text: "GSPR 合规检查", link: "/zh/guide/gspr" },
                { text: "风险管理", link: "/zh/guide/risk-management" },
                { text: "上市后监督 (PMS)", link: "/zh/guide/pms-pmcf" },
                { text: "证据注册表", link: "/zh/guide/evidence-registry" },
              ],
            },
            {
              text: "NMPA 注册资料",
              items: [
                { text: "创建 NMPA 项目", link: "/zh/guide/nmpa-create-project" },
                { text: "注册章节概览", link: "/zh/guide/nmpa-overview" },
              ],
            },
            {
              text: "AI 工具",
              items: [
                { text: "AI 工具总览", link: "/zh/guide/ai-tools" },
                { text: "翻译工具", link: "/zh/guide/translation" },
                { text: "EUDAMED UDI 批量上传", link: "/zh/guide/eudamed-udi" },
              ],
            },
            {
              text: "其他功能",
              items: [
                { text: "法规知识库", link: "/zh/guide/knowledge-base" },
                { text: "账户管理", link: "/zh/guide/account" },
              ],
            },
          ],
        },
      },
    },
    en: {
      label: "English",
      lang: "en-US",
      link: "/en/",
      themeConfig: {
        nav: [
          { text: "Home", link: "/en/" },
          { text: "Quick Start", link: "/en/guide/get-started" },
          { text: "Plans & Pricing", link: "/en/guide/pricing" },
          { text: "Feedback", link: "/en/feedback" },
          { text: "Contact", link: "/en/contact" },
        ],
        sidebar: {
          "/en/guide/": [
            {
              text: "Getting Started",
              items: [
                { text: "Quick Start", link: "/en/guide/get-started" },
                { text: "Install Plugin", link: "/en/guide/install" },
                { text: "Register & Login", link: "/en/guide/register" },
                { text: "Plans & Pricing", link: "/en/guide/pricing" },
              ],
            },
            {
              text: "EU MDR Clinical Evaluation",
              items: [
                { text: "Create Project", link: "/en/guide/eu-create-project" },
                { text: "Device Info (Step 1)", link: "/en/guide/eu-step1" },
                { text: "Clinical Background (Step 2)", link: "/en/guide/eu-step2" },
                { text: "Literature Search (Step 3)", link: "/en/guide/eu-step3" },
                { text: "Literature Screening (Step 4)", link: "/en/guide/eu-step4" },
                { text: "Safety Data (Step 5)", link: "/en/guide/eu-step5" },
                { text: "Safety Analysis (Step 6)", link: "/en/guide/eu-step6" },
                { text: "Full-text Appraisal (Step 7)", link: "/en/guide/eu-step7" },
                { text: "Literature Summary (Step 8)", link: "/en/guide/eu-step8" },
                { text: "Risk & Gap (Step 9-10)", link: "/en/guide/eu-step9" },
                { text: "Generate Documents", link: "/en/guide/eu-documents" },
              ],
            },
            {
              text: "EU MDR Other Workflows",
              items: [
                { text: "GSPR Compliance", link: "/en/guide/gspr" },
                { text: "Risk Management", link: "/en/guide/risk-management" },
                { text: "Post-Market Surveillance", link: "/en/guide/pms-pmcf" },
                { text: "Evidence Registry", link: "/en/guide/evidence-registry" },
              ],
            },
            {
              text: "NMPA Registration",
              items: [
                { text: "Create NMPA Project", link: "/en/guide/nmpa-create-project" },
                { text: "Registration Chapters", link: "/en/guide/nmpa-overview" },
              ],
            },
            {
              text: "AI Tools",
              items: [
                { text: "AI Tools Overview", link: "/en/guide/ai-tools" },
                { text: "Translation", link: "/en/guide/translation" },
                { text: "EUDAMED UDI Bulk Upload", link: "/en/guide/eudamed-udi" },
              ],
            },
            {
              text: "Other Features",
              items: [
                { text: "Knowledge Base", link: "/en/guide/knowledge-base" },
                { text: "Account Management", link: "/en/guide/account" },
              ],
            },
          ],
        },
      },
    },
  },

  themeConfig: {
    logo: { src: "/branding-4f072eca.png", alt: "Reguverse" },
    socialLinks: [
      { icon: "github", link: "https://github.com/RASAAS/docmcp-knowledge" },
    ],
    footer: {
      message: "Reguverse Assistant User Manual",
      copyright: "Copyright &copy; 2026 RASAAS",
    },
    search: { provider: "local" },
  },
});
