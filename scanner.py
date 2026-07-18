"""
scanner.py

Main entry point for Python-Network-Scanner.

Author : Vikalp Pandey
Version : 6.1
"""

from __future__ import annotations

import argparse
import sys

from colorama import init
from tabulate import tabulate

from banner import print_banner
from config import DEFAULT_THREADS
from logger import setup_logger
from progress import finish_progress, start_progress
from report import save_csv, save_json
from scanner_core import NetworkScanner
from utils import validate_network


def parse_arguments():
    """
    Parse command-line arguments.
    """

    parser = argparse.ArgumentParser(description="Python Network Scanner")

    parser.add_argument(
        "-n", "--network", help="Target network (Example: 192.168.1.0/24)"
    )

    parser.add_argument(
        "-t",
        "--threads",
        type=int,
        default=DEFAULT_THREADS,
        help="Number of worker threads",
    )

    return parser.parse_args()


def print_results(devices):
    """
    Display scan results in table format.
    """

    table = []

    for device in devices:

        table.append(
            [
                device["ip"],
                device["mac"],
                device["vendor"],
                device["hostname"],
            ]
        )

    print()

    print(
        tabulate(
            table,
            headers=[
                "IP Address",
                "MAC Address",
                "Vendor",
                "Hostname",
            ],
            tablefmt="grid",
        )
    )


def main():

    init(autoreset=True)

    logger = setup_logger()

    args = parse_arguments()

    network = args.network

    if not network:
        network = input("Enter Network (Example 192.168.1.0/24): ")

    if not validate_network(network):

        logger.error("Invalid network entered.")

        print("\nInvalid network.")

        sys.exit(1)

    print_banner(args.threads)

    logger.info(f"Scan Started for {network}")

    scanner = NetworkScanner(threads=args.threads)

    print("Scanning network...\n")

    devices = scanner.scan(network)

    start_progress(len(devices))

    finish_progress()

    print_results(devices)

    csv_file = save_csv(devices)

    json_file = save_json(devices)

    logger.info(f"Devices Found : {len(devices)}")
    logger.info(f"CSV Saved : {csv_file}")
    logger.info(f"JSON Saved : {json_file}")
    logger.info("Scan Completed")

    print(f"\nDevices Found : {len(devices)}")
    print(f"CSV Report    : {csv_file}")
    print(f"JSON Report   : {json_file}")


if __name__ == "__main__":
    main()
