import logging
import sys
import os

def get_logger(name: str = __name__, level: int = logging.INFO, log_to_file: bool = False, log_file: str = '/tmp/app.log') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False

    formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(name)s: %(message)s')

    if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if log_to_file and not any(isinstance(h, logging.FileHandler) for h in logger.handlers):
        try:
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(level)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except OSError as e:
            logger.warning(f"File logging could not be set up: {e}")

    return logger
