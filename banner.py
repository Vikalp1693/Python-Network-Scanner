"""
banner.py

Displays the application banner and startup information.
"""

from datetime import datetime

from colorama import Fore, Style

from config import (
    APP_NAME,
    APP_VERSION,
    AUTHOR,
    SEPARATOR,
)


def print_banner(threads: int) -> None:
    """
    Display the application banner.
    """

    print(Fore.CYAN + SEPARATOR)

    print(Fore.GREEN + APP_NAME.center(len(SEPARATOR)))

    print(Fore.WHITE + f"Version {APP_VERSION}".center(len(SEPARATOR)))

    print(Fore.CYAN + SEPARATOR)

    print(Fore.YELLOW + f"{'Author':<12}: {AUTHOR}")

    print(Fore.YELLOW + f"{'Threads':<12}: {threads}")

    print(
        Fore.YELLOW
        + f"{'Started':<12}: "
        + datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    )

    print(Fore.CYAN + SEPARATOR)

    print(Style.RESET_ALL)
