"""
report.py

Generate CSV and JSON reports for Python-Network-Scanner.

Author : Vikalp Pandey
Project: Python-Network-Scanner v6.1
"""

from __future__ import annotations

import csv
import json
from datetime import datetime

from config import (
    REPORTS_DIR,
    CSV_PREFIX,
    JSON_PREFIX,
)


def _timestamp() -> str:
    """
    Return current timestamp for filenames.
    """
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def save_csv(devices: list[dict]) -> str:
    """
    Save scan results to CSV.

    Returns:
        Path of generated CSV file.
    """

    filename = REPORTS_DIR / f"{CSV_PREFIX}_{_timestamp()}.csv"

    headers = [
        "IP Address",
        "MAC Address",
        "Vendor",
        "Hostname",
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow(headers)

        for device in devices:
            writer.writerow(
                [
                    device.get("ip", ""),
                    device.get("mac", ""),
                    device.get("vendor", ""),
                    device.get("hostname", ""),
                ]
            )

    return str(filename)


def save_json(devices: list[dict]) -> str:
    """
    Save scan results to JSON.

    Returns:
        Path of generated JSON file.
    """

    filename = REPORTS_DIR / f"{JSON_PREFIX}_{_timestamp()}.json"

    with open(filename, mode="w", encoding="utf-8") as json_file:

        json.dump(
            devices,
            json_file,
            indent=4,
            ensure_ascii=False,
        )

    return str(filename)
