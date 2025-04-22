
import streamlit as st
import pandas as pd
import time
from predictor import load_model, predict_next
from scraper import fetch_and_store

st.set_page_config(page_title="Aviator Predictor", layout="centered")

st.title("🎯 Aviator Multiplier Predictor")
st.markdown("Real-time data + AI model to forecast upcoming rounds")

# Display current data
placeholder = st.empty()

# Load model
model = load_model()

while True:
    fetch_and_store()
    prediction, confidence = predict_next(model)

    df = pd.read_csv("data/aviator_history.csv")
    last_rounds = df.tail(10)

    with placeholder.container():
        st.subheader("🔢 Last 10 Multipliers")
        st.dataframe(last_rounds[::-1], use_container_width=True)

        st.subheader("📈 Prediction")
        st.markdown(f"**Predicted Range:** `{prediction}`")
        st.markdown(f"**Confidence:** `{confidence:.2%}`")

    time.sleep(5)
