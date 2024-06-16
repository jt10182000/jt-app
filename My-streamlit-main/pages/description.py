import streamlit as st

st.title("Description of Different Streamlit Applications")

st.header('Simple Sentiment Analyzer App')
st.image("My-streamlit-main/pic/analyze.png", width=600)  # Adjusted width

with st.expander("🔮Sentiment Analyzer"):
    st.markdown("""
    A Sentiment Analyzer is a powerful tool in natural language processing that evaluates text to determine the underlying sentiment or emotional tone. It uses algorithms 
    and machine learning models to classify sentences or larger bodies of text as positive, negative, or neutral. The analyzer examines various
    linguistic features such as word choice, context, and syntax to identify feelings and attitudes conveyed by the text. For example, if you input
    a sentence like "I love this new smartphone!", the sentiment analyzer would detect the positive sentiment due to the use of the word "love" and 
    the overall enthusiastic tone. Conversely, a sentence like "I am really disappointed with this service" would be classified as negative, reflecting 
    dissatisfaction. This tool is widely used in customer feedback analysis, social media monitoring, and other applications where understanding emotional responses is crucial.
    """, unsafe_allow_html=True)

st.header('Fruit Image Classification')
st.image("My-streamlit-main/pic/Fruit1.png", width=600)  # Adjusted width
st.image("My-streamlit-main/pic/Fruit2.png", width=600)  # Adjusted width

with st.expander("Fruit Image Classification Project"):
    st.markdown("""
    Image Classification: In my image classification project, the focus is on accurately identifying different kinds of fruits from uploaded images. 
    The project aims to classify images into distinct categories such as lemon, apple, orange, and mandarin. It utilizes a comprehensive dataset of labeled fruit identification images, comprising thousands of images for each fruit. 
    This ensures a diverse and representative sample for training and testing the model.
    """, unsafe_allow_html=True)

st.header('🔍Prediction')
st.image("My-streamlit-main/pic/predictresult.png", width=600)  # Adjusted width

with st.expander("Image Classification"):
    st.markdown("""
    With advancements in natural language processing, predictive analytics has become indispensable for anticipating outcomes based on data-driven insights. 
    In this application, we harness the power of machine learning algorithms to make accurate predictions from input data. 
    The predictive model scrutinizes diverse linguistic nuances such as word choice, context, and syntactical structures to decipher underlying sentiments and emotional tones within text. 
    For instance, a statement like "I love this new smartphone!" would be recognized positively due to the use of affirmative language and enthusiastic expressions. 
    Conversely, phrases such as "I am really disappointed with this service" convey negative sentiments, reflecting dissatisfaction.
    This tool is pivotal in various domains, including customer feedback analysis and social media monitoring, where understanding emotional responses is critical for informed decision-making and proactive strategies.
    """, unsafe_allow_html=True)
