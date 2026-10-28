from __future__ import annotations

from app.data.catalog import CATALOG


class IngredientSafetyAgent:
    """Filters out products that conflict with user allergies or sensitivity goals."""

    ALLERGEN_MAP = {
        "fragrance": ["fragrance", "perfume", "essential oil", "parfum"],
        "alcohol": ["alcohol", "ethanol", "denatured alcohol", "sd alcohol"],
        "sulfates": ["sulfate", "sodium lauryl sulfate", "sls"],
        "retinol": ["retinol", "retinoid", "retinal"],
        "acid": ["acid", "glycolic", "lactic", "salicylic"],
    }

    def filter_products(self, products: list[dict], allergies: list[str], sensitivity_level: str) -> list[dict]:
        filtered: list[dict] = []

        allergy_set = {item.lower() for item in allergies}
        for product in products:
            product_ingredients = [ingredient.lower() for ingredient in product["ingredients"]]
            product_name = product["name"].lower()

            blocked = False
            for allergy in allergy_set:
                if allergy in product_name:
                    blocked = True
                    break
                for ingredient in product_ingredients:
                    if allergy in ingredient or ingredient in allergy:
                        blocked = True
                        break
                if blocked:
                    break

            if sensitivity_level == "high":
                if any(item in product_name for item in ["acid", "retinoid", "alcohol"]):
                    blocked = True

            if not blocked:
                filtered.append(product)

        return filtered


__all__ = ["IngredientSafetyAgent"]
