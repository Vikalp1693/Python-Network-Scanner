"""
scanner_core.py

Core scanning engine for Python-Network-Scanner.

Author : Vikalp Pandey
Project: Python-Network-Scanner v6.1
"""

from __future__ import annotations

import ipaddress
from concurrent.futures import ThreadPoolExecutor

from scapy.all import ARP, Ether, srp

from config import DEFAULT_TIMEOUT, DEFAULT_THREADS
from progress import update_progress
from utils import (
    normalize_mac,
    resolve_hostname,
    safe_string,
    sort_devices,
    unique_devices,
)
from vendor_lookup import VendorLookup


class NetworkScanner:
    """
    Core network scanner.
    """

    def __init__(
        self,
        timeout: int = DEFAULT_TIMEOUT,
        threads: int = DEFAULT_THREADS,
    ) -> None:

        self.timeout = timeout
        self.threads = threads

        self.vendor_lookup = VendorLookup()

    def _scan_network(self, network: str):
        """
        Perform ARP scan.
        """

        packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=network)

        answered, _ = srp(
            packet,
            timeout=self.timeout,
            verbose=False,
        )

        return answered

    def _process_device(self, response):
        """
        Process one discovered device.
        """

        ip = response.psrc

        mac = normalize_mac(response.hwsrc)

        vendor = self.vendor_lookup.get_vendor(mac)

        hostname = resolve_hostname(ip)

        update_progress()

        return {
            "ip": ip,
            "mac": mac,
            "vendor": safe_string(vendor),
            "hostname": safe_string(hostname),
        }

    def scan(self, network: str):
        """
        Scan an IPv4 network.
        """

        ipaddress.ip_network(
            network,
            strict=False,
        )

        answered = self._scan_network(network)

        devices = []

        with ThreadPoolExecutor(max_workers=self.threads) as executor:

            futures = [
                executor.submit(
                    self._process_device,
                    received,
                )
                for _, received in answered
            ]

            for future in futures:
                devices.append(future.result())

        devices = unique_devices(devices)

        devices = sort_devices(devices)

        return devices
