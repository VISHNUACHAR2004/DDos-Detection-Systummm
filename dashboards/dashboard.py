import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="DDoS Detection Dashboard",
    layout="wide"
)

st.title("🚨 Real-Time DDoS Attack Monitoring Dashboard")

# File paths (adjust if needed)
TRAFFIC_LOG = "logs/traffic_log.txt"
ALERT_LOG = "logs/alert_log.txt"
BLOCK_LOG = "logs/blocklist.txt"

# Function to read log files safely
def read_log(file_path):
    try:
        return pd.read_csv(file_path, names=["Time", "Flow", "Prediction"])
    except:
        return pd.DataFrame(columns=["Time", "Flow", "Prediction"])

# Real-time loop
placeholder = st.empty()

while True:
    with placeholder.container():

        # Load logs
        traffic_df = read_log(TRAFFIC_LOG)
        alert_df = read_log(ALERT_LOG)
        block_df = read_log(BLOCK_LOG)

        st.subheader("📊 Live Traffic Summary")

        # Attack counts
        if len(traffic_df) > 0:
            counts = traffic_df["Prediction"].value_counts()
            st.write(counts)
        else:
            st.write("No traffic data yet...")

        # Pie Chart
        st.subheader("📌 Attack Distribution")
        if len(traffic_df) > 0:
            fig, ax = plt.subplots()
            traffic_df["Prediction"].value_counts().plot.pie(
                autopct="%1.1f%%",
                figsize=(4, 4),
                ax=ax
            )
            st.pyplot(fig)
        else:
            st.write("Waiting for data...")

        # Alert Log Table
        st.subheader("⚠️ Live Alerts")
        if len(alert_df) > 0:
            st.dataframe(alert_df.tail(10))
        else:
            st.write("No alerts yet.")

        # Blocklist Section
        st.subheader("🔴 Blocked Flows")
        if len(block_df) > 0:
            st.dataframe(block_df.tail(10))
        else:
            st.write("No blocks yet.")

        # Auto-refresh every 1 second
        time.sleep(1)
