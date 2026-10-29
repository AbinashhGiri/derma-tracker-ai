from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class SkinQuery(BaseModel):
    user_message: str
    skin_type: Optional[str] = None
    allergies: List[str] = Field(default_factory=list)
    goals: List[str] = Field(default_factory=list)
    current_products: List[str] = Field(default_factory=list)
    current_issues: List[str] = Field(default_factory=list)
    climate: str = "moderate"
    sensitivity_level: Optional[str] = None


class SkinAnalysis(BaseModel):
    primary_concerns: List[str] = Field(default_factory=list)
    skin_type: str = "balanced"
    triggers: List[str] = Field(default_factory=list)
    goals: List[str] = Field(default_factory=list)
    sensitivity_level: str = "moderate"
    ingredient_constraints: List[str] = Field(default_factory=list)
    summary: str = ""


class ProductRecommendation(BaseModel):
    name: str
    category: str
    score: float
    rationale: str
    ingredients: List[str] = Field(default_factory=list)


class RoutineStep(BaseModel):
    time_of_day: str
    step: str
    purpose: str


class RecommendationResponse(BaseModel):
    analysis: SkinAnalysis
    products: List[ProductRecommendation]
    routine: List[RoutineStep]


class UserSignup(BaseModel):
    name: str
    email: str
    password: str
    skin_type: str = "balanced"
    sensitivity_level: str = "moderate"
    allergies: List[str] = Field(default_factory=list)
    goals: List[str] = Field(default_factory=list)


class UserLogin(BaseModel):
    email: str
    password: str


class UserProfileUpdate(BaseModel):
    name: Optional[str] = None
    skin_type: Optional[str] = None
    sensitivity_level: Optional[str] = None
    allergies: Optional[List[str]] = None
    goals: Optional[List[str]] = None


class SkinLogCreate(BaseModel):
    date: str = "today"
    dryness: int = 0
    acne: int = 0
    redness: int = 0
    irritation: int = 0
    texture: int = 0
    notes: str = ""


class SkinLogRecord(BaseModel):
    id: int
    user_id: int
    date: str
    dryness: int
    acne: int
    redness: int
    irritation: int
    texture: int
    notes: str
    created_at: str


class RoutineCreate(BaseModel):
    title: str = "My Routine"
    morning_steps: List[str] = Field(default_factory=list)
    evening_steps: List[str] = Field(default_factory=list)


class RoutineRecord(BaseModel):
    id: int
    user_id: int
    title: str
    morning_steps: List[str]
    evening_steps: List[str]
    created_at: str


__all__ = [
    "SkinQuery",
    "SkinAnalysis",
    "ProductRecommendation",
    "RoutineStep",
    "RecommendationResponse",
    "UserSignup",
    "UserLogin",
    "UserProfileUpdate",
    "SkinLogCreate",
    "SkinLogRecord",
    "RoutineCreate",
    "RoutineRecord",
]
