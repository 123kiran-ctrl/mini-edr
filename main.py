from engines.signature import scan_file
from engines.heuristic import check_file
from engines.behavior import check_behavior
from engines.network import check_network
from utils.logger import log_alert

print("\n=== MINI EDR SYSTEM STARTED ===\n")

file_path = input("Enter file path to scan: ")

# 1. Signature
sig = scan_file(file_path)
print("[Signature]", sig)
log_alert(f"Signature scan: {sig}")

# 2. Heuristic
heur = check_file(file_path)
print("[Heuristic]", heur)
log_alert(f"Heuristic scan: {heur}")

# 3. Behavior
beh = check_behavior()
print("[Behavior]", beh)
log_alert(f"Behavior scan: {beh}")

# 4. Network
net = check_network()
print("[Network]", net)
log_alert(f"Network scan: {net}")

print("\nSCAN COMPLETE - LOG SAVED")
