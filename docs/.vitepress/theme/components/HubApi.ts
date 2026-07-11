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

export function editFeature(
  id: number,
  data: { title?: string; description?: string; category?: string }
): Promise<{ message: string }> {
  return request(`/api/features/${id}`, {
    method: "PUT",
    body: JSON.stringify(data),
  });
}

export function deleteFeature(id: number): Promise<{ message: string }> {
  return request(`/api/features/${id}`, { method: "DELETE" });
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

export function editDiscussion(
  id: number,
  data: { title?: string; body?: string; category?: string }
): Promise<{ message: string }> {
  return request(`/api/discussions/${id}`, {
    method: "PUT",
    body: JSON.stringify(data),
  });
}

export function deleteDiscussion(id: number): Promise<{ message: string }> {
  return request(`/api/discussions/${id}`, { method: "DELETE" });
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

export function editComment(
  id: number,
  data: { body: string }
): Promise<{ message: string }> {
  return request(`/api/comments/${id}`, {
    method: "PUT",
    body: JSON.stringify(data),
  });
}

export function deleteComment(id: number): Promise<{ message: string }> {
  return request(`/api/comments/${id}`, { method: "DELETE" });
}

// --- Admin ---

export interface AdminRecentData {
  features: (Feature & { author_user_id?: string })[];
  discussions: (Discussion & { is_hidden?: number; author_user_id?: string })[];
  comments: (Comment & { is_hidden?: number; target_type: string; target_id: number; author_user_id?: string })[];
}

export function getAdminRecent(): Promise<AdminRecentData> {
  return request("/api/admin/recent");
}

export function hideFeature(id: number): Promise<{ message: string }> {
  return request(`/api/features/${id}/hide`, { method: "PUT" });
}

export function hideDiscussion(id: number): Promise<{ message: string }> {
  return request(`/api/discussions/${id}/hide`, { method: "PUT" });
}

export function hideComment(id: number): Promise<{ message: string }> {
  return request(`/api/comments/${id}/hide`, { method: "PUT" });
}

export function updateFeatureStatus(
  id: number,
  status: string
): Promise<{ message: string }> {
  return request(`/api/features/${id}/status`, {
    method: "PUT",
    body: JSON.stringify({ status }),
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

// --- Turnstile (guest anti-spam) ---

const TURNSTILE_SITE_KEY = "0x4AAAAAADzjZtsYPWyRAB89";
let _turnstileLoaded = false;

export function loadTurnstileScript(): Promise<void> {
  if (_turnstileLoaded || typeof window === "undefined") return Promise.resolve();
  return new Promise((resolve) => {
    if (document.querySelector('script[src*="turnstile"]')) {
      _turnstileLoaded = true;
      resolve();
      return;
    }
    const s = document.createElement("script");
    s.src = "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit";
    s.async = true;
    s.onload = () => { _turnstileLoaded = true; resolve(); };
    s.onerror = () => resolve();
    document.head.appendChild(s);
  });
}

export function renderTurnstile(container: HTMLElement): Promise<string> {
  return new Promise((resolve, reject) => {
    const w = window as Record<string, unknown>;
    const turnstile = w.turnstile as {
      render: (el: HTMLElement, opts: Record<string, unknown>) => string;
      remove: (id: string) => void;
    } | undefined;
    if (!turnstile) { reject(new Error("Turnstile not loaded")); return; }
    container.innerHTML = "";
    turnstile.render(container, {
      sitekey: TURNSTILE_SITE_KEY,
      callback: (token: string) => resolve(token),
      "error-callback": () => reject(new Error("Turnstile challenge failed")),
      "expired-callback": () => reject(new Error("Turnstile token expired")),
      theme: "auto",
      size: "normal",
    });
  });
}

// --- Auth helpers ---

function _resolveDocmcpUrl(): string {
  if (typeof window !== "undefined") {
    const override = (window as Record<string, unknown>).__DOCMCP_API_URL__;
    if (typeof override === "string" && override) return override;
    if (window.location.pathname.startsWith("/zh")) {
      return "https://llm.reguverse.com";
    }
  }
  return "https://llm.team-ra.org";
}

const DOCMCP_API_URL = _resolveDocmcpUrl();

export function isLoggedIn(): boolean {
  return !!getAuthToken();
}

export function getDisplayName(): string {
  if (typeof window === "undefined") return "";
  return localStorage.getItem("reguverse_hub_name") || "";
}

export function getUserId(): string {
  if (typeof window === "undefined") return "";
  return localStorage.getItem("reguverse_hub_uid") || "";
}

export function getUserRole(): string {
  if (typeof window === "undefined") return "";
  return localStorage.getItem("reguverse_hub_role") || "";
}

export function saveSession(token: string, name: string, userId?: string, role?: string): void {
  if (typeof window !== "undefined") {
    localStorage.setItem("reguverse_hub_token", token);
    localStorage.setItem("reguverse_hub_name", name);
    if (userId) localStorage.setItem("reguverse_hub_uid", userId);
    if (role) localStorage.setItem("reguverse_hub_role", role);
  }
}

export function logout(): void {
  if (typeof window !== "undefined") {
    localStorage.removeItem("reguverse_hub_token");
    localStorage.removeItem("reguverse_hub_name");
    localStorage.removeItem("reguverse_hub_uid");
    localStorage.removeItem("reguverse_hub_role");
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
  user_id?: string;
  role?: string;
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
