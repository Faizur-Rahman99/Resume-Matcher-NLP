from src.utils.skill_repository import SkillRepository


class SkillService:

    def __init__(self):
        self.repository = SkillRepository()

    def get_technical_terms(self) -> list[str]:
        return self.repository.get_all_skills()

    def get_skill_lookup(self) -> dict[str, str]:

        skills = self.get_technical_terms()

        return {
            skill.lower(): skill
            for skill in skills
        }

    def get_max_skill_length(self) -> int:

        skills = self.get_technical_terms()

        return max(
            len(skill.split())
            for skill in skills
        )