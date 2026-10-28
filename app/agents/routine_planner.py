from __future__ import annotations

from app.models import RecommendationResponse, RoutineStep, SkinAnalysis


class RoutinePlannerAgent:
    """Creates a simple morning and evening routine based on the skin analysis."""

    def build_routine(self, analysis: SkinAnalysis) -> list[RoutineStep]:
        steps: list[RoutineStep] = []

        if analysis.skin_type == "dry" or "dryness" in analysis.primary_concerns:
            steps.extend(
                [
                    RoutineStep(time_of_day="Morning", step="Gentle cleanser", purpose="Clean without stripping the barrier."),
                    RoutineStep(time_of_day="Morning", step="Hydrating serum", purpose="Deliver moisture and improve comfort."),
                    RoutineStep(time_of_day="Morning", step="Barrier repair moisturizer", purpose="Seal in hydration and reduce flakiness."),
                    RoutineStep(time_of_day="Morning", step="Broad-spectrum sunscreen", purpose="Protect against UV damage and irritation."),
                    RoutineStep(time_of_day="Evening", step="Cleanser", purpose="Remove sunscreen and daily buildup."),
                    RoutineStep(time_of_day="Evening", step="Moisturizer", purpose="Support hydration overnight."),
                ]
            )
        elif analysis.skin_type == "oily" or "acne" in analysis.primary_concerns:
            steps.extend(
                [
                    RoutineStep(time_of_day="Morning", step="Foaming cleanser", purpose="Reduce excess oil and debris."),
                    RoutineStep(time_of_day="Morning", step="Niacinamide serum", purpose="Control oil and support a clearer appearance."),
                    RoutineStep(time_of_day="Morning", step="Lightweight moisturizer", purpose="Hydrate without clogging pores."),
                    RoutineStep(time_of_day="Morning", step="Sunscreen", purpose="Prevent UV-triggered breakouts and pigmentation."),
                    RoutineStep(time_of_day="Evening", step="Cleanser", purpose="Remove sunscreen, sweat, and excess oil."),
                    RoutineStep(time_of_day="Evening", step="Targeted treatment", purpose="Use acne-supportive ingredients on affected zones."),
                    RoutineStep(time_of_day="Evening", step="Moisturizer", purpose="Rebalance hydration after treatment."),
                ]
            )
        else:
            steps.extend(
                [
                    RoutineStep(time_of_day="Morning", step="Gentle cleanser", purpose="Refresh without irritation."),
                    RoutineStep(time_of_day="Morning", step="Vitamin C serum", purpose="Support brightness and overall skin clarity."),
                    RoutineStep(time_of_day="Morning", step="Light moisturizer", purpose="Balance hydration."),
                    RoutineStep(time_of_day="Morning", step="Sunscreen", purpose="Daily protection."),
                    RoutineStep(time_of_day="Evening", step="Cleanser", purpose="Remove impurities and sunscreen."),
                    RoutineStep(time_of_day="Evening", step="Barrier cream", purpose="Repair the skin barrier overnight."),
                ]
            )

        if analysis.sensitivity_level == "high":
            steps = [
                RoutineStep(time_of_day="Morning", step="Minimal cleanser", purpose="Limit exposure to harsh surfactants."),
                RoutineStep(time_of_day="Morning", step="Soothing toner", purpose="Calm redness and minimize discomfort."),
                RoutineStep(time_of_day="Morning", step="Barrier moisturizer", purpose="Support the skin barrier."),
                RoutineStep(time_of_day="Morning", step="Mineral sunscreen", purpose="Low-irritation daily protection."),
                RoutineStep(time_of_day="Evening", step="Gentle cleanser", purpose="Remove dirt without over-cleansing."),
                RoutineStep(time_of_day="Evening", step="Barrier repair cream", purpose="Reinforce hydration and skin comfort."),
            ]

        return steps
