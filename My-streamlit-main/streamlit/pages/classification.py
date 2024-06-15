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

# Define the path to the fruit.csv file
csv_file_path = os.path.join("My-streamlit-main", "fruit.csv")
model_file_path = os.path.join("My-streamlit-main", "fruit_classifier.sav")

# Load fruit data
try:
    fruit_data = pd.read_csv(csv_file_path, header=None, names=["fruit_label", "mass", "width", "height", "color_score", "fruit_name"])
except FileNotFoundError:
    st.error(f"The '{csv_file_path}' file was not found. Please ensure it is in the correct directory.")
    st.stop()

# Load the model if it exists
if os.path.exists(model_file_path):
    model = joblib.load(model_file_path)
else:
    model = None

uploaded_file = st.file_uploader("Enter image", type=["png", "jpeg", "jpg"])

# Calculate statistics from the training data
mass_mean = fruit_data['mass'].mean()
mass_std = fruit_data['mass'].std()
color_score_mean = fruit_data['color_score'].mean()
color_score_std = fruit_data['color_score'].std()

def simulate_features(image):
    """Simulate mass and color score features based on training data statistics."""
    mass = np.random.normal(mass_mean, mass_std)  # Simulate mass based on normal distribution
    color_score = np.random.normal(color_score_mean, color_score_std)  # Simulate color score based on normal distribution

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
    try:
        fruit_label = model.predict(features)[0]
        fruit_name = fruit_data[fruit_data['fruit_label'] == fruit_label]['fruit_name'].values[0]
        return fruit_name
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded image', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    if model is None:
        st.write("Training model as it does not exist.")
        
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
        joblib.dump(model, model_file_path)
        st.write(f"Model saved as '{model_file_path}'")

    predicted_fruit = classify_fruit(image)

    if predicted_fruit:
        st.write(f"The uploaded fruit is {predicted_fruit}.")
    else:
        st.write("Fruit classification failed.")
