from datetime import datetime
import os

def log_alert(level, message):
    os.makedirs("logs", exist_ok=True)

    log = f"[{datetime.now()}] {level}: {message}"

    print(log)

    with open("logs/alerts.log", "a", encoding="utf-8") as f:
        f.write(log + "\n")