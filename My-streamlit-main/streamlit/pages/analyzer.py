import streamlit as st
import pandas as pd
import pickle
import os

# Set up the title and description
st.title("Toquero Feelings Analyzer:")
st.markdown("""
Welcome to Toquero's Streamlit app for analyzing different feelings.
Enter your current feeling in the text box below, and let's see what the sentiment analyzer says!
""")

# Input field for user to enter their feeling
message = st.text_input("Tell me what you feel today:")

# Load the trained Naive Bayes classifier from the saved file
model_filename = 'My-streamlit-main/pages/sentimentAnalyzerTest_model.sav'

def load_model():
    if os.path.exists('My-streamlit-main/pages/sentimentAnalyzerTest_model.sav'):
        with open(model_filename, 'rb') as file:
            return pickle.load(file)
    else:
        st.error(f"Model file '{model_filename}' not found. Please check the file path or upload the model file.")
        return None

loaded_model = load_model()

# Define function to extract features from the input message
def word_features(words):
    return {word: True for word in words}

# Function to determine and display the sentiment
def classify_feeling():
    if message:
        message_tone = loaded_model.classify(word_features(message.split()))

        # Determine the sentiment and corresponding emoji
        if message_tone == 'happy':
            st.write("You seem happy! :smile:")
        elif message_tone == 'sad':
            st.write("You seem sad. :pensive:")
        elif message_tone == 'angry':
            st.write("You seem angry. :rage:")
        elif message_tone == 'nervous':
            st.write("You seem nervous. :grimacing:")
        else:
            st.write("Hmm, I'm not sure about that feeling. :thinking_face:")
    else:
        st.write("Please enter a feeling to analyze.")

# Button to trigger the sentiment analysis
if loaded_model:
    st.button('Analyze Feeling', on_click=classify_feeling)