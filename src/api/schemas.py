from pydantic import BaseModel


class ResumeSchema(BaseModel):
    skills: list[str]
    experience_years: int


class JobSchema(BaseModel):
    skills: list[str]
    experience_years: int


class MatchRequest(BaseModel):
    resume: ResumeSchema
    job: JobSchema


class MatchResponse(BaseModel):
    overall_score: float
    rule_based_score: float
    tfidf_score: float
    semantic_score: float
    skill_score: float
    experience_score: float
    missing_skills: list[str]