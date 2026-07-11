import type { Env } from "./types";
import { verifyToken } from "./auth";
import { corsHeaders, json, error } from "./utils";
import {
  listFeatures,
  getFeature,
  createFeature,
  editFeature,
  deleteFeature,
  hideFeature,
  toggleVote,
  updateFeatureStatus,
} from "./features";
import {
  listDiscussions,
  getDiscussion,
  createDiscussion,
  editDiscussion,
  deleteDiscussion,
  toggleLike,
  hideDiscussion,
} from "./discussions";
import { listComments, createComment, editComment, deleteComment, hideComment } from "./comments";
import { isAdmin as checkAdmin } from "./utils";

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: corsHeaders(env) });
    }

    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method;

    const authHeader = request.headers.get("Authorization");
    const user = await verifyToken(authHeader, env);

    try {
      const response = await route(path, method, request, env, user, ctx);
      const headers = new Headers(response.headers);
      for (const [k, v] of Object.entries(corsHeaders(env))) {
        headers.set(k, v);
      }
      return new Response(response.body, {
        status: response.status,
        headers,
      });
    } catch (e) {
      console.error("Unhandled error:", e);
      return error(
        "Internal server error",
        500,
        env
      );
    }
  },
};

async function route(
  path: string,
  method: string,
  request: Request,
  env: Env,
  user: ReturnType<typeof verifyToken> extends Promise<infer T> ? T : never,
  ctx: ExecutionContext
): Promise<Response> {
  // --- Features ---
  const featuresMatch = path.match(/^\/api\/features(?:\/(\d+))?$/);
  if (featuresMatch) {
    const id = featuresMatch[1] ? parseInt(featuresMatch[1], 10) : null;

    if (method === "GET" && id === null) return listFeatures(request, env, user);
    if (method === "GET" && id !== null) return getFeature(id, env, user);
    if (method === "POST" && id === null) return createFeature(request, env, user, ctx);
    if (method === "PUT" && id !== null) return editFeature(id, request, env, user);
    if (method === "DELETE" && id !== null) return deleteFeature(id, env, user);
  }

  const hideFeatureMatch = path.match(/^\/api\/features\/(\d+)\/hide$/);
  if (hideFeatureMatch && method === "PUT") {
    return hideFeature(parseInt(hideFeatureMatch[1], 10), env, user);
  }

  const voteMatch = path.match(/^\/api\/features\/(\d+)\/vote$/);
  if (voteMatch && method === "POST") {
    return toggleVote(parseInt(voteMatch[1], 10), request, env, user);
  }

  const statusMatch = path.match(/^\/api\/features\/(\d+)\/status$/);
  if (statusMatch && method === "PUT") {
    return updateFeatureStatus(parseInt(statusMatch[1], 10), request, env, user);
  }

  // --- Discussions ---
  const discussionsMatch = path.match(/^\/api\/discussions(?:\/(\d+))?$/);
  if (discussionsMatch) {
    const id = discussionsMatch[1]
      ? parseInt(discussionsMatch[1], 10)
      : null;

    if (method === "GET" && id === null) return listDiscussions(request, env, user);
    if (method === "GET" && id !== null) return getDiscussion(id, env, user);
    if (method === "POST" && id === null) return createDiscussion(request, env, user, ctx);
    if (method === "PUT" && id !== null) return editDiscussion(id, request, env, user);
    if (method === "DELETE" && id !== null) return deleteDiscussion(id, env, user);
  }

  const likeMatch = path.match(/^\/api\/discussions\/(\d+)\/like$/);
  if (likeMatch && method === "POST") {
    return toggleLike(parseInt(likeMatch[1], 10), request, env, user);
  }

  const hideDiscMatch = path.match(/^\/api\/discussions\/(\d+)\/hide$/);
  if (hideDiscMatch && method === "PUT") {
    return hideDiscussion(parseInt(hideDiscMatch[1], 10), env, user);
  }

  // --- Comments ---
  if (path === "/api/comments") {
    if (method === "GET") return listComments(request, env);
    if (method === "POST") return createComment(request, env, user, ctx);
  }

  const commentMatch = path.match(/^\/api\/comments\/(\d+)$/);
  if (commentMatch) {
    const id = parseInt(commentMatch[1], 10);
    if (method === "PUT") return editComment(id, request, env, user);
    if (method === "DELETE") return deleteComment(id, env, user);
  }

  const hideCommentMatch = path.match(/^\/api\/comments\/(\d+)\/hide$/);
  if (hideCommentMatch && method === "PUT") {
    return hideComment(parseInt(hideCommentMatch[1], 10), env, user);
  }

  // --- Auth verify ---
  if (path === "/api/auth/verify" && method === "GET") {
    if (!user) return error("NO_TOKEN", 401, env);
    return json({
      verified: true,
      user_id: user.user_id,
      display_name: user.display_name,
      role: user.role,
    }, 200, env);
  }

  // --- Admin: batch delete ---
  if (path === "/api/admin/batch-delete" && method === "POST") {
    if (!checkAdmin(user)) return error("Admin access required", 403, env);
    const body = (await request.json()) as {
      features?: number[];
      discussions?: number[];
      comments?: number[];
    };
    const ops: Promise<unknown>[] = [];
    if (body.features?.length) {
      const ids = body.features.filter((n) => Number.isInteger(n));
      if (ids.length) {
        const ph = ids.map(() => "?").join(",");
        ops.push(
          env.DB.prepare(`DELETE FROM votes WHERE feature_id IN (${ph})`).bind(...ids).run(),
          env.DB.prepare(`DELETE FROM comments WHERE target_type='feature' AND target_id IN (${ph})`).bind(...ids).run(),
          env.DB.prepare(`DELETE FROM feature_requests WHERE id IN (${ph})`).bind(...ids).run(),
        );
      }
    }
    if (body.discussions?.length) {
      const ids = body.discussions.filter((n) => Number.isInteger(n));
      if (ids.length) {
        const ph = ids.map(() => "?").join(",");
        ops.push(
          env.DB.prepare(`DELETE FROM likes WHERE discussion_id IN (${ph})`).bind(...ids).run(),
          env.DB.prepare(`DELETE FROM comments WHERE target_type='discussion' AND target_id IN (${ph})`).bind(...ids).run(),
          env.DB.prepare(`DELETE FROM discussions WHERE id IN (${ph})`).bind(...ids).run(),
        );
      }
    }
    if (body.comments?.length) {
      const ids = body.comments.filter((n) => Number.isInteger(n));
      if (ids.length) {
        const ph = ids.map(() => "?").join(",");
        ops.push(
          env.DB.prepare(`DELETE FROM comments WHERE id IN (${ph})`).bind(...ids).run(),
        );
      }
    }
    await Promise.all(ops);
    return json({ deleted: true }, 200, env);
  }

  // --- Admin: recent content ---
  if (path === "/api/admin/recent" && method === "GET") {
    if (!checkAdmin(user)) return error("Admin access required", 403, env);

    const limit = 50;
    const [features, discussions, comments] = await Promise.all([
      env.DB.prepare(
        `SELECT id, title, description, category, status, author_name, author_user_id,
                is_verified, vote_count, comment_count, created_at, updated_at
         FROM feature_requests ORDER BY created_at DESC LIMIT ?`
      ).bind(limit).all(),
      env.DB.prepare(
        `SELECT id, title, body, category, author_name, author_user_id,
                is_verified, like_count, comment_count, is_hidden, created_at, updated_at
         FROM discussions ORDER BY created_at DESC LIMIT ?`
      ).bind(limit).all(),
      env.DB.prepare(
        `SELECT id, target_type, target_id, body, author_name, author_user_id,
                is_verified, is_hidden, created_at
         FROM comments ORDER BY created_at DESC LIMIT ?`
      ).bind(limit).all(),
    ]);

    return json({
      features: features.results,
      discussions: discussions.results,
      comments: comments.results,
    }, 200, env);
  }

  // --- Health ---
  if (path === "/api/health") {
    return json({ status: "ok", timestamp: new Date().toISOString() }, 200, env);
  }

  // --- Stats ---
  if (path === "/api/stats" && method === "GET") {
    const [features, discussions, comments] = await Promise.all([
      env.DB.prepare("SELECT COUNT(*) as c FROM feature_requests").first<{c: number}>(),
      env.DB.prepare("SELECT COUNT(*) as c FROM discussions WHERE is_hidden=0").first<{c: number}>(),
      env.DB.prepare("SELECT COUNT(*) as c FROM comments WHERE is_hidden=0").first<{c: number}>(),
    ]);
    return json({
      features: features?.c || 0,
      discussions: discussions?.c || 0,
      comments: comments?.c || 0,
    }, 200, env);
  }

  return error("Not found", 404, env);
}
