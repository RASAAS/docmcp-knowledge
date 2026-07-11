import type { Env } from "./types";

async function buildSignedUrl(
  webhookUrl: string,
  secret: string
): Promise<string> {
  const ts = String(Date.now());
  const stringToSign = `${ts}\n${secret}`;
  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"]
  );
  const sig = await crypto.subtle.sign(
    "HMAC",
    key,
    new TextEncoder().encode(stringToSign)
  );
  const sign = encodeURIComponent(btoa(String.fromCharCode(...new Uint8Array(sig))));
  const sep = webhookUrl.includes("?") ? "&" : "?";
  return `${webhookUrl}${sep}timestamp=${ts}&sign=${sign}`;
}

async function sendMarkdown(
  env: Env,
  title: string,
  text: string
): Promise<void> {
  const url = (env as Record<string, unknown>).DINGTALK_HUB_WEBHOOK as string | undefined;
  const secret = (env as Record<string, unknown>).DINGTALK_HUB_SECRET as string | undefined;
  if (!url) return;

  const finalUrl = secret ? await buildSignedUrl(url, secret) : url;
  try {
    await fetch(finalUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        msgtype: "markdown",
        markdown: { title, text },
      }),
    });
  } catch {
    // fire-and-forget
  }
}

const CATEGORY_LABELS: Record<string, string> = {
  ce_workflow: "临床评价",
  risk_management: "风险管理",
  pms_pmcf: "PMS/PMCF",
  gspr: "GSPR",
  ai_tools: "AI 工具",
  knowledge_base: "知识库",
  general: "通用",
  regulatory_intelligence: "法规动态",
  best_practices: "最佳实践",
  tool_tips: "使用技巧",
};

export function notifyNewFeature(
  env: Env,
  p: { title: string; category: string; authorName: string; isVerified: boolean }
): void {
  const badge = p.isVerified ? " [已认证用户]" : " [游客]";
  const cat = CATEGORY_LABELS[p.category] || p.category;
  const text =
    `### Reguverse Hub -- 新功能建议\n\n` +
    `- **标题**: ${p.title}\n` +
    `- **分类**: ${cat}\n` +
    `- **提交者**: ${p.authorName}${badge}\n`;
  sendMarkdown(env, "Hub: 新功能建议", text);
}

export function notifyNewDiscussion(
  env: Env,
  p: { title: string; category: string; authorName: string; isVerified: boolean }
): void {
  const badge = p.isVerified ? " [已认证用户]" : " [游客]";
  const cat = CATEGORY_LABELS[p.category] || p.category;
  const text =
    `### Reguverse Hub -- 新讨论\n\n` +
    `- **标题**: ${p.title}\n` +
    `- **频道**: ${cat}\n` +
    `- **发起者**: ${p.authorName}${badge}\n`;
  sendMarkdown(env, "Hub: 新讨论", text);
}

export function notifyNewComment(
  env: Env,
  p: {
    targetType: string;
    targetTitle: string;
    bodyPreview: string;
    authorName: string;
    isVerified: boolean;
  }
): void {
  const badge = p.isVerified ? " [已认证用户]" : " [游客]";
  const typeLabel = p.targetType === "feature" ? "功能建议" : "讨论";
  const preview = p.bodyPreview.length > 80 ? p.bodyPreview.slice(0, 80) + "..." : p.bodyPreview;
  const text =
    `### Reguverse Hub -- 新回复\n\n` +
    `- **目标**: ${typeLabel}「${p.targetTitle}」\n` +
    `- **内容**: ${preview}\n` +
    `- **回复者**: ${p.authorName}${badge}\n`;
  sendMarkdown(env, "Hub: 新回复", text);
}
