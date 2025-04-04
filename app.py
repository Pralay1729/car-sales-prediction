import streamlit as st 
import joblib
import numpy as np

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

st.title("Customer Car Price Estimator App")

st.divider()

st.write("""This app is for getting a price estimation for the customer so a car with the price range given can be adviced to the customer""")


age = st.number_input("Enter the age",min_value=18,max_value=90,value=40,step=1)
Salary = st.number_input("Enter the salary", min_value=1000,max_value=999999999,step = 5000,value=30000)
networth = st.number_input("Enter net worth",min_value=0,max_value=9999999999, step = 20000, value=100000)

X = [age,Salary,networth]

calculatebutton=st.button("Calculate")

st.divider()

if calculatebutton:
    st.balloons()
    
    X_2 = np.array(X)
    
    X_array = scaler.transform([X_2])
    
    prediction = model.predict(X_array)
    
    st.write(f"Prediction is {prediction[0]}")
    st.write("Advice cars in the similar values")
else:
    st.write("Please enter the values and press the calculate button")