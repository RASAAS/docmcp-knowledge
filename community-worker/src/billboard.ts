/**
 * Priority Billboard -- Admin-curated ranking list.
 * Visitors/users may vote and comment; only Admin creates/edits items.
 */
import type { Env, AuthUser, BillboardItem } from "./types";
import { FEATURE_CATEGORIES, BILLBOARD_STATUSES } from "./types";
import { json, error, sanitize, sanitizeTitle, isAdmin } from "./utils";
import { verifyTurnstile, getIdentifier } from "./auth";

/** GET /api/billboard?category=&sort=votes|newest&page=1&include_drafts=1 */
export async function listBillboard(
  request: Request,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  const url = new URL(request.url);
  const category = url.searchParams.get("category") || "";
  const sort = url.searchParams.get("sort") || "votes";
  const page = Math.max(1, parseInt(url.searchParams.get("page") || "1", 10));
  const includeDrafts = url.searchParams.get("include_drafts") === "1" && isAdmin(user);
  const limit = 50;
  const offset = (page - 1) * limit;

  const orderBy =
    sort === "newest"
      ? "created_at DESC"
      : sort === "updated"
        ? "updated_at DESC"
        : "vote_count DESC, created_at DESC";

  let where = includeDrafts ? "1=1" : "is_published = 1";
  const params: unknown[] = [];
  if (category && FEATURE_CATEGORIES.includes(category as typeof FEATURE_CATEGORIES[number])) {
    where += " AND category = ?";
    params.push(category);
  }

  const [countRes, listRes] = await Promise.all([
    env.DB.prepare(`SELECT COUNT(*) as total FROM billboard_items WHERE ${where}`)
      .bind(...params)
      .first<{ total: number }>(),
    env.DB.prepare(
      `SELECT id, title, description, category, status, source_feature_id,
              vote_count, comment_count, is_published, created_by,
              created_at, updated_at
       FROM billboard_items WHERE ${where} ORDER BY ${orderBy} LIMIT ? OFFSET ?`
    )
      .bind(...params, limit, offset)
      .all<BillboardItem>(),
  ]);

  const identifier = getIdentifier(user);
  let votedSet = new Set<number>();
  if (listRes.results.length > 0 && !identifier.startsWith("anon:")) {
    const ids = listRes.results.map((b) => b.id);
    const ph = ids.map(() => "?").join(",");
    const votesRes = await env.DB.prepare(
      `SELECT billboard_id FROM billboard_votes WHERE voter_identifier = ? AND billboard_id IN (${ph})`
    )
      .bind(identifier, ...ids)
      .all<{ billboard_id: number }>();
    votedSet = new Set(votesRes.results.map((v) => v.billboard_id));
  }

  const items = listRes.results.map((b, idx) => ({
    ...b,
    rank: offset + idx + 1,
    user_voted: votedSet.has(b.id),
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

/** POST /api/billboard (Admin) */
export async function createBillboardItem(
  request: Request,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  if (!isAdmin(user)) return error("Admin access required", 403, env);

  const body = (await request.json()) as {
    title?: string;
    description?: string;
    category?: string;
    status?: string;
    source_feature_id?: number;
    is_published?: boolean;
  };

  if (!body.title?.trim()) return error("Title is required", 400, env);

  const category = FEATURE_CATEGORIES.includes(
    body.category as typeof FEATURE_CATEGORIES[number]
  )
    ? body.category!
    : "general";
  const status = BILLBOARD_STATUSES.includes(
    body.status as typeof BILLBOARD_STATUSES[number]
  )
    ? body.status!
    : "planned";

  let sourceFeatureId: number | null = null;
  if (body.source_feature_id && Number.isInteger(body.source_feature_id)) {
    const feat = await env.DB.prepare(
      `SELECT id FROM feature_requests WHERE id = ?`
    )
      .bind(body.source_feature_id)
      .first<{ id: number }>();
    if (!feat) return error("Source feature not found", 404, env);
    sourceFeatureId = feat.id;
  }

  const result = await env.DB.prepare(
    `INSERT INTO billboard_items
      (title, description, category, status, source_feature_id, is_published, created_by)
     VALUES (?, ?, ?, ?, ?, ?, ?)`
  )
    .bind(
      sanitizeTitle(body.title),
      sanitize(body.description || ""),
      category,
      status,
      sourceFeatureId,
      body.is_published === false ? 0 : 1,
      user!.user_id
    )
    .run();

  return json({ id: result.meta.last_row_id, message: "Billboard item created" }, 201, env);
}

/** POST /api/billboard/from-feature/:featureId (Admin) */
export async function createFromFeature(
  featureId: number,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  if (!isAdmin(user)) return error("Admin access required", 403, env);

  const feature = await env.DB.prepare(
    `SELECT id, title, description, category FROM feature_requests WHERE id = ?`
  )
    .bind(featureId)
    .first<{ id: number; title: string; description: string; category: string }>();
  if (!feature) return error("Feature not found", 404, env);

  const existing = await env.DB.prepare(
    `SELECT id FROM billboard_items WHERE source_feature_id = ?`
  )
    .bind(featureId)
    .first<{ id: number }>();
  if (existing) {
    return error(`Already on billboard (id=${existing.id})`, 409, env);
  }

  const result = await env.DB.prepare(
    `INSERT INTO billboard_items
      (title, description, category, status, source_feature_id, is_published, created_by)
     VALUES (?, ?, ?, 'planned', ?, 1, ?)`
  )
    .bind(
      feature.title,
      feature.description,
      feature.category,
      feature.id,
      user!.user_id
    )
    .run();

  await env.DB.prepare(
    `UPDATE feature_requests SET status = 'planned', updated_at = datetime('now') WHERE id = ? AND status = 'under_review'`
  )
    .bind(featureId)
    .run();

  return json(
    { id: result.meta.last_row_id, message: "Added to billboard from feature" },
    201,
    env
  );
}

/** PUT /api/billboard/:id (Admin) */
export async function editBillboardItem(
  id: number,
  request: Request,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  if (!isAdmin(user)) return error("Admin access required", 403, env);

  const existing = await env.DB.prepare(
    `SELECT id FROM billboard_items WHERE id = ?`
  )
    .bind(id)
    .first();
  if (!existing) return error("Billboard item not found", 404, env);

  const body = (await request.json()) as {
    title?: string;
    description?: string;
    category?: string;
    status?: string;
    is_published?: boolean;
  };

  const updates: string[] = [];
  const params: unknown[] = [];

  if (body.title?.trim()) {
    updates.push("title = ?");
    params.push(sanitizeTitle(body.title));
  }
  if (typeof body.description === "string") {
    updates.push("description = ?");
    params.push(sanitize(body.description));
  }
  if (body.category && FEATURE_CATEGORIES.includes(body.category as typeof FEATURE_CATEGORIES[number])) {
    updates.push("category = ?");
    params.push(body.category);
  }
  if (body.status && BILLBOARD_STATUSES.includes(body.status as typeof BILLBOARD_STATUSES[number])) {
    updates.push("status = ?");
    params.push(body.status);
  }
  if (typeof body.is_published === "boolean") {
    updates.push("is_published = ?");
    params.push(body.is_published ? 1 : 0);
  }
  if (updates.length === 0) return error("No changes", 400, env);

  updates.push("updated_at = datetime('now')");
  params.push(id);

  await env.DB.prepare(
    `UPDATE billboard_items SET ${updates.join(", ")} WHERE id = ?`
  )
    .bind(...params)
    .run();

  return json({ message: "Billboard item updated" }, 200, env);
}

/** DELETE /api/billboard/:id (Admin) */
export async function deleteBillboardItem(
  id: number,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  if (!isAdmin(user)) return error("Admin access required", 403, env);

  const existing = await env.DB.prepare(
    `SELECT id FROM billboard_items WHERE id = ?`
  )
    .bind(id)
    .first();
  if (!existing) return error("Billboard item not found", 404, env);

  await env.DB.batch([
    env.DB.prepare(`DELETE FROM comments WHERE target_type = 'billboard' AND target_id = ?`).bind(id),
    env.DB.prepare(`DELETE FROM billboard_votes WHERE billboard_id = ?`).bind(id),
    env.DB.prepare(`DELETE FROM billboard_items WHERE id = ?`).bind(id),
  ]);

  return json({ message: "Billboard item deleted" }, 200, env);
}

/** POST /api/billboard/:id/vote */
export async function toggleBillboardVote(
  id: number,
  request: Request,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  const body = (await request.json().catch(() => ({}))) as {
    author_email?: string;
    turnstile_token?: string;
  };

  const item = await env.DB.prepare(
    `SELECT id, is_published FROM billboard_items WHERE id = ?`
  )
    .bind(id)
    .first<{ id: number; is_published: number }>();
  if (!item) return error("Billboard item not found", 404, env);
  if (!item.is_published && !isAdmin(user)) {
    return error("Billboard item not found", 404, env);
  }

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
    `SELECT id, weight FROM billboard_votes WHERE billboard_id = ? AND voter_identifier = ?`
  )
    .bind(id, identifier)
    .first<{ id: number; weight: number }>();

  if (existing) {
    await env.DB.batch([
      env.DB.prepare(`DELETE FROM billboard_votes WHERE id = ?`).bind(existing.id),
      env.DB.prepare(
        `UPDATE billboard_items SET vote_count = vote_count - ?, updated_at = datetime('now') WHERE id = ?`
      ).bind(existing.weight, id),
    ]);
    return json({ voted: false, message: "Vote removed" }, 200, env);
  }

  await env.DB.batch([
    env.DB.prepare(
      `INSERT INTO billboard_votes (billboard_id, voter_identifier, is_verified, weight) VALUES (?, ?, ?, ?)`
    ).bind(id, identifier, user ? 1 : 0, weight),
    env.DB.prepare(
      `UPDATE billboard_items SET vote_count = vote_count + ?, updated_at = datetime('now') WHERE id = ?`
    ).bind(weight, id),
  ]);

  return json({ voted: true, message: "Vote added" }, 200, env);
}
