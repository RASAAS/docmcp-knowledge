import type { Env } from "./types";
import { verifyToken } from "./auth";
import { corsHeaders, json, error } from "./utils";
import {
  listFeatures,
  getFeature,
  createFeature,
  toggleVote,
  updateFeatureStatus,
} from "./features";
import {
  listDiscussions,
  getDiscussion,
  createDiscussion,
  toggleLike,
  hideDiscussion,
} from "./discussions";
import { listComments, createComment, hideComment } from "./comments";

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: corsHeaders(env) });
    }

    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method;

    const authHeader = request.headers.get("Authorization");
    const user = await verifyToken(authHeader, env);

    try {
      const response = await route(path, method, request, env, user);
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
  user: ReturnType<typeof verifyToken> extends Promise<infer T> ? T : never
): Promise<Response> {
  // --- Features ---
  const featuresMatch = path.match(/^\/api\/features(?:\/(\d+))?$/);
  if (featuresMatch) {
    const id = featuresMatch[1] ? parseInt(featuresMatch[1], 10) : null;

    if (method === "GET" && id === null) return listFeatures(request, env, user);
    if (method === "GET" && id !== null) return getFeature(id, env, user);
    if (method === "POST" && id === null) return createFeature(request, env, user);
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
    if (method === "POST" && id === null) return createDiscussion(request, env, user);
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
    if (method === "POST") return createComment(request, env, user);
  }

  const hideCommentMatch = path.match(/^\/api\/comments\/(\d+)\/hide$/);
  if (hideCommentMatch && method === "PUT") {
    return hideComment(parseInt(hideCommentMatch[1], 10), env, user);
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
