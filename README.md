# DermaTracker AI

DermaTracker AI is a starter product for skin-health tracking and AI-guided recommendations. The project includes an agent-based architecture for:

- user query analysis
- product suggestions
- skincare routine planning
- skin-tracking insights

## Project structure

- `app/agents/` — rule-based AI agents for query interpretation and recommendations
- `app/data/` — structured product catalog and sample knowledge base
- `app/services/` — orchestration layer that combines the agents
- `app/main.py` — FastAPI API entry point

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API example

```bash
curl -X POST http://localhost:8000/recommendation \
  -H "Content-Type: application/json" \
  -d '{
    "user_message": "I have dry, sensitive skin and am dealing with flaky patches and redness.",
    "skin_type": "dry",
    "allergies": ["fragrance"],
    "goals": ["hydration", "barrier repair"],
    "current_products": ["cleanser"]
  }'
```

## What is included

This starter includes a lightweight “agent” system, not a full LLM service. It demonstrates how to:

1. parse a user’s skin issue
2. identify likely concerns and goals
3. score relevant products from a catalog
4. generate a personalized routine plan

You can later replace the rule-based logic with an LLM-powered agent or connect it to a real product database.
