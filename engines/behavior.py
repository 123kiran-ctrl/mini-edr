import psutil

def check_behavior():
    alerts = []

    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info['name']
            if name and "nc" in name.lower():
                alerts.append("Possible reverse shell tool detected")
        except:
            pass

    return alerts
