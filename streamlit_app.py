import streamlit as st
#import joblib
# Title of the application
st.title("Car Price Prediction App")

# Header
st.header("Predict the Price of Your Car")

# Subheader
st.subheader("Learn the value of your car using this application.")

st.image("car.jpeg", caption="Blue Car", width=400)

st.write("You can see the estimated market value of the car you are interested in below.")

#columns = joblib.load("features_list.joblib")

min_year = 2003
max_year = 2018
year = st.number_input("Year:", min_value=min_year, max_value=max_year)

min_present_price = 0.1
max_present_price = 100
Present_price = st.slider("Present_price:", min_value=min_present_price, max_value=max_present_price)

if fuel_type == "Benzin":
    fuel = 'Petrol'
elif fuel_type == 'Dizel':
    fuel = 'Diesel'
else:
    fuel = 'CNG'

st.write('You selected:', fuel_type)

seller_type = st.selectbox(
    'Owner:',
    ['Galeri', 'Sahibinden'])

if seller_type == 'Galeri':
    seller = 'Dealer'
elif seller_type ==  'Sahibinden':
    seller = 'Individual'
