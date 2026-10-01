import os

import streamlit as st

from crew import create_admission_crew
from data import PROGRAMS


# --------------------------------------------------
# Streamlit configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Pakistan University Admission Advisor",
    page_icon="🎓",
    layout="wide"
)


# --------------------------------------------------
# Load Groq API key
# --------------------------------------------------

if "GROQ_API_KEY" in st.secrets:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]


# --------------------------------------------------
# Page title
# --------------------------------------------------

st.title("🎓 Pakistan University Admission Advisor")

st.write(
    "A simple Multi-Agent University Admission System "
    "built with CrewAI, Groq and Streamlit."
)

st.divider()


# --------------------------------------------------
# Student Information
# --------------------------------------------------

st.header("Student Information")

name = st.text_input("Student Name")

qualification = st.selectbox(
    "Intermediate / HSSC Qualification",
    [
        "ICS",
        "FSc Pre-Engineering",
        "FSc Pre-Medical",
        "ICom",
        "FA"
    ]
)

percentage = st.number_input(
    "HSSC Percentage",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)


# --------------------------------------------------
# Subjects
# --------------------------------------------------

st.subheader("Subjects")

mathematics = st.checkbox("Mathematics")
physics = st.checkbox("Physics")
chemistry = st.checkbox("Chemistry")
biology = st.checkbox("Biology")
computer_science = st.checkbox("Computer Science")


# --------------------------------------------------
# Interests
# --------------------------------------------------

interests = st.multiselect(
    "Your Interests",
    [
        "Computer Science",
        "Artificial Intelligence",
        "Software Engineering",
        "Data Science",
        "Cyber Security",
        "Engineering",
        "Biotechnology",
        "Business",
        "Psychology"
    ]
)


# --------------------------------------------------
# Admission button
# --------------------------------------------------

if st.button(
    "🔍 Check Admission",
    use_container_width=True
):

    if not name:
        st.warning("Please enter your name.")
        st.stop()

    # ----------------------------------------------
    # Create student information
    # ----------------------------------------------

    student = {
        "name": name,
        "qualification": qualification,
        "percentage": percentage,
        "subjects": {
            "Mathematics": mathematics,
            "Physics": physics,
            "Chemistry": chemistry,
            "Biology": biology,
            "Computer Science": computer_science
        },
        "interests": interests
    }

    # ----------------------------------------------
    # Prepare program information
    # ----------------------------------------------

    programs_text = ""

    for program_name, details in PROGRAMS.items():

        programs_text += f"""
Program:
{program_name}

Accepted Qualifications:
{", ".join(details["qualifications"])}

Minimum Percentage:
{details["minimum_percentage"]}%

Required Subjects:
{", ".join(details["subjects"])}

Description:
{details["description"]}

----------------------------
"""

    # ----------------------------------------------
    # Run Multi-Agent system
    # ----------------------------------------------

    try:

        with st.spinner(
            "🤖 AI agents are analyzing your admission..."
        ):

            crew = create_admission_crew()

            result = crew.kickoff(
                inputs={
                    "student": str(student),
                    "programs": programs_text
                }
            )

        # ------------------------------------------
        # Display result
        # ------------------------------------------

        st.success("Admission analysis completed!")

        st.divider()

        st.header("📋 Admission Assessment")

        st.markdown(str(result))

    except Exception as e:

        st.error(
            "Something went wrong while running the "
            "Multi-Agent system."
        )

        st.exception(e)
