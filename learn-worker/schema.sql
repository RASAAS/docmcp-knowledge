-- Reguverse Learn D1 Schema (independent of Hub)

CREATE TABLE IF NOT EXISTS courses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  slug TEXT NOT NULL UNIQUE,
  title_en TEXT NOT NULL,
  title_zh TEXT NOT NULL,
  description_en TEXT NOT NULL DEFAULT '',
  description_zh TEXT NOT NULL DEFAULT '',
  published INTEGER NOT NULL DEFAULT 1,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS questions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  course_id INTEGER NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
  qid TEXT NOT NULL UNIQUE,
  qtype TEXT NOT NULL DEFAULT 'single' CHECK(qtype IN ('single', 'multi')),
  prompt_en TEXT NOT NULL,
  prompt_zh TEXT NOT NULL,
  options_json TEXT NOT NULL,
  correct_json TEXT NOT NULL,
  explanation_en TEXT NOT NULL DEFAULT '',
  explanation_zh TEXT NOT NULL DEFAULT '',
  tags_json TEXT NOT NULL DEFAULT '[]',
  sort_order INTEGER NOT NULL DEFAULT 0,
  published INTEGER NOT NULL DEFAULT 1,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS live_sessions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL UNIQUE,
  course_id INTEGER NOT NULL REFERENCES courses(id),
  host_token_hash TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'lobby' CHECK(status IN ('lobby', 'active', 'ended')),
  current_question_id INTEGER REFERENCES questions(id),
  phase TEXT NOT NULL DEFAULT 'waiting' CHECK(phase IN ('waiting', 'open', 'locked', 'reveal')),
  title TEXT NOT NULL DEFAULT '',
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now')),
  expires_at TEXT
);

CREATE TABLE IF NOT EXISTS live_participants (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  session_id INTEGER NOT NULL REFERENCES live_sessions(id) ON DELETE CASCADE,
  participant_key TEXT NOT NULL,
  nickname TEXT NOT NULL,
  display_name TEXT NOT NULL DEFAULT '',
  user_id TEXT,
  joined_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(session_id, participant_key)
);

CREATE TABLE IF NOT EXISTS live_answers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  session_id INTEGER NOT NULL REFERENCES live_sessions(id) ON DELETE CASCADE,
  question_id INTEGER NOT NULL REFERENCES questions(id),
  participant_id INTEGER NOT NULL REFERENCES live_participants(id) ON DELETE CASCADE,
  answer_json TEXT NOT NULL,
  is_correct INTEGER,
  answered_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(session_id, question_id, participant_id)
);

-- L2 practice progress (self-paced)
CREATE TABLE IF NOT EXISTS practice_attempts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  course_id INTEGER NOT NULL REFERENCES courses(id),
  participant_key TEXT NOT NULL,
  nickname TEXT NOT NULL DEFAULT '',
  user_id TEXT,
  score INTEGER NOT NULL DEFAULT 0,
  total INTEGER NOT NULL DEFAULT 0,
  detail_json TEXT NOT NULL DEFAULT '[]',
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- L3 certificate stub (PDF + badge later)
CREATE TABLE IF NOT EXISTS certificates (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  course_id INTEGER NOT NULL REFERENCES courses(id),
  participant_key TEXT NOT NULL,
  display_name TEXT NOT NULL DEFAULT '',
  user_id TEXT,
  identity_verified INTEGER NOT NULL DEFAULT 0,
  badge_id TEXT NOT NULL UNIQUE,
  pdf_ready INTEGER NOT NULL DEFAULT 0,
  score INTEGER NOT NULL DEFAULT 0,
  total INTEGER NOT NULL DEFAULT 0,
  issued_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_questions_course ON questions(course_id, sort_order);
CREATE INDEX IF NOT EXISTS idx_live_sessions_code ON live_sessions(code);
CREATE INDEX IF NOT EXISTS idx_live_participants_session ON live_participants(session_id);
CREATE INDEX IF NOT EXISTS idx_live_answers_session_q ON live_answers(session_id, question_id);
CREATE INDEX IF NOT EXISTS idx_practice_course ON practice_attempts(course_id, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_certificates_user ON certificates(user_id);
