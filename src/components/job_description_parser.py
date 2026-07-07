from src.components.experience_extractor import ExperienceExtractor
from src.components.skill_extractor import SkillExtractor
from src.entity.job_description import JobDescription


class JobDescriptionParser:

    def __init__(self):
        self.skill_extractor = SkillExtractor()
        self.experience_extractor = ExperienceExtractor()

    def parse(self, text: str) -> JobDescription:

        job = JobDescription()

        job.skills = self.skill_extractor.extract_skills(text)
        job.experience_years = self.experience_extractor.extract(text)

        return job