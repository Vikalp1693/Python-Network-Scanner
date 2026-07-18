"""
logger.py
Logging configuration for Python Network Scanner Professional.
"""

import logging
import os
from datetime import datetime

from config import LOG_FOLDER

# -------------------------------------------------------
# Create Logs Folder
# -------------------------------------------------------

os.makedirs(LOG_FOLDER, exist_ok=True)

# -------------------------------------------------------
# Log File
# -------------------------------------------------------

LOG_FILE = os.path.join(
    LOG_FOLDER,
    f"scan_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
)


def setup_logger():
    """
    Configure and return the application logger.
    """

    logger = logging.getLogger("NetworkScanner")

    # Prevent duplicate handlers
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # File Handler
    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger