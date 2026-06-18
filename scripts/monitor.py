# Cloud Security Monitor
# Erkennt verdächtige Login-Versuche in Log-Dateien

from collections import defaultdict
from datetime import datetime
import os

LOG_FILE = "logs/auth.log"
REPORT_FILE = "logs/report.txt"
THRESHOLD = 3

def analyze_logs():
    failed_attempts = defaultdict(int)
    successful_logins = []

    with open(LOG_FILE, "r") as f:
        for line in f:
            if "Failed password" in line:
                ip = line.split("from")[1].split("port")[0].strip()
                failed_attempts[ip] += 1
            elif "Accepted password" in line:
                ip = line.split("from")[1].split("port")[0].strip()
                successful_logins.append(ip)

    # Report erstellen
    report = []
    report.append("=== Cloud Security Monitor Report ===")
    report.append(f"Erstellt am: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")
    report.append("--- Verdächtige IPs ---")

    for ip, count in failed_attempts.items():
        if count >= THRESHOLD:
            report.append(f"🚨 ALERT: {ip} hatte {count} fehlgeschlagene Logins!")
        else:
            report.append(f"✅ OK: {ip} hatte {count} fehlgeschlagenen Login")

    report.append("")
    report.append("--- Erfolgreiche Logins ---")
    for ip in successful_logins:
        report.append(f"✅ Erfolgreicher Login von: {ip}")

    # Ausgabe im Terminal
    for line in report:
        print(line)

    # Report als Datei speichern
    with open(REPORT_FILE, "w") as f:
        f.write("\n".join(report))

    print(f"\n📄 Report gespeichert unter: {REPORT_FILE}")

analyze_logs()
