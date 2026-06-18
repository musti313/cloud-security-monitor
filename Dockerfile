# Basis-Image: Python auf Linux
FROM python:3.11-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Dateien in den Container kopieren
COPY scripts/ ./scripts/
COPY logs/ ./logs/

# Befehl der beim Start ausgeführt wird
CMD ["python3", "scripts/monitor.py"]
