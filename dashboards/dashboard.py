import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="DDoS Detection Dashboard",
    layout="wide"
)

st.markdown("""
<style>
<style>

/* TOP MOST WRAPPER */
.stAppViewContainer {
    background-color: #000000 !important;
}

/* MAIN APP BACKGROUND */
.stApp {
    background-color: #000000 !important;
}
            /* --- Make all text neon green --- */
*, h1, h2, h3, h4, p, label, div {
    color: #00ff9f !important;
}

/* HEADER / TOOLBAR (RUN, STOP, DEPLOY) */
.st-emotion-cache-12fmjuu, header, .st-emotion-cache-18ni7ap {
    background-color: #000000 !important;
    color: #00ff9f !important;
}


/* Increase default font sizes */
html, body, [class*="css"]  {
    font-size: 65px !important;
}

/* Make table text bigger */
.dataframe tbody tr td {
    font-size: 88px !important;
}
.dataframe thead tr th {
    font-size: 50px !important;
    font-weight: bold !important;
}

/* Improve section headers */
h1, h2, h3, h4 {
    font-size: 120px !important;
    font-weight: 900 !important;
}

/* Center titles */
h1 {
    text-align: center;
}

/* Clean pie chart padding */
.block-container {
    padding-top: 1rem;
}
fig, ax = plt.subplots(figsize=(2, 2))  # smaller pie chart
traffic_df["Prediction"].value_counts().plot.pie(
    autopct="%1.1f%%",
    ax=ax
)


/* Bold labels inside app */
label, .stText {
    font-size: 20px !important;
}

</style>
""", unsafe_allow_html=True)

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
            counts = traffic_df["Prediction"].value_counts()

            fig, ax = plt.subplots(figsize=(1, 1))  # small pie chart

            # Draw pie using Pandas for category labels
            pie = counts.plot.pie(
                autopct="%1.1f%%",
                ax=ax,
                textprops={'fontsize': 3}  # reduce percentage + label size
            )

            # Reduce default label size further
            for label in ax.texts:
                label.set_fontsize(3)

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
