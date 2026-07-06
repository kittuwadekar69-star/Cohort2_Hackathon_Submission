import os
import joblib
import numpy as np

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(CURRENT_DIR)
MODEL_DIR = os.path.join(PROJECT_DIR, "models")

model = joblib.load(os.path.join(MODEL_DIR, "scarcity_model.pkl"))
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
scarcity_encoder = joblib.load(os.path.join(MODEL_DIR, "scarcity_encoder.pkl"))

def predict_scarcity(features):
    features = np.array(features).reshape(1, -1)
    features = scaler.transform(features)

    prediction = model.predict(features)

    return scarcity_encoder.inverse_transform(prediction)[0]