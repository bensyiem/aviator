
import pandas as pd
import joblib

MODEL_PATH = "models/model.pkl"
HISTORY_PATH = "data/aviator_history.csv"

def load_model():
    return joblib.load(MODEL_PATH)

def predict_next(model, window=10):
    df = pd.read_csv(HISTORY_PATH)
    if len(df) < window:
        return "Not enough data", 0.0

    recent = df["multiplier"].tail(window).values.reshape(1, -1)
    prediction = model.predict(recent)[0]
    probas = model.predict_proba(recent)[0]
    confidence = max(probas)
    return prediction, confidence
