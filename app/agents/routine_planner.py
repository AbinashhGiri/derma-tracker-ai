from __future__ import annotations

from app.models import RoutineStep, SkinAnalysis


class RoutinePlannerAgent:
    """Builds a pragmatic skincare routine for the detected skin needs."""

    def build_routine(self, analysis: SkinAnalysis) -> list[RoutineStep]:
        concern_set = set(analysis.primary_concerns)

        if "dryness" in concern_set or analysis.skin_type == "dry":
            steps = [
                RoutineStep(time_of_day="Morning", step="Gentle hydrating cleanser", purpose="Cleans without stripping the barrier."),
                RoutineStep(time_of_day="Morning", step="Hydrating serum with glycerin or hyaluronic acid", purpose="Boosts moisture and improves comfort."),
                RoutineStep(time_of_day="Morning", step="Barrier repair moisturizer", purpose="Locks in hydration and reduces tightness."),
                RoutineStep(time_of_day="Morning", step="Mineral sunscreen SPF 30+", purpose="Protects from UV damage and irritation."),
                RoutineStep(time_of_day="Evening", step="Cream cleanser", purpose="Removes sunscreen and pollutants while staying gentle."),
                RoutineStep(time_of_day="Evening", step="Ceramide-rich moisturizer", purpose="Supports overnight repair and reduces flaking."),
            ]
        elif "acne" in concern_set or analysis.skin_type == "oily":
            steps = [
                RoutineStep(time_of_day="Morning", step="Foaming cleanser", purpose="Clears excess oil and keeps pores feeling fresh."),
                RoutineStep(time_of_day="Morning", step="Niacinamide serum", purpose="Helps reduce oil production and redness."),
                RoutineStep(time_of_day="Morning", step="Lightweight moisturizer", purpose="Maintains hydration without clogging pores."),
                RoutineStep(time_of_day="Morning", step="Broad-spectrum sunscreen", purpose="Prevents UV-triggered post-acne pigmentation."),
                RoutineStep(time_of_day="Evening", step="Cleanser", purpose="Removes excess oil and product residue."),
                RoutineStep(time_of_day="Evening", step="Targeted treatment (if needed)", purpose="Treat active breakouts while keeping the routine balanced."),
                RoutineStep(time_of_day="Evening", step="Oil-free moisturizer", purpose="Prevents rebound dryness after treatment."),
            ]
        else:
            steps = [
                RoutineStep(time_of_day="Morning", step="Gentle cleanser", purpose="Refreshes skin without irritation."),
                RoutineStep(time_of_day="Morning", step="Vitamin C or niacinamide serum", purpose="Supports brightness and even tone."),
                RoutineStep(time_of_day="Morning", step="Light moisturizer", purpose="Balances hydration."),
                RoutineStep(time_of_day="Morning", step="Sunscreen", purpose="Daily protection against UV damage."),
                RoutineStep(time_of_day="Evening", step="Cleanser", purpose="Removes sunscreen and impurities."),
                RoutineStep(time_of_day="Evening", step="Repair cream", purpose="Supports overnight barrier recovery."),
            ]

        if analysis.sensitivity_level == "high":
            steps = [
                RoutineStep(time_of_day="Morning", step="Minimal fragrance-free cleanser", purpose="Avoids triggering irritation."),
                RoutineStep(time_of_day="Morning", step="Soothing toner or hydrating essence", purpose="Calms redness and strengthens comfort."),
                RoutineStep(time_of_day="Morning", step="Barrier moisturizer", purpose="Reinforces hydration and reduces stinging."),
                RoutineStep(time_of_day="Morning", step="Mineral sunscreen", purpose="Low-irritation UV protection."),
                RoutineStep(time_of_day="Evening", step="Gentle cleanser", purpose="Keeps cleansing simple and non-stripping."),
                RoutineStep(time_of_day="Evening", step="Barrier repair cream", purpose="Supports recovery while the skin is resting."),
            ]

        return steps


__all__ = ["RoutinePlannerAgent"]
