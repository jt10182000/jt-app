import numpy as np
import pickle
import streamlit as st

# Define the path to trained_model.sav within the My-streamlit-main folder
model_file_path = "My-streamlit-main/trained_model.sav"

# Load the model
try:
    with open(model_file_path, 'rb') as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    st.error(f"The '{model_file_path}' file was not found. Please ensure it is in the correct directory.")
    st.stop()

# Define crops and label mapping
crops = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
         'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
         'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
         'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']
crops.sort()
labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
label_crops = dict(zip(labels, crops))

html_code = '''
<h1 style="color:blue; text-align:center">Crop Recommendation System</h1>
'''

def CropRecommendation(input_data):
    """Function to predict which crop is best suited for a particular region."""
    input_data = np.array(input_data).reshape(1, -1)
    recommend = model.predict(input_data)
    return label_crops[recommend[0]]

def main():
    st.markdown(html_code, unsafe_allow_html=True)

    nitrogen = st.text_input("Enter Nitrogen content in soil ")
    phosphorous = st.text_input("Enter Phosphorous content in soil ")
    potassium = st.text_input("Enter Potassium content in soil ")
    temperature = st.text_input("Enter Temperature in Celsius")
    humidity = st.text_input("Enter relative humidity in %")
    ph = st.text_input("Enter pH value of the soil")
    rainfall = st.text_input("Enter rainfall in mm")

    BestCrop = ""
    if st.button("Recommend Crop"):
        if (nitrogen and phosphorous and potassium and temperature and humidity and ph and rainfall):
            BestCrop = CropRecommendation([int(nitrogen), int(phosphorous), int(potassium),
                                           float(temperature), float(humidity), float(ph), float(rainfall)])
            st.success(f"The recommended crop is: {BestCrop}")
        else:
            st.write("Please enter correct values.")

if __name__ == '__main__':
    main()
