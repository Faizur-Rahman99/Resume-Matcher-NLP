from src.configuration.configuration import ConfigurationManager
from src.components.data_preprocessing import DataPreprocessing

config = ConfigurationManager().get_data_preprocessing_config()
preprocessor = DataPreprocessing(config)

examples = [
    "Experienced in C++, Node.js and TensorFlow.",
    "Expert in ASP.NET, SQL Server and Python.",
    "Worked with React.js, Next.js and Docker.",
]

for text in examples:
    print("=" * 50)
    print("Original :", text)
    print("Processed:", preprocessor.preprocess_text(text))