import os

# =========================================================
# CrewAI + Groq compatibility fix
# =========================================================
# CrewAI may add cache_breakpoint=True to messages.
# Groq does not support this property.
#
# This patch disables the unsupported marker before
# CrewAI agents are created.
# =========================================================

import crewai.llms.cache as _crewai_cache

_crewai_cache.mark_cache_breakpoint = lambda message: message


# =========================================================
# Imports
# =========================================================

import streamlit as st

from crew import create_admission_crew
from data import PROGRAMS


# =========================================================
# Groq API Key
# =========================================================

if "GROQ_API_KEY" in st.secrets:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="Pakistan University Admission Advisor",
    page_icon="🎓",
    layout="centered"
)


# =========================================================
# Title
# =========================================================

st.title("🎓 Pakistan University Admission Advisor")

st.write(
    "Enter your academic information and interests. "
    "The AI agents will analyze your eligibility and "
    "recommend suitable programs."
)

st.info(
    "Demo system: program requirements are sample data "
    "and should not be treated as official university requirements."
)


# =========================================================
# Student Information
# =========================================================

st.header("👨‍🎓 Student Information")

name = st.text_input(
    "Student Name"
)


qualification = st.selectbox(
    "Current Qualification",
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
    value=60.0,
    step=0.1
)


# =========================================================
# Subjects
# =========================================================

st.subheader("📚 Subjects")

col1, col2 = st.columns(2)

with col1:
    mathematics = st.checkbox("Mathematics")
    physics = st.checkbox("Physics")
    chemistry = st.checkbox("Chemistry")

with col2:
    biology = st.checkbox("Biology")
    computer_science = st.checkbox("Computer Science")


subjects = []

if mathematics:
    subjects.append("Mathematics")

if physics:
    subjects.append("Physics")

if chemistry:
    subjects.append("Chemistry")

if biology:
    subjects.append("Biology")

if computer_science:
    subjects.append("Computer Science")


# =========================================================
# Interests
# =========================================================

st.subheader("💡 Interests")

interests = st.multiselect(
    "Select your areas of interest",
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


# =========================================================
# Program Information
# =========================================================

programs_text = ""

for program_name, details in PROGRAMS.items():

    programs_text += f"""
Program: {program_name}

Accepted Qualifications:
{", ".join(details["qualifications"])}

Minimum Percentage:
{details["minimum_percentage"]}

Required Subjects:
{", ".join(details["subjects"])}

Description:
{details["description"]}

-----------------------------
"""


# =========================================================
# Analyze Button
# =========================================================

if st.button(
    "🚀 Analyze Admission",
    type="primary",
    use_container_width=True
):

    if not name.strip():
        st.warning("Please enter the student's name.")
        st.stop()

    if not subjects:
        st.warning("Please select at least one subject.")
        st.stop()

    if not interests:
        st.warning("Please select at least one interest.")
        st.stop()


    # -----------------------------------------------------
    # Student Profile
    # -----------------------------------------------------

    student = {
        "name": name,
        "qualification": qualification,
        "percentage": percentage,
        "subjects": subjects,
        "interests": interests
    }


    # -----------------------------------------------------
    # Run Multi-Agent System
    # -----------------------------------------------------

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


        # -------------------------------------------------
        # Result
        # -------------------------------------------------

        st.success(
            "Admission analysis completed!"
        )

        st.divider()

        st.header("📋 Admission Assessment")

        st.markdown(str(result))


        # -------------------------------------------------
        # Disclaimer
        # -------------------------------------------------

        st.divider()

        st.caption(
            "This is an AI-generated assessment based on "
            "the supplied demo program data. It does not "
            "guarantee university admission. Always verify "
            "requirements with the official university."
        )


    except Exception as e:

        st.error(
            "Something went wrong while running "
            "the Multi-Agent system."
        )

        st.exception(e)
