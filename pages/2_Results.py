# pages/2_Results.py
import streamlit as st

st.title("Prediction Results")

# Check if the prediction result exists in the session state
if 'prediction_result' in st.session_state:
    prediction = st.session_state['prediction_result']
    prediction_proba = st.session_state['prediction_proba']

    st.write("Based on the provided data, the prediction is:")

    # Display the result
    if prediction == 1:
        st.error("Outcome: Diabetic", icon="⚠️")
    else:
        st.success("Outcome: Not Diabetic", icon="✅")
    
    st.write(f"**Confidence:** {prediction_proba.max():.2%}")
    st.markdown("---")

    # Button to go back to the input page
    if st.button("Make Another Prediction"):
        # Clear the previous results from session state (optional but good practice)
        del st.session_state['prediction_result']
        del st.session_state['prediction_proba']
        # Switch back to the input page
        st.switch_page("pages/1_Input_Features.py")
else:
    # If the user lands here without a prediction
    st.warning("Please go to the 'Input Features' page to make a prediction first.")
    if st.button("Go to Input Page"):
        st.switch_page("pages/1_Input_Features.py")