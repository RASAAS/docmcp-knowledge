import type { Env, AuthUser, Comment } from "./types";
import { json, error, sanitize, isAdmin, isOwner, withinEditWindow } from "./utils";
import { verifyTurnstile } from "./auth";

/** GET /api/comments?target_type=feature|discussion&target_id=1&page=1 */
export async function listComments(
  request: Request,
  env: Env
): Promise<Response> {
  const url = new URL(request.url);
  const targetType = url.searchParams.get("target_type") || "";
  const targetId = parseInt(url.searchParams.get("target_id") || "0", 10);
  const page = Math.max(1, parseInt(url.searchParams.get("page") || "1", 10));
  const limit = 30;
  const offset = (page - 1) * limit;

  if (!["feature", "discussion"].includes(targetType) || !targetId) {
    return error("target_type and target_id are required", 400, env);
  }

  const countRes = await env.DB.prepare(
    `SELECT COUNT(*) as total FROM comments WHERE target_type = ? AND target_id = ? AND is_hidden = 0`
  ).bind(targetType, targetId).first<{ total: number }>();

  const listRes = await env.DB.prepare(
    `SELECT id, target_type, target_id, body, author_name, author_user_id,
            is_verified, created_at
     FROM comments
     WHERE target_type = ? AND target_id = ? AND is_hidden = 0
     ORDER BY created_at ASC LIMIT ? OFFSET ?`
  ).bind(targetType, targetId, limit, offset).all<Comment>();

  return json(
    {
      items: listRes.results,
      total: countRes?.total || 0,
      page,
      pages: Math.ceil((countRes?.total || 0) / limit),
    },
    200,
    env
  );
}

/** POST /api/comments */
export async function createComment(
  request: Request,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  const body = (await request.json()) as {
    target_type?: string;
    target_id?: number;
    body?: string;
    author_name?: string;
    author_email?: string;
    turnstile_token?: string;
  };

  if (!body.body?.trim()) {
    return error("Comment body is required", 400, env);
  }
  if (
    !["feature", "discussion"].includes(body.target_type || "") ||
    !body.target_id
  ) {
    return error("target_type and target_id are required", 400, env);
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

  const result = await env.DB.prepare(
    `INSERT INTO comments (target_type, target_id, body, author_name, author_email, author_user_id, is_verified)
     VALUES (?, ?, ?, ?, ?, ?, ?)`
  )
    .bind(
      body.target_type!,
      body.target_id!,
      sanitize(body.body!, 2000),
      user ? sanitize(user.display_name || "User") : sanitize(body.author_name!),
      user ? null : (body.author_email || null),
      user ? user.user_id : null,
      user ? 1 : 0
    )
    .run();

  const counterTable =
    body.target_type === "feature" ? "feature_requests" : "discussions";
  await env.DB.prepare(
    `UPDATE ${counterTable} SET comment_count = comment_count + 1, updated_at = datetime('now') WHERE id = ?`
  ).bind(body.target_id!).run();

  return json(
    { id: result.meta.last_row_id, message: "Comment added" },
    201,
    env
  );
}

/** PUT /api/comments/:id (Owner within edit window, or Admin) */
export async function editComment(
  id: number,
  request: Request,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  if (!user) return error("Login required", 401, env);

  const comment = await env.DB.prepare(
    `SELECT author_user_id, created_at FROM comments WHERE id = ?`
  ).bind(id).first<{ author_user_id: string | null; created_at: string }>();
  if (!comment) return error("Comment not found", 404, env);

  if (!isAdmin(user)) {
    if (!isOwner(user, comment.author_user_id)) return error("Not authorized", 403, env);
    if (!withinEditWindow(comment.created_at)) return error("Edit window expired (30 minutes)", 403, env);
  }

  const body = (await request.json()) as { body?: string };
  if (!body.body?.trim()) return error("Comment body is required", 400, env);

  await env.DB.prepare(
    `UPDATE comments SET body = ? WHERE id = ?`
  ).bind(sanitize(body.body, 2000), id).run();

  return json({ message: "Comment updated" }, 200, env);
}

/** DELETE /api/comments/:id (Owner or Admin) */
export async function deleteComment(
  id: number,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  if (!user) return error("Login required", 401, env);

  const comment = await env.DB.prepare(
    `SELECT author_user_id, target_type, target_id FROM comments WHERE id = ?`
  ).bind(id).first<{ author_user_id: string | null; target_type: string; target_id: number }>();
  if (!comment) return error("Comment not found", 404, env);

  if (!isAdmin(user) && !isOwner(user, comment.author_user_id)) {
    return error("Not authorized", 403, env);
  }

  const counterTable = comment.target_type === "feature" ? "feature_requests" : "discussions";
  await env.DB.batch([
    env.DB.prepare(`DELETE FROM comments WHERE id = ?`).bind(id),
    env.DB.prepare(
      `UPDATE ${counterTable} SET comment_count = MAX(0, comment_count - 1), updated_at = datetime('now') WHERE id = ?`
    ).bind(comment.target_id),
  ]);

  return json({ message: "Comment deleted" }, 200, env);
}

/** PUT /api/comments/:id/hide (Admin only) */
export async function hideComment(
  id: number,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  if (!user || !["admin", "super_admin"].includes(user.role)) {
    return error("Admin access required", 403, env);
  }

  await env.DB.prepare(
    `UPDATE comments SET is_hidden = 1 WHERE id = ?`
  ).bind(id).run();

  return json({ message: "Comment hidden" }, 200, env);
}
