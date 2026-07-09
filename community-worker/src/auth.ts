import type { Env, AuthUser } from "./types";

/**
 * Verify a Hub HMAC token (from hub-otp/verify flow).
 * The token is base64url-encoded: user_id|display_name|role|tier|expires|sig
 * We forward it to the docmcp backend for signature verification.
 */
export async function verifyToken(
  authHeader: string | null,
  env: Env
): Promise<AuthUser | null> {
  if (!authHeader || !authHeader.startsWith("Bearer ")) return null;
  const token = authHeader.slice(7);
  if (!token) return null;

  try {
    const resp = await fetch(
      `${env.DOCMCP_API_URL}/api/v1/auth/hub-token/verify`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ hub_token: token }),
      }
    );
    if (!resp.ok) return null;
    const data = (await resp.json()) as {
      verified?: boolean;
      user_id?: string;
      display_name?: string;
      role?: string;
      subscription_tier?: string;
    };
    if (!data.verified) return null;
    return {
      verified: true,
      user_id: data.user_id || "",
      display_name: data.display_name || "",
      role: data.role || "user",
      subscription_tier: data.subscription_tier || "",
    };
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
