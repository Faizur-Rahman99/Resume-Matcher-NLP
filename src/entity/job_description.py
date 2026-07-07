from dataclasses import dataclass, field


@dataclass
class JobDescription:
    skills: list[str] = field(default_factory=list)
    experience_years: int | None = None
    job_role: str | None = None