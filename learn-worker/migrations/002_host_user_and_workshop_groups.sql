-- Host ownership for session isolation + blank user-designed workshop groups

ALTER TABLE live_sessions ADD COLUMN host_user_id TEXT;

CREATE TABLE IF NOT EXISTS workshop_groups (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  session_id INTEGER NOT NULL REFERENCES live_sessions(id) ON DELETE CASCADE,
  sort_order INTEGER NOT NULL DEFAULT 0,
  name TEXT NOT NULL DEFAULT '',
  content_json TEXT NOT NULL DEFAULT '{"sections":[]}',
  updated_by TEXT NOT NULL DEFAULT '',
  updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_live_sessions_host_user ON live_sessions(host_user_id);
CREATE INDEX IF NOT EXISTS idx_workshop_groups_session ON workshop_groups(session_id, sort_order);
