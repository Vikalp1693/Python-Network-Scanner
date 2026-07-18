"""
utils.py

Reusable helper functions for Python-Network-Scanner.

Author : Vikalp Pandey
Project: Python-Network-Scanner v6.1
"""

from __future__ import annotations

import ipaddress
import socket


def validate_network(network: str) -> bool:
    """
    Validate CIDR network.

    Example:
        192.168.1.0/24
    """

    try:
        ipaddress.ip_network(network, strict=False)
        return True

    except ValueError:
        return False


def normalize_mac(mac: str) -> str:
    """
    Convert MAC address to uppercase format.

    Example:
        aa:bb:cc:11:22:33
            ↓
        AA:BB:CC:11:22:33
    """

    if not mac:
        return "Unknown"

    return mac.upper()


def resolve_hostname(ip: str) -> str:
    """
    Resolve hostname from IP address.
    """

    try:
        hostname = socket.gethostbyaddr(ip)[0]

        if hostname.strip():
            return hostname

    except (
        socket.herror,
        socket.gaierror,
        TimeoutError,
        OSError,
    ):
        pass

    return "Unknown"


def sort_devices(devices: list[dict]) -> list[dict]:
    """
    Sort devices by IP address.
    """

    return sorted(devices, key=lambda device: ipaddress.ip_address(device["ip"]))


def unique_devices(devices: list[dict]) -> list[dict]:
    """
    Remove duplicate devices based on IP.
    """

    seen = set()

    result = []

    for device in devices:

        ip = device["ip"]

        if ip not in seen:
            seen.add(ip)
            result.append(device)

    return result


def safe_string(value: str | None) -> str:
    """
    Convert None or empty values into 'Unknown'.
    """

    if value is None:
        return "Unknown"

    value = str(value).strip()

    if not value:
        return "Unknown"

    return value
