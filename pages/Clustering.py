import streamlit as st
import numpy as np
import joblib

# -----------------------------
# Load Model and Scaler
# -----------------------------
kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

# -----------------------------
# Page Title
# -----------------------------
st.title("📊 Customer Segmentation")

st.write("Enter the customer's RFM values to predict the customer segment.")

# -----------------------------
# User Inputs
# -----------------------------
recency = st.number_input(
    "Recency (days since last purchase)",
    min_value=0,
    value=7
)

frequency = st.number_input(
    "Frequency (number of purchases)",
    min_value=0,
    value=1
)

monetary = st.number_input(
    "Monetary (total spend)",
    min_value=0.0,
    value=100.0
)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Segment"):

    # Prepare input
    customer = np.array([[recency, frequency, monetary]])

    # Scale input
    customer_scaled = scaler.transform(customer)

    # Predict cluster
    cluster = int(kmeans.predict(customer_scaled)[0])

    # Display predicted cluster
    st.success(f"Predicted Cluster: {cluster}")

    # Cluster labels
    cluster_labels = {
        0: "🟢 Regular Customer",
        1: "🟠 At-Risk Customer",
        2: "⭐ High-Value Customer",
        3: "🔵 Loyal Customer",
        4: "🟣 Premium Customer",
        5: "🟡 Potential Customer",
        6: "🟤 Occasional Customer",
        7: "🔴 Lost Customer",
        8: "🟢 Active Customer",
        9: "🔵 New Customer"
    }

    label = cluster_labels.get(cluster, "Unknown Customer Segment")

    st.info(f"Customer Segment: {label}")