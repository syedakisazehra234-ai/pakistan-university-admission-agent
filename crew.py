from crewai import Crew
from crewai import Process

from agents import create_agents
from tasks import create_tasks


def create_admission_crew():

    (
        requirements_agent,
        eligibility_agent,
        recommendation_agent,
        advisor_agent
    ) = create_agents()

    (
        requirements_task,
        eligibility_task,
        recommendation_task,
        advisor_task
    ) = create_tasks(
        requirements_agent,
        eligibility_agent,
        recommendation_agent,
        advisor_agent
    )

    crew = Crew(
        agents=[
            requirements_agent,
            eligibility_agent,
            recommendation_agent,
            advisor_agent
        ],
        tasks=[
            requirements_task,
            eligibility_task,
            recommendation_task,
            advisor_task
        ],
        process=Process.sequential,
        verbose=False
    )

    return crew
