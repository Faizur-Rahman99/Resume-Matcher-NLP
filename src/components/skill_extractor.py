from src.nlp.lemmatizer import TextLemmatizer
from src.nlp.ngram_generator import NGramGenerator
from src.nlp.stopwords import StopwordRemover
from src.nlp.tokenizer import TextTokenizer
from src.services.skill_service import SkillService


class SkillExtractor:

    def __init__(self):
        self.skill_service = SkillService()
        self.stopword_remover = StopwordRemover()
        self.lemmatizer = TextLemmatizer()

    def extract_skills(self, text: str) -> list[str]:

        lookup = self.skill_service.get_skill_lookup()
        max_length = self.skill_service.get_max_skill_length()

        tokens = TextTokenizer.tokenize(text)
        tokens = self.stopword_remover.remove(tokens)
        tokens = self.lemmatizer.lemmatize(tokens)

        matches = set()

        for n in range(1, max_length + 1):

            ngrams = NGramGenerator.generate(tokens, n)

            for phrase in ngrams:

                skill = lookup.get(phrase.lower())

                if skill:
                    matches.add(skill)

        return sorted(matches)