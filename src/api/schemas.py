from pydantic import BaseModel, Field


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
    matched_skills: list[str]
    missing_skills: list[str]
    explanation: list[str]

class ResumeData(BaseModel):

    filename: str

    name: str | None = None

    email: str | None = None

    phone: str | None = None

    education: list[str] = Field(default_factory=list)

    projects: list[str] = Field(default_factory=list)

    skills: list[str]

    experience_years: int


class JobData(BaseModel):

    skills: list[str]

    experience_years: int


class BatchMatchRequest(BaseModel):

    job: JobData

    resumes: list[ResumeData]

class CandidateResult(BaseModel):

    filename: str

    name: str | None = None

    email: str | None = None

    phone: str | None = None

    education: list[str] = Field(default_factory=list)

    projects: list[str] = Field(default_factory=list)

    overall_score: float

    skill_score: float

    experience_score: float

    matched_skills: list[str]

    missing_skills: list[str]

    explanation: list[str]


class BatchMatchResponse(BaseModel):

    results: list[CandidateResult]