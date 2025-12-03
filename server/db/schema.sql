/*
===============================================================
Script to create tables for to_do_db
===============================================================
*/
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS tokens;

-- ============================================================
--      USERS TABLE - User info
-- ============================================================

CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    createdAt TEXT NOT NULL
  );

-- ============================================================
--      TASKS TABLE - Task info
-- ============================================================

CREATE TABLE IF NOT EXISTS tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL CHECK (length(title) <= 30),
    description TEXT CHECK (length(title) <= 50),
    status TEXT NOT NULL DEFAULT 'to-do' CHECK (status in ('to-do', 'in-progress', 'done')),
    active_status TEXT NON NULL DEFAULT 'active' CHECK (active_status in ('active', 'inactive')),
    createdAt TEXT NOT NULL,
    updatedAt TEXT,
    deactivatedAt TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- ============================================================
--      TOKENS TABLE - token info
-- ============================================================

CREATE TABLE IF NOT EXISTS tokens(
    token_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    token TEXT NOT NULL UNIQUE,
    createdAt TEXT NOT NULL,
    expiresAt TEXT NULL,
    revoked INTEGER NOT NULL DEFAULT 0,
    revokedAt TEXT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);