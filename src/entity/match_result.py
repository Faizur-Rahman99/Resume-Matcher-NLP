from dataclasses import dataclass, field


@dataclass
class MatchResult:
    overall_score: float
    rule_based_score: float
    tfidf_score: float
    semantic_score: float
    skill_score: float
    experience_score: float
    missing_skills: list[str] = field(default_factory=list)