from dataclasses import dataclass


@dataclass
class MatchReport:
    overall_score: float
    matched_skills: list[str]
    missing_skills: list[str]
    experience_gap: int
    recommendation: str