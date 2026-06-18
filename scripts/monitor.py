# Cloud Security Monitor
# Erkennt verdächtige Login-Versuche in Log-Dateien

from collections import defaultdict

LOG_FILE = "logs/auth.log"
THRESHOLD = 3  # Ab wie vielen Fehlversuchen Alarm

def analyze_logs():
    failed_attempts = defaultdict(int)

    with open(LOG_FILE, "r") as f:
        for line in f:
            if "Failed password" in line:
                ip = line.split("from")[1].split("port")[0].strip()
                failed_attempts[ip] += 1

    print("=== Security Monitor Report ===\n")
    
    for ip, count in failed_attempts.items():
        if count >= THRESHOLD:
            print(f"🚨 ALERT: {ip} hatte {count} fehlgeschlagene Logins!")
        else:
            print(f"✅ OK: {ip} hatte {count} fehlgeschlagenen Login")

analyze_logs()
