import os

def check_file(path):
    alerts = []

    if not os.path.exists(path):
        return ["File not found"]

    if "/tmp" in path:
        alerts.append("Suspicious location")

    if path.endswith(".sh"):
        alerts.append("Script file detected")

    return alerts
