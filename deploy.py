# Importing the necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pickle
import streamlit as st

# Load the trained linear regression model
with open('lr_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the label encoders
with open('airline_encoder.pkl', 'rb') as file:
    airline_encoder = pickle.load(file)

with open('source_city_encoder.pkl', 'rb') as file:
    source_city_encoder = pickle.load(file)

with open('departure_time_encoder.pkl', 'rb') as file:
    departure_time_encoder = pickle.load(file)

with open('stops_encoder.pkl', 'rb') as file:
    stops_encoder = pickle.load(file)

with open('arrival_time_encoder.pkl', 'rb') as file:
    arrival_time_encoder = pickle.load(file)

with open('destination_city_encoder.pkl', 'rb') as file:
    destination_city_encoder = pickle.load(file)

with open('class_encoder.pkl', 'rb') as file:
    class_encoder = pickle.load(file)

# Define the prediction function
def predict_price(airline, source_city, departure_time, stops, arrival_time, destination_city, travel_class, duration, days_left):
    # Encode the categorical input data
    input_data = [
        airline_encoder.transform([airline])[0], 
        source_city_encoder.transform([source_city])[0], 
        departure_time_encoder.transform([departure_time])[0], 
        stops_encoder.transform([stops])[0], 
        arrival_time_encoder.transform([arrival_time])[0], 
        destination_city_encoder.transform([destination_city])[0], 
        class_encoder.transform([travel_class])[0],
        duration,
        days_left
    ]
    
    # Convert to numpy array and reshape for prediction
    input_data_encoded = np.array(input_data).reshape(1, -1)
    
    # Predict the price using the pre-trained model
    prediction = model.predict(input_data_encoded)
    
    return prediction[0]

from PIL import Image

# Background and header image
background_image = Image.open('airport.png')

# Set background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{st.image(background_image, use_column_width=True)}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Set up the Streamlit app
st.title("Indian Flight Price Prediction")

# Input fields
airline = st.selectbox("Airline", airline_encoder.classes_)
source_city = st.selectbox("Source City", source_city_encoder.classes_)
departure_time = st.selectbox("Departure Time", departure_time_encoder.classes_)
stops = st.selectbox("Number of Stops", stops_encoder.classes_)
arrival_time = st.selectbox("Arrival Time", arrival_time_encoder.classes_)
destination_city = st.selectbox("Destination City", destination_city_encoder.classes_)
travel_class = st.selectbox("Class", class_encoder.classes_)
duration = st.number_input("Flight Duration (in hours)", min_value=0.0, max_value=24.0, step=0.1)
days_left = st.number_input("Days Left Before Flight", min_value=0, max_value=365, step=1)

# Predict button
if st.button("Predict"):
    # Prediction
    prediction = predict_price(airline, source_city, departure_time, stops, arrival_time, destination_city, travel_class, duration, days_left)
    
    # Display the prediction
    st.success(f"Predicted Flight Price: ₹{prediction:.2f}")

# Add a footer
st.markdown('---')
st.markdown('Developed by [Caleb Osagie](https://github.com/Phenomkay)')    
