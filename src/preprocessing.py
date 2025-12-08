import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import joblib

# Load data
df = pd.read_csv("data/final_entropy_data.csv")

# Separate features and target
X = df.drop("attack_category", axis=1)
y = df["attack_category"]

# Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Save encoder for inference later
joblib.dump(label_encoder, "models/label_encoder.pkl")

# Scale numeric features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Save scaler for inference
joblib.dump(scaler, "models/scaler.pkl")

# Train/test split 
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

# Save processed datasets
import numpy as np

np.save("data/X_train.npy", X_train)
np.save("data/X_test.npy", X_test)
np.save("data/y_train.npy", y_train)
np.save("data/y_test.npy", y_test)

print("Preprocessing completed!")
print("Train shapes:", X_train.shape, y_train.shape)
print("Test shapes:", X_test.shape, y_test.shape)
