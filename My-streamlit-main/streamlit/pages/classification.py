
from PIL import Image
import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import os

st.title("Fruit Identification")
st.header("Supported fruits: lemon, apple, mandarin, orange")
st.text("Upload a clear image of a fruit")

# Load fruit data
fruit_data = pd.read_csv("fruit.csv", header=None, names=["fruit_label", "mass", "width", "height", "color_score", "fruit_name"])

# Load the model if it exists
if os.path.exists('fruit_classifier.sav'):
    model = joblib.load('fruit_classifier.sav')
else:
    model = None

uploaded_file = st.file_uploader("Enter image", type=["png", "jpeg", "jpg"])

def simulate_features(image):
    """Simulate mass and color score features for demonstration purposes."""
    # Simulating feature extraction process
    mass = np.random.randint(50, 500)  # Random mass between 50 and 500 grams
    color_score = np.random.uniform(0, 1)  # Random color score between 0 and 1

    return mass, color_score

def classify_fruit(image):
    """Classify the fruit based on the simulated features."""
    if model is None:
        return "Model not trained yet."

    # Simulate feature extraction from the image
    mass, color_score = simulate_features(image)

    # Prepare feature vector
    features = np.array([[mass, color_score]])

    # Predict using the trained model
    fruit_label = model.predict(features)[0]
    fruit_name = fruit_data[fruit_data['fruit_label'] == fruit_label]['fruit_name'].values[0]

    return fruit_name

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded image', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    predicted_fruit = classify_fruit(image)

    if predicted_fruit:
        st.write(f"The uploaded fruit is {predicted_fruit}.")
    else:
        st.write("Fruit classification failed.")

    # Prepare training data
    X = fruit_data[['mass', 'color_score']]
    y = fruit_data['fruit_label']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    st.write(f"Model accuracy: {accuracy}")

    # Save the trained model as a .sav file
    joblib.dump(model, 'fruit_classifier.sav')
    st.write("Model saved as 'fruit_classifier.sav'")
