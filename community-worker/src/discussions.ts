import type { Env, AuthUser, Discussion } from "./types";
import { DISCUSSION_CATEGORIES } from "./types";
import { json, error, sanitize, sanitizeTitle, isAdmin, isOwner, withinEditWindow } from "./utils";
import { verifyTurnstile, getIdentifier } from "./auth";

/** GET /api/discussions?category=&sort=latest|likes&page=1 */
export async function listDiscussions(
  request: Request,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  const url = new URL(request.url);
  const category = url.searchParams.get("category") || "";
  const sort = url.searchParams.get("sort") || "latest";
  const page = Math.max(1, parseInt(url.searchParams.get("page") || "1", 10));
  const limit = 20;
  const offset = (page - 1) * limit;

  const orderBy =
    sort === "likes"
      ? "like_count DESC, created_at DESC"
      : "created_at DESC";

  let where = "is_hidden = 0";
  const params: unknown[] = [];
  if (
    category &&
    DISCUSSION_CATEGORIES.includes(category as typeof DISCUSSION_CATEGORIES[number])
  ) {
    where += " AND category = ?";
    params.push(category);
  }

  const countStmt = env.DB.prepare(
    `SELECT COUNT(*) as total FROM discussions WHERE ${where}`
  );
  const listStmt = env.DB.prepare(
    `SELECT id, title, body, category, author_name, author_user_id,
            is_verified, like_count, comment_count, created_at, updated_at
     FROM discussions WHERE ${where} ORDER BY ${orderBy} LIMIT ? OFFSET ?`
  );

  const [countRes, listRes] = await Promise.all([
    countStmt.bind(...params).first<{ total: number }>(),
    listStmt.bind(...params, limit, offset).all<Discussion>(),
  ]);

  const identifier = getIdentifier(user);
  let likedSet = new Set<number>();
  if (user && listRes.results.length > 0) {
    const ids = listRes.results.map((d) => d.id);
    const placeholders = ids.map(() => "?").join(",");
    const likesRes = await env.DB.prepare(
      `SELECT discussion_id FROM likes WHERE liker_identifier = ? AND discussion_id IN (${placeholders})`
    ).bind(identifier, ...ids).all<{ discussion_id: number }>();
    likedSet = new Set(likesRes.results.map((l) => l.discussion_id));
  }

  const items = listRes.results.map((d) => ({
    ...d,
    user_liked: likedSet.has(d.id),
  }));

  return json(
    {
      items,
      total: countRes?.total || 0,
      page,
      pages: Math.ceil((countRes?.total || 0) / limit),
    },
    200,
    env
  );
}

/** GET /api/discussions/:id */
export async function getDiscussion(
  id: number,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  const disc = await env.DB.prepare(
    `SELECT * FROM discussions WHERE id = ? AND is_hidden = 0`
  ).bind(id).first<Discussion>();
  if (!disc) return error("Discussion not found", 404, env);

  const identifier = getIdentifier(user);
  const liked = await env.DB.prepare(
    `SELECT id FROM likes WHERE discussion_id = ? AND liker_identifier = ?`
  ).bind(id, identifier).first();

  return json({ ...disc, user_liked: !!liked }, 200, env);
}

/** POST /api/discussions */
export async function createDiscussion(
  request: Request,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  const body = (await request.json()) as {
    title?: string;
    body?: string;
    category?: string;
    author_name?: string;
    author_email?: string;
    turnstile_token?: string;
  };

  if (!body.title?.trim() || !body.body?.trim()) {
    return error("Title and body are required", 400, env);
  }

  if (!user) {
    if (!body.author_name?.trim()) {
      return error("Name is required for guests", 400, env);
    }
    if (!body.turnstile_token) {
      return error("Verification required", 400, env);
    }
    const ip = request.headers.get("CF-Connecting-IP") || "";
    const ok = await verifyTurnstile(body.turnstile_token, ip, env);
    if (!ok) return error("Turnstile verification failed", 403, env);
  }

  const category = DISCUSSION_CATEGORIES.includes(
    body.category as typeof DISCUSSION_CATEGORIES[number]
  )
    ? body.category!
    : "general";

  const result = await env.DB.prepare(
    `INSERT INTO discussions (title, body, category, author_name, author_email, author_user_id, is_verified)
     VALUES (?, ?, ?, ?, ?, ?, ?)`
  )
    .bind(
      sanitizeTitle(body.title!),
      sanitize(body.body!),
      category,
      user ? sanitize(user.display_name || "User") : sanitize(body.author_name!),
      user ? null : (body.author_email || null),
      user ? user.user_id : null,
      user ? 1 : 0
    )
    .run();

  return json(
    { id: result.meta.last_row_id, message: "Discussion created" },
    201,
    env
  );
}

/** POST /api/discussions/:id/like */
export async function toggleLike(
  id: number,
  request: Request,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  const body = (await request.json().catch(() => ({}))) as {
    author_email?: string;
    turnstile_token?: string;
  };

  const identifier = getIdentifier(user, body.author_email);
  if (identifier.startsWith("anon:")) {
    return error("Email or login required to like", 400, env);
  }

  if (!user && body.turnstile_token) {
    const ip = request.headers.get("CF-Connecting-IP") || "";
    const ok = await verifyTurnstile(body.turnstile_token, ip, env);
    if (!ok) return error("Turnstile verification failed", 403, env);
  }

  const existing = await env.DB.prepare(
    `SELECT id FROM likes WHERE discussion_id = ? AND liker_identifier = ?`
  ).bind(id, identifier).first<{ id: number }>();

  if (existing) {
    await env.DB.batch([
      env.DB.prepare(`DELETE FROM likes WHERE id = ?`).bind(existing.id),
      env.DB.prepare(
        `UPDATE discussions SET like_count = like_count - 1, updated_at = datetime('now') WHERE id = ?`
      ).bind(id),
    ]);
    return json({ liked: false, message: "Like removed" }, 200, env);
  }

  await env.DB.batch([
    env.DB.prepare(
      `INSERT INTO likes (discussion_id, liker_identifier) VALUES (?, ?)`
    ).bind(id, identifier),
    env.DB.prepare(
      `UPDATE discussions SET like_count = like_count + 1, updated_at = datetime('now') WHERE id = ?`
    ).bind(id),
  ]);

  return json({ liked: true, message: "Like added" }, 200, env);
}

/** PUT /api/discussions/:id (Owner within edit window, or Admin) */
export async function editDiscussion(
  id: number,
  request: Request,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  if (!user) return error("Login required", 401, env);

  const disc = await env.DB.prepare(
    `SELECT author_user_id, created_at FROM discussions WHERE id = ?`
  ).bind(id).first<{ author_user_id: string | null; created_at: string }>();
  if (!disc) return error("Discussion not found", 404, env);

  if (!isAdmin(user)) {
    if (!isOwner(user, disc.author_user_id)) return error("Not authorized", 403, env);
    if (!withinEditWindow(disc.created_at)) return error("Edit window expired (30 minutes)", 403, env);
  }

  const body = (await request.json()) as { title?: string; body?: string; category?: string };
  const updates: string[] = [];
  const params: unknown[] = [];

  if (body.title?.trim()) { updates.push("title = ?"); params.push(sanitizeTitle(body.title)); }
  if (body.body?.trim()) { updates.push("body = ?"); params.push(sanitize(body.body)); }
  if (body.category && DISCUSSION_CATEGORIES.includes(body.category as typeof DISCUSSION_CATEGORIES[number])) {
    updates.push("category = ?"); params.push(body.category);
  }
  if (updates.length === 0) return error("No changes", 400, env);

  updates.push("updated_at = datetime('now')");
  params.push(id);

  await env.DB.prepare(`UPDATE discussions SET ${updates.join(", ")} WHERE id = ?`).bind(...params).run();
  return json({ message: "Discussion updated" }, 200, env);
}

/** DELETE /api/discussions/:id (Owner or Admin) */
export async function deleteDiscussion(
  id: number,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  if (!user) return error("Login required", 401, env);

  const disc = await env.DB.prepare(
    `SELECT author_user_id FROM discussions WHERE id = ?`
  ).bind(id).first<{ author_user_id: string | null }>();
  if (!disc) return error("Discussion not found", 404, env);

  if (!isAdmin(user) && !isOwner(user, disc.author_user_id)) {
    return error("Not authorized", 403, env);
  }

  await env.DB.batch([
    env.DB.prepare(`DELETE FROM comments WHERE target_type = 'discussion' AND target_id = ?`).bind(id),
    env.DB.prepare(`DELETE FROM likes WHERE discussion_id = ?`).bind(id),
    env.DB.prepare(`DELETE FROM discussions WHERE id = ?`).bind(id),
  ]);

  return json({ message: "Discussion deleted" }, 200, env);
}

/** PUT /api/discussions/:id/hide (Admin only) */
export async function hideDiscussion(
  id: number,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  if (!user || !["admin", "super_admin"].includes(user.role)) {
    return error("Admin access required", 403, env);
  }

  await env.DB.prepare(
    `UPDATE discussions SET is_hidden = 1, updated_at = datetime('now') WHERE id = ?`
  ).bind(id).run();

  return json({ message: "Discussion hidden" }, 200, env);
}
