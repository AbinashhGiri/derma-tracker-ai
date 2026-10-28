from __future__ import annotations

from app.models import SkinAnalysis, SkinQuery


class UserQueryAnalysisAgent:
    """Rules-based agent that converts a user message into structured skin insights."""

    def analyze_query(self, query: SkinQuery) -> SkinAnalysis:
        message = query.user_message.lower()

        primary_concerns: list[str] = []
        triggers: list[str] = []
        goals: list[str] = []

        concern_map = {
            "acne": "acne",
            "pimples": "acne",
            "breakouts": "acne",
            "dry": "dryness",
            "flaky": "dryness",
            "flaking": "dryness",
            "oily": "oiliness",
            "shine": "oiliness",
            "redness": "redness",
            "sensitive": "sensitivity",
            "irritated": "sensitivity",
            "dull": "dullness",
            "texture": "texture",
            "scar": "post-acne marks",
            "dark spot": "hyperpigmentation",
        }

        for keyword, concern in concern_map.items():
            if keyword in message:
                primary_concerns.append(concern)

        if "sun" in message or "sunburn" in message:
            triggers.append("sun exposure")
        if "stress" in message:
            triggers.append("stress")
        if "weather" in message or "cold" in message:
            triggers.append("cold weather")
        if "sweat" in message or "exercise" in message:
            triggers.append("heat and sweat")

        if query.goals:
            goals.extend(query.goals)

        if "dry" in message or query.skin_type == "dry":
            goals.append("hydration")
        if "acne" in message or "breakout" in message:
            goals.append("clear pores")
        if "sensitive" in message or "irritated" in message:
            goals.append("soothing and barrier support")
        if "dark spot" in message or "pigmentation" in message:
            goals.append("brightening")

        if not primary_concerns:
            primary_concerns = ["general skin health"]

        if query.skin_type:
            skin_type = query.skin_type.lower()
        elif "oily" in message:
            skin_type = "oily"
        elif "dry" in message or "flaky" in message:
            skin_type = "dry"
        elif "sensitive" in message:
            skin_type = "sensitive"
        else:
            skin_type = "balanced"

        sensitivity_level = "high" if "sensitive" in message or "irritated" in message else "moderate"

        summary = (
            f"The user describes {', '.join(primary_concerns)} with a {skin_type} skin profile. "
            f"Key focus areas include {', '.join(goals) if goals else 'overall skin balance'}."
        )

        return SkinAnalysis(
            primary_concerns=list(dict.fromkeys(primary_concerns)),
            skin_type=skin_type,
            triggers=list(dict.fromkeys(triggers)),
            goals=list(dict.fromkeys(goals)),
            sensitivity_level=sensitivity_level,
            summary=summary,
        )
