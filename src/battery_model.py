import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

print("🔄 Loading dataset...")

data = pd.read_csv("data/ev_data.csv")

X = data[["distance_km", "avg_speed", "load_kg", "temperature"]]
y = data["battery_used_kwh"]

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X, y)

joblib.dump(model, "battery_model.pkl")

print("✅ Model trained and saved successfully")
