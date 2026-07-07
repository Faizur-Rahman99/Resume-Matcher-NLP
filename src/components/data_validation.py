from pathlib import Path
import pandas as pd

from src.entity.config_entity import DataValidationConfig
from src.logger.logging import logger


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_file_existence(self) -> bool:
        files = [
            self.config.resume_data_path,
            self.config.job_roles_path,
            self.config.skills_list_path,
            self.config.skills_database_path,
            self.config.test_resumes_path,
        ]

        for file_path in files:
            if not Path(file_path).exists():
                logger.error(f"Missing file: {file_path}")
                return False

            logger.info(f"Found: {file_path}")

        return True

    def validate_resume_schema(self) -> bool:
        """
        Validate the schema of the resume dataset.
        """

        df = pd.read_csv(self.config.resume_data_path)

        missing_columns = [
            column
            for column in self.config.required_resume_columns
            if column not in df.columns
        ]

        if missing_columns:
            logger.error(
                f"Resume dataset is missing columns: {missing_columns}"
            )
            return False

        logger.info("Resume schema validation passed.")

        return True