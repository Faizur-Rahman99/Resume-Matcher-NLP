from src.matching.skill_matcher import SkillMatcher


def test_full_match():

    matcher = SkillMatcher()

    score = matcher.match(
        ["Python", "SQL", "Docker"],
        ["Python", "SQL", "Docker"]
    )

    assert score == 1.0


def test_partial_match():

    matcher = SkillMatcher()

    score = matcher.match(
        ["Python", "SQL"],
        ["Python", "SQL", "Docker", "AWS"]
    )

    assert score == 0.5


def test_no_match():

    matcher = SkillMatcher()

    score = matcher.match(
        ["Java"],
        ["Python", "SQL"]
    )

    assert score == 0.0