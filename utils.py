"""
utils.py
Utility functions for Python Network Scanner Professional.
"""

import ipaddress
import socket

from mac_vendor_lookup import MacLookup

# -------------------------------------------------------
# Initialize Vendor Lookup
# -------------------------------------------------------

vendor_lookup = MacLookup()

# -------------------------------------------------------
# Hostname Lookup
# -------------------------------------------------------

def get_hostname(ip):
    """
    Returns the hostname of an IP address.
    """

    try:
        return socket.gethostbyaddr(ip)[0]

    except Exception:
        return "Unknown"


# -------------------------------------------------------
# Vendor Lookup
# -------------------------------------------------------

def get_vendor(mac):
    """
    Returns the vendor name from a MAC address.
    """

    try:
        return vendor_lookup.lookup(mac)

    except Exception:
        return "Unknown"


# -------------------------------------------------------
# Validate Network
# -------------------------------------------------------

def validate_network(network):
    """
    Validate network address.

    Raises:
        ValueError if invalid.
    """

    return ipaddress.ip_network(
        network,
        strict=False
    )


# -------------------------------------------------------
# Sort Devices
# -------------------------------------------------------

def sort_devices(devices):
    """
    Sort devices by IP Address.
    """

    return sorted(
        devices,
        key=lambda x: list(
            map(
                int,
                x[0].split(".")
            )
        )
    )


# -------------------------------------------------------
# Device Statistics
# -------------------------------------------------------

def calculate_statistics(devices):
    """
    Calculate scan statistics.
    """

    stats = {

        "devices": len(devices),

        "known_vendors": 0,
        "unknown_vendors": 0,

        "known_hostnames": 0,
        "unknown_hostnames": 0
    }

    for device in devices:

        vendor = device[2]
        hostname = device[3]

        if vendor == "Unknown":
            stats["unknown_vendors"] += 1
        else:
            stats["known_vendors"] += 1

        if hostname == "Unknown":
            stats["unknown_hostnames"] += 1
        else:
            stats["known_hostnames"] += 1

    return stats