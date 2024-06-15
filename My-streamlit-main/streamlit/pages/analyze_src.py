import streamlit as st


st.header('Sentiment Analyzer App')
st.subheader('This model was trained using a dataset')
st.code('''

import streamlit as st
import pickle
import numpy as np
from nltk.classify import NaiveBayesClassifier

# Define features (words) and their corresponding labels (emotions)
def word_features(words):
    return dict([(word, True) for word in words])

# Define emotions and their associated words
emotions = {
    'happy': ['happy', 'joyful', 'excited'],
    'sad': ['sad', 'unhappy', 'depressed'],
    'angry': ['angry', 'mad', 'furious'],
    'excited': ['excited', 'thrilled', 'eager'],
    'nervous': ['nervous', 'anxious', 'worried'],
    'scared': ['scared', 'fearful', 'terrified']
}

# Generate training set for each emotion
train_set = [(word_features(word.split()), emotion)
             for emotion, words in emotions.items()
             for word in words]

# Train the Naive Bayes classifier
classifier = NaiveBayesClassifier.train(train_set)

# Function to predict emotions
def predict_emotions(docx):
    results = classifier.classify(word_features(docx.split()))
    return results

# Function to get prediction probabilities
def get_prediction_proba(docx):
    results = classifier.prob_classify(word_features(docx.split()))
    probabilities = {label: results.prob(label) for label in results.samples()}
    return probabilities

# Function to save the trained classifier to a pickle file
def save_model_to_pickle(model, filename):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

# Main Application
def main():
    st.title("Emotion Classifier App")

    # Text input for user to enter a sentence
    sentence = st.text_input("Enter a sentence:")

    if sentence:
        # Classify the sentence
        sentiment = predict_emotions(sentence)
        probabilities = get_prediction_proba(sentence)

        st.write(f"Predicted Emotion: {sentiment}")

        st.write("Prediction Probabilities:")
        for emotion, probability in probabilities.items():
            st.write(f"{emotion}: {probability:.4f}")

        # Button to save the trained classifier to a pickle file
        if st.button("Save Model"):
            save_model_to_pickle(classifier, 'My-streamlit-main/trained_classifier.pkl')
            st.success("Model saved to 'My-streamlit-main/trained_classifier.pkl'")

if __name__ == '__main__':
    main()
''')
