import type { Env, AuthUser, FeatureRequest } from "./types";
import { FEATURE_CATEGORIES, FEATURE_STATUSES } from "./types";
import { json, error, sanitize, sanitizeTitle } from "./utils";
import { verifyTurnstile, getIdentifier } from "./auth";

/** GET /api/features?category=&sort=votes|newest&page=1 */
export async function listFeatures(
  request: Request,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  const url = new URL(request.url);
  const category = url.searchParams.get("category") || "";
  const sort = url.searchParams.get("sort") || "votes";
  const page = Math.max(1, parseInt(url.searchParams.get("page") || "1", 10));
  const limit = 20;
  const offset = (page - 1) * limit;

  const orderBy =
    sort === "newest"
      ? "created_at DESC"
      : sort === "updated"
        ? "updated_at DESC"
        : "vote_count DESC, created_at DESC";

  let where = "1=1";
  const params: unknown[] = [];
  if (category && FEATURE_CATEGORIES.includes(category as typeof FEATURE_CATEGORIES[number])) {
    where += " AND category = ?";
    params.push(category);
  }

  const countStmt = env.DB.prepare(
    `SELECT COUNT(*) as total FROM feature_requests WHERE ${where}`
  );
  const listStmt = env.DB.prepare(
    `SELECT id, title, description, category, status, author_name,
            author_user_id, is_verified, vote_count, comment_count,
            created_at, updated_at
     FROM feature_requests WHERE ${where} ORDER BY ${orderBy} LIMIT ? OFFSET ?`
  );

  const [countRes, listRes] = await Promise.all([
    countStmt.bind(...params).first<{ total: number }>(),
    listStmt.bind(...params, limit, offset).all<FeatureRequest>(),
  ]);

  const identifier = getIdentifier(user);
  let votedSet = new Set<number>();
  if (user && listRes.results.length > 0) {
    const ids = listRes.results.map((f) => f.id);
    const placeholders = ids.map(() => "?").join(",");
    const votesRes = await env.DB.prepare(
      `SELECT feature_id FROM votes WHERE voter_identifier = ? AND feature_id IN (${placeholders})`
    ).bind(identifier, ...ids).all<{ feature_id: number }>();
    votedSet = new Set(votesRes.results.map((v) => v.feature_id));
  }

  const items = listRes.results.map((f) => ({
    ...f,
    user_voted: votedSet.has(f.id),
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

/** GET /api/features/:id */
export async function getFeature(
  id: number,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  const feature = await env.DB.prepare(
    `SELECT * FROM feature_requests WHERE id = ?`
  ).bind(id).first<FeatureRequest>();
  if (!feature) return error("Feature not found", 404, env);

  const identifier = getIdentifier(user);
  const vote = await env.DB.prepare(
    `SELECT id FROM votes WHERE feature_id = ? AND voter_identifier = ?`
  ).bind(id, identifier).first();

  return json({ ...feature, user_voted: !!vote }, 200, env);
}

/** POST /api/features */
export async function createFeature(
  request: Request,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  const body = (await request.json()) as {
    title?: string;
    description?: string;
    category?: string;
    author_name?: string;
    author_email?: string;
    turnstile_token?: string;
  };

  if (!body.title?.trim() || !body.description?.trim()) {
    return error("Title and description are required", 400, env);
  }

  if (!user) {
    if (!body.author_name?.trim()) {
      return error("Name is required for guests", 400, env);
    }
    if (body.turnstile_token) {
      const ip = request.headers.get("CF-Connecting-IP") || "";
      const ok = await verifyTurnstile(body.turnstile_token, ip, env);
      if (!ok) return error("Turnstile verification failed", 403, env);
    }
  }

  const category = FEATURE_CATEGORIES.includes(
    body.category as typeof FEATURE_CATEGORIES[number]
  )
    ? body.category!
    : "general";

  const result = await env.DB.prepare(
    `INSERT INTO feature_requests (title, description, category, author_name, author_email, author_user_id, is_verified)
     VALUES (?, ?, ?, ?, ?, ?, ?)`
  )
    .bind(
      sanitizeTitle(body.title!),
      sanitize(body.description!),
      category,
      user ? sanitize(user.display_name || "User") : sanitize(body.author_name!),
      user ? null : (body.author_email || null),
      user ? user.user_id : null,
      user ? 1 : 0
    )
    .run();

  const newId = result.meta.last_row_id;
  return json({ id: newId, message: "Feature request created" }, 201, env);
}

/** POST /api/features/:id/vote */
export async function toggleVote(
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
    return error("Email or login required to vote", 400, env);
  }

  if (!user && body.turnstile_token) {
    const ip = request.headers.get("CF-Connecting-IP") || "";
    const ok = await verifyTurnstile(body.turnstile_token, ip, env);
    if (!ok) return error("Turnstile verification failed", 403, env);
  }

  const weight = user ? 2 : 1;

  const existing = await env.DB.prepare(
    `SELECT id, weight FROM votes WHERE feature_id = ? AND voter_identifier = ?`
  ).bind(id, identifier).first<{ id: number; weight: number }>();

  if (existing) {
    await env.DB.batch([
      env.DB.prepare(`DELETE FROM votes WHERE id = ?`).bind(existing.id),
      env.DB.prepare(
        `UPDATE feature_requests SET vote_count = vote_count - ?, updated_at = datetime('now') WHERE id = ?`
      ).bind(existing.weight, id),
    ]);
    return json({ voted: false, message: "Vote removed" }, 200, env);
  }

  await env.DB.batch([
    env.DB.prepare(
      `INSERT INTO votes (feature_id, voter_identifier, is_verified, weight) VALUES (?, ?, ?, ?)`
    ).bind(id, identifier, user ? 1 : 0, weight),
    env.DB.prepare(
      `UPDATE feature_requests SET vote_count = vote_count + ?, updated_at = datetime('now') WHERE id = ?`
    ).bind(weight, id),
  ]);

  return json({ voted: true, message: "Vote added" }, 200, env);
}

/** PUT /api/features/:id/status (Admin only) */
export async function updateFeatureStatus(
  id: number,
  request: Request,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  if (!user || !["admin", "super_admin"].includes(user.role)) {
    return error("Admin access required", 403, env);
  }

  const body = (await request.json()) as { status?: string };
  if (!body.status || !FEATURE_STATUSES.includes(body.status as typeof FEATURE_STATUSES[number])) {
    return error(`Invalid status. Allowed: ${FEATURE_STATUSES.join(", ")}`, 400, env);
  }

  await env.DB.prepare(
    `UPDATE feature_requests SET status = ?, updated_at = datetime('now') WHERE id = ?`
  ).bind(body.status, id).run();

  return json({ message: "Status updated" }, 200, env);
}
