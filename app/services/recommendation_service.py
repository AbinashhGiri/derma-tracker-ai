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
        analysis_data = self.query_agent.analyze_query(query)
        analysis = self._build_analysis_model(analysis_data)
        products = self.product_agent.recommend(analysis)
        routine = self.routine_agent.build_routine(analysis)

        return RecommendationResponse(
            analysis=analysis,
            products=products,
            routine=routine,
        )

    def _build_analysis_model(self, analysis_data: dict):
        from app.models import SkinAnalysis

        return SkinAnalysis(
            primary_concerns=analysis_data["primary_concerns"],
            skin_type=analysis_data["skin_type"],
            triggers=analysis_data["triggers"],
            goals=analysis_data["goals"],
            sensitivity_level=analysis_data["sensitivity_level"],
            ingredient_constraints=analysis_data["ingredient_constraints"],
            summary=analysis_data["summary"],
        )


__all__ = ["RecommendationService"]
