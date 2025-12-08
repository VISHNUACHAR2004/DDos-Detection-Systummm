import pandas as pd
import os

data_folder = "data/processed"
dfs = []

for file in os.listdir(data_folder):
    if file.endswith(".csv"):
        path = os.path.join(data_folder, file)
        df = pd.read_csv(path)
        df["source_file"] = file  # optional but useful
        dfs.append(df)
        print("Loaded:", file, df.shape)

final_df = pd.concat(dfs, ignore_index=True)

print("Final dataset shape:", final_df.shape)
print("Unique labels:", final_df["Label"].unique())

final_df.to_csv("data/all_data_combined.csv", index=False)
