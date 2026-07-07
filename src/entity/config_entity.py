from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataValidationConfig:
    resume_data_path: Path
    job_roles_path: Path
    skills_list_path: Path
    skills_database_path: Path
    test_resumes_path: Path

    required_resume_columns: list[str]
    required_job_role_columns: list[str]
    required_skill_columns: list[str]

@dataclass(frozen=True)
class DataIngestionConfig:
    resume_data_path: Path
    job_roles_path: Path
    skills_list_path: Path
    skills_database_path: Path
    test_resumes_path: Path

@dataclass(frozen=True)
class DataPreprocessingConfig:
    lowercase: bool = True
    remove_punctuation: bool = True
    remove_extra_spaces: bool = True