# DermaTracker AI

DermaTracker AI is a clinical-style skincare recommendation engine for people who want better skin health guidance without guesswork. The app combines user-query analysis, product matching, ingredient safety checks, and a personalized routine planner.

## What the app does

- understands skin concerns from natural-language queries
- detects likely skin type and sensitivity
- flags allergens and harsh ingredients
- recommends products from a curated catalog
- builds a simple morning/evening routine
- exposes a clean API and lightweight web UI

## Architecture

- `app/agents/` — AI-style agents for analysis, recommendation, and planning
- `app/data/` — curated product catalog and product metadata
- `app/services/` — orchestration layer
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
    "user_message": "I have dry, sensitive skin with redness and flaky patches. I want to repair my barrier and avoid fragrance.",
    "skin_type": "dry",
    "allergies": ["fragrance"],
    "goals": ["hydration", "barrier repair"],
    "current_products": ["cleanser"],
    "sensitivity_level": "high"
  }'
```

## Product intelligence included

This version goes beyond a basic demo by adding:

1. structured skin concern extraction
2. ingredient-safety filtering based on allergies
3. concern-to-product scoring with priors for skin type and sensitivity
4. routine planning tailored to dry, oily, acne-prone, and sensitive skin
5. lightweight UI for quick prototyping and demos

The project is ready to extend into a real product database, authentication, user profiles, and LLM-backed recommendation logic.
