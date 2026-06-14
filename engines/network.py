import psutil

def check_network():
    alerts = []

    for conn in psutil.net_connections():
        if conn.status == "LISTEN":
            if conn.laddr.port in [4444, 1337, 9001]:
                alerts.append(f"Suspicious port: {conn.laddr.port}")

    return alerts
