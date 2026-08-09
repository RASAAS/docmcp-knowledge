import type { AuthUser, Env, LiveSessionRow, QuestionRow } from "./types";
import {
  arraysEqualAsSet,
  error,
  json,
  randomCode,
  randomToken,
  sanitize,
  sha256Hex,
} from "./utils";

async function getSessionByCode(code: string, env: Env): Promise<LiveSessionRow | null> {
  return env.DB.prepare(`SELECT * FROM live_sessions WHERE code=?`)
    .bind(code.toUpperCase())
    .first<LiveSessionRow>();
}

async function requireHost(session: LiveSessionRow, hostToken: string | null, env: Env): Promise<boolean> {
  if (!hostToken) return false;
  const hash = await sha256Hex(hostToken);
  return hash === session.host_token_hash;
}

function parseAnswers(raw: unknown): string[] {
  if (!Array.isArray(raw)) return [];
  return raw.filter((x): x is string => typeof x === "string").map((s) => s.trim()).filter(Boolean);
}

function publicQuestionForPhase(q: QuestionRow, phase: string) {
  const base = {
    id: q.id,
    qid: q.qid,
    qtype: q.qtype,
    prompt_en: q.prompt_en,
    prompt_zh: q.prompt_zh,
    options: JSON.parse(q.options_json),
  };
  if (phase === "reveal") {
    return {
      ...base,
      correct: JSON.parse(q.correct_json),
      explanation_en: q.explanation_en,
      explanation_zh: q.explanation_zh,
    };
  }
  return base;
}

export async function createSession(request: Request, env: Env, user: AuthUser | null): Promise<Response> {
  // Hosting requires a registered DocMCP / Hub account (same gate as practice).
  if (!user) return error("LOGIN_REQUIRED", 401, env);

  if (env.HOST_CREATE_SECRET) {
    const createSecret = request.headers.get("X-Create-Secret") || "";
    if (createSecret !== env.HOST_CREATE_SECRET) {
      return error("Create secret required", 403, env);
    }
  }

  const body = (await request.json().catch(() => ({}))) as {
    course_slug?: string;
    title?: string;
  };
  const slug = (body.course_slug || "").trim();
  if (!slug) return error("course_slug required", 400, env);
  const course = await env.DB.prepare(`SELECT id FROM courses WHERE slug=? AND published=1`)
    .bind(slug)
    .first<{ id: number }>();
  if (!course) return error("Course not found", 404, env);

  const hostToken = randomToken(24);
  const hostHash = await sha256Hex(hostToken);

  let code = "";
  for (let i = 0; i < 8; i++) {
    const candidate = randomCode(6);
    const exists = await env.DB.prepare(`SELECT id FROM live_sessions WHERE code=?`)
      .bind(candidate)
      .first();
    if (!exists) {
      code = candidate;
      break;
    }
  }
  if (!code) return error("Failed to allocate session code", 500, env);

  const title = sanitize(body.title || "", 120);
  const expires = new Date(Date.now() + 12 * 3600 * 1000).toISOString().replace("T", " ").slice(0, 19);

  await env.DB.prepare(
    `INSERT INTO live_sessions
       (code, course_id, host_token_hash, host_user_id, status, phase, title, expires_at)
     VALUES (?, ?, ?, ?, 'lobby', 'waiting', ?, ?)`
  )
    .bind(code, course.id, hostHash, user.user_id, title, expires)
    .run();

  return json(
    {
      code,
      host_token: hostToken,
      course_slug: slug,
      join_path: `/learn/?code=${code}`,
      host_user_id: user.user_id,
    },
    201,
    env
  );
}

/** List non-ended live sessions owned by the authenticated host (no host_token). */
export async function listMyHostSessions(env: Env, user: AuthUser | null): Promise<Response> {
  if (!user) return error("LOGIN_REQUIRED", 401, env);
  const rows = await env.DB.prepare(
    `SELECT s.code, s.title, s.status, s.phase, s.created_at, s.updated_at,
            c.slug AS course_slug, c.title_en AS course_title_en, c.title_zh AS course_title_zh
     FROM live_sessions s
     JOIN courses c ON c.id = s.course_id
     WHERE s.host_user_id=? AND s.status != 'ended'
     ORDER BY s.updated_at DESC
     LIMIT 30`
  )
    .bind(user.user_id)
    .all();
  return json({ items: rows.results || [] }, 200, env);
}

/**
 * Reclaim host control for a session owned by the logged-in user.
 * Issues a new host_token (invalidates previous token hash).
 */
export async function reclaimHostSession(
  code: string,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  if (!user) return error("LOGIN_REQUIRED", 401, env);
  const session = await getSessionByCode(code, env);
  if (!session) return error("Session not found", 404, env);
  if (session.status === "ended") return error("Session ended", 410, env);
  if (!session.host_user_id || session.host_user_id !== user.user_id) {
    return error("NOT_YOUR_SESSION", 403, env);
  }

  const hostToken = randomToken(24);
  const hostHash = await sha256Hex(hostToken);
  await env.DB.prepare(
    `UPDATE live_sessions SET host_token_hash=?, updated_at=datetime('now') WHERE id=?`
  )
    .bind(hostHash, session.id)
    .run();

  const course = await env.DB.prepare(`SELECT slug FROM courses WHERE id=?`)
    .bind(session.course_id)
    .first<{ slug: string }>();

  return json(
    {
      code: session.code,
      host_token: hostToken,
      course_slug: course?.slug || "",
      title: session.title,
      status: session.status,
      phase: session.phase,
    },
    200,
    env
  );
}

export async function joinSession(code: string, request: Request, env: Env, user: AuthUser | null): Promise<Response> {
  const session = await getSessionByCode(code, env);
  if (!session) return error("Session not found", 404, env);
  if (session.status === "ended") return error("Session ended", 410, env);

  const body = (await request.json().catch(() => ({}))) as {
    nickname?: string;
    display_name?: string;
    participant_key?: string;
  };

  const nickname = sanitize((body.nickname || "").trim(), 40);
  if (!nickname || nickname.length < 1) return error("Nickname required", 400, env);

  const displayName = sanitize((body.display_name || "").trim(), 80);
  let participantKey = sanitize((body.participant_key || "").trim(), 64);
  if (!participantKey || participantKey.length < 8) {
    participantKey = randomToken(16);
  }

  const existing = await env.DB.prepare(
    `SELECT id, nickname, display_name, user_id FROM live_participants
     WHERE session_id=? AND participant_key=?`
  )
    .bind(session.id, participantKey)
    .first<{ id: number; nickname: string; display_name: string; user_id: string | null }>();

  if (existing) {
    await env.DB.prepare(
      `UPDATE live_participants SET nickname=?, display_name=?, user_id=COALESCE(?, user_id)
       WHERE id=?`
    )
      .bind(nickname, displayName, user?.user_id || null, existing.id)
      .run();
    return json(
      {
        participant_key: participantKey,
        participant_id: existing.id,
        nickname,
        display_name: displayName,
        session_code: session.code,
      },
      200,
      env
    );
  }

  const result = await env.DB.prepare(
    `INSERT INTO live_participants (session_id, participant_key, nickname, display_name, user_id)
     VALUES (?, ?, ?, ?, ?)`
  )
    .bind(session.id, participantKey, nickname, displayName, user?.user_id || null)
    .run();

  return json(
    {
      participant_key: participantKey,
      participant_id: result.meta.last_row_id,
      nickname,
      display_name: displayName,
      session_code: session.code,
    },
    201,
    env
  );
}

export async function getParticipantState(
  code: string,
  request: Request,
  env: Env
): Promise<Response> {
  const session = await getSessionByCode(code, env);
  if (!session) return error("Session not found", 404, env);

  const url = new URL(request.url);
  const participantKey = url.searchParams.get("participant_key") || "";

  let myAnswer: string[] | null = null;
  let participantId: number | null = null;
  if (participantKey) {
    const p = await env.DB.prepare(
      `SELECT id FROM live_participants WHERE session_id=? AND participant_key=?`
    )
      .bind(session.id, participantKey)
      .first<{ id: number }>();
    participantId = p?.id ?? null;
    if (participantId && session.current_question_id) {
      const ans = await env.DB.prepare(
        `SELECT answer_json FROM live_answers
         WHERE session_id=? AND question_id=? AND participant_id=?`
      )
        .bind(session.id, session.current_question_id, participantId)
        .first<{ answer_json: string }>();
      if (ans) myAnswer = JSON.parse(ans.answer_json);
    }
  }

  let question = null;
  if (session.current_question_id && session.phase !== "waiting") {
    const q = await env.DB.prepare(`SELECT * FROM questions WHERE id=?`)
      .bind(session.current_question_id)
      .first<QuestionRow>();
    if (q) question = publicQuestionForPhase(q, session.phase);
  }

  const count = await env.DB.prepare(
    `SELECT COUNT(*) AS c FROM live_participants WHERE session_id=?`
  )
    .bind(session.id)
    .first<{ c: number }>();

  return json(
    {
      code: session.code,
      status: session.status,
      phase: session.phase,
      title: session.title,
      participant_count: count?.c || 0,
      question,
      my_answer: myAnswer,
      can_answer: session.phase === "open" && !!participantId,
    },
    200,
    env
  );
}

export async function submitAnswer(
  code: string,
  request: Request,
  env: Env
): Promise<Response> {
  const session = await getSessionByCode(code, env);
  if (!session) return error("Session not found", 404, env);
  if (session.phase !== "open") return error("Answering is closed", 409, env);
  if (!session.current_question_id) return error("No active question", 409, env);

  const body = (await request.json().catch(() => ({}))) as {
    participant_key?: string;
    answer?: string[];
  };
  const participantKey = (body.participant_key || "").trim();
  if (!participantKey) return error("participant_key required", 400, env);

  const p = await env.DB.prepare(
    `SELECT id FROM live_participants WHERE session_id=? AND participant_key=?`
  )
    .bind(session.id, participantKey)
    .first<{ id: number }>();
  if (!p) return error("Not joined", 403, env);

  const q = await env.DB.prepare(`SELECT * FROM questions WHERE id=?`)
    .bind(session.current_question_id)
    .first<QuestionRow>();
  if (!q) return error("Question not found", 404, env);

  let answers = parseAnswers(body.answer);
  if (q.qtype === "single" && answers.length > 1) answers = [answers[0]];
  if (answers.length === 0) return error("Answer required", 400, env);

  const correct = JSON.parse(q.correct_json) as string[];
  const isCorrect = arraysEqualAsSet(answers, correct) ? 1 : 0;

  await env.DB.prepare(
    `INSERT INTO live_answers (session_id, question_id, participant_id, answer_json, is_correct)
     VALUES (?, ?, ?, ?, ?)
     ON CONFLICT(session_id, question_id, participant_id)
     DO UPDATE SET answer_json=excluded.answer_json, is_correct=excluded.is_correct,
                   answered_at=datetime('now')`
  )
    .bind(session.id, q.id, p.id, JSON.stringify(answers), isCorrect)
    .run();

  return json({ ok: true, accepted: true }, 200, env);
}

export async function hostAction(
  code: string,
  action: "push" | "lock" | "reveal" | "waiting" | "end" | "stats",
  request: Request,
  env: Env
): Promise<Response> {
  const session = await getSessionByCode(code, env);
  if (!session) return error("Session not found", 404, env);

  const hostToken = request.headers.get("X-Host-Token");
  if (!(await requireHost(session, hostToken, env))) {
    return error("Host token required", 403, env);
  }

  if (action === "stats") {
    return hostStats(session, env);
  }

  if (action === "end") {
    await env.DB.prepare(
      `UPDATE live_sessions SET status='ended', phase='waiting', current_question_id=NULL,
       updated_at=datetime('now') WHERE id=?`
    )
      .bind(session.id)
      .run();
    // Return full host snapshot so UI need not issue a second GET.
    return hostStats(
      { ...session, status: "ended", phase: "waiting", current_question_id: null },
      env,
      false,
      { includeQuestionList: false }
    );
  }

  if (action === "waiting") {
    await env.DB.prepare(
      `UPDATE live_sessions SET phase='waiting', current_question_id=NULL, status='active',
       updated_at=datetime('now') WHERE id=?`
    )
      .bind(session.id)
      .run();
    return hostStats(
      { ...session, phase: "waiting", status: "active", current_question_id: null },
      env,
      false,
      { includeQuestionList: false }
    );
  }

  if (action === "lock") {
    if (session.phase !== "open") return error("Nothing to lock", 409, env);
    await env.DB.prepare(
      `UPDATE live_sessions SET phase='locked', updated_at=datetime('now') WHERE id=?`
    )
      .bind(session.id)
      .run();
    return hostStats({ ...session, phase: "locked" }, env, false, { includeQuestionList: false });
  }

  if (action === "reveal") {
    if (session.phase !== "open" && session.phase !== "locked") {
      return error("Nothing to reveal", 409, env);
    }
    await env.DB.prepare(
      `UPDATE live_sessions SET phase='reveal', updated_at=datetime('now') WHERE id=?`
    )
      .bind(session.id)
      .run();
    return hostStats({ ...session, phase: "reveal" }, env, true, { includeQuestionList: false });
  }

  // push
  const body = (await request.json().catch(() => ({}))) as { qid?: string; question_id?: number };
  let q: QuestionRow | null = null;
  if (body.question_id) {
    q = await env.DB.prepare(
      `SELECT * FROM questions WHERE id=? AND course_id=? AND published=1`
    )
      .bind(body.question_id, session.course_id)
      .first<QuestionRow>();
  } else if (body.qid) {
    q = await env.DB.prepare(
      `SELECT * FROM questions WHERE qid=? AND course_id=? AND published=1`
    )
      .bind(body.qid, session.course_id)
      .first<QuestionRow>();
  } else {
    // next unpublished relative to current: first by sort_order after current, or first
    if (session.current_question_id) {
      const cur = await env.DB.prepare(`SELECT sort_order FROM questions WHERE id=?`)
        .bind(session.current_question_id)
        .first<{ sort_order: number }>();
      q = await env.DB.prepare(
        `SELECT * FROM questions WHERE course_id=? AND published=1 AND sort_order>?
         ORDER BY sort_order ASC, id ASC LIMIT 1`
      )
        .bind(session.course_id, cur?.sort_order ?? -1)
        .first<QuestionRow>();
    }
    if (!q) {
      q = await env.DB.prepare(
        `SELECT * FROM questions WHERE course_id=? AND published=1
         ORDER BY sort_order ASC, id ASC LIMIT 1`
      )
        .bind(session.course_id)
        .first<QuestionRow>();
    }
  }
  if (!q) return error("No question available", 404, env);

  await env.DB.prepare(
    `UPDATE live_sessions SET current_question_id=?, phase='open', status='active',
     updated_at=datetime('now') WHERE id=?`
  )
    .bind(q.id, session.id)
    .run();

  // Return full host snapshot (same shape as GET /host) — avoids slow second round-trip.
  return hostStats(
    { ...session, current_question_id: q.id, phase: "open", status: "active" },
    env,
    false,
    { includeQuestionList: false }
  );
}

async function hostStats(
  session: LiveSessionRow,
  env: Env,
  withReveal = false,
  opts: { includeQuestionList?: boolean } = {}
): Promise<Response> {
  const includeQuestionList = opts.includeQuestionList !== false;

  const participantP = env.DB.prepare(
    `SELECT COUNT(*) AS c FROM live_participants WHERE session_id=?`
  )
    .bind(session.id)
    .first<{ c: number }>();

  const questionP = session.current_question_id
    ? env.DB.prepare(`SELECT * FROM questions WHERE id=?`)
        .bind(session.current_question_id)
        .first<QuestionRow>()
    : Promise.resolve(null);

  const listP = includeQuestionList
    ? env.DB.prepare(
        `SELECT id, qid, sort_order, prompt_en, prompt_zh FROM questions
         WHERE course_id=? AND published=1 ORDER BY sort_order ASC, id ASC`
      )
        .bind(session.course_id)
        .all()
    : Promise.resolve({ results: [] as unknown[] });

  const [participantCount, q, questions] = await Promise.all([participantP, questionP, listP]);

  let question = null;
  let optionCounts: Record<string, number> = {};
  let answered = 0;
  let correctCount = 0;

  if (q) {
    question = publicQuestionForPhase(
      q,
      withReveal || session.phase === "reveal" ? "reveal" : session.phase
    );
    const answers = await env.DB.prepare(
      `SELECT answer_json, is_correct FROM live_answers
       WHERE session_id=? AND question_id=?`
    )
      .bind(session.id, q.id)
      .all<{ answer_json: string; is_correct: number | null }>();

    for (const row of answers.results || []) {
      answered += 1;
      if (row.is_correct === 1) correctCount += 1;
      try {
        const arr = JSON.parse(row.answer_json) as string[];
        for (const opt of arr) {
          optionCounts[opt] = (optionCounts[opt] || 0) + 1;
        }
      } catch {
        /* ignore bad row */
      }
    }
  }

  const payload: Record<string, unknown> = {
    ok: true,
    code: session.code,
    status: session.status,
    phase: withReveal ? "reveal" : session.phase,
    title: session.title,
    participant_count: participantCount?.c || 0,
    answered,
    correct_count: session.phase === "reveal" || withReveal ? correctCount : undefined,
    option_counts: optionCounts,
    question,
  };
  if (includeQuestionList) {
    payload.question_list = questions.results || [];
  }

  return json(payload, 200, env);
}

export async function hostOverview(code: string, request: Request, env: Env): Promise<Response> {
  const session = await getSessionByCode(code, env);
  if (!session) return error("Session not found", 404, env);

  const hostToken = request.headers.get("X-Host-Token");
  if (!(await requireHost(session, hostToken, env))) {
    return error("Host token required", 403, env);
  }

  const url = new URL(request.url);
  const light = url.searchParams.get("light") === "1";
  return hostStats(session, env, false, { includeQuestionList: !light });
}

export async function linkParticipantAccount(
  code: string,
  request: Request,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  if (!user) return error("Hub token required", 401, env);
  const session = await getSessionByCode(code, env);
  if (!session) return error("Session not found", 404, env);

  const body = (await request.json().catch(() => ({}))) as { participant_key?: string };
  const key = (body.participant_key || "").trim();
  if (!key) return error("participant_key required", 400, env);

  const result = await env.DB.prepare(
    `UPDATE live_participants SET user_id=? WHERE session_id=? AND participant_key=?`
  )
    .bind(user.user_id, session.id, key)
    .run();

  if (!result.meta.changes) return error("Participant not found", 404, env);
  return json(
    {
      ok: true,
      user_id: user.user_id,
      display_name: user.display_name,
    },
    200,
    env
  );
}
