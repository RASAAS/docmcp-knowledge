/**
 * Reguverse Learn API client (independent learn-api Worker).
 * Optional Hub token reuse for account linking (same localStorage keys as Hub).
 */

const LEARN_API_URL =
  (typeof window !== "undefined" &&
    (window as Record<string, unknown>).__LEARN_API_URL__) ||
  "https://learn-api.team-ra.org";

function getHubToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem("reguverse_hub_token");
}

function headers(extra?: Record<string, string>): Record<string, string> {
  const h: Record<string, string> = { "Content-Type": "application/json", ...(extra || {}) };
  const token = getHubToken();
  if (token) h["Authorization"] = `Bearer ${token}`;
  return h;
}

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const resp = await fetch(`${LEARN_API_URL}${path}`, {
    ...options,
    headers: { ...headers(), ...(options?.headers as Record<string, string> | undefined) },
  });
  if (!resp.ok) {
    const err = await resp.json().catch(() => ({ error: resp.statusText }));
    throw new Error((err as { error?: string }).error || resp.statusText);
  }
  return resp.json() as Promise<T>;
}

export interface CourseSummary {
  id: number;
  slug: string;
  title_en: string;
  title_zh: string;
  description_en: string;
  description_zh: string;
  question_count?: number;
}

export interface QuestionOption {
  id: string;
  text_en: string;
  text_zh: string;
}

export interface LiveQuestion {
  id: number;
  qid: string;
  qtype: "single" | "multi";
  prompt_en: string;
  prompt_zh: string;
  options: QuestionOption[];
  correct?: string[];
  explanation_en?: string;
  explanation_zh?: string;
}

export function listCourses(): Promise<{ items: CourseSummary[] }> {
  return request("/api/courses");
}

export function getPractice(slug: string): Promise<{
  course: CourseSummary;
  questions: LiveQuestion[];
}> {
  return request(`/api/courses/${slug}/practice`);
}

export function submitPractice(
  slug: string,
  data: {
    participant_key: string;
    nickname?: string;
    answers: Record<string, string[]>;
  }
): Promise<{
  score: number;
  total: number;
  detail: Array<{
    qid: string;
    correct: boolean;
    your: string[];
    expected: string[];
    explanation_en: string;
    explanation_zh: string;
  }>;
}> {
  return request(`/api/courses/${slug}/practice`, {
    method: "POST",
    body: JSON.stringify(data),
  });
}

export function createLiveSession(data: {
  course_slug?: string;
  title?: string;
  create_secret?: string;
}): Promise<{ code: string; host_token: string; course_slug: string; join_path: string }> {
  const extra: Record<string, string> = {};
  if (data.create_secret) extra["X-Create-Secret"] = data.create_secret;
  return request("/api/live/sessions", {
    method: "POST",
    headers: extra,
    body: JSON.stringify({
      course_slug: data.course_slug,
      title: data.title,
    }),
  });
}

export function joinLiveSession(
  code: string,
  data: { nickname: string; display_name?: string; participant_key?: string }
): Promise<{
  participant_key: string;
  participant_id: number;
  nickname: string;
  display_name: string;
  session_code: string;
}> {
  return request(`/api/live/sessions/${code}/join`, {
    method: "POST",
    body: JSON.stringify(data),
  });
}

export function getLiveState(
  code: string,
  participantKey?: string
): Promise<{
  code: string;
  status: string;
  phase: string;
  title: string;
  participant_count: number;
  question: LiveQuestion | null;
  my_answer: string[] | null;
  can_answer: boolean;
}> {
  const sp = participantKey ? `?participant_key=${encodeURIComponent(participantKey)}` : "";
  return request(`/api/live/sessions/${code}/state${sp}`);
}

export function submitLiveAnswer(
  code: string,
  data: { participant_key: string; answer: string[] }
): Promise<{ ok: boolean }> {
  return request(`/api/live/sessions/${code}/answer`, {
    method: "POST",
    body: JSON.stringify(data),
  });
}

function hostHeaders(hostToken: string): Record<string, string> {
  return headers({ "X-Host-Token": hostToken });
}

export function hostGet(
  code: string,
  hostToken: string
): Promise<{
  code: string;
  status: string;
  phase: string;
  title: string;
  participant_count: number;
  answered: number;
  correct_count?: number;
  option_counts: Record<string, number>;
  question: LiveQuestion | null;
  question_list: Array<{ id: number; qid: string; sort_order: number; prompt_en: string; prompt_zh: string }>;
}> {
  return fetch(`${LEARN_API_URL}/api/live/sessions/${code}/host`, {
    headers: hostHeaders(hostToken),
  }).then(async (resp) => {
    if (!resp.ok) {
      const err = await resp.json().catch(() => ({ error: resp.statusText }));
      throw new Error((err as { error?: string }).error || resp.statusText);
    }
    return resp.json();
  });
}

async function hostPost<T>(code: string, hostToken: string, action: string, body?: unknown): Promise<T> {
  const resp = await fetch(`${LEARN_API_URL}/api/live/sessions/${code}/${action}`, {
    method: "POST",
    headers: hostHeaders(hostToken),
    body: body ? JSON.stringify(body) : "{}",
  });
  if (!resp.ok) {
    const err = await resp.json().catch(() => ({ error: resp.statusText }));
    throw new Error((err as { error?: string }).error || resp.statusText);
  }
  return resp.json() as Promise<T>;
}

export function hostPush(code: string, hostToken: string, body?: { qid?: string; question_id?: number }) {
  return hostPost(code, hostToken, "push", body || {});
}
export function hostLock(code: string, hostToken: string) {
  return hostPost(code, hostToken, "lock");
}
export function hostReveal(code: string, hostToken: string) {
  return hostPost(code, hostToken, "reveal");
}
export function hostWaiting(code: string, hostToken: string) {
  return hostPost(code, hostToken, "waiting");
}
export function hostEnd(code: string, hostToken: string) {
  return hostPost(code, hostToken, "end");
}

export function linkAccount(code: string, participantKey: string) {
  return request(`/api/live/sessions/${code}/link`, {
    method: "POST",
    body: JSON.stringify({ participant_key: participantKey }),
  });
}

export function ensureParticipantKey(): string {
  if (typeof window === "undefined") return "";
  const keyName = "reguverse_learn_participant_key";
  let key = localStorage.getItem(keyName);
  if (!key) {
    key = crypto.randomUUID().replace(/-/g, "");
    localStorage.setItem(keyName, key);
  }
  return key;
}

export function saveHostSession(code: string, hostToken: string): void {
  if (typeof window === "undefined") return;
  localStorage.setItem("reguverse_learn_host", JSON.stringify({ code, host_token: hostToken }));
}

export function loadHostSession(): { code: string; host_token: string } | null {
  if (typeof window === "undefined") return null;
  try {
    const raw = localStorage.getItem("reguverse_learn_host");
    if (!raw) return null;
    return JSON.parse(raw);
  } catch {
    return null;
  }
}

export { LEARN_API_URL };
