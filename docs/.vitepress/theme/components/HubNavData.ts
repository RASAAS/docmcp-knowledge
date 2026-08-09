/**
 * Shared Hub navigation labels (EN/ZH) for sidebar + boards.
 * Keep category/channel values in sync with community-worker API.
 */

export type HubTabKey = "features" | "discussions" | "roadmap" | "admin";

export interface HubNavItem {
  value: string;
  labelEn: string;
  labelZh: string;
  descEn?: string;
  descZh?: string;
  icon: string;
}

export interface HubTabDef {
  key: HubTabKey;
  labelEn: string;
  labelZh: string;
  icon: string;
}

export const HUB_TABS: HubTabDef[] = [
  {
    key: "features",
    labelEn: "Feature Board",
    labelZh: "功能建议",
    icon: "M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z",
  },
  {
    key: "discussions",
    labelEn: "Discussions",
    labelZh: "讨论区",
    icon: "M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z",
  },
  {
    key: "roadmap",
    labelEn: "Roadmap",
    labelZh: "路线图",
    icon: "M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7",
  },
];

export const HUB_ADMIN_TAB: HubTabDef = {
  key: "admin",
  labelEn: "Admin",
  labelZh: "内容管理",
  icon: "M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.066 2.573c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.573 1.066c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.066-2.573c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z M15 12a3 3 0 11-6 0 3 3 0 016 0z",
};

export const FEATURE_CATEGORIES: HubNavItem[] = [
  { value: "", labelEn: "All", labelZh: "全部", icon: "M4 6h16M4 12h16M4 18h16" },
  { value: "ce_workflow", labelEn: "Clinical Evaluation", labelZh: "临床评价", icon: "M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" },
  { value: "risk_management", labelEn: "Risk Management", labelZh: "风险管理", icon: "M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" },
  { value: "pms_pmcf", labelEn: "PMS / PMCF", labelZh: "PMS / PMCF", icon: "M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" },
  { value: "gspr", labelEn: "GSPR", labelZh: "GSPR", icon: "M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" },
  { value: "ai_tools", labelEn: "AI Tools", labelZh: "AI 工具", icon: "M13 10V3L4 14h7v7l9-11h-7z" },
  { value: "knowledge_base", labelEn: "Knowledge Base", labelZh: "知识库", icon: "M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" },
  { value: "general", labelEn: "General", labelZh: "通用", icon: "M4 6h16M4 12h16M4 18h7" },
];

export const DISCUSSION_CHANNELS: HubNavItem[] = [
  {
    value: "",
    labelEn: "# all-channels",
    labelZh: "# 全部频道",
    descEn: "View all discussions",
    descZh: "查看所有讨论",
    icon: "M4 6h16M4 12h16M4 18h16",
  },
  {
    value: "regulatory_intelligence",
    labelEn: "# regulatory-intel",
    labelZh: "# 法规情报",
    descEn: "Updates and policy analysis",
    descZh: "法规动态和政策解读",
    icon: "M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253",
  },
  {
    value: "best_practices",
    labelEn: "# best-practices",
    labelZh: "# 最佳实践",
    descEn: "Compliance tips and methodology",
    descZh: "合规经验分享和方法论",
    icon: "M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z",
  },
  {
    value: "tool_tips",
    labelEn: "# tool-tips",
    labelZh: "# 工具技巧",
    descEn: "Reguverse usage tips",
    descZh: "Reguverse 使用技巧",
    icon: "M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.066 2.573c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.573 1.066c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.066-2.573c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z",
  },
  {
    value: "general",
    labelEn: "# general",
    labelZh: "# 综合讨论",
    descEn: "Open discussion",
    descZh: "自由话题",
    icon: "M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z",
  },
];

export function hubLabel(item: { labelEn: string; labelZh: string }, isZh: boolean): string {
  return isZh ? item.labelZh : item.labelEn;
}

export function hubDesc(item: HubNavItem, isZh: boolean): string {
  return (isZh ? item.descZh : item.descEn) || "";
}
