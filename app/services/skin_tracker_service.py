from __future__ import annotations

from app.db import add_skin_log as db_add_skin_log
from app.db import get_routines as db_get_routines
from app.db import get_skin_logs as db_get_skin_logs
from app.db import save_routine as db_save_routine


class SkinTrackerService:
    def add_log(self, user_id: int, payload: dict) -> dict:
        return db_add_skin_log(user_id, payload)

    def get_logs(self, user_id: int) -> list[dict]:
        return db_get_skin_logs(user_id)

    def save_routine(self, user_id: int, payload: dict) -> dict:
        return db_save_routine(user_id, payload)

    def get_routines(self, user_id: int) -> list[dict]:
        return db_get_routines(user_id)


__all__ = ["SkinTrackerService"]
