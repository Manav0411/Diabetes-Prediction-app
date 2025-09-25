# pages/1_Input_Features.py
import streamlit as st
import pandas as pd
import joblib

# Load the model
try:
    model = joblib.load("diabetes_model.pkl")
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'diabetes_model.pkl' is in the root directory.")
    st.stop()

st.title("Enter Patient Features")
st.write("Provide the patient's details below.")

# --- Feature Inputs ---
pregnancies = st.number_input("Pregnancies", 0, 20, 1)
glucose = st.number_input("Glucose", 0, 300, 120)
blood_pressure = st.number_input("Blood Pressure (mm Hg)", 0, 200, 70)
skin_thickness = st.number_input("Skin Thickness (mm)", 0, 100, 20)
insulin = st.number_input("Insulin (mu U/ml)", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.number_input("Age (years)", 1, 120, 30)

# --- Predict Button and Page Switch ---
if st.button("Get Prediction", use_container_width=True):
    # Create a DataFrame from the inputs
    user_data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]],
                             columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
    
    # Make prediction and get probabilities
    prediction = model.predict(user_data)[0]
    prediction_proba = model.predict_proba(user_data)[0]

    # Store results in session state
    st.session_state['prediction_result'] = prediction
    st.session_state['prediction_proba'] = prediction_proba

    # Switch to the results page
    st.switch_page("pages/2_Results.py")