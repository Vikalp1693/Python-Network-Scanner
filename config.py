"""
config.py

Central configuration file for Python-Network-Scanner.

All application-wide constants are defined here to make the
project easier to maintain and configure.
"""

from pathlib import Path

# ==========================================================
# Application Information
# ==========================================================

APP_NAME = "Python-Network-Scanner"
APP_VERSION = "6.1.0"
AUTHOR = "Vikalp Pandey"

# ==========================================================
# Network Scanner
# ==========================================================

DEFAULT_TIMEOUT = 2
DEFAULT_THREADS = 10
MAX_THREADS = 100

# ==========================================================
# Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

REPORTS_DIR = BASE_DIR / "reports"
LOGS_DIR = BASE_DIR / "logs"
DATA_DIR = BASE_DIR / "data"
SCREENSHOTS_DIR = BASE_DIR / "screenshots"

# IEEE OUI Database

OUI_DATABASE = DATA_DIR / "oui.csv"

# ==========================================================
# Report File Names
# ==========================================================

CSV_PREFIX = "scan"

JSON_PREFIX = "scan"

LOG_PREFIX = "scanner"

# ==========================================================
# Output
# ==========================================================

TABLE_FORMAT = "grid"

PROGRESS_BAR_WIDTH = 40

SEPARATOR = "=" * 80

# ==========================================================
# Create Required Directories
# ==========================================================

for directory in (
    REPORTS_DIR,
    LOGS_DIR,
    DATA_DIR,
    SCREENSHOTS_DIR,
):
    directory.mkdir(parents=True, exist_ok=True)
