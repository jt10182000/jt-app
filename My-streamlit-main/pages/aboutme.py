import streamlit as st

st.title("About Jessa 👦")

st.title("🖼️Self Gallery")

image_paths = ["My-streamlit-main/pic/M4.jpg", "My-streamlit-main/pic/M1.jpg", "My-streamlit-main/pic/M2.jpg"]

cols = st.columns(len(image_paths))

for col, image_path in zip(cols, image_paths):
    col.image(image_path)

st.header("Toquero, Jessa O.")

st.markdown("""
##### 👨‍👦‍👦 Family Members

* 🤱 Mother's Name: Merlisa Toquero
* 👨 Father's Name: Diego Toquero
* 👧 Sister's Name: April Joy Toquero
* 👧 Sister's Name: Merjie Toquero
* 👧 Brother's Name: Jeremie Toquero
* 👧 Sister's Name: Crislyn Toquero

### 🔎 Overview
""", unsafe_allow_html=True)

# Personal Information
st.header("Personal Information")
st.write("**Name:** Toquero, Jessa O.")
st.write("**Age:** 23 years old")
st.write("**Education:** Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY")
st.write("**Year:** 3rd year Bachelor of Science in Information Systems Student")
st.write("**Location:** Currently boarding in Zone 1 Talisay City, Permanent Address is Don Salvador Benedicto Negross Occidental")

with st.expander("Who am I 10 years From now??"):
    st.markdown("""
    
    #
                Ten years from now, I envision myself as a highly skilled Information Systems (IS) professional, recognized for leading innovative projects that solve complex business challenges. 
                With advanced certifications and possibly a master’s degree, I excel in the field of my degrees
                As a manager, I foster a collaborative and innovative team environment, driving high-impact projects that enhance business performance. 
                Additionally, I am a thought leader in the IS community, sharing insights at industry conferences and through professional publications.
                Balancing my professional and personal life, I remain committed to continuous learning and staying at the forefront of technological advancements.

                Personal Growth and Vision, My path to becoming a leading information professional will be defined by ongoing learning and personal development.
                I will adopt a mindset of curiosity and resilience, consistently pursuing new knowledge and adapting to evolving circumstances. 
                My enthusiasm for information science will be driven by a commitment to positively impact the world, tackling societal challenges with innovative solutions.

                In 2034, I will show how education, hard work, and forward-thinking can transform a person. My career will include research, teaching, leadership, 
                and making a difference in society. Looking back at my journey from an eager student to a leading professional, I will be proud of my contributions to the field.

               In conclusion, ten years from now, I will be an influential information scientist, teacher, and leader, focused on advancing the field and using data to help others. 
               My story will be about a constant pursuit of knowledge, creative thinking, and a strong commitment to making a positive impact.
    """, unsafe_allow_html=True)

st.title("🖼️Gallery")

images = [
    {"path": "My-streamlit-main/pic/fam2.jpg", "caption": "Through every high and low, your unwavering support has been our anchor. This family picture is not just a snapshot; it's a testament to the love and strength we share. Thank you for being by my side, making every step of this journey meaningful and memorable."},
    {"path": "My-streamlit-main/pic/Fri1.jpg", "caption": "Grateful for a friend like you who's been with me through every twist and turn of this journey. Your support has been a beacon of light in the darkest of times. Thank you for being there, always. 🙏💫 #FriendshipGoals #Gratitude"},
    {"path": "My-streamlit-main/pic/us3.jpg", "caption": "Sharing laughter, learning, and countless memories together. Classmates today, friends forever. 📚✨"}
]

for image in images:
    st.image(image["path"], caption=image["caption"])

st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        padding: 2em;
    }
    h1, h2 {
        color: #4CAF50;
    }
    .stText {
        font-size: 1.2em;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer or additional sections (optional)
st.write("### Thank you for visiting my profile!")
st.write("Feel free to connect and reach out if you share similar interests or have any questions.")
