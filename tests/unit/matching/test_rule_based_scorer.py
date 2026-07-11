from src.scoring.rule_based_scorer import RuleBasedScorer


def test_rule_based_scorer():

    scorer = RuleBasedScorer()

    score = scorer.calculate(
        skill_score=0.75,
        experience_score=0.8,
    )

    assert score == 0.765