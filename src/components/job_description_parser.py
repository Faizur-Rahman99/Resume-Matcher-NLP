from src.components.experience_extractor import ExperienceExtractor
from src.components.skill_extractor import SkillExtractor

from src.entity.job_description import JobDescription


class JobDescriptionParser:
    """
    Parses raw job description text into a structured JobDescription object.
    """

    def __init__(self):
        self.skill_extractor = SkillExtractor()
        self.experience_extractor = ExperienceExtractor()

    def parse(self, text: str) -> JobDescription:
        """
        Extract structured information from a job description.
        """

        job = JobDescription()

        job.skills = self.skill_extractor.extract_skills(text)

        experience = self.experience_extractor.extract(text)

        job.experience_years = (
            experience
            if experience is not None
            else 0
        )

        return job