import joblib
import pandas as pd
import streamlit as st

model = joblib.load("house_price_model.pkl")

st.title("house price prediction")

st.write("Enter house details to predict the price")

area = st.slider("Area (sq ft )",500,5000,1500)

bedrooms = st.selectbox(
    "Bedroom",
    [1,2,3,4,5,6]
)

bathrooms = st.selectbox(
    "Bathroom",
    [1,2,3,4,5,6]
)

Location = st.selectbox(
    "loactaion",
    ["Lahore","Karachi","Islamabad","Rawalpindi","Faislabad"]
)

house_age = st.slider(
    "House age",
    0,30,5
)

if st.button("Predict Price"):

    new_house = pd.DataFrame({
        "area_sqft":[area],
        "bedrooms":[bedrooms],
        "bathrooms":[bathrooms],
        "location":[Location],
        "house_age":[house_age],

    })

    price = model.predict(new_house)[0]

    st.success(f"Estimated House Price: Rs.{price:,.0f}")