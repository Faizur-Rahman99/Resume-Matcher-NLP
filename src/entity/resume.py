from dataclasses import dataclass, field


@dataclass
class Resume:
    skills: list[str] = field(default_factory=list)
    education: list[str] = field(default_factory=list)
    experience_years: int | None = None
    job_role: str | None = None