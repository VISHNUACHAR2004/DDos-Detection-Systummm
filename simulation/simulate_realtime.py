import pandas as pd
import requests
import time
from termcolor import colored
import colorama
from datetime import datetime

colorama.init()

# Load dataset
df = pd.read_csv("data/final_entropy_data.csv")
sample_flows = df.sample(100)

API_URL = "http://127.0.0.1:8000/predict"

# ---- LOG FILES ----
traffic_log = open("logs/traffic_log.txt", "a")
alert_log = open("logs/alert_log.txt", "a")
block_log = open("logs/blocklist.txt", "a")

# ---- BLOCKING SYSTEM ----
block_counter = {}      # tracks repeated malicious flows
block_threshold = 3     # block after 3 detections
blocked = set()

for idx, row in sample_flows.iterrows():
    
    timestamp = datetime.now().strftime("%H:%M:%S")
    flow_id = idx
    flow_data = row.drop("attack_category").to_dict()

    # Send to backend
    response = requests.post(API_URL, json=flow_data)
    result = response.json()
    attack = result["attack_type"]

    # ---- CONSOLE ALERTS ----
    print(f"\nFlow #{flow_id}")

    if attack == "Benign":
        print(colored(f"[{timestamp}] ✔ NORMAL TRAFFIC", "green"))

    elif attack == "SYN":
        print(colored(f"[{timestamp}] ⚠️  ALERT - SYN Flood Detected", "yellow"))

    elif attack == "UDP":
        print(colored(f"[{timestamp}] ⚠️  ALERT - UDP Flood Detected", "yellow"))

    elif attack == "DrDoS":
        print(colored(f"[{timestamp}] 🚨 CRITICAL - DrDoS Amplification Attack", "red"))

    # ---- WRITE TO LOGS ----
    traffic_log.write(f"{timestamp}, {flow_id}, {attack}\n")

    if attack != "Benign":
        alert_log.write(f"{timestamp}, {flow_id}, {attack}\n")

        # ---- BLOCKING LOGIC ----
        block_counter[flow_id] = block_counter.get(flow_id, 0) + 1
        
        if block_counter[flow_id] >= block_threshold and flow_id not in blocked:
            blocked.add(flow_id)
            block_log.write(f"{timestamp}, BLOCKED, Flow={flow_id}, Reason={attack}\n")
            print(colored(f"[{timestamp}] 🔴 BLOCKED → Flow {flow_id}", "red"))

    # ---- delay to simulate real-time flow ----
    time.sleep(0.2)

# Close logs
traffic_log.close()
alert_log.close()
block_log.close()


sss
sss
sss