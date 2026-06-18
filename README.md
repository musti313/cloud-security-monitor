# Cloud Security Monitor

## Was ist das?
Ein Python-basiertes Tool das eine Cloud-Umgebung überwacht 
und verdächtige Login-Versuche automatisch erkennt und meldet.

## Das Problem
Ohne Überwachung können sich unerwünschte Nutzer unbemerkt 
in Cloud-Systeme einloggen und Schaden anrichten. 
Brute-Force Angriffe – bei denen automatisch viele Passwörter 
ausprobiert werden – sind eine der häufigsten Angriffsmethoden.

## Wie funktioniert es?
Das Tool analysiert Server-Logdateien und zählt fehlgeschlagene 
Login-Versuche pro IP-Adresse. Überschreitet eine IP den 
festgelegten Schwellenwert, wird automatisch ein Alert ausgegeben.

## Benutzung
1. Repository klonen
2. Logdatei unter `logs/auth.log` platzieren
3. Monitor starten:
   python3 scripts/monitor.py

## Technologien
- Python 3
- Linux/WSL
- Git & GitHub

## Autor
Erstellt als praktisches IT-Security Projekt# cloud-security-monitor
A Python based tool to monitor server logs and detect suspicious activity
