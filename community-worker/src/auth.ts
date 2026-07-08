import type { Env, AuthUser } from "./types";

/**
 * Verify a Reguverse JWT token against the docmcp backend.
 * Returns AuthUser on success, null on failure.
 */
export async function verifyToken(
  authHeader: string | null,
  env: Env
): Promise<AuthUser | null> {
  if (!authHeader || !authHeader.startsWith("Bearer ")) return null;

  try {
    const resp = await fetch(
      `${env.DOCMCP_API_URL}/api/v1/auth/community-verify`,
      {
        method: "GET",
        headers: { Authorization: authHeader },
      }
    );
    if (!resp.ok) return null;
    const data = (await resp.json()) as AuthUser & { verified?: boolean };
    if (!data.verified) return null;
    return data;
  } catch {
    return null;
  }
}

/**
 * Verify Cloudflare Turnstile token.
 * Required for all write operations from guests.
 */
export async function verifyTurnstile(
  token: string,
  ip: string,
  env: Env
): Promise<boolean> {
  if (!env.TURNSTILE_SECRET) return true; // skip if not configured

  try {
    const resp = await fetch(
      "https://challenges.cloudflare.com/turnstile/v0/siteverify",
      {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({
          secret: env.TURNSTILE_SECRET,
          response: token,
          remoteip: ip,
        }),
      }
    );
    const result = (await resp.json()) as { success: boolean };
    return result.success;
  } catch {
    return false;
  }
}

/** Derive a stable identifier for vote/like deduplication. */
export function getIdentifier(user: AuthUser | null, email?: string): string {
  if (user) return `user:${user.user_id}`;
  if (email) return `email:${hashEmail(email)}`;
  return `anon:${Date.now()}`;
}

function hashEmail(email: string): string {
  let hash = 0;
  for (let i = 0; i < email.length; i++) {
    const c = email.charCodeAt(i);
    hash = ((hash << 5) - hash + c) | 0;
  }
  return Math.abs(hash).toString(36);
}
