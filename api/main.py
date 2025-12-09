from fastapi import FastAPI
import numpy as np
import joblib

app = FastAPI()

# Load model components
model = joblib.load("api/ddos_model.pkl")
scaler = joblib.load("api/scaler.pkl")
label_encoder = joblib.load("api/label_encoder.pkl")

@app.get("/")
def home():
    return {"message": "DDoS Detection API is running!"}

@app.post("/predict")
def predict(features: dict):
    """
    Features should be sent as JSON:
    {
       "Protocol": 6,
       "Flow Duration": 12345,
       ...
    }
    """
    # Convert to correct input format
    data = np.array(list(features.values())).reshape(1, -1)
    
    # Scale features
    scaled_data = scaler.transform(data)
    
    # Predict
    pred = model.predict(scaled_data)[0]
    
    # Decode label
    attack_type = label_encoder.inverse_transform([pred])[0]

    return {
        "prediction": int(pred),
        "attack_type": attack_type
    }
