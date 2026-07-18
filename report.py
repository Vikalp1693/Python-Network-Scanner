"""
report.py
Handles report generation for Python Network Scanner Professional.
"""

import csv
import json
import os
from datetime import datetime

from config import (
    REPORT_FOLDER,
    CSV_PREFIX,
    JSON_PREFIX
)

# -------------------------------------------------------
# Create Reports Folder
# -------------------------------------------------------

os.makedirs(REPORT_FOLDER, exist_ok=True)


def get_report_filenames():
    """
    Generate timestamped report filenames.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    csv_file = os.path.join(
        REPORT_FOLDER,
        f"{CSV_PREFIX}_{timestamp}.csv"
    )

    json_file = os.path.join(
        REPORT_FOLDER,
        f"{JSON_PREFIX}_{timestamp}.json"
    )

    return csv_file, json_file


def save_csv(devices):
    """
    Save scan results to CSV.
    """

    csv_file, _ = get_report_filenames()

    with open(csv_file, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "IP Address",
            "MAC Address",
            "Vendor",
            "Hostname"
        ])

        writer.writerows(devices)

    return csv_file


def save_json(devices):
    """
    Save scan results to JSON.
    """

    _, json_file = get_report_filenames()

    data = []

    for device in devices:

        data.append({

            "IP Address": device[0],
            "MAC Address": device[1],
            "Vendor": device[2],
            "Hostname": device[3]

        })

    with open(json_file, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4
        )

    return json_file


def save_reports(devices):
    """
    Save both CSV and JSON reports.
    """

    csv_file = save_csv(devices)

    json_file = save_json(devices)

    return csv_file, json_file