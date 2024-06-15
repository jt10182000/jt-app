import streamlit as st

st.title("Description of Different Streamlit Application")

# Insert custom HTML for background video
st.markdown(
    f"""
    <style>
    .bg-video {{
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        z-index: -1;
    }}
    </style>
    <video autoplay loop muted class="bg-video">
        <source src="./pic/bgk.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    """,
    unsafe_allow_html=True
)

st.header('Simple Sentiment Analyzer App')
st.image("My-streamlit-main/pic/analyze.png")

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

st.header('Fruit Image Classification')
st.image("My-streamlit-main/pic/Fruit1.png", "My-streamlit-main/pic/Fruit2.png")

with st.expander("Fruit Image Classification Project"):
    st.markdown("""
    
    #
                Image Classification
In my image classification project, the focus is on accurately identifying different kinds of Fruits from uploaded images. 
The project aims to classify images into the following distinct categories: lemon, apple, orange, and mandarin.
The goal is to analyze and categorize the Fruit images based on their distinct features. The project utilizes a comprehensive dataset of labeled Fruit Identification images, comprising thousands of images for each fruits. 
This ensures a diverse and representative sample for training and testing the model.

                
    """, unsafe_allow_html=True)

st.header('🔍Prediction')
st.image("My-streamlit-main/pic/predictresult.png")

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
