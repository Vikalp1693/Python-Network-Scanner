"""
progress.py

Thread-safe progress bar for Python-Network-Scanner.
"""

import threading
import time

from colorama import Fore, Style

from config import PROGRESS_BAR_WIDTH

# ==========================================================
# Global Progress State
# ==========================================================

_lock = threading.Lock()

_current = 0
_total = 0
_start_time = 0.0


# ==========================================================
# Initialize Progress
# ==========================================================


def start_progress(total: int) -> None:
    """
    Initialize the progress bar.

    Args:
        total: Total number of tasks.
    """

    global _current, _total, _start_time

    _current = 0
    _total = total
    _start_time = time.perf_counter()


# ==========================================================
# Update Progress
# ==========================================================


def update_progress() -> None:
    """
    Increment and display the progress bar.
    """

    global _current

    with _lock:

        _current += 1

        percentage = _current / _total if _total else 1

        filled = int(PROGRESS_BAR_WIDTH * percentage)

        bar = "█" * filled + "░" * (PROGRESS_BAR_WIDTH - filled)

        elapsed = time.perf_counter() - _start_time

        print(
            f"\r{Fore.CYAN}"
            f"[{bar}] "
            f"{percentage * 100:6.2f}% "
            f"({_current}/{_total}) "
            f"Elapsed: {elapsed:5.2f}s",
            end="",
            flush=True,
        )


# ==========================================================
# Finish Progress
# ==========================================================


def finish_progress() -> None:
    """
    Finish the progress bar.
    """

    print(Style.RESET_ALL)
