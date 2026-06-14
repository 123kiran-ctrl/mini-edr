MINI EDR / ANTIVIRUS PROJECT (KALI LINUX)
====================================================

1. PROJECT OVERVIEW
----------------------------------------------------
This project is a simple Mini EDR (Endpoint Detection and Response) system built using Python on Kali Linux.

It is designed to simulate how real antivirus systems work by combining multiple detection techniques such as signature scanning, heuristic rules, behavior monitoring, and network inspection.

The main purpose of this project is learning and understanding cybersecurity concepts in a practical way.

---

2. PURPOSE OF THE PROJECT
----------------------------------------------------
This project was created to understand:

- How antivirus systems detect malware
- How EDR systems monitor system activity
- How suspicious behavior is identified in real time
- Basic cybersecurity monitoring techniques

---

3. FEATURES OF THE SYSTEM
----------------------------------------------------

3.1 Signature-Based Detection
- Uses ClamAV antivirus engine
- Detects known malware using virus signatures

3.2 Heuristic Detection
- Uses rule-based logic
- Detects suspicious file behavior or patterns

3.3 Behavioral Monitoring
- Monitors running processes
- Detects unusual system activity

3.4 Network Monitoring
- Checks active connections
- Detects suspicious ports and services

3.5 Logging System
- Stores all alerts in log files
- Helps in tracking and analysis

---

4. PROJECT STRUCTURE
----------------------------------------------------
mini_edr/
│
├── main.py
├── engines/
│   ├── signature.py
│   ├── heuristic.py
│   ├── behavior.py
│   ├── network.py
│
├── utils/
│   └── logger.py
│
├── logs/
│   └── alerts.log

---

5. INSTALLATION REQUIREMENTS
----------------------------------------------------

Run the following commands before using the project:

sudo apt update
sudo apt install clamav python3-pip -y
pip install psutil

---

6. DATABASE UPDATE (IMPORTANT)
----------------------------------------------------
sudo freshclam

This updates the virus signature database used by ClamAV.

---

7. HOW TO RUN THE PROJECT
----------------------------------------------------
python3 main.py

---

8. SYSTEM WORKING FLOW
----------------------------------------------------
Input (File or System Activity)
        ↓
Signature-Based Scan (ClamAV)
        ↓
Heuristic Rule Check
        ↓
Behavior Monitoring
        ↓
Network Monitoring
        ↓
Logs Generated

---

9. LIMITATIONS
----------------------------------------------------
This project is only for educational purposes and does not provide real-world enterprise-level security protection.

---

10. CONCLUSION
----------------------------------------------------
This project helped in understanding how modern antivirus and EDR systems work internally by combining multiple detection techniques into one system.

---

11. AUTHOR
    Kiran Dangal (Hack_oppy)
----------------------------------------------------
Cybersecurity Learning Project (Built on Kali Linux)
