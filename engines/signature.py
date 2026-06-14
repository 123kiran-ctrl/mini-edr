import subprocess

def scan_file(path):
    result = subprocess.run(["clamscan", path], capture_output=True, text=True)

    if "FOUND" in result.stdout:
        return "MALICIOUS (Signature)"
    return "CLEAN"
