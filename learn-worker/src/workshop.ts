import type { Env } from "./types";
import { error, json, sanitize, sha256Hex } from "./utils";

type BoardRow = {
  group_no: number;
  task1_json: string;
  task2_json: string;
  task3_json: string;
  task4_json: string;
  updated_by: string;
  updated_at: string;
};

const EMPTY_TASK = "{}";

async function getSession(code: string, env: Env) {
  return env.DB.prepare(`SELECT * FROM live_sessions WHERE code=?`)
    .bind(code.toUpperCase())
    .first<{
      id: number;
      host_token_hash: string;
      status: string;
    }>();
}

async function ensureBoards(sessionId: number, env: Env): Promise<void> {
  for (let g = 1; g <= 4; g++) {
    await env.DB.prepare(
      `INSERT OR IGNORE INTO workshop_boards
       (session_id, group_no, task1_json, task2_json, task3_json, task4_json, updated_by)
       VALUES (?, ?, '{}', '{}', '{}', '{}', '')`
    )
      .bind(sessionId, g)
      .run();
  }
}

function parseTask(raw: string): Record<string, unknown> {
  try {
    const v = JSON.parse(raw || EMPTY_TASK);
    return v && typeof v === "object" && !Array.isArray(v) ? (v as Record<string, unknown>) : {};
  } catch {
    return {};
  }
}

function serializeBoard(row: BoardRow) {
  return {
    group_no: row.group_no,
    task1: parseTask(row.task1_json),
    task2: parseTask(row.task2_json),
    task3: parseTask(row.task3_json),
    task4: parseTask(row.task4_json),
    updated_by: row.updated_by,
    updated_at: row.updated_at,
  };
}

export async function listWorkshopBoards(code: string, env: Env): Promise<Response> {
  const session = await getSession(code, env);
  if (!session) return error("Session not found", 404, env);
  if (session.status === "ended") return error("Session ended", 410, env);

  await ensureBoards(session.id, env);
  const rows = await env.DB.prepare(
    `SELECT group_no, task1_json, task2_json, task3_json, task4_json, updated_by, updated_at
     FROM workshop_boards WHERE session_id=? ORDER BY group_no ASC`
  )
    .bind(session.id)
    .all<BoardRow>();

  return json(
    {
      code: code.toUpperCase(),
      groups: (rows.results || []).map(serializeBoard),
      template: {
        task1: {
          users: "",
          environment: "",
          intended_use: "",
          pof_candidates: "",
          foreseeable_misuse: "",
        },
        task2: {
          use_errors: "",
          summative_candidates: "",
          primary_hrus: "",
        },
        task3: {
          inherent_safety: "",
          protective: "",
          information_for_safety: "",
          needs_ue_eval: "",
        },
        task4: {
          formative_needed: "",
          summative_needed: "",
          success_criteria: "",
          failure_reentry: "",
        },
      },
    },
    200,
    env
  );
}

export async function upsertWorkshopBoard(
  code: string,
  groupNo: number,
  request: Request,
  env: Env
): Promise<Response> {
  if (groupNo < 1 || groupNo > 4) return error("group must be 1-4", 400, env);

  const session = await getSession(code, env);
  if (!session) return error("Session not found", 404, env);
  if (session.status === "ended") return error("Session ended", 410, env);

  const body = (await request.json().catch(() => ({}))) as {
    task1?: Record<string, unknown>;
    task2?: Record<string, unknown>;
    task3?: Record<string, unknown>;
    task4?: Record<string, unknown>;
    updated_by?: string;
    host_token?: string;
    participant_key?: string;
  };

  // Allow host token OR any participant of this session.
  const hostToken = request.headers.get("X-Host-Token") || body.host_token || "";
  let allowed = false;
  if (hostToken) {
    const hash = await sha256Hex(hostToken);
    allowed = hash === session.host_token_hash;
  }
  if (!allowed && body.participant_key) {
    const p = await env.DB.prepare(
      `SELECT id FROM live_participants WHERE session_id=? AND participant_key=?`
    )
      .bind(session.id, body.participant_key)
      .first();
    allowed = !!p;
  }
  if (!allowed) return error("Join the session or provide host token", 403, env);

  await ensureBoards(session.id, env);

  const updatedBy = sanitize(body.updated_by || "", 80);
  const t1 = JSON.stringify(body.task1 || {});
  const t2 = JSON.stringify(body.task2 || {});
  const t3 = JSON.stringify(body.task3 || {});
  const t4 = JSON.stringify(body.task4 || {});

  await env.DB.prepare(
    `UPDATE workshop_boards
     SET task1_json=?, task2_json=?, task3_json=?, task4_json=?,
         updated_by=?, updated_at=datetime('now')
     WHERE session_id=? AND group_no=?`
  )
    .bind(t1, t2, t3, t4, updatedBy, session.id, groupNo)
    .run();

  return listWorkshopBoards(code, env);
}
