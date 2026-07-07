from src.config.scoring import EXPERIENCE_WEIGHT, SKILL_WEIGHT


class RuleBasedScorer:

    def calculate(
        self,
        skill_score: float,
        experience_score: float,
    ) -> float:

        return round(
            skill_score * SKILL_WEIGHT +
            experience_score * EXPERIENCE_WEIGHT,
            3,
        )