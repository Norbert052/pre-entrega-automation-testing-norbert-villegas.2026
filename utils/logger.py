import logging
import os

LOG_DIR = "logs"
LOG_FILE = "automation.log"


def create_logger():
    os.makedirs(LOG_DIR, exist_ok=True)
    logger = logging.getLogger("automation")
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s", "%Y-%m-%d %H:%M:%S")

    file_handler = logging.FileHandler(os.path.join(LOG_DIR, LOG_FILE), encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


logger = create_logger()
