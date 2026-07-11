from src.utils.skill_repository import SkillRepository


def test_skill_repository():

    repository = SkillRepository()

    skills = repository.get_all_skills()

    assert len(skills) > 100

    assert "Python" in skills

    assert "SQL" in skills

    assert len(skills) == len(set(skills))