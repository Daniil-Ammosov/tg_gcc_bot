import logging
import sys


def create_logger():
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.StreamHandler(sys.stderr))
    logger.addHandler(logging.StreamHandler(sys.stdout))
    return logger
