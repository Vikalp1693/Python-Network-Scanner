"""
vendor_lookup.py

Offline MAC Vendor Lookup using the official IEEE OUI database.

Author : Vikalp Pandey
Project: Python-Network-Scanner v6.1
"""

from __future__ import annotations

import csv

from config import OUI_DATABASE


class VendorLookup:
    """
    Loads the IEEE OUI database once and performs
    fast vendor lookups using an in-memory dictionary.
    """

    def __init__(self) -> None:
        self._vendors: dict[str, str] = {}
        self._load_database()

    def _load_database(self) -> None:
        """
        Load the IEEE OUI CSV into memory.
        """

        if not OUI_DATABASE.exists():
            print(f"[WARNING] OUI database not found: {OUI_DATABASE}")
            return

        try:
            with open(OUI_DATABASE, mode="r", encoding="utf-8", newline="") as csv_file:

                reader = csv.DictReader(csv_file)

                for row in reader:

                    prefix = row["Assignment"].strip().upper()
                    vendor = row["Organization Name"].strip()

                    self._vendors[prefix] = vendor

        except Exception as error:
            print(f"[ERROR] Failed to load OUI database: {error}")

    def get_vendor(self, mac: str) -> str:
        """
        Return vendor name for a MAC address.

        Example:
            80:D2:1D:AA:BB:CC
                 ↓
            80D21D
        """

        if not mac:
            return "Unknown"

        prefix = mac.replace(":", "").replace("-", "").upper()[:6]

        return self._vendors.get(prefix, "Unknown")

    @property
    def total_vendors(self) -> int:
        """
        Number of vendors loaded.
        """
        return len(self._vendors)
