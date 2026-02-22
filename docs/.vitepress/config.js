import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'DocMCP Knowledge Base',
  description: 'Open regulatory knowledge base for medical device compliance',
  srcDir: '.',

  locales: {
    root: {
      label: 'English',
      lang: 'en',
      link: '/en/',
      themeConfig: {
        nav: [
          { text: 'Home', link: '/en/' },
          { text: 'EU MDR', link: '/en/eu_mdr/' },
          { text: 'FDA', link: '/en/fda/' },
          { text: 'NMPA', link: '/en/nmpa/' },
          { text: 'Standards', link: '/en/shared/standards' },
        ],
        sidebar: {
          '/en/eu_mdr/': [
            { text: 'EU MDR Overview', link: '/en/eu_mdr/' },
            { text: 'Regulations', link: '/en/eu_mdr/regulations' },
            { text: 'Harmonised Standards', link: '/en/eu_mdr/standards' },
            { text: 'MDCG Guidance', link: '/en/eu_mdr/mdcg' },
            { text: 'TEAM-NB Position Papers', link: '/en/eu_mdr/team_nb' },
          ],
          '/en/fda/': [
            { text: 'FDA Overview', link: '/en/fda/' },
            { text: 'Regulations (21 CFR)', link: '/en/fda/regulations' },
            { text: 'Consensus Standards', link: '/en/fda/standards' },
            { text: 'Guidance Documents', link: '/en/fda/guidance' },
          ],
          '/en/nmpa/': [
            { text: 'NMPA Overview', link: '/en/nmpa/' },
            { text: 'Regulations', link: '/en/nmpa/regulations' },
            { text: 'GB/YY Standards', link: '/en/nmpa/standards' },
            { text: 'Guidance Principles', link: '/en/nmpa/guidance' },
            { text: 'Classification', link: '/en/nmpa/classification' },
          ],
        },
        socialLinks: [
          { icon: 'github', link: 'https://github.com/RASAAS/docmcp-knowledge' }
        ],
        footer: {
          message: 'Content licensed under CC BY 4.0',
          copyright: 'Copyright \u00a9 2026 RASAAS'
        },
        search: { provider: 'local' }
      }
    },
    zh: {
      label: '\u4e2d\u6587',
      lang: 'zh-CN',
      link: '/zh/',
      themeConfig: {
        nav: [
          { text: '\u9996\u9875', link: '/zh/' },
          { text: 'EU MDR', link: '/zh/eu_mdr/' },
          { text: 'FDA', link: '/zh/fda/' },
          { text: 'NMPA', link: '/zh/nmpa/' },
          { text: '\u6807\u51c6', link: '/zh/shared/standards' },
        ],
        sidebar: {
          '/zh/eu_mdr/': [
            { text: 'EU MDR \u6982\u8ff0', link: '/zh/eu_mdr/' },
            { text: '\u6cd5\u89c4\u6587\u672c', link: '/zh/eu_mdr/regulations' },
            { text: '\u534f\u8c03\u6807\u51c6', link: '/zh/eu_mdr/standards' },
            { text: 'MDCG \u6307\u5357', link: '/zh/eu_mdr/mdcg' },
            { text: 'TEAM-NB \u7acb\u573a\u6587\u4ef6', link: '/zh/eu_mdr/team_nb' },
          ],
          '/zh/fda/': [
            { text: 'FDA \u6982\u8ff0', link: '/zh/fda/' },
            { text: '\u6cd5\u89c4 (21 CFR)', link: '/zh/fda/regulations' },
            { text: '\u5171\u8bc6\u6807\u51c6', link: '/zh/fda/standards' },
            { text: '\u6307\u5357\u6587\u4ef6', link: '/zh/fda/guidance' },
          ],
          '/zh/nmpa/': [
            { text: 'NMPA \u6982\u8ff0', link: '/zh/nmpa/' },
            { text: '\u6cd5\u89c4\u6587\u672c', link: '/zh/nmpa/regulations' },
            { text: 'GB/YY \u6807\u51c6', link: '/zh/nmpa/standards' },
            { text: '\u6307\u5bfc\u539f\u5219', link: '/zh/nmpa/guidance' },
            { text: '\u5206\u7c7b\u76ee\u5f55', link: '/zh/nmpa/classification' },
          ],
        },
        socialLinks: [
          { icon: 'github', link: 'https://github.com/RASAAS/docmcp-knowledge' }
        ],
        footer: {
          message: '\u5185\u5bb9\u4ee5 CC BY 4.0 \u8bb8\u53ef\u8bc1\u6388\u6743',
          copyright: 'Copyright \u00a9 2026 RASAAS'
        },
        search: { provider: 'local' }
      }
    }
  },

  themeConfig: {
    logo: { light: '/logo.png', dark: '/logo-dark.png', alt: 'ARS' },
  }
})
