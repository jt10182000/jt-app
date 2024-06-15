import streamlit as st
from PIL import Image
import os

# Set page configuration
st.set_page_config(layout="wide", page_title="Learnings")

# Title and Header
st.title("🧠What I haved Learned")
st.header('💭Learnings..!')

# Image
image_path = "My-streamlit-main/ml.jpg"
if os.path.exists("My-streamlit-main/ml.jpg"):
    image = Image.open("My-streamlit-main/ml.jpg")
    st.image(image)
else:
    st.warning("Image not found. Please check the file path.")

# Main Markdown Content
st.markdown("""
#
                Learnings from Quantitative Methods: Building Foundations for the Future:
                
Studying Quantitative Methods has given me a strong understanding of the basic skills and techniques needed to analyze and interpret data. 
This course taught me everything from simple data analysis to more complex tasks like image classification and sentiment analysis. 
The knowledge and skills I gained from this course will serve as a foundation for my future goals.

The skills I learned are not just academic but practical tools that will boost my future career. 
Being able to analyze data, write code, and use machine learning techniques opens up many opportunities in different fields. 
Whether I go into data science, AI, finance, healthcare, or any other industry, the foundation from this course will be key to my success.

These skills are also interdisciplinary, meaning I can work on innovative projects and solve complex problems that need both analytical
thinking and technical know-how. The quantitative methods I've learned will help me adapt to new challenges, keep learning, 
and stay current with technological advances.

Overall, Quantitative Methods has been a transformative learning experience, giving me essential skills and knowledge crucial for my future. 
From basic coding and data analysis to advanced applications like image classification and sentiment analysis, the skills from this course will enable me 
to make significant contributions in my chosen field and beyond.         
            """, unsafe_allow_html=True)

# Expander with Practical Applications
with st.expander("🔧Practical Applications"):
    st.markdown("""
    #
                Image Classification:
One exciting use of the skills learned in Quantitative Methods is image classification. 
By learning how to preprocess data, train machine learning models, and evaluate their performance, I can create systems that accurately classify images. 
For example, I could build a model to identify different types of flowers like roses, sunflowers, lilies, lavenders, and daisies. This shows how theoretical knowledge can solve real-world problems. 
This skill is especially useful in fields like computer vision, agriculture, and environmental monitoring.
                
                Sentiment Analysis:
Another useful application is sentiment analysis, which looks at text data to figure out if the sentiment is positive, negative, or neutral. 
Building sentiment analyzers is very helpful for things like market research, customer feedback, and monitoring social media. 
By using data analysis and natural language processing (NLP), I can create tools that help businesses understand customer feelings and improve their products and services.
    """, unsafe_allow_html=True)
