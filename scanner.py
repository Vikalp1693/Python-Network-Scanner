from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup
from colorama import Fore, init
from tabulate import tabulate
from concurrent.futures import ThreadPoolExecutor, as_completed

import argparse
import csv
import ipaddress
import json
import logging
import os
import socket
import threading
import time
from datetime import datetime

init(autoreset=True)

os.makedirs("reports", exist_ok=True)
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/scanner.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

vendor_lookup = MacLookup()
progress_lock = threading.Lock()
processed = 0

def print_banner():
    print(Fore.CYAN + "=" * 100)
    print(Fore.GREEN + "Python Network Scanner v6.0")
    print(Fore.CYAN + "=" * 100)

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return "Unknown"

def get_vendor(mac):
    try:
        return vendor_lookup.lookup(mac)
    except Exception:
        return "Unknown"

def save_csv(rows, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["IP Address","MAC Address","Vendor","Hostname"])
        w.writerows(rows)

def save_json(rows, filename):
    data=[{"IP Address":r[0],"MAC Address":r[1],"Vendor":r[2],"Hostname":r[3]} for r in rows]
    with open(filename,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=4)

def process_device(received,total):
    global processed
    ip=received.psrc
    mac=received.hwsrc
    host=get_hostname(ip)
    vendor=get_vendor(mac)
    with progress_lock:
        processed+=1
        print(f"\rProcessing {processed}/{total}",end="",flush=True)
    return [ip,mac,vendor,host]

def scan_network(network,threads):
    global processed
    processed=0
    print_banner()
    start=time.time()
    packet=Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=network)
    answered=srp(packet,timeout=2,verbose=False)[0]
    devices=[]
    with ThreadPoolExecutor(max_workers=threads) as ex:
        futures=[ex.submit(process_device,r,len(answered)) for _,r in answered]
        for f in as_completed(futures):
            devices.append(f.result())
    print()
    devices.sort(key=lambda x:list(map(int,x[0].split("."))))
    print(tabulate(devices,headers=["IP Address","MAC Address","Vendor","Hostname"],tablefmt="grid"))
    ts=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    csvf=f"reports/scan_{ts}.csv"
    jsonf=f"reports/scan_{ts}.json"
    save_csv(devices,csvf)
    save_json(devices,jsonf)
    elapsed=time.time()-start
    print(f"\nDevices: {len(devices)}")
    print(f"Time: {elapsed:.2f}s")
    print(f"Threads: {threads}")
    print(f"CSV: {csvf}")
    print(f"JSON: {jsonf}")

def main():
    p=argparse.ArgumentParser(description="Python Network Scanner v6.0")
    p.add_argument("-n","--network")
    p.add_argument("-t","--threads",type=int,default=10)
    a=p.parse_args()
    network=a.network or input("Enter network (Example: 192.168.1.0/24): ")
    ipaddress.ip_network(network,strict=False)
    scan_network(network,a.threads)

if __name__=="__main__":
    main()
