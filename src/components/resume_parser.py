from src.components.contact_extractor import ContactExtractor
from src.components.education_extractor import EducationExtractor
from src.components.experience_extractor import ExperienceExtractor
from src.components.name_extractor import NameExtractor
from src.components.project_extractor import ProjectExtractor
from src.components.skill_extractor import SkillExtractor

from src.entity.resume import Resume


class ResumeParser:
    """
    Parses raw resume text into a structured Resume object.
    """

    def __init__(self):
        self.skill_extractor = SkillExtractor()
        self.experience_extractor = ExperienceExtractor()
        self.contact_extractor = ContactExtractor()
        self.name_extractor = NameExtractor()
        self.education_extractor = EducationExtractor()
        self.project_extractor = ProjectExtractor()

    def parse(self, text: str) -> Resume:
        """
        Extract structured information from resume text.
        """

        resume = Resume()

        # Personal information
        resume.name = self.name_extractor.extract(text)
        resume.email = self.contact_extractor.extract_email(text)
        resume.phone = self.contact_extractor.extract_phone(text)

        # Resume content
        resume.skills = self.skill_extractor.extract_skills(text)
        resume.education = self.education_extractor.extract(text)
        resume.projects = self.project_extractor.extract(text)

        # Experience
        experience = self.experience_extractor.extract(text)
        resume.experience_years = experience if experience is not None else 0

        return resume