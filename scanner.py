#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ════════════════════════════════════════════════════════════════
# DEOXYS PYSCAN
# Adaptive Python Security Scanner
# Windows + Linux
# Auth: https://github.com/Guilherme-alexander
# ════════════════════════════════════════════════════════════════

import os
import sys
import time
import json
import logging
import platform
import subprocess

from pathlib import Path
from datetime import datetime

# ════════════════════════════════════════════════════════════════
# ENABLE ANSI WINDOWS
# ════════════════════════════════════════════════════════════════

if os.name == "nt":
    os.system("")

# ════════════════════════════════════════════════════════════════
# COLORS
# ════════════════════════════════════════════════════════════════

G = "\033[92m"
R = "\033[91m"
Y = "\033[93m"
C = "\033[96m"
B = "\033[1m"
X = "\033[0m"

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_PURPLE = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# ════════════════════════════════════════════════════════════════
# PATHS
# ════════════════════════════════════════════════════════════════

BASE_DIR = Path(__file__).resolve().parent

REPORTS_DIR = BASE_DIR / "reports"
QUARANTINE_DIR = BASE_DIR / "quarantine"
SIGNATURES_DIR = BASE_DIR / "signatures"

REPORTS_DIR.mkdir(exist_ok=True)
QUARANTINE_DIR.mkdir(exist_ok=True)
SIGNATURES_DIR.mkdir(exist_ok=True)

LOG_FILE = REPORTS_DIR / "deoxys.log"
AUDIT_FILE = REPORTS_DIR / "audit_report.txt"
SEARCH_FILE = REPORTS_DIR / "search_report.txt"

# ════════════════════════════════════════════════════════════════
# IGNORE DIRECTORIES
# ════════════════════════════════════════════════════════════════

IGNORE_DIRS = {
    "node_modules",
    ".git",
    "__pycache__",
    "venv",
    ".venv",
    "dist",
    "build",
    "cache",
    ".cache"
}

# ════════════════════════════════════════════════════════════════
# LOGGING
# ════════════════════════════════════════════════════════════════

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ════════════════════════════════════════════════════════════════
# ANIMATION
# ════════════════════════════════════════════════════════════════

def slow(text, d=0.01):

    try:

        for c in text:

            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(d)

        print()

    except KeyboardInterrupt:

        print(f"\n{R}[!] Interrupted{X}")

# ════════════════════════════════════════════════════════════════
# CLEAR
# ════════════════════════════════════════════════════════════════

def clear():

    os.system("cls" if os.name == "nt" else "clear")

# ════════════════════════════════════════════════════════════════
# BANNER
# ════════════════════════════════════════════════════════════════

def banner():

    clear()

    print(f"""{BRIGHT_PURPLE}
██████╗ ███████╗ ██████╗ ██╗  ██╗██╗   ██╗███████╗
██╔══██╗██╔════╝██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝██╔════╝
██║  ██║█████╗  ██║   ██║ ╚███╔╝  ╚████╔╝ ███████╗
██║  ██║██╔══╝  ██║   ██║ ██╔██╗   ╚██╔╝  ╚════██║
██████╔╝███████╗╚██████╔╝██╔╝ ██╗   ██║   ███████║
╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝

██████╗ ██╗   ██╗███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝ ╚████╔╝ ███████╗██║     ███████║██╔██╗ ██║
██╔═══╝   ╚██╔╝  ╚════██║██║     ██╔══██║██║╚██╗██║
██║        ██║   ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝        ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
{RESET}""")

    print(f"{BRIGHT_CYAN}Adaptive Python Security Scanner{RESET}")
    print(f"{DIM}Windows | Linux | Supply-Chain Security{RESET}\n")

# ════════════════════════════════════════════════════════════════
# COMMAND RUNNER
# ════════════════════════════════════════════════════════════════

def run_command(command):

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        return result.stdout + result.stderr

    except Exception as e:

        logging.exception(e)

        return str(e)

# ════════════════════════════════════════════════════════════════
# SAVE FILE
# ════════════════════════════════════════════════════════════════

def save_file(path, data):

    with open(path, "a", encoding="utf-8") as f:

        f.write(data + "\n")

# ════════════════════════════════════════════════════════════════
# LOAD SIGNATURES
# ════════════════════════════════════════════════════════════════

def load_signatures(filename):

    path = SIGNATURES_DIR / filename

    signatures = []

    if not path.exists():

        return signatures

    with open(path, "r", encoding="utf-8") as f:

        for line in f:

            line = line.strip().lower()

            if line and not line.startswith("#"):

                signatures.append(line)

    return signatures

# ════════════════════════════════════════════════════════════════
# GET INSTALLED PACKAGES
# ════════════════════════════════════════════════════════════════

def get_installed_packages():

    output = run_command([
        sys.executable,
        "-m",
        "pip",
        "list",
        "--format=json"
    ])

    installed = []

    try:

        packages = json.loads(output)

        for pkg in packages:

            installed.append((
                pkg["name"].lower(),
                pkg["version"].lower()
            ))

    except Exception as e:

        logging.exception(e)

    return installed

# ════════════════════════════════════════════════════════════════
# DEPENDENCY TREE
# ════════════════════════════════════════════════════════════════

def dependency_tree():

    slow(f"{Y}[*] Running pipdeptree...{X}")

    output = run_command([
        sys.executable,
        "-m",
        "pipdeptree"
    ])

    print(output)

    save_file(
        AUDIT_FILE,
        "\n\n===== DEPENDENCY TREE =====\n" + output
    )

# ════════════════════════════════════════════════════════════════
# PIP AUDIT
# ════════════════════════════════════════════════════════════════

def vulnerability_audit():

    slow(f"{Y}[*] Running pip-audit...{X}")

    output = run_command([
        sys.executable,
        "-m",
        "pip_audit"
    ])

    print(output)

    save_file(
        AUDIT_FILE,
        "\n\n===== PIP AUDIT =====\n" + output
    )

# ════════════════════════════════════════════════════════════════
# UPDATE LIBRARIES
# ════════════════════════════════════════════════════════════════

def update_libraries():

    slow(f"{C}[*] Checking outdated packages...{X}")

    output = run_command([
        sys.executable,
        "-m",
        "pip",
        "list",
        "--outdated",
        "--format=json"
    ])

    try:

        packages = json.loads(output)

    except Exception:

        print(f"{R}[!] Failed to parse package list{X}")
        return

    if not packages:

        print(f"{G}[+] All packages are updated{X}")
        return

    print()

    for pkg in packages:

        print(
            f"{BRIGHT_YELLOW}"
            f"{pkg['name']} "
            f"{pkg['version']} -> "
            f"{pkg['latest_version']}"
            f"{RESET}"
        )

    choice = input(
        f"\n{Y}[?] Update all packages? (y/n): {X}"
    ).lower()

    if choice != "y":
        return

    for pkg in packages:

        name = pkg["name"]

        print(
            f"{BRIGHT_CYAN}Updating {name}...{RESET}"
        )

        run_command([
            sys.executable,
            "-m",
            "pip",
            "install",
            "--upgrade",
            name
        ])

    print(f"{G}[+] Update complete{X}")

# ════════════════════════════════════════════════════════════════
# SEARCH PACKAGE
# ════════════════════════════════════════════════════════════════

def search_package():

    pkg = input(
        f"{BRIGHT_CYAN}[?] Package name:{RESET} "
    ).strip()

    if not pkg:
        return

    slow(f"{Y}[*] Searching package...{X}")

    output = run_command([
        sys.executable,
        "-m",
        "pip",
        "show",
        pkg
    ])

    print(output)

    save_file(
        SEARCH_FILE,
        "\n\n===== PACKAGE SEARCH =====\n" + output
    )

# ════════════════════════════════════════════════════════════════
# GENERATE REPORT
# ════════════════════════════════════════════════════════════════

def generate_report():

    report = f"""
==================================================
DEOXYS PYSCAN REPORT
==================================================

Generated:
{datetime.now()}

Platform:
{platform.platform()}

Python:
{platform.python_version()}

Machine:
{platform.machine()}

Processor:
{platform.processor()}

==================================================
"""

    save_file(AUDIT_FILE, report)

    print(
        f"{G}[+] Report generated:{X} {AUDIT_FILE}"
    )

# ════════════════════════════════════════════════════════════════
# FULL ENVIRONMENT SCAN
# ════════════════════════════════════════════════════════════════

def full_environment_scan():

    slow(f"{BRIGHT_CYAN}[*] Starting full scan...{RESET}")

    dependency_tree()

    vulnerability_audit()

    malware_heuristics()

    generate_report()

    print(
        f"{G}[+] Full environment scan complete{X}"
    )

# ════════════════════════════════════════════════════════════════
# MALWARE HEURISTICS
# ════════════════════════════════════════════════════════════════

def malware_heuristics():

    malicious = set(load_signatures("malicious.txt"))
    compromised = set(load_signatures("compromised.txt"))
    malwares = set(load_signatures("malwares.txt"))

    findings = []

    slow(f"{Y}[*] Checking installed packages...{X}")

    installed = get_installed_packages()

    # ════════════════════════════════════════
    # MALICIOUS PACKAGES
    # ════════════════════════════════════════

    for sig in malicious:

        for pkg, ver in installed:

            if pkg == sig:

                findings.append({
                    "type": "MALICIOUS PACKAGE",
                    "name": pkg,
                    "version": ver
                })

    # ════════════════════════════════════════
    # COMPROMISED PACKAGES / VERSIONS
    # ════════════════════════════════════════

    for sig in compromised:

        if "==" in sig:

            sig_name, sig_ver = sig.split("==", 1)

            for pkg, ver in installed:

                if pkg == sig_name and ver == sig_ver:

                    findings.append({
                        "type": "COMPROMISED VERSION",
                        "name": pkg,
                        "version": ver
                    })

        else:

            for pkg, ver in installed:

                if pkg == sig:

                    findings.append({
                        "type": "COMPROMISED PACKAGE",
                        "name": pkg,
                        "version": ver
                    })

    # ════════════════════════════════════════
    # FILESYSTEM SCAN
    # ════════════════════════════════════════

    slow(f"{C}[*] Scanning filesystem...{X}")

    search_paths = []

    if os.name == "nt":

        search_paths.extend([
            Path.home(),
            Path("C:/Users"),
            Path("C:/ProgramData"),
            Path(os.getenv("TEMP", "C:/Temp"))
        ])

    else:

        search_paths.extend([
            Path.home(),
            Path("/tmp"),
            Path("/var/tmp"),
            Path("/opt")
        ])

    for base in search_paths:

        if not base.exists():
            continue

        try:

            for root, dirs, files in os.walk(base):

                dirs[:] = [
                    d for d in dirs
                    if d not in IGNORE_DIRS
                ]

                for file in files:

                    lower = file.lower()

                    for malware in malwares:

                        if malware in lower:

                            fullpath = Path(root) / file

                            try:

                                size = fullpath.stat().st_size

                            except Exception:

                                size = "Unknown"

                            findings.append({
                                "type": "SUSPICIOUS FILE",
                                "name": file,
                                "path": str(fullpath),
                                "size": size
                            })

        except PermissionError:

            pass

        except Exception as e:

            logging.exception(e)

    # ════════════════════════════════════════
    # RESULTS
    # ════════════════════════════════════════

    if findings:

        print(f"\n{BRIGHT_RED}[!] Threats Detected{RESET}\n")

        report_data = []

        for item in findings:

            if item["type"] == "SUSPICIOUS FILE":

                msg = (
                    f"[FILE] "
                    f"{item['name']} | "
                    f"{item['path']} | "
                    f"Size: {item['size']}"
                )

            else:

                msg = (
                    f"[PACKAGE] "
                    f"{item['name']}=={item['version']} | "
                    f"{item['type']}"
                )

            print(f"{BRIGHT_RED}{msg}{RESET}")

            report_data.append(msg)

        save_file(
            AUDIT_FILE,
            "\n\n===== THREATS =====\n" +
            "\n".join(report_data)
        )

        logging.warning(
            f"Threats detected: {len(findings)}"
        )

    else:

        print(f"{G}[+] No threats detected{X}")

        logging.info("No threats detected")

# ════════════════════════════════════════════════════════════════
# MENU
# ════════════════════════════════════════════════════════════════

def menu():

    print(f"""{BRIGHT_CYAN}═══════════════════════════════════════════{RESET}

[1] Dependency Tree
[2] Vulnerability Audit
[3] Update Libraries
[4] Search Package
[5] Full Environment Scan
[6] Malware Heuristics
[7] Generate Report
[0] Exit / Ctrl+C

{BRIGHT_CYAN}═══════════════════════════════════════════{RESET}""")

# ════════════════════════════════════════════════════════════════
# MAIN LOOP
# ════════════════════════════════════════════════════════════════

def start():

    while True:

        try:

            banner()

            menu()

            choice = input(
                f"{BRIGHT_YELLOW}Choose an option:{RESET} ").strip()

            if choice == "1":

                dependency_tree()

            elif choice == "2":

                vulnerability_audit()

            elif choice == "3":

                update_libraries()

            elif choice == "4":

                search_package()

            elif choice == "5":

                full_environment_scan()

            elif choice == "6":

                malware_heuristics()

            elif choice == "7":

                generate_report()

            elif choice == "0" or choice == "exit":

                print(f"{BRIGHT_RED}Exiting...{RESET}")

                sys.exit()

            else:

                print(
                    f"{R}[!] Invalid option{X}"
                )

            input(
                f"\n{DIM}Press ENTER to continue...{RESET}"
            )

        except KeyboardInterrupt:

            print(
                f"\n{BRIGHT_RED}[!] Interrupted by user{RESET}"
            )

            sys.exit()

        except Exception as e:

            print(
                f"{R}[!] Error: {e}{X}"
            )

            logging.exception(e)
