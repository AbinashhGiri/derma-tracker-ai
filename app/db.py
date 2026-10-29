from __future__ import annotations

import json
import os
import sqlite3

DB_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(DB_DIR, "derma_tracker.db")


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                skin_type TEXT DEFAULT 'balanced',
                sensitivity_level TEXT DEFAULT 'moderate',
                allergies TEXT DEFAULT '[]',
                goals TEXT DEFAULT '[]',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS skin_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                log_date TEXT NOT NULL,
                dryness INTEGER NOT NULL,
                acne INTEGER NOT NULL,
                redness INTEGER NOT NULL,
                irritation INTEGER NOT NULL,
                texture INTEGER NOT NULL,
                notes TEXT DEFAULT '',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS routines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                morning_steps TEXT DEFAULT '[]',
                evening_steps TEXT DEFAULT '[]',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
            """
        )

        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_skin_logs_user_id ON skin_logs(user_id)"
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_routines_user_id ON routines(user_id)"
        )


def dump_json(value: list[str] | None) -> str:
    return json.dumps(value or [])


def load_json(value: str | None) -> list[str]:
    if not value:
        return []
    try:
        loaded = json.loads(value)
        if isinstance(loaded, list):
            return [str(item) for item in loaded]
    except json.JSONDecodeError:
        pass
    return []


__all__ = ["get_connection", "init_db", "dump_json", "load_json"]
