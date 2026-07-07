from src.nlp.lemmatizer import TextLemmatizer
from src.nlp.normalizer import TextNormalizer
from src.nlp.stopwords import StopwordRemover
from src.nlp.technical_terms import TechnicalTermProtector
from src.nlp.tokenizer import TextTokenizer


class NLPPipeline:

    def __init__(self):
        self.protector = TechnicalTermProtector()
        self.stopwords = StopwordRemover()
        self.lemmatizer = TextLemmatizer()

    def process(self, text: str) -> list[str]:
        text, mapping = self.protector.protect(text)

        text = TextNormalizer.normalize(text)

        tokens = TextTokenizer.tokenize(text)
        tokens = self.stopwords.remove(tokens)
        tokens = self.lemmatizer.lemmatize(tokens)

        text = " ".join(tokens)
        text = self.protector.restore(text, mapping)

        return text.split()