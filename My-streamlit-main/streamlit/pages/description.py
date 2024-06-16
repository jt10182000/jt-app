import streamlit as st

st.title("Description of Different Streamlit Application")

st.header('Simple Sentiment Analyzer App')
st.image("My-streamlit-main/pic/analyze.png")

with st.expander("🔮Sentiment Analyzer"):
     st.markdown("""
    A Sentiment Analyzer is a powerful tool in natural language processing that evaluates text to determine the underlying sentiment or emotional tone.
    """)

st.header('Fruit Image Classification')
st.image("My-streamlit-main/pic/Fruit1.png", "My-streamlit-main/pic/Fruit2.png", use_column_width=True)

with st.expander("Fruit Image Classification Project"):
    st.markdown("""
    Image Classification: Classify fruit images into different categories.
    """)

st.header('🔍 Prediction')
st.image("My-streamlit-main/pic/predictresult.png", use_column_width=True)

with st.expander("Sentiment Analyzer"):
    st.markdown("""
    A Sentiment Analyzer is a powerful tool in natural language processing.
    """)


    
    #
                A Sentiment Analyzer 
It is a powerful tool in natural language processing that evaluates text to determine the underlying sentiment or emotional tone. It uses algorithms 
and machine learning models to classify sentences or larger bodies of text as positive, negative, or neutral. The analyzer examines various
linguistic features such as word choice, context, and syntax to identify feelings and attitudes conveyed by the text. For example, if you input
a sentence like "I love this new smartphone!", the sentiment analyzer would detect the positive sentiment due to the use of the word "love" and 
the overall enthusiastic tone. Conversely, a sentence like "I am really disappointed with this service" would be classified as negative, reflecting 
dissatisfaction. This tool is widely used in customer feedback analysis, social media monitoring, and other applications where understanding emotional responses is crucial.

                
    """, unsafe_allow_html=True)
