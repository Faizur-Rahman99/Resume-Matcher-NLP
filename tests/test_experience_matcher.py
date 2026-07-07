from src.matching.experience_matcher import ExperienceMatcher


matcher = ExperienceMatcher()


def test_exact_match():
    assert matcher.match(5, 5) == 1.0


def test_more_experience():
    assert matcher.match(8, 5) == 1.0


def test_partial_match():
    assert matcher.match(3, 5) == 0.6


def test_no_experience():
    assert matcher.match(None, 5) == 0.0


def test_no_requirement():
    assert matcher.match(5, None) == 1.0