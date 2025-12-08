import pandas as pd

df = pd.read_csv("data/all_data_combined.csv")

def map_label(label):

    # 1. Normal Traffic
    if label == "Benign":
        return "Benign"

    # 2. SYN Flood
    if label == "Syn":
        return "SYN"

    # 3. UDP Flood Variants
    if label in ["UDP", "UDP-lag", "UDPLag"]:
        return "UDP"

    # 4. Web DDoS
    if label == "WebDDoS":
        return "WebDDoS"

    # 5. Everything Else = DrDoS / Amplification
    return "DrDoS"

df["attack_category"] = df["Label"].apply(map_label)

print(df["attack_category"].value_counts())

df.to_csv("data/all_data_multiclass.csv", index=False)

print("\nSaved as all_data_multiclass.csv")
