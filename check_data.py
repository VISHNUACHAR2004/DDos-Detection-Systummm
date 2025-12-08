import pandas as pd
# import os
# df = pd.read_csv("data/processed/Syn-training.csv")

# print(df.head())
# print(df.shape)
# print(df.columns)


df = pd.read_csv("data/processed/UDP-training.csv")  # or any other file
print(df.head())
print(df.shape)
print(df["Label"].unique())
