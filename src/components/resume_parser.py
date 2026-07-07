from src.components.skill_extractor import SkillExtractor
from src.entity.resume import Resume
from src.components.experience_extractor import ExperienceExtractor

class ResumeParser:

    def __init__(self):
        self.skill_extractor = SkillExtractor()
        self.experience_extractor = ExperienceExtractor()

    def parse(self, text: str) -> Resume:

        resume = Resume()

        resume.skills = self.skill_extractor.extract_skills(text)
        resume.experience_years = self.experience_extractor.extract(text)
        return resume