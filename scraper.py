
import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")
API_HOST = os.getenv("RAPIDAPI_HOST")
URL = "https://bet7k-aviator-api.p.rapidapi.com/bet7k-aviator-latest"

HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": API_HOST
}

def fetch_and_store():
    response = requests.get(URL, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        last_entry = data["data"][-1]
        multiplier = float(last_entry["round"])

        # Load existing data
        file_path = "data/aviator_history.csv"
        df = pd.read_csv(file_path) if os.path.exists(file_path) else pd.DataFrame(columns=["multiplier"])

        # Avoid duplicate entries
        if df.empty or df["multiplier"].iloc[-1] != multiplier:
            df.loc[len(df)] = [multiplier]
            df.to_csv(file_path, index=False)
            print(f"Logged new multiplier: {multiplier}")
    else:
        print(f"Error fetching data: {response.status_code} - {response.text}")
