from src.nlp.technical_terms import TechnicalTermProtector


def test_protect_and_restore():

    text = "Experienced in C++, Node.js and TensorFlow."

    protected, mapping = TechnicalTermProtector.protect(text)

    restored = TechnicalTermProtector.restore(
        protected,
        mapping
    )

    assert restored == "Experienced in c++, node.js and tensorflow."