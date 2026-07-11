from src.components.experience_extractor import ExperienceExtractor


extractor = ExperienceExtractor()


def test_extract_years():

    assert extractor.extract(
        "Software engineer with 5 years of experience."
    ) == 5


def test_extract_plus():

    assert extractor.extract(
        "Python developer with 10+ years experience."
    ) == 10


def test_extract_none():

    assert extractor.extract(
        "Recent graduate looking for opportunities."
    ) is None