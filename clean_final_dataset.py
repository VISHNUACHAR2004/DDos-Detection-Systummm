import pandas as pd

df = pd.read_csv("data/all_data_multiclass.csv")

# Remove WebDDoS samples
df = df[df["attack_category"] != "WebDDoS"]

print(df["attack_category"].value_counts())

df.to_csv("data/final_multiclass_data.csv", index=False)

print("\nSaved cleaned dataset as final_multiclass_data.csv")
