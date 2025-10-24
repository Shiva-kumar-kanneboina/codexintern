import pickle as pk
import pandas as pd
import streamlit as st

# Load the trained model
model = pk.load(open('house_price_model.pkl', 'rb'))

st.header("Hyderabad House Price Predictor")

# Use raw string (r"...") or forward slashes for path
data = pd.read_csv(r"C:\shiva\projects\house price prediction\cleaned_house_data.csv")

# Input fields
loc = st.selectbox('Choose the location', data['Location'].unique())
sqft = st.number_input('Enter the Area in sqft')
bed = st.number_input('Enter the number of bedrooms', min_value=1)
bath = st.number_input('Enter the number of Bathrooms', min_value=1)
dining = st.number_input('Enter the number of DiningTables', min_value=0)

# Build input DataFrame (must match training column names)
input_df = pd.DataFrame([[loc, sqft, bed, bath, dining]],
                        columns=['Location', 'Area', 'No. of Bedrooms', 'Bathrooms', 'DiningTables'])

# Predict
if st.button('Predict Price'):
    output = model.predict(input_df)
    predicted_price =int(output[0])
    st.success(f"The predicted price of the house is Rs.{predicted_price}/-")
    
