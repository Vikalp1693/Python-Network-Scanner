"""
logger.py

Logging configuration for Python-Network-Scanner.
"""

import logging
from datetime import datetime

from config import (
    LOGS_DIR,
    LOG_PREFIX,
)

# ==========================================================
# Log File
# ==========================================================

LOG_FILE = LOGS_DIR / (
    f"{LOG_PREFIX}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
)

# ==========================================================
# Logger Name
# ==========================================================

LOGGER_NAME = "PythonNetworkScanner"


def setup_logger() -> logging.Logger:
    """
    Create and configure the application logger.

    Returns:
        logging.Logger
    """

    logger = logging.getLogger(LOGGER_NAME)

    # Prevent duplicate logs
    logger.propagate = False

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # ------------------------------------------------------
    # File Handler
    # ------------------------------------------------------

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")

    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # ------------------------------------------------------
    # Console Handler
    # ------------------------------------------------------

    console_handler = logging.StreamHandler()

    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # ------------------------------------------------------
    # Register Handlers
    # ------------------------------------------------------

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
