import os

from crewai import Agent
from crewai import LLM


def create_agents():

    llm = LLM(
        model="groq/openai/gpt-oss-120b",
        api_key=os.environ["GROQ_API_KEY"],
        temperature=0.2
    )

    requirements_agent = Agent(
        role="University Admission Requirements Checker",
        goal=(
            "Check the admission requirements for university "
            "programs using only the information provided."
        ),
        backstory=(
            "You understand the Pakistani education system, "
            "including ICS, FSc Pre-Engineering and "
            "FSc Pre-Medical."
        ),
        llm=llm,
        verbose=False
    )

    eligibility_agent = Agent(
        role="Student Eligibility Checker",
        goal=(
            "Determine whether the student meets the "
            "provided admission requirements."
        ),
        backstory=(
            "You carefully compare a student's qualification, "
            "percentage and subjects with admission requirements."
        ),
        llm=llm,
        verbose=False
    )

    recommendation_agent = Agent(
        role="University Program Recommendation Agent",
        goal=(
            "Recommend suitable university programs based "
            "on the student's academic background and interests."
        ),
        backstory=(
            "You help Pakistani students understand which "
            "academic programs may fit their educational "
            "background and interests."
        ),
        llm=llm,
        verbose=False
    )

    advisor_agent = Agent(
        role="Final Admission Advisor",
        goal=(
            "Combine the results from the other agents and "
            "give the student a clear admission assessment."
        ),
        backstory=(
            "You are a university admission advisor. "
            "You explain results clearly and never invent "
            "requirements that were not provided."
        ),
        llm=llm,
        verbose=False
    )

    return (
        requirements_agent,
        eligibility_agent,
        recommendation_agent,
        advisor_agent
    )
