from __future__ import annotations

from app.agents.product_recommender import ProductRecommenderAgent
from app.agents.routine_planner import RoutinePlannerAgent
from app.agents.user_query_analysis import UserQueryAnalysisAgent
from app.models import RecommendationResponse, SkinQuery


class RecommendationService:
    def __init__(self) -> None:
        self.query_agent = UserQueryAnalysisAgent()
        self.product_agent = ProductRecommenderAgent()
        self.routine_agent = RoutinePlannerAgent()

    def generate_recommendations(self, query: SkinQuery) -> RecommendationResponse:
        analysis = self.query_agent.analyze_query(query)
        products = self.product_agent.recommend(analysis)
        routine = self.routine_agent.build_routine(analysis)

        return RecommendationResponse(
            analysis=analysis,
            products=products,
            routine=routine,
        )
