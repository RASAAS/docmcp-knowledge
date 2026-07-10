import type { Env, AuthUser } from "./types";

const HUB_TOKEN_MAX_AGE = 30 * 24 * 3600; // 30 days (must match backend)

/**
 * Verify a Hub HMAC token locally using Web Crypto API.
 * Token format (base64url-encoded): user_id|display_name|role|tier|expires|sig
 * sig = HMAC-SHA256(secret, "user_id|display_name|role|tier|expires")[:32hex]
 */
export async function verifyToken(
  authHeader: string | null,
  env: Env
): Promise<AuthUser | null> {
  if (!authHeader || !authHeader.startsWith("Bearer ")) return null;
  const token = authHeader.slice(7);
  if (!token) return null;
  if (!env.HUB_TOKEN_SECRET) return null;

  try {
    // Decode base64url -> UTF-8 string (atob fails on non-ASCII like CJK)
    const b64 = token.replace(/-/g, "+").replace(/_/g, "/");
    const binStr = atob(b64);
    const bytes = Uint8Array.from(binStr, (c) => c.charCodeAt(0));
    const raw = new TextDecoder().decode(bytes);
    const parts = raw.split("|");
    if (parts.length !== 6) return null;

    const [userId, displayName, role, tier, expiresStr, sig] = parts;
    const expires = parseInt(expiresStr, 10);
    if (isNaN(expires) || Date.now() / 1000 > expires) return null;

    const payload = `${userId}|${displayName}|${role}|${tier}|${expiresStr}`;
    const key = await crypto.subtle.importKey(
      "raw",
      new TextEncoder().encode(env.HUB_TOKEN_SECRET),
      { name: "HMAC", hash: "SHA-256" },
      false,
      ["sign"]
    );
    const sigBuf = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(payload));
    const expectedSig = Array.from(new Uint8Array(sigBuf))
      .map((b) => b.toString(16).padStart(2, "0"))
      .join("")
      .slice(0, 32);

    if (sig !== expectedSig) return null;

    return {
      verified: true,
      user_id: userId,
      display_name: displayName,
      role: role || "user",
      subscription_tier: tier || "",
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
