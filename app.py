# app.py
import streamlit as st

st.set_page_config(
    page_title="Diabetes Prediction Home",
    layout="centered"
)

st.title("Welcome to the Diabetes Prediction App")
st.write("""
This application uses a machine learning model to predict the likelihood of an individual having diabetes based on several health metrics.

Navigate to the **Input Features** page from the sidebar to enter patient data.
""")

st.info("Please remember this is a demonstration and not a substitute for professional medical advice.")