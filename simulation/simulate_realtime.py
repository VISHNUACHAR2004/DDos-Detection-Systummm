import pandas as pd
import requests
import time

# Load some test flows
df = pd.read_csv("data/final_entropy_data.csv")

# Select 100 random flows to simulate live traffic
sample_flows = df.sample(100)

API_URL = "http://127.0.0.1:8000/predict"

for idx, row in sample_flows.iterrows():
    flow_data = row.drop("attack_category").to_dict()
    
    response = requests.post(API_URL, json=flow_data)
    result = response.json()
    
    print(f"\nFlow #{idx}")
    print("Predicted:", result["attack_type"])
    
    # simulate real-time traffic delay
    time.sleep(0.2)
