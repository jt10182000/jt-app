import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

# Add the page title
add_page_title()

# Define the pages and sections
show_pages(
    [
        Page("My-streamlit-main/home.py", "ITEQMT Machine Learning Application Portfolio", "👨‍💻"),
        Section("Main Page", "📢"),
        Page("My-streamlit-main/pages/aboutme.py", "ABOUT ME", "1️⃣", in_section=True),
        Page("My-streamlit-main/pages/description.py", "Streamlit App Description", "2️⃣", in_section=True),
        Page("My-streamlit-main/pages/learnings.py", "🧠 What I Have Learned", "3️⃣", in_section=True),

        Section("Sample Projects", "📂"),
        Page("My-streamlit-main/pages/analyzer.py", "📝Basic Sentiment Analyzer", "1️⃣", in_section=True),
        Page("My-streamlit-main/pages/classification.py", "Fruit Identification", "2️⃣", in_section=True),
        Page("My-streamlit-main/pages/prediction.py", "📊 Prediction", "3️⃣", in_section=True),

        Section("Project Source Code", "💻"),
        Page("My-streamlit-main/pages/analyze_src.py", "Sentiment Analyzer SRC", "1️⃣", in_section=True),
        Page("My-streamlit-main/pages/classification_src.py", "Image Classification SRC", "2️⃣", in_section=True),
        Page("My-streamlit-main/pages/prediction_src.py", "Prediction SRC", "3️⃣", in_section=True),
    ]
)

# Hide specific pages
hide_pages(["Thank you"])

# Main content of the home page
st.markdown("### FINAL REQUIREMENTS PRESENTED BY: ")
st.header("Toquero, Jessa of BSIS 3B")
st.image("My-streamlit-main/M6.jpg")
st.markdown(
    """<a href="/photographer/thinkstock-83786">Thinkstock</a> on <a href="/">Freeimages.com</a>""",
    unsafe_allow_html=True,
)

# Contact information
st.info("For more info, contact [Toquero, Jessa O.](https://www.facebook.com/jessa.toquero.942?mibextid=JRoKGi) on Facebook", icon="📧")
st.info("Contact [Toquero, Jessa O.](https://www.instagram.com/toquero.jessa?igsh=MXdnaGY0Z2hzNzJqag==) on Instagram", icon="📧")
st.markdown("---")


st.image("./blacks.jpg")

# Expander section for history, purpose, and usage
with st.expander("History, Purpose, and Usage"):
    st.markdown(
        """
        ### History of Machine Learning
        
        Machine learning has a rich history spanning several decades. It began in the 1940s-1950s with the foundation of AI and the introduction of neural networks by Frank Rosenblatt. 
        The 1950s-1960s saw symbolic AI using explicit rules and logic, with early programs like the Logic Theorist. From the 1960s-1980s, machine learning algorithms emerged, including the nearest neighbor algorithm and the backpropagation algorithm for neural networks. Despite an "AI Winter" in the 1970s-1980s, foundational work continued. The 1990s brought a resurgence with statistical methods like SVMs and ensemble methods.
        The 2000s-2010s marked the deep learning revolution with CNNs and RNNs, significantly advancing image and sequence data processing. By the 2010s, machine learning became crucial in various fields, aided by frameworks like TensorFlow and PyTorch. 
        Key figures include Geoffrey Hinton, Yann LeCun, and Yoshua Bengio, pioneers in deep learning. Today, machine learning continues to evolve rapidly, driving innovation across numerous applications.
               
        ### Purpose of Machine Learning
                 
        The purpose of machine learning is to enable computers to learn from data and make decisions or predictions without being explicitly programmed. 
        It aims to create systems that can automatically improve their performance over time through experience. Machine learning is used to recognize patterns, classify information, and make forecasts based on data. It helps in automating tasks, enhancing efficiency, and providing insights in various fields such as healthcare, finance, marketing, and technology. By leveraging algorithms and statistical models, machine learning enables the development of intelligent applications that can adapt and respond to new data, ultimately driving innovation and solving complex problems.
                
        ### Usage of Machine Learning
        Machine learning is used across various industries and applications, including:

        * Healthcare: Machine learning is used to analyze medical data for diagnosing diseases, predicting patient outcomes, and personalizing treatment plans.
        * Entertainment: It powers recommendation systems for streaming services, helping to suggest movies, shows, and music tailored to individual preferences.
        * Transportation: Machine learning enhances autonomous driving technologies, optimizing routes, and improving safety through predictive maintenance and traffic management.
        * Retail: Machine learning helps in demand forecasting, personalized marketing, and inventory management, enhancing customer experience and sales.
        * Manufacturing: It enables predictive maintenance, quality control, and supply chain optimization, improving efficiency and reducing downtime.
        * Business: It is used for financial analysis, fraud detection, and customer relationship management, driving better decision-making and operational efficiency.
        """
    )

# Introduction to the Streamlit Application Project
st.title('Introduction to the Streamlit Application Project')

st.markdown(
    """
    Welcome to our Streamlit Application Project, a comprehensive initiative designed to harness the power of machine learning through an intuitive and interactive web interface. This project aims to showcase the versatility and practicality of machine learning models in real-world applications, specifically focusing on three key areas: sentiment analysis, image classification, and predictive analytics.
    ### 🔎 Overview
    """
)

st.image("My-streamlit-main/ml.jpg")

st.markdown(
    """
    Machine learning is a branch of artificial intelligence (AI) that focuses on developing algorithms and statistical models that enable computers to perform tasks without explicit instructions. Instead, these systems learn from data, identifying patterns and making decisions with minimal human intervention. The core idea is to allow the machine to improve its performance over time as it is exposed to more data.

    Quantitative methods refer to a set of techniques used in research and analysis that rely on quantifiable data, numerical values, and statistical methods to investigate phenomena, test hypotheses, and draw conclusions. These methods are particularly useful in fields such as social sciences, economics, psychology, and natural sciences, where researchers seek to measure and analyze observable and measurable variables.

    ### ⭐ Star the project on Github
    <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true" width="150" height="20" title="GitHub"></iframe>
    """
)

# Hide Streamlit style elements
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
