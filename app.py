import streamlit as st

st.set_page_config(page_title="LifeBalance AI", layout="centered")

st.title("LifeBalance AI")
st.subheader("Predict Burnout, Focus Loss & Lifestyle Health Risks")

st.write("This demo analyzes digital habits to provide early risk insights.")

# User Inputs
screen_time = st.slider("Daily Screen Time (hours)", 0, 16, 6)
sleep_hours = st.slider("Sleep Duration (hours)", 0, 12, 7)
activity_level = st.selectbox(
    "Physical Activity Level",
    ["Low", "Moderate", "High"]
)

st.divider()

# Risk Logic
burnout = "Low"
focus_loss = "Low"
health_risk = "Low"

if screen_time > 8 and sleep_hours < 6:
    burnout = "High"
    focus_loss = "High"
    health_risk = "High"
elif screen_time > 6 and sleep_hours < 7:
    burnout = "Medium"
    focus_loss = "Medium"
    health_risk = "Medium"

if activity_level == "Low":
    health_risk = "High"

# Output
st.subheader("Predicted Risk Levels")

st.metric("Burnout Risk", burnout)
st.metric("Focus Loss Risk", focus_loss)
st.metric("Lifestyle Health Risk", health_risk)

st.divider()

st.info(
    "Note: This system provides preventive lifestyle risk indicators and does not offer medical diagnosis."
)
