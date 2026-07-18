"""
scanner_core.py
Core scanning logic for Python Network Scanner Professional.
"""

import time

from concurrent.futures import ThreadPoolExecutor, as_completed

from colorama import Fore
from scapy.all import ARP, Ether, srp
from tabulate import tabulate

from banner import print_banner
from config import (
    DEFAULT_THREADS,
    SCAN_TIMEOUT,
    TABLE_FORMAT
)
from logger import setup_logger
from progress import (
    reset_progress,
    update_progress,
    finish_progress
)
from report import save_reports
from utils import (
    calculate_statistics,
    get_hostname,
    get_vendor,
    sort_devices
)

logger = setup_logger()


# -------------------------------------------------------
# Process One Device
# -------------------------------------------------------

def process_device(received, total):
    """
    Process a single discovered device.
    """

    ip = received.psrc
    mac = received.hwsrc

    hostname = get_hostname(ip)
    vendor = get_vendor(mac)

    update_progress(total)

    return [
        ip,
        mac,
        vendor,
        hostname
    ]


# -------------------------------------------------------
# Scan Network
# -------------------------------------------------------

def scan_network(network, threads=DEFAULT_THREADS):
    """
    Scan the target network.
    """

    logger.info(f"Scan Started : {network}")

    print_banner(threads)

    print(Fore.YELLOW + f"\nTarget Network : {network}")
    print(Fore.YELLOW + "Scanning...\n")

    start_time = time.time()

    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether / arp

    answered = srp(
        packet,
        timeout=SCAN_TIMEOUT,
        verbose=False
    )[0]

    if len(answered) == 0:

        print(Fore.RED + "No active devices found.")

        logger.warning("No devices found.")

        return

    reset_progress()

    devices = []

    with ThreadPoolExecutor(max_workers=threads) as executor:

        futures = [

            executor.submit(
                process_device,
                received,
                len(answered)
            )

            for _, received in answered

        ]

        for future in as_completed(futures):

            try:

                devices.append(
                    future.result()
                )

            except Exception as e:

                logger.exception(e)

    finish_progress()

    devices = sort_devices(devices)

    print()

    print(
        Fore.CYAN +
        tabulate(
            devices,
            headers=[
                "IP Address",
                "MAC Address",
                "Vendor",
                "Hostname"
            ],
            tablefmt=TABLE_FORMAT
        )
    )

    csv_file, json_file = save_reports(devices)

    stats = calculate_statistics(devices)

    end_time = time.time()

    duration = end_time - start_time

    print()

    print(Fore.GREEN + "=" * 60)
    print(Fore.GREEN + "SCAN SUMMARY")
    print(Fore.GREEN + "=" * 60)

    print(f"Devices Found      : {stats['devices']}")
    print(f"Known Vendors     : {stats['known_vendors']}")
    print(f"Unknown Vendors   : {stats['unknown_vendors']}")
    print(f"Known Hostnames   : {stats['known_hostnames']}")
    print(f"Unknown Hostnames : {stats['unknown_hostnames']}")
    print(f"Threads Used      : {threads}")
    print(f"Time Taken        : {duration:.2f} sec")

    if duration > 0:

        print(
            f"Speed             : "
            f"{stats['devices']/duration:.2f} devices/sec"
        )

    print()

    print(Fore.BLUE + f"CSV Report  : {csv_file}")
    print(Fore.BLUE + f"JSON Report : {json_file}")

    logger.info(f"Devices Found : {stats['devices']}")
    logger.info("Scan Completed")