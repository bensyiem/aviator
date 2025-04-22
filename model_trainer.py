
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("data/aviator_history.csv")
window = 10

# Create rolling features
X, y = [], []
for i in range(len(df) - window):
    features = df["multiplier"].iloc[i:i+window].values
    target = df["multiplier"].iloc[i+window]
    label = ">10x" if target > 10 else ">2x" if target > 2 else "<=2x"
    X.append(features)
    y.append(label)

X = np.array(X)
y = LabelEncoder().fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "models/model.pkl")
print("Model trained and saved to models/model.pkl")
