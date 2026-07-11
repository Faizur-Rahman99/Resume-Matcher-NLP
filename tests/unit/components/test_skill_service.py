from src.services.skill_service import SkillService


def test_skill_lookup():

    service = SkillService()

    lookup = service.get_skill_lookup()

    assert "python" in lookup
    assert lookup["python"] == "Python"


def test_max_skill_length():

    service = SkillService()

    max_length = service.get_max_skill_length()

    assert max_length >= 1