# 🌐 Python Network Scanner

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Scapy](https://img.shields.io/badge/Scapy-Networking-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

A professional Python-based network scanner that discovers devices on a local network using ARP requests, resolves hostnames, identifies MAC vendors using the official IEEE OUI database, and exports scan results in CSV and JSON formats.

Designed for learning networking fundamentals, cybersecurity, and Python development.

---

## ✨ Features

- Discover active devices on a local network
- Retrieve IP Address
- Retrieve MAC Address
- Resolve Hostname
- Offline IEEE MAC Vendor Lookup
- CSV Report Generation
- JSON Report Generation
- Colorful Terminal Output
- Progress Bar
- Multi-threaded Device Processing
- Logging Support
- Cross Platform (Windows & Linux)

---

## 📂 Project Structure

```text
Python-Network-Scanner/
│
├── scanner.py
├── scanner_core.py
├── vendor_lookup.py
├── report.py
├── logger.py
├── progress.py
├── banner.py
├── config.py
├── utils.py
│
├── data/
│   └── oui.csv
│
├── reports/
├── logs/
├── screenshots/
│
├── requirements.txt
├── LICENSE
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Python-Network-Scanner.git

cd Python-Network-Scanner
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Interactive Mode

```bash
python scanner.py
```

Command Line

```bash
python scanner.py -n 192.168.1.0/24
```

Custom Threads

```bash
python scanner.py -n 192.168.1.0/24 -t 20
```

---

## 📊 Example Output

```
+---------------+-------------------+---------------------------+------------+
| IP Address    | MAC Address       | Vendor                    | Hostname   |
+---------------+-------------------+---------------------------+------------+
| 192.168.1.1   | 98:9D:B2:56:83:E9 | Cisco Systems             | Router     |
| 192.168.1.15  | 80:D2:1D:EF:11:DD | AzureWave Technology Inc. | Desktop    |
| 192.168.1.23  | 38:E2:CA:11:22:33 | Katun Corporation         | Laptop     |
+---------------+-------------------+---------------------------+------------+
```

---

## 📄 Reports

The scanner automatically generates:

```
reports/

scan_YYYY-MM-DD_HH-MM-SS.csv

scan_YYYY-MM-DD_HH-MM-SS.json
```

---

## 📜 Log Files

Logs are stored inside:

```
logs/
```

Each execution generates a timestamped log file.

---

## 🛠 Technologies Used

- Python
- Scapy
- Colorama
- Tabulate
- ThreadPoolExecutor
- IEEE OUI Database

---

## 📸 Screenshots

Place screenshots inside:

```
screenshots/
```

Example:

```
screenshots/
├── banner.png
├── scanning.png
├── output.png
├── csv_report.png
```

Then include them like:

```markdown
## Application

![Banner](screenshots/banner.png)

![Scan](screenshots/scanning.png)

![Output](screenshots/output.png)
```

---

## 🚀 Future Improvements

- Port Scanner
- OS Detection
- Ping Sweep
- Service Detection
- HTML Reports
- Excel Export
- GUI Version
- Interface Selection
- IPv6 Support

---

## 👨‍💻 Author

**Vikalp Pandey**

MCA Graduate

Cybersecurity Enthusiast

Python Developer

Networking Learner

GitHub:
https://github.com/YOUR_USERNAME

LinkedIn:
https://linkedin.com/in/YOUR_PROFILE

---

## ⭐ If you found this project useful, consider giving it a star.