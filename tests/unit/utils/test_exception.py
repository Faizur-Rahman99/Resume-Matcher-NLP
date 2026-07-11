import sys
import pytest

from src.exception.exception import CustomException


def test_custom_exception():

    with pytest.raises(CustomException):

        try:
            _ = 10 / 0

        except Exception as e:
            raise CustomException(e, sys)