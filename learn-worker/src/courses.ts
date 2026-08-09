import type { Env, AuthUser, QuestionRow } from "./types";
import { json, error } from "./utils";

function publicQuestion(q: QuestionRow, includeAnswer: boolean) {
  const base = {
    id: q.id,
    qid: q.qid,
    qtype: q.qtype,
    prompt_en: q.prompt_en,
    prompt_zh: q.prompt_zh,
    options: JSON.parse(q.options_json),
    tags: JSON.parse(q.tags_json || "[]"),
    sort_order: q.sort_order,
  };
  if (!includeAnswer) return base;
  return {
    ...base,
    correct: JSON.parse(q.correct_json),
    explanation_en: q.explanation_en,
    explanation_zh: q.explanation_zh,
  };
}

export async function listCourses(env: Env): Promise<Response> {
  const rows = await env.DB.prepare(
    `SELECT c.*,
            (SELECT COUNT(*) FROM questions q WHERE q.course_id=c.id AND q.published=1) AS question_count
     FROM courses c WHERE c.published=1 ORDER BY c.id ASC`
  ).all();
  return json({ items: rows.results || [] }, 200, env);
}

export async function getCourse(
  slug: string,
  env: Env,
  opts: { includeAnswers?: boolean; user?: AuthUser | null } = {}
): Promise<Response> {
  const course = await env.DB.prepare(
    `SELECT * FROM courses WHERE slug=? AND published=1`
  )
    .bind(slug)
    .first();
  if (!course) return error("Course not found", 404, env);

  const qs = await env.DB.prepare(
    `SELECT * FROM questions WHERE course_id=? AND published=1 ORDER BY sort_order ASC, id ASC`
  )
    .bind((course as { id: number }).id)
    .all<QuestionRow>();

  const includeAnswers = !!opts.includeAnswers;
  return json(
    {
      course,
      questions: (qs.results || []).map((q) => publicQuestion(q, includeAnswers)),
    },
    200,
    env
  );
}

/** Practice: return questions without answers; answers only after submit. */
export async function getPracticeQuestions(slug: string, env: Env): Promise<Response> {
  return getCourse(slug, env, { includeAnswers: false });
}
