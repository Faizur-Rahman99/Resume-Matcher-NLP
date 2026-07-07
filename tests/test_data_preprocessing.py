from src.components.data_preprocessing import DataPreprocessing
from src.configuration.configuration import ConfigurationManager


def test_preprocess_text():

    config = ConfigurationManager().get_data_preprocessing_config()

    preprocessor = DataPreprocessing(config)

    text = "Education: Bachelor's in Computer Science."

    cleaned = preprocessor.preprocess_text(text)

    assert cleaned == "education bachelor s in computer science"



def test_preserve_technical_terms():

    config = ConfigurationManager().get_data_preprocessing_config()

    preprocessor = DataPreprocessing(config)

    text = "Experienced in C++, Node.js and TensorFlow."

    cleaned = preprocessor.preprocess_text(text)

    assert cleaned == "experienced in c++ node.js and tensorflow"