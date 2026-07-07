from src.entity.config_entity import DataPreprocessingConfig
from src.nlp.normalizer import TextNormalizer
from src.nlp.technical_terms import TechnicalTermProtector

class DataPreprocessing:

    def __init__(self, config: DataPreprocessingConfig):
        self.config = config

    def preprocess_text(self, text: str) -> str:

        protected_text, mapping = TechnicalTermProtector.protect(text)

        if self.config.lowercase:
            protected_text = TextNormalizer.lowercase(protected_text)

        if self.config.remove_punctuation:
            protected_text = TextNormalizer.remove_punctuation(protected_text)

        if self.config.remove_extra_spaces:
            protected_text = TextNormalizer.remove_extra_spaces(protected_text)

        protected_text = TechnicalTermProtector.restore(
            protected_text,
            mapping
        )

        return protected_text