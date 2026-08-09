import type { Env, AuthUser } from "./types";

/**
 * Verify Hub HMAC token (same format as hub-api) for optional account linking.
 * Token format (base64url): user_id|display_name|role|tier|expires|sig
 */
export async function verifyHubToken(
  authHeader: string | null,
  env: Env
): Promise<AuthUser | null> {
  if (!authHeader || !authHeader.startsWith("Bearer ")) return null;
  const token = authHeader.slice(7);
  if (!token || !env.HUB_TOKEN_SECRET) return null;

  try {
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
