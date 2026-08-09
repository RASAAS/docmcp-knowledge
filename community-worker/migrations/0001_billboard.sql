-- Priority Billboard (Admin-curated ranking; public vote + comment)

CREATE TABLE IF NOT EXISTS billboard_items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT NOT NULL DEFAULT '',
  category TEXT NOT NULL DEFAULT 'general',
  status TEXT NOT NULL DEFAULT 'planned',
  source_feature_id INTEGER,
  vote_count INTEGER NOT NULL DEFAULT 0,
  comment_count INTEGER NOT NULL DEFAULT 0,
  is_published INTEGER NOT NULL DEFAULT 1,
  created_by TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS billboard_votes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  billboard_id INTEGER NOT NULL REFERENCES billboard_items(id) ON DELETE CASCADE,
  voter_identifier TEXT NOT NULL,
  is_verified INTEGER NOT NULL DEFAULT 0,
  weight INTEGER NOT NULL DEFAULT 1,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(billboard_id, voter_identifier)
);

CREATE INDEX IF NOT EXISTS idx_billboard_vote_count ON billboard_items(vote_count DESC);
CREATE INDEX IF NOT EXISTS idx_billboard_category ON billboard_items(category);
CREATE INDEX IF NOT EXISTS idx_billboard_published ON billboard_items(is_published);
CREATE INDEX IF NOT EXISTS idx_billboard_votes_item ON billboard_votes(billboard_id);
CREATE INDEX IF NOT EXISTS idx_billboard_source_feature ON billboard_items(source_feature_id);

-- Expand comments.target_type to allow 'billboard' (recreate table; SQLite CHECK is immutable)
CREATE TABLE IF NOT EXISTS comments_new (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  target_type TEXT NOT NULL CHECK(target_type IN ('feature', 'discussion', 'billboard')),
  target_id INTEGER NOT NULL,
  body TEXT NOT NULL,
  author_name TEXT NOT NULL,
  author_email TEXT,
  author_user_id TEXT,
  is_verified INTEGER NOT NULL DEFAULT 0,
  is_hidden INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

INSERT INTO comments_new (
  id, target_type, target_id, body, author_name, author_email,
  author_user_id, is_verified, is_hidden, created_at
)
SELECT
  id, target_type, target_id, body, author_name, author_email,
  author_user_id, is_verified, is_hidden, created_at
FROM comments;

DROP TABLE comments;
ALTER TABLE comments_new RENAME TO comments;
CREATE INDEX IF NOT EXISTS idx_comments_target ON comments(target_type, target_id);
