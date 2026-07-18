"""
scanner.py
Main entry point for Python Network Scanner Professional v6.0
"""

import argparse
from colorama import Fore, init

from config import (
    DEFAULT_THREADS,
    MAX_THREADS
)

from utils import validate_network
from scanner_core import scan_network

# -------------------------------------------------------
# Initialize Colorama
# -------------------------------------------------------

init(autoreset=True)


# -------------------------------------------------------
# Main Function
# -------------------------------------------------------

def main():

    parser = argparse.ArgumentParser(
        description="Python Network Scanner Professional v6.0"
    )

    parser.add_argument(
        "-n",
        "--network",
        help="Target Network (Example: 192.168.1.0/24)"
    )

    parser.add_argument(
        "-t",
        "--threads",
        type=int,
        default=DEFAULT_THREADS,
        help=f"Worker Threads (1-{MAX_THREADS})"
    )

    args = parser.parse_args()

    # ---------------------------------------------------
    # Get Network
    # ---------------------------------------------------

    if args.network:

        network = args.network

    else:

        network = input(
            "Enter Target Network (Example: 192.168.1.0/24): "
        )

    # ---------------------------------------------------
    # Validate Threads
    # ---------------------------------------------------

    if args.threads < 1:

        print(Fore.RED + "Thread count must be at least 1.")
        return

    if args.threads > MAX_THREADS:

        print(
            Fore.RED +
            f"Maximum allowed threads: {MAX_THREADS}"
        )
        return

    # ---------------------------------------------------
    # Validate Network
    # ---------------------------------------------------

    try:

        validate_network(network)

    except ValueError:

        print(Fore.RED + "Invalid network address.")
        return

    # ---------------------------------------------------
    # Start Scanner
    # ---------------------------------------------------

    try:

        scan_network(
            network,
            args.threads
        )

    except KeyboardInterrupt:

        print(
            Fore.RED +
            "\n\nScan cancelled by user."
        )

    except Exception as e:

        print(
            Fore.RED +
            f"\nUnexpected Error: {e}"
        )


# -------------------------------------------------------
# Program Entry
# -------------------------------------------------------

if __name__ == "__main__":
    main()