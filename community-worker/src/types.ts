export interface Env {
  DB: D1Database;
  ALLOWED_ORIGIN: string;
  DOCMCP_API_URL: string;
  TURNSTILE_SECRET: string;
  HUB_TOKEN_SECRET: string;
  DINGTALK_HUB_WEBHOOK: string;
  DINGTALK_HUB_SECRET: string;
}

export interface AuthUser {
  verified: true;
  user_id: string;
  display_name: string;
  role: string;
  subscription_tier: string;
}

export interface FeatureRequest {
  id: number;
  title: string;
  description: string;
  category: string;
  status: string;
  author_name: string;
  author_user_id: string | null;
  is_verified: number;
  vote_count: number;
  comment_count: number;
  created_at: string;
  updated_at: string;
  user_voted?: boolean;
}

export interface Discussion {
  id: number;
  title: string;
  body: string;
  category: string;
  author_name: string;
  author_user_id: string | null;
  is_verified: number;
  like_count: number;
  comment_count: number;
  created_at: string;
  updated_at: string;
  user_liked?: boolean;
}

export interface Comment {
  id: number;
  target_type: string;
  target_id: number;
  body: string;
  author_name: string;
  author_user_id: string | null;
  is_verified: number;
  created_at: string;
}

export const FEATURE_CATEGORIES = [
  "ce_workflow",
  "risk_management",
  "pms_pmcf",
  "gspr",
  "ai_tools",
  "knowledge_base",
  "general",
] as const;

export const DISCUSSION_CATEGORIES = [
  "regulatory_intelligence",
  "best_practices",
  "tool_tips",
  "general",
] as const;

export const FEATURE_STATUSES = [
  "under_review",
  "planned",
  "in_progress",
  "completed",
  "declined",
] as const;
