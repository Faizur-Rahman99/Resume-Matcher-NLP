from src.configuration.configuration import ConfigurationManager
from src.components.data_validation import DataValidation


def test_data_validation():

    config = ConfigurationManager().get_data_validation_config()

    validator = DataValidation(config)

    assert validator.validate_file_existence() is True
    assert validator.validate_resume_schema() is True