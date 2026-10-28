from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.models import SkinQuery
from app.services.recommendation_service import RecommendationService

app = FastAPI(title="DermaTracker AI", version="1.0.0")
service = RecommendationService()


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
                    max-width: 960px;
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
                code {
                    background: #f5f5f5;
                    padding: 4px 8px;
                    border-radius: 8px;
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
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="pill">AI Skin Guidance</div>
                <h1>DermaTracker AI</h1>
                <p>
                    A skin-health assistant that analyzes user concerns, filters ingredients for safety,
                    recommends products, and plans a personalized routine.
                </p>
                <div class="section">
                    <h2>Core features</h2>
                    <ul>
                        <li>Natural-language skin concern extraction</li>
                        <li>Ingredient allergy and sensitivity filtering</li>
                        <li>Smart product matching by skin type and goals</li>
                        <li>Daily routine generation for different skin needs</li>
                    </ul>
                </div>
                <div class="section">
                    <h2>Try the API</h2>
                    <p>Open <code>/docs</code> for the FastAPI Swagger UI or send a POST to <code>/recommendation</code>.</p>
                    <a class="btn" href="/docs">Open API Docs</a>
                </div>
            </div>
        </body>
        </html>
        """
    )


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "derma-tracker-ai"}


@app.post("/recommendation")
def recommendation(query: SkinQuery):
    return service.generate_recommendations(query)
