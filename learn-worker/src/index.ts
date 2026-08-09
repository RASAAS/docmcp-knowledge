import type { Env } from "./types";
import { verifyHubToken } from "./auth";
import { corsHeaders, error, json } from "./utils";
import { getCourse, getPracticeQuestions, listCourses } from "./courses";
import {
  createSession,
  getParticipantState,
  hostAction,
  hostOverview,
  joinSession,
  linkParticipantAccount,
  submitAnswer,
} from "./live";
import { submitPractice } from "./practice";

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: corsHeaders(env) });
    }

    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method;
    const user = await verifyHubToken(request.headers.get("Authorization"), env);

    try {
      const response = await route(path, method, request, env, user);
      const headers = new Headers(response.headers);
      for (const [k, v] of Object.entries(corsHeaders(env))) headers.set(k, v);
      return new Response(response.body, { status: response.status, headers });
    } catch (e) {
      console.error("Unhandled learn-api error:", e);
      return error("Internal server error", 500, env);
    }
  },
};

async function route(
  path: string,
  method: string,
  request: Request,
  env: Env,
  user: Awaited<ReturnType<typeof verifyHubToken>>
): Promise<Response> {
  if (path === "/api/health") {
    return json({ status: "ok", service: "learn-api", timestamp: new Date().toISOString() }, 200, env);
  }

  if (path === "/api/auth/verify" && method === "GET") {
    if (!user) return error("NO_TOKEN", 401, env);
    return json(
      {
        verified: true,
        user_id: user.user_id,
        display_name: user.display_name,
        role: user.role,
      },
      200,
      env
    );
  }

  if (path === "/api/courses" && method === "GET") {
    return listCourses(env);
  }

  const courseMatch = path.match(/^\/api\/courses\/([a-z0-9-]+)$/);
  if (courseMatch && method === "GET") {
    const includeAnswers = new URL(request.url).searchParams.get("answers") === "1";
    // Never expose answers publicly unless admin (host uses live flow)
    if (includeAnswers && (!user || !["admin", "super_admin"].includes(user.role))) {
      return getPracticeQuestions(courseMatch[1], env);
    }
    return getCourse(courseMatch[1], env, { includeAnswers, user });
  }

  const practiceMatch = path.match(/^\/api\/courses\/([a-z0-9-]+)\/practice$/);
  if (practiceMatch) {
    if (method === "GET") return getPracticeQuestions(practiceMatch[1], env);
    if (method === "POST") return submitPractice(practiceMatch[1], request, env, user);
  }

  if (path === "/api/live/sessions" && method === "POST") {
    return createSession(request, env, user);
  }

  const joinMatch = path.match(/^\/api\/live\/sessions\/([A-Z0-9]+)\/join$/i);
  if (joinMatch && method === "POST") {
    return joinSession(joinMatch[1], request, env, user);
  }

  const stateMatch = path.match(/^\/api\/live\/sessions\/([A-Z0-9]+)\/state$/i);
  if (stateMatch && method === "GET") {
    return getParticipantState(stateMatch[1], request, env);
  }

  const answerMatch = path.match(/^\/api\/live\/sessions\/([A-Z0-9]+)\/answer$/i);
  if (answerMatch && method === "POST") {
    return submitAnswer(answerMatch[1], request, env);
  }

  const linkMatch = path.match(/^\/api\/live\/sessions\/([A-Z0-9]+)\/link$/i);
  if (linkMatch && method === "POST") {
    return linkParticipantAccount(linkMatch[1], request, env, user);
  }

  const hostMatch = path.match(
    /^\/api\/live\/sessions\/([A-Z0-9]+)\/(push|lock|reveal|waiting|end|stats)$/i
  );
  if (hostMatch && method === "POST") {
    const action = hostMatch[2].toLowerCase() as "push" | "lock" | "reveal" | "waiting" | "end" | "stats";
    return hostAction(hostMatch[1], action, request, env);
  }

  const hostGet = path.match(/^\/api\/live\/sessions\/([A-Z0-9]+)\/host$/i);
  if (hostGet && method === "GET") {
    return hostOverview(hostGet[1], request, env);
  }

  return error("Not found", 404, env);
}
