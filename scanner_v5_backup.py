from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup
from colorama import Fore, Style, init
from tabulate import tabulate

import ipaddress
import csv
import socket
import time
import argparse
import json
import logging
import os

from datetime import datetime

# -------------------------------------------------------
# Initialize Colorama
# -------------------------------------------------------

init(autoreset=True)

# -------------------------------------------------------
# Create Required Folders
# -------------------------------------------------------

os.makedirs("reports", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# -------------------------------------------------------
# Logging Configuration
# -------------------------------------------------------

logging.basicConfig(
    filename="logs/scanner.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

# -------------------------------------------------------
# Helper Functions
# -------------------------------------------------------

def get_hostname(ip):
    """
    Returns hostname for a given IP.
    """

    try:
        return socket.gethostbyaddr(ip)[0]

    except Exception:
        return "Unknown"


def get_vendor(mac):
    """
    Returns vendor using MAC Address.
    """

    try:
        return MacLookup().lookup(mac)

    except Exception:
        return "Unknown"


def save_csv(devices, filename):
    """
    Save scan results as CSV.
    """

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "IP Address",
                "MAC Address",
                "Vendor",
                "Hostname",
            ]
        )

        writer.writerows(devices)


def save_json(devices, filename):
    """
    Save scan results as JSON.
    """

    data = []

    for device in devices:

        data.append(
            {
                "IP Address": device[0],
                "MAC Address": device[1],
                "Vendor": device[2],
                "Hostname": device[3],
            }
        )

    with open(filename, "w", encoding="utf-8") as file:

        json.dump(data, file, indent=4)


def print_banner():

    print(Fore.CYAN + "=" * 100)

    print(
        Fore.GREEN
        + "                  Python Network Scanner v5.0"
    )

    print(Fore.CYAN + "=" * 100)

    # -------------------------------------------------------
# Main Network Scan Function
# -------------------------------------------------------

def scan_network(network):

    logging.info(f"Scan Started for {network}")

    print_banner()

    print(Fore.YELLOW + f"\nTarget Network : {network}")
    print(Fore.YELLOW + "Scanning network...")
    print(Fore.YELLOW + "Please wait...\n")

    start_time = time.time()

    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether / arp

    result = srp(
        packet,
        timeout=2,
        verbose=False
    )[0]

    devices = []

    for _, received in result:

        ip = received.psrc
        mac = received.hwsrc

        hostname = get_hostname(ip)
        vendor = get_vendor(mac)

        devices.append([
            ip,
            mac,
            vendor,
            hostname
        ])

    end_time = time.time()

    devices.sort(key=lambda x: list(map(int, x[0].split("."))))

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
            tablefmt="grid"
        )
    )

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    csv_file = f"reports/scan_{timestamp}.csv"

    json_file = f"reports/scan_{timestamp}.json"

    save_csv(
        devices,
        csv_file
    )

    save_json(
        devices,
        json_file
    )

    logging.info(f"Devices Found : {len(devices)}")

    logging.info(f"CSV Saved : {csv_file}")

    logging.info(f"JSON Saved : {json_file}")

    logging.info("Scan Completed")

    print()

    print(
        Fore.GREEN +
        f"Devices Found : {len(devices)}"
    )

    print(
        Fore.GREEN +
        f"Time Taken    : {end_time-start_time:.2f} seconds"
    )

    print(
        Fore.BLUE +
        f"CSV Report    : {csv_file}"
    )

    print(
        Fore.BLUE +
        f"JSON Report   : {json_file}"
    )

    print(
        Fore.CYAN +
        "=" * 100
    )
    # -------------------------------------------------------
# Main Function
# -------------------------------------------------------

def main():

    parser = argparse.ArgumentParser(
        description="Python Network Scanner v5.0"
    )

    parser.add_argument(
        "-n",
        "--network",
        help="Target network (Example: 192.168.1.0/24)"
    )

    args = parser.parse_args()

    if args.network:
        network = args.network
    else:
        network = input(
            "Enter network (Example: 192.168.1.0/24): "
        )

    try:

        # Validate network
        ipaddress.ip_network(network, strict=False)

        scan_network(network)

    except ValueError:

        print(
            Fore.RED +
            "\nInvalid network address!"
        )

        logging.error("Invalid network entered.")

    except KeyboardInterrupt:

        print(
            Fore.RED +
            "\nScan cancelled by user."
        )

        logging.warning("Scan cancelled by user.")

    except Exception as e:

        print(
            Fore.RED +
            f"\nUnexpected Error : {e}"
        )

        logging.exception(str(e))


# -------------------------------------------------------
# Program Entry
# -------------------------------------------------------

if __name__ == "__main__":

    main()