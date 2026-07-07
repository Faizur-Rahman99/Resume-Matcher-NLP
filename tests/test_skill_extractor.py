from src.components.skill_extractor import SkillExtractor


def test_extract_single_and_multi_word_skills():

    extractor = SkillExtractor()

    text = """
    Experienced in Python, SQL Server, Machine Learning,
    Docker and TensorFlow.
    """

    skills = extractor.extract_skills(text)

    assert "Python" in skills
    assert "Docker" in skills
    assert "TensorFlow" in skills

    if "SQL Server" in extractor.skill_service.get_technical_terms():
        assert "SQL Server" in skills

    if "Machine Learning" in extractor.skill_service.get_technical_terms():
        assert "Machine Learning" in skills