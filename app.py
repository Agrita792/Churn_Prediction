code = '''
import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("decision_tree_model_t.pkl")

st.title("Churn Prediction App 📉")

st.write("Fill in the details below to predict if a customer will churn.")

# Input fields based on your data
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 18, 100, 35)
no_of_days_subscribed = st.number_input("No. of Days Subscribed", min_value=1)
multi_screen = st.selectbox("Multi Screen Subscription", ["yes", "no"])
mail_subscribed = st.selectbox("Mail Subscribed", ["yes", "no"])
weekly_mins_watched = st.number_input("Weekly Minutes Watched")
minimum_daily_mins = st.number_input("Minimum Daily Minutes")
maximum_daily_mins = st.number_input("Maximum Daily Minutes")
weekly_max_night_mins = st.number_input("Weekly Max Night Minutes")
videos_watched = st.number_input("Videos Watched")
maximum_days_inactive = st.number_input("Max Days Inactive")
customer_support_calls = st.number_input("Customer Support Calls")

# Convert inputs to match model format
gender = 1 if gender == "Male" else 0
multi_screen = 1 if multi_screen == "yes" else 0
mail_subscribed = 1 if mail_subscribed == "yes" else 0

features = np.array([[gender, age, no_of_days_subscribed, multi_screen, mail_subscribed,
                      weekly_mins_watched, minimum_daily_mins, maximum_daily_mins,
                      weekly_max_night_mins, videos_watched, maximum_days_inactive,
                      customer_support_calls]])

# Prediction
if st.button("Predict Churn"):
    prediction = model.predict(features)[0]
    if prediction == 1:
        st.error("Prediction: Customer is likely to churn ❌")
    else:
        st.success("Prediction: Customer is not likely to churn ✅")
'''

# Save to a .py file on desktop
with open(r'C:\Users\Agrita Vatish\OneDrive\Desktop\app.py', 'w') as f:
    f.write(code)
