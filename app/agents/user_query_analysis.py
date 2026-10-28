from __future__ import annotations

from app.data.catalog import CATALOG


class UserQueryAnalysisAgent:
    """Converts a user message into structured skin insights and safety constraints."""

    CONCERN_MAP = {
        "acne": "acne",
        "pimples": "acne",
        "breakouts": "acne",
        "dry": "dryness",
        "dryness": "dryness",
        "flaky": "dryness",
        "oily": "oiliness",
        "greasy": "oiliness",
        "shine": "oiliness",
        "redness": "redness",
        "sensitive": "sensitivity",
        "irritated": "sensitivity",
        "dull": "dullness",
        "texture": "texture",
        "rough": "texture",
        "dark spot": "hyperpigmentation",
        "pigmentation": "hyperpigmentation",
        "scar": "post-acne marks",
        "barrier": "barrier repair",
        "damaged skin": "barrier repair",
        "eczema": "sensitivity",
        "rosacea": "sensitivity",
    }

    def analyze_query(self, query) -> dict:
        message = (query.user_message or "").lower()

        primary_concerns: list[str] = []
        triggers: list[str] = []
        goals: list[str] = []

        for keyword, concern in self.CONCERN_MAP.items():
            if keyword in message:
                primary_concerns.append(concern)

        if any(word in message for word in ["sun", "sunburn", "uv", "outdoor"]):
            triggers.append("sun exposure")
        if "stress" in message:
            triggers.append("stress")
        if any(word in message for word in ["winter", "cold", "weather"]):
            triggers.append("cold weather")
        if any(word in message for word in ["hot", "sweat", "exercise"]):
            triggers.append("heat and sweat")

        if query.goals:
            goals.extend(str(goal).lower() for goal in query.goals)

        if any(word in message for word in ["dry", "flaky", "dehydrated"]):
            goals.append("hydration")
        if any(word in message for word in ["acne", "breakout", "pimple"]):
            goals.append("clear pores")
        if any(word in message for word in ["sensitive", "irritated", "redness"]):
            goals.append("soothing and barrier support")
        if any(word in message for word in ["dark spot", "pigmentation", "uneven tone"]):
            goals.append("brightening")

        if not primary_concerns:
            primary_concerns = ["general skin health"]

        skin_type = query.skin_type.lower() if query.skin_type else "balanced"
        if not query.skin_type:
            if "oily" in message or "greasy" in message:
                skin_type = "oily"
            elif "dry" in message or "flaky" in message:
                skin_type = "dry"
            elif "sensitive" in message:
                skin_type = "sensitive"
            else:
                skin_type = "balanced"

        sensitivity_level = query.sensitivity_level.lower() if query.sensitivity_level else "moderate"
        if not query.sensitivity_level and any(word in message for word in ["sensitive", "irritated", "burning"]):
            sensitivity_level = "high"

        ingredient_constraints = []
        for allergy in query.allergies:
            ingredient_constraints.append(str(allergy).lower())

        summary = (
            f"The user reports {', '.join(primary_concerns)} with a {skin_type} skin profile. "
            f"Key goals include {', '.join(goals) if goals else 'overall skin balance'}."
        )

        return {
            "primary_concerns": list(dict.fromkeys(primary_concerns)),
            "skin_type": skin_type,
            "triggers": list(dict.fromkeys(triggers)),
            "goals": list(dict.fromkeys(goals)),
            "sensitivity_level": sensitivity_level,
            "ingredient_constraints": list(dict.fromkeys(ingredient_constraints)),
            "summary": summary,
        }


__all__ = ["UserQueryAnalysisAgent"]
