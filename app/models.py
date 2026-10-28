from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class SkinQuery(BaseModel):
    user_message: str
    skin_type: Optional[str] = None
    allergies: List[str] = Field(default_factory=list)
    goals: List[str] = Field(default_factory=list)
    current_products: List[str] = Field(default_factory=list)


class SkinAnalysis(BaseModel):
    primary_concerns: List[str] = Field(default_factory=list)
    skin_type: str = "balanced"
    triggers: List[str] = Field(default_factory=list)
    goals: List[str] = Field(default_factory=list)
    sensitivity_level: str = "moderate"
    summary: str = ""


class ProductRecommendation(BaseModel):
    name: str
    category: str
    score: float
    rationale: str


class RoutineStep(BaseModel):
    time_of_day: str
    step: str
    purpose: str


class RecommendationResponse(BaseModel):
    analysis: SkinAnalysis
    products: List[ProductRecommendation]
    routine: List[RoutineStep]
