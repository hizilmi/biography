import streamlit as st
import datetime

st.set_page_config(page_title="My Biography", page_icon="🌻", layout="wide")

# ---- HEADER SECTION ----
st.title("Biography")
st.subheader("Hello, I'm Hazel")
st.write("I am a 1st Year student. As I grew, I nurtured a passion for learning through leadership in Church from being an ASM President, and this drive led me to graduate with honors from junior high school in Northern Eastern Mindanao Colleges (NEMCO), a milestone that marked not only academic achievement but also the culmination of years of dedication and hard work. Now, as I stand at the threshold of my future, I am filled with ambition and purpose. My sights are set on pursuing a Bachelor of Science in Computer Engineering, a field that captivates me with its blend of creativity, problem-solving, and real-world impact.")

# ---- Personal Info (Left Side) ----
with st.container():
    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("Personal Information")
        
        st.image("1.jpg", use_container_width=True)
        name = st.text_input("Name", "Hazel Mae P. Jamero")
        

        # Age selection
        age = st.selectbox("Age", [str(i) for i in range(18, 101)])  # ages 18-100
    
        # Birthday
        bday = st.date_input("Birthday", datetime.date(2006, 10, 3))
        guardian = st.text_input("Birthplace", " Surigao City, Surigao del Norte")
        # Gender
        options = ["Male", "Female"]
        gender = st.selectbox("Gender", options[1])

        # Family Background
        st.subheader("Family Background")
        
        mother = st.text_input("Mother's Name", "Geraldine P. Jamero")
        mbday_mother = st.date_input("Mother's Birthday", datetime.date(1980, 12, 14))

        father = st.text_input("Father's Name", "Floremar M. Jamero")
        mbday_father = st.date_input("Father's Birthday", datetime.date(1978, 11, 23))

        guardian = st.text_input("Guardian", " ")

        st.write("[Facebook](https://www.facebook.com/share/17R2kGzc9J/?mibextid=LQQJ4d)")  # hyperlink
        st.write("---")

        # Educational Attainment
        st.subheader("Educational Attainment")
        elementary = st.text_area("Elementary School", "Surigao West Central Elementary School")
        highschool = st.text_area("High School", "Northeastern Mindanao Colleges")
        college = st.text_area("College", "Surigao Del Norte State University")
        course = st.text_input("Course", "Bachelor of Science in Computer Engineering")
        year = st.text_input("Year", "1st year")
        
    with right_column:
        st.subheader("Personal Achievement")
        
        
        
        # Social Media Accounts
        st.subheader("Social Media Accounts")
        st.text_area("Junior high", """Grade 7 - With honor
Grade 8 - With honor
Grade 9 - With honor
Grade 10 - With honor
""",  height=125)
        st.text_area("Junior high", """Grade 10 - With honor
Grade 12 - With High Honor
""",  height=92)
        
        fb = st.text_input("Facebook", "Hazel Jamero")
        instagram = st.text_input("Instagram", "hasselemae")
        twitter = st.text_input("Tiktok", "heyouuuuuux")