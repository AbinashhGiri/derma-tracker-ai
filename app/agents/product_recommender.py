from __future__ import annotations

from app.models import ProductRecommendation, SkinAnalysis


class ProductRecommenderAgent:
    """Matches product ingredients to the user's skin concerns and context."""

    def __init__(self) -> None:
        self.catalog = [
            {
                "name": "Hydrating Cleanser",
                "category": "cleanser",
                "tags": ["dryness", "sensitivity", "hydration"],
                "ingredient_notes": ["ceramides", "glycerin"],
            },
            {
                "name": "Salicylic Acid Wash",
                "category": "cleanser",
                "tags": ["acne", "oiliness", "texture"],
                "ingredient_notes": ["salicylic acid"],
            },
            {
                "name": "Niacinamide Serum",
                "category": "serum",
                "tags": ["oiliness", "texture", "redness", "acne"],
                "ingredient_notes": ["niacinamide"],
            },
            {
                "name": "Barrier Repair Cream",
                "category": "moisturizer",
                "tags": ["dryness", "sensitivity", "redness"],
                "ingredient_notes": ["ceramides", "squalane"],
            },
            {
                "name": "Vitamin C Brightening Serum",
                "category": "serum",
                "tags": ["dullness", "hyperpigmentation", "brightening"],
                "ingredient_notes": ["vitamin c", "kojic acid"],
            },
            {
                "name": "Daily Mineral Sunscreen",
                "category": "sunscreen",
                "tags": ["sensitivity", "sun exposure", "hydration"],
                "ingredient_notes": ["zinc oxide", "broad spectrum"],
            },
            {
                "name": "Gentle Soothing Toner",
                "category": "toner",
                "tags": ["sensitivity", "redness", "hydration"],
                "ingredient_notes": ["panthenol", "beta-glucan"],
            },
        ]

    def recommend(self, analysis: SkinAnalysis) -> list[ProductRecommendation]:
        recommendations: list[ProductRecommendation] = []

        for product in self.catalog:
            score = 0
            matched_tags = []
            for tag in product["tags"]:
                if tag in analysis.primary_concerns or tag in analysis.goals or tag in analysis.triggers:
                    score += 20
                    matched_tags.append(tag)

            if analysis.skin_type in ["dry", "sensitive"] and product["category"] in ["cleanser", "moisturizer", "sunscreen"]:
                score += 15
            if analysis.skin_type == "oily" and product["category"] in ["cleanser", "serum"]:
                score += 10

            if analysis.sensitivity_level == "high" and product["category"] in ["cleanser", "moisturizer", "sunscreen"]:
                score += 10

            if score > 0:
                recommendations.append(
                    ProductRecommendation(
                        name=product["name"],
                        category=product["category"],
                        score=round(min(score, 100), 1),
                        rationale=f"Matches {', '.join(matched_tags) if matched_tags else 'your skin goals'} and suits {analysis.skin_type} skin.",
                    )
                )

        return sorted(recommendations, key=lambda item: item.score, reverse=True)[:4]
