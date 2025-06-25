import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load('churn_random_forest_model.pkl')

st.title("Customer Churn Predictor 💼")

# Form input with default placeholders
gender = st.selectbox("Gender", ["Select...", "Male", "Female"])
senior = st.selectbox("Senior Citizen", ["Select...", "Yes", "No"])
partner = st.selectbox("Partner", ["Select...", "Yes", "No"])
dependents = st.selectbox("Dependents", ["Select...", "Yes", "No"])
tenure = st.slider("Tenure (Months)", 0, 72, 12)
phone = st.selectbox("Phone Service", ["Select...", "Yes", "No"])
paperless = st.selectbox("Paperless Billing", ["Select...", "Yes", "No"])
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
contract = st.selectbox("Contract", ["Select...", "Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet Service", ["Select...", "DSL", "Fiber optic", "No"])
payment = st.selectbox("Payment Method", [
    "Select...", "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])
streaming_tv = st.selectbox("Streaming TV", ["Select...", "Yes", "No"])
streaming_movies = st.selectbox("Streaming Movies", ["Select...", "Yes", "No"])
tech_support = st.selectbox("Tech Support", ["Select...", "Yes", "No"])
device_protection = st.selectbox("Device Protection", ["Select...", "Yes", "No"])
online_security = st.selectbox("Online Security", ["Select...", "Yes", "No"])
online_backup = st.selectbox("Online Backup", ["Select...", "Yes", "No"])
multiple_lines = st.selectbox("Multiple Lines", ["Select...", "Yes", "No"])


if st.button("Predict"):
    # Check if any selectbox has "Select..." still selected
    required_fields = [gender, senior, partner, dependents, phone, paperless, contract, internet, payment]
    if "Select..." in required_fields:
        st.warning("Please fill out all fields before predicting.")
    else:
        # Feature engineering
        input_dict = {
            'gender': 1 if gender == "Male" else 0,
            'SeniorCitizen': 1 if senior == "Yes" else 0,
            'Partner': 1 if partner == "Yes" else 0,
            'Dependents': 1 if dependents == "Yes" else 0,
            'tenure': tenure,
            'PhoneService': 1 if phone == "Yes" else 0,
            'PaperlessBilling': 1 if paperless == "Yes" else 0,
            'MonthlyCharges': monthly_charges,
            'Contract_One year': int(contract == "One year"),
            'Contract_Two year': int(contract == "Two year"),
            'InternetService_Fiber optic': int(internet == "Fiber optic"),
            'InternetService_No': int(internet == "No"),
            'PaymentMethod_Electronic check': int(payment == "Electronic check"),
            'PaymentMethod_Mailed check': int(payment == "Mailed check"),
            'PaymentMethod_Credit card (automatic)': int(payment == "Credit card (automatic)"),
            'StreamingTV_Yes': int(streaming_tv == "Yes"),
            'StreamingMovies_Yes': int(streaming_movies == "Yes"),
            'TechSupport_Yes': int(tech_support == "Yes"),
            'DeviceProtection_Yes': int(device_protection == "Yes"),
            'OnlineSecurity_Yes': int(online_security == "Yes"),
            'OnlineBackup_Yes': int(online_backup == "Yes"),
            'MultipleLines_Yes': int(multiple_lines == "Yes")

        }

        input_df = pd.DataFrame([input_dict])
        prediction = model.predict(input_df)[0]
        st.success(f"Churn Prediction: {'Yes' if prediction == 1 else 'No'}")
