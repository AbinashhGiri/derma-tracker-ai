from __future__ import annotations

from app.db import get_profile
from app.db import get_skin_logs


class DashboardService:
    def get_dashboard(self, user_id: int) -> dict:
        profile = get_profile(user_id)
        if not profile:
            raise ValueError("User not found.")

        logs = get_skin_logs(user_id)
        if not logs:
            return {
                "profile": profile,
                "average_scores": {
                    "dryness": 0,
                    "acne": 0,
                    "redness": 0,
                    "irritation": 0,
                    "texture": 0,
                },
                "recent_logs": [],
                "insights": ["Start tracking your skin routine with your first log."],
            }

        avg = {
            "dryness": round(sum(item["dryness"] for item in logs) / len(logs), 1),
            "acne": round(sum(item["acne"] for item in logs) / len(logs), 1),
            "redness": round(sum(item["redness"] for item in logs) / len(logs), 1),
            "irritation": round(sum(item["irritation"] for item in logs) / len(logs), 1),
            "texture": round(sum(item["texture"] for item in logs) / len(logs), 1),
        }

        insights = []
        if avg["dryness"] > 5:
            insights.append("Your dryness trend is elevated. Prioritize gentle hydration and barrier-supporting products.")
        if avg["acne"] > 4:
            insights.append("Breakout activity is trending upward. Consider a cleanser or serum with acne-focused support.")
        if avg["redness"] > 4:
            insights.append("Redness appears higher than usual. A fragrance-free, soothing regimen may help.")
        if not insights:
            insights.append("Your recent skin trend is stable. Keep your routine consistent for better results.")

        return {
            "profile": profile,
            "average_scores": avg,
            "recent_logs": logs[:5],
            "insights": insights,
        }


__all__ = ["DashboardService"]
