"""
config.py
Application configuration for Python Network Scanner Professional
"""

# -------------------------------------------------------
# Application Information
# -------------------------------------------------------

APP_NAME = "Python Network Scanner Professional"
VERSION = "6.0"
AUTHOR = "Vikalp Pandey"

# -------------------------------------------------------
# Scanner Configuration
# -------------------------------------------------------

DEFAULT_THREADS = 10
MAX_THREADS = 100
SCAN_TIMEOUT = 2

# -------------------------------------------------------
# Report Configuration
# -------------------------------------------------------

REPORT_FOLDER = "reports"
LOG_FOLDER = "logs"

CSV_PREFIX = "scan"
JSON_PREFIX = "scan"

# -------------------------------------------------------
# Display Configuration
# -------------------------------------------------------

TABLE_FORMAT = "grid"

BANNER_WIDTH = 100

# -------------------------------------------------------
# Progress Bar
# -------------------------------------------------------

PROGRESS_BAR_LENGTH = 30