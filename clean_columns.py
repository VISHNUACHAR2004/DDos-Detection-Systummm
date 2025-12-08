import pandas as pd

df = pd.read_csv("data/final_multiclass_data.csv")

cols_to_drop = [
    "Label", "source_file",
    "Fwd URG Flags", "Bwd URG Flags", "CWE Flag Count",
    "ECE Flag Count", "Down/Up Ratio",
    "Fwd Avg Bytes/Bulk", "Fwd Avg Packets/Bulk", "Fwd Avg Bulk Rate",
    "Bwd Avg Bytes/Bulk", "Bwd Avg Packets/Bulk", "Bwd Avg Bulk Rate",
    "Avg Packet Size", "Avg Fwd Segment Size", "Avg Bwd Segment Size",
    "Subflow Fwd Packets", "Subflow Fwd Bytes",
    "Subflow Bwd Packets", "Subflow Bwd Bytes",
    "Active Mean", "Active Std", "Active Max", "Active Min",
    "Idle Mean", "Idle Std", "Idle Max", "Idle Min"
]

df = df.drop(columns=cols_to_drop, errors='ignore')

print("Remaining columns:", len(df.columns))
print(df.columns)

df.to_csv("data/final_cleaned_data.csv", index=False)
print("Saved as final_cleaned_data.csv")



#These columns should be removed immediately because they:
# either leak information

# or are constant

# or add no ML value

# or will cause overfitting