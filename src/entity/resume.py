from dataclasses import dataclass, field


@dataclass
class Resume:

    name: str | None = None

    email: str | None = None

    phone: str | None = None

    skills: list[str] = field(default_factory=list)

    education: list[str] = field(default_factory=list)

    projects: list[str] = field(default_factory=list)

    experience_years: int = 0

    job_role: str | None = None