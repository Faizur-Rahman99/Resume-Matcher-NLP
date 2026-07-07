from src.logger.logging import logger


def test_logger():
    logger.info("Logger is working!")
    assert True