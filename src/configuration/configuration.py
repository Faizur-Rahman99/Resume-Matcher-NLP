from pathlib import Path

from src.entity.config_entity import DataValidationConfig

from src.entity.config_entity import (
    DataValidationConfig,
    DataIngestionConfig,
    DataPreprocessingConfig,
)


class ConfigurationManager:
    def get_data_validation_config(self) -> DataValidationConfig:
        return DataValidationConfig(
            resume_data_path=Path("data/raw/resumes/training_data.csv"),
            job_roles_path=Path("data/raw/job_roles/job_roles.csv"),
            skills_list_path=Path("data/raw/skills/skills_list.csv"),
            skills_database_path=Path("data/raw/skills/skills_database.json"),
            test_resumes_path=Path("data/raw/resumes/test_resumes.json"),

            required_resume_columns=[
                "Resume ID",
                "Resume Text",
                "Education",
                "Experience Years",
                "Skills",
                "Job Role",
                "Category",
            ],

            required_job_role_columns=[
                "Job Title",
                "Category",
                "Education Requirement",
                "Experience Required",
                "Required Skills",
                "Salary Range",
            ],

            required_skill_columns=[
                "Skill Name",
                "Category",
            ],
        )

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        return DataIngestionConfig(
            resume_data_path=Path("data/raw/resumes/training_data.csv"),
            job_roles_path=Path("data/raw/job_roles/job_roles.csv"),
            skills_list_path=Path("data/raw/skills/skills_list.csv"),
            skills_database_path=Path("data/raw/skills/skills_database.json"),
            test_resumes_path=Path("data/raw/resumes/test_resumes.json"),
        )

    def get_data_preprocessing_config(self) -> DataPreprocessingConfig:
        return DataPreprocessingConfig()