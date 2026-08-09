import type { AuthUser, Env, QuestionRow } from "./types";
import { arraysEqualAsSet, error, json, sanitize } from "./utils";

export async function submitPractice(
  slug: string,
  request: Request,
  env: Env,
  user: AuthUser | null
): Promise<Response> {
  const course = await env.DB.prepare(`SELECT id FROM courses WHERE slug=? AND published=1`)
    .bind(slug)
    .first<{ id: number }>();
  if (!course) return error("Course not found", 404, env);

  const body = (await request.json().catch(() => ({}))) as {
    participant_key?: string;
    nickname?: string;
    answers?: Record<string, string[]>;
  };

  const answersMap = body.answers || {};
  const qs = await env.DB.prepare(
    `SELECT * FROM questions WHERE course_id=? AND published=1 ORDER BY sort_order ASC`
  )
    .bind(course.id)
    .all<QuestionRow>();

  const detail: Array<{
    qid: string;
    correct: boolean;
    your: string[];
    expected: string[];
    explanation_en: string;
    explanation_zh: string;
  }> = [];

  let score = 0;
  for (const q of qs.results || []) {
    const expected = JSON.parse(q.correct_json) as string[];
    const your = Array.isArray(answersMap[q.qid]) ? answersMap[q.qid] : [];
    const ok = arraysEqualAsSet(your, expected);
    if (ok) score += 1;
    detail.push({
      qid: q.qid,
      correct: ok,
      your,
      expected,
      explanation_en: q.explanation_en,
      explanation_zh: q.explanation_zh,
    });
  }

  const total = (qs.results || []).length;
  const participantKey = sanitize((body.participant_key || "anon").trim(), 64) || "anon";
  const nickname = sanitize((body.nickname || "").trim(), 40);

  await env.DB.prepare(
    `INSERT INTO practice_attempts (course_id, participant_key, nickname, user_id, score, total, detail_json)
     VALUES (?, ?, ?, ?, ?, ?, ?)`
  )
    .bind(
      course.id,
      participantKey,
      nickname,
      user?.user_id || null,
      score,
      total,
      JSON.stringify(detail.map((d) => ({ qid: d.qid, correct: d.correct, your: d.your })))
    )
    .run();

  return json({ score, total, detail }, 200, env);
}
