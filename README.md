# 🔍 Python Network Scanner Professional v6.0

A professional multithreaded network scanner built with Python and Scapy.

The scanner discovers active devices on a local network using ARP requests and provides detailed information such as IP address, MAC address, hostname, and device vendor. It also generates CSV and JSON reports for later analysis.

---

## 🚀 Features

- ARP Network Discovery
- Multithreaded Device Processing
- Hostname Resolution
- MAC Vendor Identification
- CSV Report Generation
- JSON Report Generation
- Timestamped Reports
- Professional Logging
- Thread-safe Progress Bar
- Configurable Worker Threads
- Colored Terminal Output
- Automatic Device Sorting

---

## 🛠 Technologies Used

- Python 3.x
- Scapy
- Colorama
- Tabulate
- mac-vendor-lookup

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Vikalp1693/Python-Network-Scanner.git
```

Move into the project directory:

```bash
cd Python-Network-Scanner
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

Windows:

```powershell
.\venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶ Usage

Interactive mode:

```bash
python scanner.py
```

Specify a network:

```bash
python scanner.py -n 192.168.1.0/24
```

Specify worker threads:

```bash
python scanner.py -n 192.168.1.0/24 -t 20
```

---

## 📊 Example Output

```
====================================================================================================
Python Network Scanner Professional
====================================================================================================

Target Network : 192.168.1.0/24

+---------------+-------------------+-------------+------------+
| IP Address    | MAC Address       | Vendor      | Hostname   |
+---------------+-------------------+-------------+------------+

Devices Found : 8

Time Taken : 2.41 sec
```

---

## 📁 Project Structure

```
Python-Network-Scanner/
│
├── scanner.py
├── scanner_core.py
├── utils.py
├── report.py
├── progress.py
├── banner.py
├── logger.py
├── config.py
│
├── reports/
├── logs/
├── screenshots/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📸 Screenshots

Create a folder named **screenshots** and add images such as:

- Banner
- Progress Bar
- Device Table
- CSV Report
- JSON Report

Example:

```
screenshots/
├── banner.png
├── progress.png
├── results.png
└── reports.png
```

---

## 🗺 Roadmap

### ✅ Version 1
- ARP Scanner

### ✅ Version 2
- Hostname Resolution

### ✅ Version 3
- Vendor Lookup

### ✅ Version 4
- CSV Export

### ✅ Version 5
- JSON Reports & Logging

### ✅ Version 6
- Multithreading
- Modular Project Structure
- Progress Bar

### 🔜 Version 7
- Gateway Detection
- Network Statistics
- Device History

### 🔜 Version 8
- Security Audit

### 🔜 Version 9
- GUI Application

### 🔜 Version 10
- Professional Edition

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Vikalp Pandey**

GitHub: https://github.com/Vikalp1693