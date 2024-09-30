import streamlit as st
import joblib
import pandas as pd

# Title of the application
st.title("Car Price Prediction App")

# Header
st.header("Predict the Price of Your Car")

# Subheader
st.subheader("Learn the value of your car using this application.")

st.image("car.jpeg", caption="Blue Car", width=400)

st.write("You can see the estimated market value of the car you are interested in below.")

columns = joblib.load("features_list.joblib")

min_year = 2003
max_year = 2018
year = st.number_input("Year:", min_value=min_year, max_value=max_year)

min_present_price = 0.1
max_present_price = 100.0
present_price = st.slider("Present Price:", min_value=min_present_price, max_value=max_present_price)

min_km = 500
max_km = 500_000
km = st.slider("km:", min_value=min_km, max_value=max_km)

fuel_type = st.selectbox(
    'Fuel Type:',
    ['Petrol', 'Diesel', 'LPG'])

seller_type = st.selectbox(
    'Owner:',
    ['Dealer', 'Individual'])

transmission = st.selectbox(
    'Transmission:',
    ['Manual', 'Automatic'])

owner = st.selectbox(
    'Number of Previous Owners:',
    [0, 1, 3])

sample_one = [{
    "Year": year,
    "Present_Price": present_price,
    "Kms_Driven": km,
    "Fuel_Type": fuel_type,
    "Seller_Type": seller_type,
    "Transmission": transmission,
    "Owner": owner
}]

df_s = pd.DataFrame(sample_one)
st.dataframe(df_s)

df_s["Year"] = max_year - df_s["Year"]
df_s = pd.get_dummies(df_s).reindex(columns=columns, fill_value=0)

scaler = joblib.load(open("scaler.joblib", "rb"))
model = joblib.load(open("xgb_model.joblib", "rb"))
df_s = scaler.transform(df_s)

if st.button('Predict!'):
    prediction = round(model.predict(df_s)[0] * 10_000)
    st.write('Estimated market value of your car:', prediction)
else:
    st.write('Goodbye')
