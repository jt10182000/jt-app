import streamlit as st

st.title("Description of Different Streamlit Application")


st.header('Simple Sentiment Analyzer App')
st.image("./pic/analyze.png")

with st.expander("🔮Sentiment Analyzer"):
    st.markdown("""
    
    #
                A Sentiment Analyzer 
It is a powerful tool in natural language processing that evaluates text to determine the underlying sentiment or emotional tone. It uses algorithms 
and machine learning models to classify sentences or larger bodies of text as positive, negative, or neutral. The analyzer examines various
linguistic features such as word choice, context, and syntax to identify feelings and attitudes conveyed by the text. For example, if you input
a sentence like "I love this new smartphone!", the sentiment analyzer would detect the positive sentiment due to the use of the word "love" and 
the overall enthusiastic tone. Conversely, a sentence like "I am really disappointed with this service" would be classified as negative, reflecting 
dissatisfaction. This tool is widely used in customer feedback analysis, social media monitoring, and other applications where understanding emotional responses is crucial.

                
    """, unsafe_allow_html=True)

st.header('Dog Breed Image Classification')
st.image("./pic/image.png")

with st.expander("Dog Breed Image Classification Project"):
    st.markdown("""
    
    #
                Image Classification
In my image classification project, the focus is on accurately identifying different types of dog breeds from uploaded images. 
The project aims to classify images into eight distinct categories: Beagle, Dachshund, French Bulldog, German Shepherd, Labrador, Poodle, Rottweiler, and Golden Retriever. 
The goal is to analyze and categorize the dog breed images based on their distinct features. The project utilizes a comprehensive dataset of labeled dog breed images, comprising thousands of images for each breed. 
This ensures a diverse and representative sample for training and testing the model.

                
    """, unsafe_allow_html=True)

st.header('🔍Prediction')
st.image("./pic/predict.jpg")

with st.expander("Sentiment Analyzer"):
    st.markdown("""
    
    #
                A Sentiment Analyzer 
It is a powerful tool in natural language processing that evaluates text to determine the underlying sentiment or emotional tone. It uses algorithms 
and machine learning models to classify sentences or larger bodies of text as positive, negative, or neutral. The analyzer examines various
linguistic features such as word choice, context, and syntax to identify feelings and attitudes conveyed by the text. For example, if you input
a sentence like "I love this new smartphone!", the sentiment analyzer would detect the positive sentiment due to the use of the word "love" and 
the overall enthusiastic tone. Conversely, a sentence like "I am really disappointed with this service" would be classified as negative, reflecting 
dissatisfaction. This tool is widely used in customer feedback analysis, social media monitoring, and other applications where understanding emotional responses is crucial.

                
    """, unsafe_allow_html=True)
