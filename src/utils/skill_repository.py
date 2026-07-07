import pandas as pd

from src.configuration.configuration import ConfigurationManager


class SkillRepository:
    """
    Loads and provides access to skills from skills_list.csv.
    """

    def __init__(self):

        config = ConfigurationManager().get_data_validation_config()

        self.skills_path = config.skills_list_path

        self._skills = self._load_skills()

    def _load_skills(self) -> list[str]:
        """
        Load skills once during initialization.
        """

        df = pd.read_csv(self.skills_path)

        skills = (
            df["Skill Name"]
            .dropna()
            .drop_duplicates()
            .sort_values()
            .tolist()
        )

        return skills

    def get_all_skills(self) -> list[str]:
        """
        Return cached skills.
        """

        return self._skills.copy()