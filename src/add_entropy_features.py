import pandas as pd
from entropy_utils import calculate_entropy

df = pd.read_csv("data/final_cleaned_data.csv")

# 1. Packet length entropy
df["packet_length_entropy"] = calculate_entropy(df["Packet Length Mean"])

# 2. IAT entropy
df["iat_entropy"] = calculate_entropy(df["Flow IAT Mean"])

# 3. Flag entropy (SYN, ACK, RST, FIN, PSH)
flag_cols = ["FIN Flag Count", "SYN Flag Count", "RST Flag Count",
             "PSH Flag Count", "ACK Flag Count", "URG Flag Count"]

df["flag_entropy"] = calculate_entropy(df[flag_cols].sum(axis=1))

df.to_csv("data/final_entropy_data.csv", index=False)

print("Entropy features added successfully!")
print("New shape:", df.shape)
