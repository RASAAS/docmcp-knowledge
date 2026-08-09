export interface Env {
  DB: D1Database;
  ALLOWED_ORIGIN: string;
  DOCMCP_API_URL: string;
  HUB_TOKEN_SECRET: string;
  /** Optional shared secret required in X-Create-Secret when creating sessions */
  HOST_CREATE_SECRET?: string;
}

export interface AuthUser {
  verified: true;
  user_id: string;
  display_name: string;
  role: string;
  subscription_tier: string;
}

export interface QuestionOption {
  id: string;
  text_en: string;
  text_zh: string;
}

export interface QuestionRow {
  id: number;
  course_id: number;
  qid: string;
  qtype: "single" | "multi";
  prompt_en: string;
  prompt_zh: string;
  options_json: string;
  correct_json: string;
  explanation_en: string;
  explanation_zh: string;
  tags_json: string;
  sort_order: number;
  published: number;
}

export interface LiveSessionRow {
  id: number;
  code: string;
  course_id: number;
  host_token_hash: string;
  host_user_id: string | null;
  status: "lobby" | "active" | "ended";
  current_question_id: number | null;
  phase: "waiting" | "open" | "locked" | "reveal";
  title: string;
  created_at: string;
  updated_at: string;
  expires_at: string | null;
}
