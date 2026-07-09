/**
 * Reguverse Hub API client for VitePress frontend.
 * Communicates with Cloudflare Workers backend.
 */

const HUB_API_URL =
  (typeof window !== "undefined" &&
    (window as Record<string, unknown>).__HUB_API_URL__) ||
  "https://hub-api.team-ra.org";

function getAuthToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem("reguverse_hub_token");
}

function headers(withAuth = true): Record<string, string> {
  const h: Record<string, string> = { "Content-Type": "application/json" };
  if (withAuth) {
    const token = getAuthToken();
    if (token) h["Authorization"] = `Bearer ${token}`;
  }
  return h;
}

async function request<T>(
  path: string,
  options?: RequestInit
): Promise<T> {
  const resp = await fetch(`${HUB_API_URL}${path}`, {
    ...options,
    headers: { ...headers(), ...(options?.headers || {}) },
  });
  if (!resp.ok) {
    const err = await resp.json().catch(() => ({ error: resp.statusText }));
    throw new Error((err as { error?: string }).error || resp.statusText);
  }
  return resp.json() as Promise<T>;
}

// --- Features ---

export interface Feature {
  id: number;
  title: string;
  description: string;
  category: string;
  status: string;
  author_name: string;
  is_verified: number;
  vote_count: number;
  comment_count: number;
  created_at: string;
  updated_at: string;
  user_voted?: boolean;
}

export interface PaginatedResponse<T> {
  items: T[];
  total: number;
  page: number;
  pages: number;
}

export function listFeatures(
  params: { category?: string; sort?: string; page?: number } = {}
): Promise<PaginatedResponse<Feature>> {
  const sp = new URLSearchParams();
  if (params.category) sp.set("category", params.category);
  if (params.sort) sp.set("sort", params.sort);
  if (params.page) sp.set("page", String(params.page));
  return request(`/api/features?${sp}`);
}

export function getFeature(id: number): Promise<Feature> {
  return request(`/api/features/${id}`);
}

export function createFeature(data: {
  title: string;
  description: string;
  category?: string;
  author_name?: string;
  author_email?: string;
  turnstile_token?: string;
}): Promise<{ id: number; message: string }> {
  return request("/api/features", {
    method: "POST",
    body: JSON.stringify(data),
  });
}

export function toggleVote(
  featureId: number,
  data?: { author_email?: string; turnstile_token?: string }
): Promise<{ voted: boolean; message: string }> {
  return request(`/api/features/${featureId}/vote`, {
    method: "POST",
    body: JSON.stringify(data || {}),
  });
}

// --- Discussions ---

export interface Discussion {
  id: number;
  title: string;
  body: string;
  category: string;
  author_name: string;
  is_verified: number;
  like_count: number;
  comment_count: number;
  created_at: string;
  user_liked?: boolean;
}

export function listDiscussions(
  params: { category?: string; sort?: string; page?: number } = {}
): Promise<PaginatedResponse<Discussion>> {
  const sp = new URLSearchParams();
  if (params.category) sp.set("category", params.category);
  if (params.sort) sp.set("sort", params.sort);
  if (params.page) sp.set("page", String(params.page));
  return request(`/api/discussions?${sp}`);
}

export function createDiscussion(data: {
  title: string;
  body: string;
  category?: string;
  author_name?: string;
  turnstile_token?: string;
}): Promise<{ id: number; message: string }> {
  return request("/api/discussions", {
    method: "POST",
    body: JSON.stringify(data),
  });
}

export function toggleLike(
  discussionId: number,
  data?: { author_email?: string; turnstile_token?: string }
): Promise<{ liked: boolean; message: string }> {
  return request(`/api/discussions/${discussionId}/like`, {
    method: "POST",
    body: JSON.stringify(data || {}),
  });
}

// --- Comments ---

export interface Comment {
  id: number;
  body: string;
  author_name: string;
  is_verified: number;
  created_at: string;
}

export function listComments(
  targetType: string,
  targetId: number,
  page = 1
): Promise<PaginatedResponse<Comment>> {
  return request(
    `/api/comments?target_type=${targetType}&target_id=${targetId}&page=${page}`
  );
}

export function createComment(data: {
  target_type: string;
  target_id: number;
  body: string;
  author_name?: string;
  turnstile_token?: string;
}): Promise<{ id: number; message: string }> {
  return request("/api/comments", {
    method: "POST",
    body: JSON.stringify(data),
  });
}

// --- Stats ---

export interface HubStats {
  features: number;
  discussions: number;
  comments: number;
}

export function getStats(): Promise<HubStats> {
  return request("/api/stats");
}

// --- Auth helpers ---

const DOCMCP_API_URL =
  (typeof window !== "undefined" &&
    (window as Record<string, unknown>).__DOCMCP_API_URL__) ||
  "https://llm.team-ra.org";

export function isLoggedIn(): boolean {
  return !!getAuthToken();
}

export function getDisplayName(): string {
  if (typeof window === "undefined") return "";
  return localStorage.getItem("reguverse_hub_name") || "";
}

export function saveSession(token: string, name: string): void {
  if (typeof window !== "undefined") {
    localStorage.setItem("reguverse_hub_token", token);
    localStorage.setItem("reguverse_hub_name", name);
  }
}

export function logout(): void {
  if (typeof window !== "undefined") {
    localStorage.removeItem("reguverse_hub_token");
    localStorage.removeItem("reguverse_hub_name");
  }
}

export async function sendOtp(email: string): Promise<{ ok?: boolean; error?: string }> {
  const resp = await fetch(`${DOCMCP_API_URL}/api/v1/auth/hub-otp/send`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email }),
  });
  return resp.json();
}

export async function verifyOtp(
  email: string,
  code: string
): Promise<{
  verified?: boolean;
  hub_token?: string;
  display_name?: string;
  error?: string;
  attempts_remaining?: number;
}> {
  const resp = await fetch(`${DOCMCP_API_URL}/api/v1/auth/hub-otp/verify`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, code }),
  });
  return resp.json();
}

export async function verifyAuth(): Promise<{
  verified: boolean;
  display_name?: string;
}> {
  const token = getAuthToken();
  if (!token) return { verified: false };
  try {
    const resp = await fetch(`${HUB_API_URL}/api/auth/verify`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    if (!resp.ok) return { verified: false };
    return resp.json();
  } catch {
    return { verified: false };
  }
}
