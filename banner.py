"""
banner.py
Displays the application banner.
"""

from colorama import Fore, Style
from datetime import datetime

from config import (
    APP_NAME,
    VERSION,
    AUTHOR,
    BANNER_WIDTH
)


def print_banner(threads):
    """
    Display the application banner.
    """

    print(Fore.CYAN + "=" * BANNER_WIDTH)

    print(
        Fore.GREEN +
        APP_NAME.center(BANNER_WIDTH)
    )

    print(Fore.CYAN + "=" * BANNER_WIDTH)

    print(
        Fore.YELLOW +
        f"Version : {VERSION}"
    )

    print(
        Fore.YELLOW +
        f"Author  : {AUTHOR}"
    )

    print(
        Fore.YELLOW +
        f"Threads : {threads}"
    )

    print(
        Fore.YELLOW +
        "Started : "
        + datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    )

    print(Fore.CYAN + "=" * BANNER_WIDTH)
    print(Style.RESET_ALL)