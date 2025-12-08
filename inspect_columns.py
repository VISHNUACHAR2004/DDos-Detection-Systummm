import pandas as pd

df = pd.read_csv("data/final_multiclass_data.csv")

print("Columns:\n")
for col in df.columns:
    print(col)
