import type { Env, AuthUser } from "./types";

export const EDIT_WINDOW_MS = 30 * 60 * 1000; // 30 minutes

export function corsHeaders(env: Env): Record<string, string> {
  return {
    "Access-Control-Allow-Origin": env.ALLOWED_ORIGIN,
    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
    "Access-Control-Max-Age": "3600",
  };
}

export function json(data: unknown, status = 200, env?: Env): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      "Content-Type": "application/json",
      ...(env ? corsHeaders(env) : {}),
    },
  });
}

export function error(message: string, status: number, env?: Env): Response {
  return json({ error: message }, status, env);
}

/** Sanitize user input to prevent XSS in stored content. */
export function sanitize(input: string, maxLen = 5000): string {
  return input
    .slice(0, maxLen)
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

export function sanitizeTitle(input: string): string {
  return sanitize(input, 200).trim();
}

export function isAdmin(user: AuthUser | null): boolean {
  return !!user && ["admin", "super_admin"].includes(user.role);
}

export function isOwner(user: AuthUser | null, authorUserId: string | null): boolean {
  return !!user && !!authorUserId && user.user_id === authorUserId;
}

export function withinEditWindow(createdAt: string): boolean {
  const created = new Date(createdAt + "Z").getTime();
  return Date.now() - created < EDIT_WINDOW_MS;
}
