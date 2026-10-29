from __future__ import annotations

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse

from app.agents.product_recommender import ProductRecommenderAgent
from app.agents.routine_planner import RoutinePlannerAgent
from app.agents.user_query_analysis import UserQueryAnalysisAgent
from app.data.catalog import CATALOG
from app.db import init_db
from app.models import (
    RecommendationResponse,
    RoutineCreate,
    SkinLogCreate,
    SkinQuery,
    UserLogin,
    UserProfileUpdate,
    UserSignup,
)
from app.services.dashboard_service import DashboardService
from app.services.skin_tracker_service import SkinTrackerService
from app.services.user_service import authenticate_user, create_user, get_profile, update_profile

app = FastAPI(title="DermaTracker AI", version="1.1.0")
init_db()

query_agent = UserQueryAnalysisAgent()
product_agent = ProductRecommenderAgent()
routine_agent = RoutinePlannerAgent()
tracker_service = SkinTrackerService()
dashboard_service = DashboardService()


@app.get("/")
def home() -> HTMLResponse:
    return HTMLResponse(
        """
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <title>DermaTracker AI</title>
            <style>
                body {
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #fffaf7, #f5f1ff);
                    color: #201b2d;
                }
                .container {
                    max-width: 980px;
                    margin: 80px auto;
                    padding: 32px;
                    background: rgba(255,255,255,0.82);
                    border-radius: 24px;
                    box-shadow: 0 18px 50px rgba(76, 41, 93, 0.12);
                }
                h1 {
                    margin-top: 0;
                    font-size: 2.6rem;
                }
                .pill {
                    display: inline-block;
                    padding: 8px 14px;
                    border-radius: 999px;
                    background: #f1e7ff;
                    color: #4c2d7a;
                    font-weight: 700;
                    margin-bottom: 18px;
                }
                .section {
                    margin-top: 28px;
                }
                .grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                    gap: 18px;
                    margin-top: 20px;
                }
                .card {
                    background: #fff;
                    border-radius: 18px;
                    padding: 18px;
                    border: 1px solid #f0e1ff;
                }
                .btn {
                    display: inline-block;
                    margin-top: 18px;
                    text-decoration: none;
                    background: #6a3ef0;
                    color: white;
                    padding: 12px 20px;
                    border-radius: 12px;
                    font-weight: 700;
                    margin-right: 10px;
                }
                code {
                    background: #f5f5f5;
                    padding: 4px 8px;
                    border-radius: 8px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="pill">AI Skin Guidance</div>
                <h1>DermaTracker AI</h1>
                <p>
                    A mini skincare tracking project that combines skin analysis, product safety review,
                    personalized recommendations, and routine tracking for better skin health management.
                </p>
                <div class="section">
                    <h2>Included features</h2>
                    <div class="grid">
                        <div class="card">Profile-based skin tracking</div>
                        <div class="card">Daily skin journal and notes</div>
                        <div class="card">Saved routines and product safeties</div>
                        <div class="card">AI-based product recommendation API</div>
                    </div>
                </div>
                <div class="section">
                    <h2>Open the app</h2>
                    <p>Use the API docs or start with the recommendation endpoint.</p>
                    <a class="btn" href="/docs">Open API Docs</a>
                    <a class="btn" href="/health">Health Check</a>
                </div>
            </div>
        </body>
        </html>
        """
    )


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "derma-tracker-ai"}


@app.post("/auth/signup")
def signup(payload: UserSignup):
    try:
        user = create_user(
            {
                "name": payload.name,
                "email": payload.email,
                "password": payload.password,
                "skin_type": payload.skin_type,
                "sensitivity_level": payload.sensitivity_level,
                "allergies": payload.allergies,
                "goals": payload.goals,
            }
        )
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc

    return {"message": "User created successfully", "user": user}


@app.post("/auth/login")
def login(payload: UserLogin):
    user = authenticate_user(payload.email, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"message": "Login successful", "user": user}


@app.get("/profile")
def get_user_profile(user_id: int = Query(..., description="User ID")):
    profile = get_profile(user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="User not found")
    return profile


@app.put("/profile")
def update_user_profile(payload: UserProfileUpdate, user_id: int = Query(...)):
    updated = update_profile(user_id, payload.model_dump(exclude_none=True))
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Profile updated successfully", "user": updated}


@app.post("/skin-log")
def create_skin_log(payload: SkinLogCreate, user_id: int = Query(...)):
    profile = get_profile(user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="User not found")

    entry = tracker_service.add_log(user_id, payload.model_dump())
    return {"message": "Skin log saved", "entry": entry}


@app.get("/skin-logs")
def list_skin_logs(user_id: int = Query(...)):
    profile = get_profile(user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="User not found")
    return {"logs": tracker_service.get_logs(user_id)}


@app.post("/routines")
def create_routine(payload: RoutineCreate, user_id: int = Query(...)):
    profile = get_profile(user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="User not found")

    routine = tracker_service.save_routine(user_id, payload.model_dump())
    return {"message": "Routine saved", "routine": routine}


@app.get("/routines")
def list_routines(user_id: int = Query(...)):
    profile = get_profile(user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="User not found")
    return {"routines": tracker_service.get_routines(user_id)}


@app.get("/dashboard")
def dashboard(user_id: int = Query(...)):
    profile = get_profile(user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="User not found")

    return dashboard_service.get_dashboard(user_id)


@app.get("/products")
def product_catalog():
    return {"products": CATALOG}


@app.post("/recommendation")
def recommendation(query: SkinQuery):
    analysis_data = query_agent.analyze_query(query)
    analysis = RecommendationResponse.model_validate({
        "analysis": analysis_data,
        "products": [],
        "routine": [],
    }).analysis
    products = product_agent.recommend(analysis)
    routine = routine_agent.build_routine(analysis)
    return {
        "analysis": analysis.model_dump(),
        "products": [product.model_dump() for product in products],
        "routine": [step.model_dump() for step in routine],
    }


__all__ = ["app"]
