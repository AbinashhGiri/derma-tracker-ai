from __future__ import annotations

CATALOG = [
    {
        "name": "Hydrating Cream Cleanser",
        "category": "cleanser",
        "tags": ["dryness", "sensitivity", "hydration", "barrier repair"],
        "ingredients": ["glycerin", "ceramides", "squalane"],
        "avoid_if": ["fragrance"],
        "skin_types": ["dry", "sensitive"],
    },
    {
        "name": "Salicylic Acid Foaming Cleanser",
        "category": "cleanser",
        "tags": ["acne", "oiliness", "texture", "congestion"],
        "ingredients": ["salicylic acid", "tea tree", "panthenol"],
        "avoid_if": ["sensitive"],
        "skin_types": ["oily", "combination"],
    },
    {
        "name": "Niacinamide Serum",
        "category": "serum",
        "tags": ["oiliness", "redness", "texture", "acne", "pores"],
        "ingredients": ["niacinamide", "zinc", "panthenol"],
        "avoid_if": [],
        "skin_types": ["oily", "combination", "sensitive"],
    },
    {
        "name": "Barrier Repair Moisturizer",
        "category": "moisturizer",
        "tags": ["dryness", "sensitivity", "redness", "barrier repair", "hydration"],
        "ingredients": ["ceramides", "squalane", "cholesterol"],
        "avoid_if": ["fragrance"],
        "skin_types": ["dry", "sensitive"],
    },
    {
        "name": "Vitamin C Brightening Serum",
        "category": "serum",
        "tags": ["dullness", "hyperpigmentation", "brightening", "radiance"],
        "ingredients": ["vitamin c", "kojic acid", "alpha arbutin"],
        "avoid_if": ["sensitive"],
        "skin_types": ["balanced", "combination", "dry"],
    },
    {
        "name": "Mineral UV Defense SPF 50",
        "category": "sunscreen",
        "tags": ["sun exposure", "sensitivity", "hydration", "barrier repair"],
        "ingredients": ["zinc oxide", "titanium dioxide", "niacinamide"],
        "avoid_if": ["fragrance"],
        "skin_types": ["dry", "sensitive", "combination"],
    },
    {
        "name": "Soothing Toner",
        "category": "toner",
        "tags": ["sensitivity", "redness", "hydration", "calming"],
        "ingredients": ["beta glucan", "panthenol", "hyaluronic acid"],
        "avoid_if": ["alcohol", "fragrance"],
        "skin_types": ["dry", "sensitive"],
    },
    {
        "name": "Overnight Repair Cream",
        "category": "moisturizer",
        "tags": ["dryness", "barrier repair", "redness", "repair"],
        "ingredients": ["peptides", "ceramides", "shea butter"],
        "avoid_if": ["fragrance"],
        "skin_types": ["dry", "sensitive"],
    },
]

__all__ = ["CATALOG"]
