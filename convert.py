import pandas as pd
import os

input_folder = "data/raw"
output_folder = "data/processed"

for file in os.listdir(input_folder):
    if file.endswith(".parquet"):
        df = pd.read_parquet(os.path.join(input_folder, file))
        out_name = file.replace(".parquet", ".csv")
        df.to_csv(os.path.join(output_folder, out_name), index=False)
        print(f"Converted: {file} → {out_name}")
