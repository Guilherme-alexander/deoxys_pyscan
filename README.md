# ☄️ Deoxys PyScan (deoxys_pyscan)

> Adaptive Python Security Scanner for Supply-Chain Analysis, Vulnerability Detection and Malware Heuristics.

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux-lightgrey)
![Status](https://img.shields.io/badge/status-active-success)
![Security](https://img.shields.io/badge/focus-security-red)

---

# ✨ Features

- 🔍 Python environment analysis
- 🧬 Dependency tree mapping
- ☣️ Vulnerability auditing using `pip-audit`
- ⚠️ Detection of compromised package versions
- ☠️ Suspicious package detection
- 🕵️ Filesystem malware heuristics
- 📁 Threat report generation
- 📦 Package update manager
- 🎨 Native ANSI colored terminal UI
- ⚡ Smooth terminal animations
- 🖥️ Windows + Linux support
- 🧠 Modular signature-based detection engine

---

# 🧬 Threat Intelligence Engine

Deoxys PyScan uses signature databases located in:

```text
signatures/
├── malicious.txt
├── compromised.txt
└── malwares.txt
````

---

## ☠️ malicious.txt

Detects:

* malicious libraries
* trojans
* stealers
* miners
* suspicious packages

Example:

```txt
cipher
evil-package
token-grabber
```

---

## ⚠️ compromised.txt

Detects vulnerable versions.

Example:

```txt
aiohttp==3.9.5
requests==2.31.0
urllib3==2.2.1
```

---

## 🦠 malwares.txt

Searches the filesystem for suspicious files.

Example:

```txt
xmrig.exe
stealer.py
miner.exe
rat.exe
```

---

# 📁 Project Structure

```text
deoxys_pyscan/
│
├── scanner.py
├── main.py
├── requirements.txt
├── README.md
│
├── reports/
├── quarantine/
│
└── signatures/
    ├── malicious.txt
    ├── compromised.txt
    └── malwares.txt
```

---

# ⚙️ Installation

## Linux

```bash
git clone https://github.com/Guilherme-alexander/deoxys_pyscan.git

cd deoxys_pyscan

python3 -m pip install -r requirements.txt
```

---

## Windows

```bash
git clone https://github.com/Guilherme-alexander/deoxys_pyscan.git

cd deoxys_pyscan

python -m pip install -r requirements.txt
```

---

# 🚀 Usage

```bash
python main.py
```

---

# 🖥️ Menu

```text
═══════════════════════════════════════════

[1] Dependency Tree
[2] Vulnerability Audit
[3] Update Libraries
[4] Search Package
[5] Full Environment Scan
[6] Malware Heuristics
[7] Generate Report
[8] Exit / Ctrl+C

═══════════════════════════════════════════
```

---

# 🔍 Features Explained

---

## [1] Dependency Tree

Runs:

```bash
python -m pipdeptree
```

Shows:

* dependency chains
* nested packages
* hidden libraries
* package relationships

Useful for:

* supply-chain analysis
* dependency auditing
* hidden dependency detection

---

## [2] Vulnerability Audit

Runs:

```bash
python -m pip_audit
```

Detects:

* CVEs
* vulnerable versions
* known security flaws
* outdated packages

Based on:

* PyPI advisory database
* OSV
* Python security advisories

---

## [3] Update Libraries

Checks:

```bash
python -m pip list --outdated
```

Then allows:

* updating all packages
* patching vulnerable libraries
* security hardening

---

## [4] Search Package

Searches installed packages and shows:

* version
* metadata
* author
* location
* dependencies

Useful for:

* malware investigation
* suspicious package analysis
* package validation

---

## [5] Full Environment Scan

Runs:

* dependency tree
* vulnerability audit
* malware heuristics
* report generation

Complete security inspection of the Python environment.

---

## [6] Malware Heuristics

Performs:

* malicious package detection
* compromised version detection
* filesystem IOC scanning

Scans:

* home directories
* temp folders
* ProgramData
* Linux temp paths

Detects:

* suspicious filenames
* miners
* stealers
* RATs
* trojans

---

## [7] Generate Report

Creates reports inside:

```text
reports/
```

Generated files:

```text
audit_report.txt
search_report.txt
deoxys.log
```

---

# 📄 Reports

Example:

```text
[PACKAGE] requests==2.31.0 | COMPROMISED VERSION

[FILE] xmrig.exe | C:\Users\user\AppData\Temp\xmrig.exe
```

---

# 🎨 Terminal UI

Deoxys PyScan uses:

* native ANSI escape sequences
* no external color libraries
* smooth terminal animations
* cross-platform terminal support

---

# 🛡️ Security Goals

This project focuses on:

* Python supply-chain security
* dependency auditing
* IOC hunting
* malware heuristics
* environment hardening
* vulnerability management

---

# 🚀 Future Features

Planned:

* SHA256 signature scanning
* YARA integration
* automatic quarantine
* live CVE feeds
* VirusTotal integration
* behavior analysis
* process scanning
* real-time filesystem monitoring

---

# ⚠️ Disclaimer

This tool is intended for:

* educational purposes
* defensive security
* environment auditing
* malware analysis labs

Use responsibly.

---

# 📦 Requirements

* Python 3.10+
* pip
* pip-audit
* pipdeptree

---

# 📜 License

MIT License

---

# 👾 Deoxys PyScan

Adaptive Python Security Scanner Framework.
