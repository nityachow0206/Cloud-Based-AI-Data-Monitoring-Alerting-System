import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="AI Monitoring Dashboard", layout="wide")

st.title("🚀 AI Monitoring Dashboard")

🔗 Replace with your actual Replit backend URL
BASE_URL = "https://b2606f98-7f6e-4b20-ba6c-1287b4f49da9-00-3m8pidcxsauq2.riker.replit.dev"

Buttons
col1, col2 = st.columns(2)

with col1:
if st.button("Generate Data"):
res = requests.get(f"{BASE_URL}/generate")
st.success("Data generated")

with col2:
if st.button("Run Monitoring"):
res = requests.get(f"{BASE_URL}/monitor")
st.write(res.json())

Fetch history
st.subheader("📊 Pipeline Metrics")

res = requests.get(f"{BASE_URL}/history")
data = res.json()

if data:
df = pd.DataFrame(data)

# Graphs
st.line_chart(df["latency"], use_container_width=True)
st.line_chart(df["error_rate"], use_container_width=True)
st.line_chart(df["throughput"], use_container_width=True)
# 🚨 Highlight anomalies
st.subheader("🚨 Detected Anomalies")
anomalies = df[
    (df["latency"] > 4) | (df["error_rate"] > 0.15)
]
if not anomalies.empty:
    st.dataframe(anomalies)
else:
    st.success("No anomalies detected yet")

else:
st.warning("No data yet. Click 'Generate Data'")
