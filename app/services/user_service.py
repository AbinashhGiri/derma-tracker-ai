from __future__ import annotations

import hashlib
import json

from app.db import get_connection, load_json, dump_json


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.strip().encode("utf-8")).hexdigest()


def create_user(data: dict) -> dict:
    email = str(data["email"]).strip().lower()
    with get_connection() as conn:
        existing = conn.execute(
            "SELECT id FROM users WHERE email = ?",
            (email,),
        ).fetchone()
        if existing:
            raise ValueError("A user with this email already exists.")

        cursor = conn.execute(
            """
            INSERT INTO users (name, email, password_hash, skin_type, sensitivity_level, allergies, goals)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data["name"],
                email,
                _hash_password(str(data["password"])),
                data.get("skin_type", "balanced"),
                data.get("sensitivity_level", "moderate"),
                dump_json(data.get("allergies", [])),
                dump_json(data.get("goals", [])),
            ),
        )
        user_id = cursor.lastrowid

    return get_profile(user_id)


def authenticate_user(email: str, password: str) -> dict | None:
    email = str(email).strip().lower()
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,),
        ).fetchone()

    if not row:
        return None

    if row["password_hash"] != _hash_password(password):
        return None

    return get_profile(row["id"])


def get_profile(user_id: int) -> dict | None:
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM users WHERE id = ?",
            (user_id,),
        ).fetchone()

    if not row:
        return None

    return {
        "id": row["id"],
        "name": row["name"],
        "email": row["email"],
        "skin_type": row["skin_type"],
        "sensitivity_level": row["sensitivity_level"],
        "allergies": load_json(row["allergies"]),
        "goals": load_json(row["goals"]),
        "created_at": row["created_at"],
    }


def update_profile(user_id: int, updates: dict) -> dict | None:
    current = get_profile(user_id)
    if not current:
        return None

    new_values = {
        "name": updates.get("name", current["name"]),
        "skin_type": updates.get("skin_type", current["skin_type"]),
        "sensitivity_level": updates.get("sensitivity_level", current["sensitivity_level"]),
        "allergies": dump_json(updates.get("allergies", current["allergies"])),
        "goals": dump_json(updates.get("goals", current["goals"])),
    }

    with get_connection() as conn:
        conn.execute(
            """
            UPDATE users
            SET name = ?, skin_type = ?, sensitivity_level = ?, allergies = ?, goals = ?
            WHERE id = ?
            """,
            (
                new_values["name"],
                new_values["skin_type"],
                new_values["sensitivity_level"],
                new_values["allergies"],
                new_values["goals"],
                user_id,
            ),
        )

    return get_profile(user_id)


def add_skin_log(user_id: int, payload: dict) -> dict:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO skin_logs (user_id, log_date, dryness, acne, redness, irritation, texture, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                payload.get("date") or payload.get("log_date") or "today",
                int(payload.get("dryness", 0)),
                int(payload.get("acne", 0)),
                int(payload.get("redness", 0)),
                int(payload.get("irritation", 0)),
                int(payload.get("texture", 0)),
                payload.get("notes", ""),
            ),
        )
        log_id = cursor.lastrowid

    return get_skin_log(log_id)


def get_skin_log(log_id: int) -> dict | None:
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM skin_logs WHERE id = ?",
            (log_id,),
        ).fetchone()

    if not row:
        return None

    return {
        "id": row["id"],
        "user_id": row["user_id"],
        "date": row["log_date"],
        "dryness": row["dryness"],
        "acne": row["acne"],
        "redness": row["redness"],
        "irritation": row["irritation"],
        "texture": row["texture"],
        "notes": row["notes"],
        "created_at": row["created_at"],
    }


def get_skin_logs(user_id: int) -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM skin_logs WHERE user_id = ? ORDER BY created_at DESC",
            (user_id,),
        ).fetchall()

    return [
        {
            "id": row["id"],
            "user_id": row["user_id"],
            "date": row["log_date"],
            "dryness": row["dryness"],
            "acne": row["acne"],
            "redness": row["redness"],
            "irritation": row["irritation"],
            "texture": row["texture"],
            "notes": row["notes"],
            "created_at": row["created_at"],
        }
        for row in rows
    ]


def save_routine(user_id: int, payload: dict) -> dict:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO routines (user_id, title, morning_steps, evening_steps)
            VALUES (?, ?, ?, ?)
            """,
            (
                user_id,
                payload.get("title", "My Routine"),
                dump_json(payload.get("morning_steps", [])),
                dump_json(payload.get("evening_steps", [])),
            ),
        )
        routine_id = cursor.lastrowid

    return get_routine(routine_id)


def get_routine(routine_id: int) -> dict | None:
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM routines WHERE id = ?",
            (routine_id,),
        ).fetchone()

    if not row:
        return None

    return {
        "id": row["id"],
        "user_id": row["user_id"],
        "title": row["title"],
        "morning_steps": load_json(row["morning_steps"]),
        "evening_steps": load_json(row["evening_steps"]),
        "created_at": row["created_at"],
    }


def get_routines(user_id: int) -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM routines WHERE user_id = ? ORDER BY created_at DESC",
            (user_id,),
        ).fetchall()

    return [
        {
            "id": row["id"],
            "user_id": row["user_id"],
            "title": row["title"],
            "morning_steps": load_json(row["morning_steps"]),
            "evening_steps": load_json(row["evening_steps"]),
            "created_at": row["created_at"],
        }
        for row in rows
    ]


__all__ = [
    "create_user",
    "authenticate_user",
    "get_profile",
    "update_profile",
    "add_skin_log",
    "get_skin_logs",
    "save_routine",
    "get_routines",
]
