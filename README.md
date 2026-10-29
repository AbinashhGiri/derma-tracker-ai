# DermaTracker AI

DermaTracker AI is a clinical-style skincare recommendation engine designed to transform natural-language skin concerns into structured guidance, ingredient-safe product suggestions, and personalized routines. The system models user needs across skin type, concerns, ingredients, allergies, and budget to build a more practical recommendation experience.

## What the app does

- Understands skin concerns from natural-language queries
- Detects likely skin type and sensitivity level
- Flags allergens and harsh ingredients
- Matches products based on concern fit and skin profile
- Generates a simple morning and evening skincare routine
- Accounts for budget constraints when prioritizing recommendations
- Exposes a clean API and lightweight web UI

## Architecture

### Agent 1 — Skin analysis
This agent converts user input into a structured skin profile.

It identifies:
- skin type
- primary concerns
- triggers and environmental factors
- goals such as hydration, brightening, or barrier repair
- sensitivity level

This analysis creates a consistent foundation before any product recommendations are made.

### Agent 2 — Ingredient intelligence
This agent evaluates product ingredients against a user’s profile.

It checks for:
- allergies
- fragrance or harsh ingredients
- sensitivity risk
- ingredient-level conflicts with skin goals

Products that violate a user’s constraints are filtered before recommendation scoring begins.

### Agent 3 — Routine generation
This agent turns the analyzed skin needs into a practical daily routine.

It builds structured routines for:
- dry and dehydrated skin
- oily or acne-prone skin
- sensitive or irritated skin
- general balanced skin maintenance

The routine includes morning and evening steps with clear purposes for each action.

## Personalized skincare recommendations

After analysis and safety filtering, DermaTracker AI ranks products based on:
- concern match
- skin type fit
- sensitivity suitability
- ingredient safety
- budget alignment

The result is a shortlist of the most relevant, skin-compatible recommendations rather than a generic product list.

## Project structure

- `app/agents/` — AI-style agents for skin analysis, ingredient safety, product matching, and routine planning
- `app/data/` — curated skincare catalog and product metadata
- `app/services/` — orchestration layer for the recommendation pipeline
- `app/main.py` — API and web entry point
- `app/models.py` — validated request and response models

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open:

- API docs: http://localhost:8000/docs
- App UI: http://localhost:8000/

## Example request

```bash
curl -X POST http://localhost:8000/recommendation \
  -H "Content-Type: application/json" \
  -d '{
    "user_message": "I have dry, sensitive skin with redness and flaky patches. I want to repair my barrier, avoid fragrance, and stay under a $40 budget.",
    "skin_type": "dry",
    "allergies": ["fragrance"],
    "goals": ["hydration", "barrier repair"],
    "current_products": ["cleanser"],
    "sensitivity_level": "high",
    "budget": 40
  }'
```

## Product intelligence included

This version goes beyond a basic demo by adding:

1. structured skin concern extraction
2. ingredient-safety filtering based on allergies and sensitivity
3. concern-to-product scoring with priors for skin type and sensitivity
4. routine planning tailored to dry, oily, acne-prone, and sensitive skin
5. budget-aware recommendation prioritization
6. lightweight UI for quick prototyping and demos

The project is ready to extend into a real product database, authentication, user profiles, and more advanced LLM-backed recommendation logic.
