"""
progress.py
Professional progress bar for Python Network Scanner Professional.
"""

import threading
from colorama import Fore

from config import PROGRESS_BAR_LENGTH

# -------------------------------------------------------
# Thread Safe Variables
# -------------------------------------------------------

progress_lock = threading.Lock()

current_progress = 0


def reset_progress():
    """
    Reset progress before every scan.
    """

    global current_progress

    current_progress = 0


def update_progress(total):
    """
    Update progress bar safely.
    """

    global current_progress

    with progress_lock:

        current_progress += 1

        percent = current_progress / total

        filled = int(PROGRESS_BAR_LENGTH * percent)

        bar = (
            "█" * filled +
            "░" * (PROGRESS_BAR_LENGTH - filled)
        )

        print(
            Fore.YELLOW +
            f"\r[{bar}] {percent*100:6.2f}% "
            f"({current_progress}/{total})",
            end="",
            flush=True
        )


def finish_progress():
    """
    Move cursor to next line after progress completes.
    """

    print()