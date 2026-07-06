import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib
from prediction import predict_scarcity
from recommendation import generate_recommendations

# Folder containing app.py
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Go one folder up
PROJECT_DIR = os.path.dirname(CURRENT_DIR)

# Models folder
MODEL_DIR = os.path.join(PROJECT_DIR, "models")


country_encoder = joblib.load(
    os.path.join(MODEL_DIR, "country_encoder.pkl")
)

# ------------------------

st.set_page_config(
    page_title="AquaIntel",
    layout="wide"
)

st.title("💧 AquaIntel")
st.subheader("AI-Powered Water Decision Intelligence Platform")
st.write(
"""
The prediction considers:

- Total Water Consumption
- Groundwater Depletion
- Rainfall
- Agricultural Water Usage
- Industrial Water Usage
- Household Water Usage
"""
)

#sidebar inputs
st.sidebar.header("Water Parameters")

country = st.sidebar.selectbox(
    "Country",
    list(country_encoder.classes_)
)

year = st.sidebar.slider(
    "Year",
    2000,
    2024,
    2024
)

consumption = st.sidebar.number_input(
    "Total Water Consumption",
    value=200.0
)

per_capita = st.sidebar.number_input(
    "Per Capita Water Use",
    value=150.0
)

agriculture = st.sidebar.slider(
    "Agricultural Water Use %",
    0,
    100,
    60
)

industry = st.sidebar.slider(
    "Industrial Water Use %",
    0,
    100,
    20
)

household = st.sidebar.slider(
    "Household Water Use %",
    0,
    100,
    20
)

rainfall = st.sidebar.number_input(
    "Rainfall (mm)",
    value=700.0
)

groundwater = st.sidebar.slider(
    "Groundwater Depletion %",
    0,
    100,
    40
)

#prediction
# -----------------------------
# Prediction
# -----------------------------

if st.button("🚀 Predict Water Scarcity"):

    country_encoded = country_encoder.transform([country])[0]

    features = [
        country_encoded,
        year,
        consumption,
        per_capita,
        agriculture,
        industry,
        household,
        rainfall,
        groundwater
    ]

    scarcity = predict_scarcity(features)

    st.markdown("---")

    if scarcity.lower() == "high":
        st.error(f"🔴 Predicted Water Scarcity : {scarcity}")

    elif scarcity.lower() == "medium":
        st.warning(f"🟡 Predicted Water Scarcity : {scarcity}")

    else:
        st.success(f"🟢 Predicted Water Scarcity : {scarcity}")

    # Dashboard metrics
    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Groundwater",
        f"{groundwater}%"
    )

    c2.metric(
        "Rainfall",
        f"{rainfall} mm"
    )

    c3.metric(
        "Agricultural Usage",
        f"{agriculture}%"
    )

    st.markdown("---")

    st.subheader("📊 AI Decision Summary")

    st.info(
        f"""
The AI analyzed historical water usage patterns, rainfall,
groundwater depletion and sector-wise consumption.

### Prediction

**{scarcity} Water Scarcity**

This prediction is generated using a Random Forest Machine Learning model.
"""
    )

    recommendations = generate_recommendations(
        scarcity,
        groundwater,
        rainfall,
        agriculture,
        consumption
    )

    st.subheader("💡 Recommended Actions")

    for recommendation in recommendations:
        st.success(recommendation)

    st.markdown("---")

    st.subheader("🤖 AI Agents Status")

    a1, a2, a3, a4 = st.columns(4)

    a1.success("📥 Data Agent")
    a2.success("📈 Analytics Agent")
    a3.success("🧠 Prediction Agent")
    a4.success("💡 Recommendation Agent")

    st.markdown("---")

    st.subheader("📌 Water Risk Indicators")

    st.progress(min(groundwater/100,1.0))
    st.write(f"Groundwater Depletion : {groundwater}%")

    st.progress(min(agriculture/100,1.0))
    st.write(f"Agricultural Water Usage : {agriculture}%")

    st.progress(min(industry/100,1.0))
    st.write(f"Industrial Water Usage : {industry}%")

    st.progress(min(household/100,1.0))
    st.write(f"Household Water Usage : {household}%")

    st.markdown("---")

    st.caption(
        "AquaIntel converts historical water data into actionable intelligence using AI-powered prediction and recommendations."
    )