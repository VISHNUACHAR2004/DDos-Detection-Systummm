# 🚨 Real-Time DDoS Detection System Using Machine Learning + Entropy Features

## FastAPI Backend | Streamlit SOC Dashboard | Real-Time Traffic Simulation

#### This project implements a production-style Intrusion Detection System (IDS) capable of detecting and classifying DDoS attacks in real time using machine learning and Entropy features.

#### This project implements a production-style Intrusion Detection System (IDS) capable of detecting and classifying DDoS attacks in real time using machine learning.
The system uses:

- Entropy-based features

- Multi-class classification (DrDoS, SYN, UDP, Benign)

- FastAPI model inference server

- Real-time traffic simulator

- Streaming SOC dashboard (Streamlit)

- Auto-blocking & logging engine

This is not a basic notebook project — it is a full end-to-end security pipeline inspired by enterprise IDS systems.

## 🧠 Key Features

### ✅ 1. Machine Learning DDoS Classifier (4 Classes)

Trained on 431,000+ network flows with:

Cleaned CICDDoS2019 dataset

52 base features + 3 entropy features:

- Packet length entropy

- IAT entropy

- TCP flag entropy

Achieved 97% overall accuracy.

Classes detected:

- DrDoS (Reflection Attacks)

- SYN Flood

- UDP Flood

- Benign Traffic

### ✅ 2. FastAPI Backend (Real-Time Classification)

The ML model is deployed using FastAPI:

Accepts JSON flow records

Scales input with saved StandardScaler

Decodes predictions with LabelEncoder

Returns predicted attack type instantly
Endpoint example:
```bash
POST /predict
{
  "Flow Duration": 12345,
  "Total Fwd Packets": 10,
  ...
}
```

### ✅ 3. Real-Time Traffic Simulator

Simulates live network traffic by streaming random flows to the API.

Sends flows one-by-one

Receives predictions in real time

Generates alerts

Writes logs used by the dashboard

### ✅ 4. SOC Dashboard (Streamlit)

A professional Security Operations Center UI, featuring:

- Live attack counts

- Pie chart of attack distribution

- Recent alerts table

- Blocklist table

- Auto-refresh (1 sec)

Serves as the main visualization layer for analysts.

### ✅ 5. Auto-Blocking & Logging Engine

Simulates a firewall/IPS system:

- Logs every flow to traffic_log.txt

- Logs alerts to alert_log.txt

- Blocks malicious flows after repeated detection

- Stores block events in blocklist.txt

## 🗂️ Project Structure

```bash
DDoS-detection-system/
│
├── api/
│   ├── main.py              # FastAPI model server
│   ├── ddos_model.pkl
│   ├── scaler.pkl
│   ├── label_encoder.pkl
│
├── simulation/
│   ├── simulate_realtime.py # Real-time traffic generator
│
├── dashboard/
│   ├── dashboard.py         # Streamlit SOC dashboard
│
├── src/
│   ├── preprocess_for_ml.py
│   ├── train_model.py
│   ├── clean_columns.py
│   ├── entropy_utils.py
│   ├── add_entropy_features.py
│
├── data/
│   ├── final_entropy_data.csv
│   ├── X_train.npy, y_train.npy
│   ├── X_test.npy, y_test.npy
│
├── logs/
│   ├── traffic_log.txt
│   ├── alert_log.txt
│   ├── blocklist.txt
│
└── README.md
```

## ⚙️ How to Run the Project

#### 1️⃣ Start the FastAPI Server:
```bash
uvicorn api.main:app --reload
```
Visit:

 http://127.0.0.1:8000

 http://127.0.0.1:8000/docs
 (Interactive Swagger UI)

#### 2️⃣ Start the Traffic Simulation
```bash
python simulation/simulate_realtime.py
```
#### 3️⃣ Open the Live SOC Dashboard
```bash
streamlit run dashboard/dashboard.py
```
Dashboard Components:

- 📊 Attack distribution pie chart

- 📈 Live attack frequency

- ⚠️ Alerts table

- 🔴 Blocklist

## System Architecture

```bash
        ┌──────────────┐
        │  Simulation   │
        │  Engine       │
        └───────┬──────┘
                │ (Flow JSON)
                ▼
        ┌─────────────────┐
        │   FastAPI ML    │
        │   Inference     │
        └───────┬─────────┘
                │ Prediction
                ▼
        ┌─────────────────┐
        │  Alert Engine   │
        │ + Auto-Block    │
        └───────┬─────────┘
                │ Logs
                ▼
        ┌─────────────────┐
        │ Streamlit SOC   │
        │ Dashboard       │
        └─────────────────┘
```

## Future Improvements

- Integrate Kafka for high-volume traffic

- Deploy using Docker + Kubernetes

- Extend to more attack types