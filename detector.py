from collections import defaultdict
from logger import log_alert
import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

ip_counter = defaultdict(int)
ip_ports = defaultdict(set)

def detect(ip, port):
    # игнорируем whitelist
    if ip in config["whitelist"]:
        return

    ip_counter[ip] += 1

    # Flood detection
    if ip_counter[ip] > config["flood_threshold"]:
        alert("WARNING", f"Flood detected from {ip}")

    # Port scan detection
    if port is not None:
        ip_ports[ip].add(port)

        if len(ip_ports[ip]) > config["scan_threshold"]:
            alert("CRITICAL", f"Port Scan detected from {ip}")

def alert(level, message):
    log_alert(level, message)