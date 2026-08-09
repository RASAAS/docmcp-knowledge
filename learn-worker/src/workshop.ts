import type { AuthUser, Env } from "./types";
import { error, json, sanitize, sha256Hex } from "./utils";

type GroupRow = {
  id: number;
  sort_order: number;
  name: string;
  content_json: string;
  updated_by: string;
  updated_at: string;
};

export type WorkshopSection = { id: string; title: string; body: string };

async function getSession(code: string, env: Env) {
  return env.DB.prepare(`SELECT * FROM live_sessions WHERE code=?`)
    .bind(code.toUpperCase())
    .first<{
      id: number;
      host_token_hash: string;
      host_user_id: string | null;
      status: string;
    }>();
}

function parseSections(raw: string): WorkshopSection[] {
  try {
    const v = JSON.parse(raw || '{"sections":[]}');
    const sections = Array.isArray(v?.sections) ? v.sections : Array.isArray(v) ? v : [];
    return sections
      .filter((s: unknown) => s && typeof s === "object")
      .map((s: { id?: string; title?: string; body?: string }, i: number) => ({
        id: sanitize(String(s.id || `s${i + 1}`), 40) || `s${i + 1}`,
        title: sanitize(String(s.title || ""), 120),
        body: sanitize(String(s.body || ""), 8000),
      }));
  } catch {
    return [];
  }
}

function serializeGroup(row: GroupRow) {
  return {
    id: row.id,
    sort_order: row.sort_order,
    name: row.name,
    sections: parseSections(row.content_json),
    updated_by: row.updated_by,
    updated_at: row.updated_at,
  };
}

async function canEditSession(
  session: { id: number; host_token_hash: string },
  request: Request,
  body: { host_token?: string; participant_key?: string },
  env: Env,
  opts?: { hostOnly?: boolean }
): Promise<boolean> {
  const hostToken = request.headers.get("X-Host-Token") || body.host_token || "";
  if (hostToken) {
    const hash = await sha256Hex(hostToken);
    if (hash === session.host_token_hash) return true;
  }
  if (opts?.hostOnly) return false;
  if (body.participant_key) {
    const p = await env.DB.prepare(
      `SELECT id FROM live_participants WHERE session_id=? AND participant_key=?`
    )
      .bind(session.id, body.participant_key)
      .first();
    return !!p;
  }
  return false;
}

async function listGroupsPayload(code: string, sessionId: number, env: Env) {
  const rows = await env.DB.prepare(
    `SELECT id, sort_order, name, content_json, updated_by, updated_at
     FROM workshop_groups WHERE session_id=? ORDER BY sort_order ASC, id ASC`
  )
    .bind(sessionId)
    .all<GroupRow>();
  return {
    code: code.toUpperCase(),
    groups: (rows.results || []).map(serializeGroup),
  };
}

export async function listWorkshopGroups(code: string, env: Env): Promise<Response> {
  const session = await getSession(code, env);
  if (!session) return error("Session not found", 404, env);
  if (session.status === "ended") return error("Session ended", 410, env);
  return json(await listGroupsPayload(code, session.id, env), 200, env);
}

export async function createWorkshopGroup(
  code: string,
  request: Request,
  env: Env,
  _user: AuthUser | null
): Promise<Response> {
  const session = await getSession(code, env);
  if (!session) return error("Session not found", 404, env);
  if (session.status === "ended") return error("Session ended", 410, env);

  const body = (await request.json().catch(() => ({}))) as {
    name?: string;
    host_token?: string;
  };
  if (!(await canEditSession(session, request, body, env, { hostOnly: true }))) {
    return error("Host token required to create groups", 403, env);
  }

  const name = sanitize((body.name || "").trim(), 80) || "Group";
  const maxRow = await env.DB.prepare(
    `SELECT COALESCE(MAX(sort_order), 0) AS m FROM workshop_groups WHERE session_id=?`
  )
    .bind(session.id)
    .first<{ m: number }>();
  const sortOrder = (maxRow?.m || 0) + 1;

  const countRow = await env.DB.prepare(
    `SELECT COUNT(*) AS c FROM workshop_groups WHERE session_id=?`
  )
    .bind(session.id)
    .first<{ c: number }>();
  if ((countRow?.c || 0) >= 24) return error("Too many groups (max 24)", 400, env);

  await env.DB.prepare(
    `INSERT INTO workshop_groups (session_id, sort_order, name, content_json, updated_by)
     VALUES (?, ?, ?, '{"sections":[]}', ?)`
  )
    .bind(session.id, sortOrder, name, "host")
    .run();

  return json(await listGroupsPayload(code, session.id, env), 201, env);
}

export async function updateWorkshopGroup(
  code: string,
  groupId: number,
  request: Request,
  env: Env
): Promise<Response> {
  const session = await getSession(code, env);
  if (!session) return error("Session not found", 404, env);
  if (session.status === "ended") return error("Session ended", 410, env);

  const body = (await request.json().catch(() => ({}))) as {
    name?: string;
    sections?: WorkshopSection[];
    updated_by?: string;
    host_token?: string;
    participant_key?: string;
  };

  if (!(await canEditSession(session, request, body, env))) {
    return error("Join the session or provide host token", 403, env);
  }

  const existing = await env.DB.prepare(
    `SELECT id FROM workshop_groups WHERE id=? AND session_id=?`
  )
    .bind(groupId, session.id)
    .first();
  if (!existing) return error("Group not found", 404, env);

  const updates: string[] = [];
  const binds: unknown[] = [];

  if (typeof body.name === "string") {
    updates.push("name=?");
    binds.push(sanitize(body.name.trim(), 80) || "Group");
  }
  if (Array.isArray(body.sections)) {
    const sections = body.sections.slice(0, 40).map((s, i) => ({
      id: sanitize(String(s?.id || `s${i + 1}`), 40) || `s${i + 1}`,
      title: sanitize(String(s?.title || ""), 120),
      body: sanitize(String(s?.body || ""), 8000),
    }));
    updates.push("content_json=?");
    binds.push(JSON.stringify({ sections }));
  }
  if (!updates.length) return error("Nothing to update", 400, env);

  updates.push("updated_by=?", "updated_at=datetime('now')");
  binds.push(sanitize(body.updated_by || "", 80));
  binds.push(groupId, session.id);

  await env.DB.prepare(
    `UPDATE workshop_groups SET ${updates.join(", ")} WHERE id=? AND session_id=?`
  )
    .bind(...binds)
    .run();

  return json(await listGroupsPayload(code, session.id, env), 200, env);
}

export async function deleteWorkshopGroup(
  code: string,
  groupId: number,
  request: Request,
  env: Env
): Promise<Response> {
  const session = await getSession(code, env);
  if (!session) return error("Session not found", 404, env);
  if (session.status === "ended") return error("Session ended", 410, env);

  const body = (await request.json().catch(() => ({}))) as { host_token?: string };
  if (!(await canEditSession(session, request, body, env, { hostOnly: true }))) {
    return error("Host token required to delete groups", 403, env);
  }

  await env.DB.prepare(`DELETE FROM workshop_groups WHERE id=? AND session_id=?`)
    .bind(groupId, session.id)
    .run();

  return json(await listGroupsPayload(code, session.id, env), 200, env);
}
