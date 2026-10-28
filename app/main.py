from __future__ import annotations

from fastapi import FastAPI

from app.models import SkinQuery
from app.services.recommendation_service import RecommendationService

app = FastAPI(title="DermaTracker AI", version="0.1.0")
service = RecommendationService()


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "derma-tracker-ai"}


@app.post("/recommendation")
def recommendation(query: SkinQuery):
    return service.generate_recommendations(query)
