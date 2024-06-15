

import streamlit as st
import pandas as pd
import pickle
from nltk.corpus import names

# Load the trained Naive Bayes classifier from the saved file
filename = 'pages/sentimentAnalyzerTest_Model.sav'
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

st.title("Weather Forecast Predictor :sun_behind_cloud:")
st.subheader("Enter levels of different factors to predict the weather:")

# User inputs for different factors
temperature_input = st.slider("Temperature (°C): ", -50, 50)
humidity_input = st.slider("Humidity Level (%): ", 0, 100)
wind_speed_input = st.slider("Wind Speed (km/h): ", 0, 150)
pressure_input = st.slider("Atmospheric Pressure (hPa): ", 900, 1100)

# Function to make a prediction
def predict_weather(temperature, humidity, wind_speed, pressure):
    if temperature == 0 and humidity == 0 and wind_speed == 0 and pressure == 900:
        return "No significant factors entered"
    else:
        features = {
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'pressure': pressure
        }
        # Replace 'loaded_model.classify' with your actual prediction model/method
        prediction = loaded_model.classify(features)
        return prediction

# Display button and result
if st.button('Predict'):
    weather_prediction = predict_weather(temperature_input, humidity_input, wind_speed_input, pressure_input)
    st.text("The predicted weather is:")
    st.text_area(label="", value=weather_prediction, height=100)