import streamlit as st
import pandas as pd
import plotly.express as px
import time
from predictor import load_model, predict_next
from scraper import fetch_and_store
from utils import play_sound, track_stats

st.set_page_config(page_title="Aviator Predictor", layout="centered")

st.title("🎯 Aviator Multiplier Predictor")
st.markdown("Real-time data + AI model to forecast upcoming rounds")

# Load model
model = load_model()

# Display area
placeholder = st.empty()
stats_placeholder = st.sidebar.empty()

# Track stats
rounds_predicted = 0
safe_signals = 0

while True:
    fetch_and_store()
    prediction, confidence = predict_next(model)

    if prediction in [">2x", ">10x"] and confidence >= 0.85:
        play_sound()
        safe_signals += 1

    rounds_predicted += 1

    # Load and display history
    df = pd.read_csv("data/aviator_history.csv")
    recent = df.tail(30)

    with placeholder.container():
        st.subheader("🔢 Last 10 Multipliers")
        st.dataframe(df.tail(10)[::-1], use_container_width=True)

        st.subheader("📊 Multiplier Trend")
        fig = px.line(recent, y="multiplier", title="Last 30 Rounds", markers=True)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("📈 Prediction")
        st.markdown(f"**Predicted Range:** `{prediction}`")
        st.markdown(f"**Confidence:** `{confidence:.2%}`")

    # Show stats
    stats_placeholder.markdown(track_stats(rounds_predicted, safe_signals))

    time.sleep(5)
