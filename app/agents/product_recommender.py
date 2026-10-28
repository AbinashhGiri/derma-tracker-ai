from __future__ import annotations

from app.agents.safety_filter import IngredientSafetyAgent
from app.data.catalog import CATALOG
from app.models import ProductRecommendation, SkinAnalysis


class ProductRecommenderAgent:
    """Weights products by concern match, skin type, and safety constraints."""

    def __init__(self) -> None:
        self.safety_agent = IngredientSafetyAgent()

    def recommend(self, analysis: SkinAnalysis) -> list[ProductRecommendation]:
        safe_products = self.safety_agent.filter_products(
            CATALOG,
            analysis.ingredient_constraints,
            analysis.sensitivity_level,
        )

        recommendations: list[ProductRecommendation] = []

        for product in safe_products:
            score = 0.0
            matched_tags: list[str] = []

            for tag in product["tags"]:
                if tag in analysis.primary_concerns or tag in analysis.goals or tag in analysis.triggers:
                    score += 25
                    matched_tags.append(tag)

            if analysis.skin_type in product.get("skin_types", []):
                score += 20

            if analysis.sensitivity_level == "high" and "sensitivity" in product["tags"]:
                score += 15
            elif analysis.sensitivity_level == "high" and "acid" in product["name"].lower():
                score -= 25

            if "dryness" in analysis.primary_concerns and product["category"] in ["cleanser", "moisturizer", "sunscreen"]:
                score += 10
            if "acne" in analysis.primary_concerns and product["category"] in ["cleanser", "serum"]:
                score += 12
            if "sensitivity" in analysis.primary_concerns and product["category"] in ["cleanser", "toner", "moisturizer", "sunscreen"]:
                score += 12

            if score > 0:
                recommendations.append(
                    ProductRecommendation(
                        name=product["name"],
                        category=product["category"],
                        score=round(min(score, 100), 1),
                        rationale=f"Matches {', '.join(matched_tags) if matched_tags else 'your skin goals'} and avoids ingredients flagged by your profile.",
                        ingredients=product["ingredients"],
                    )
                )

        return sorted(recommendations, key=lambda item: item.score, reverse=True)[:4]


__all__ = ["ProductRecommenderAgent"]
