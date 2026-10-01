from crewai import Task


def create_tasks(
    requirements_agent,
    eligibility_agent,
    recommendation_agent,
    advisor_agent
):

    requirements_task = Task(

        description="""
        Analyze the student's information below.

        Student:
        {student}

        Available university programs and requirements:
        {programs}

        Identify the admission requirements that are
        relevant to this student.

        Do not invent requirements.
        Only use the information provided.
        """,

        expected_output="""
        A clear explanation of the relevant admission
        requirements for the student.
        """,

        agent=requirements_agent
    )

    eligibility_task = Task(

        description="""
        Determine whether the student meets the requirements
        identified by the previous agent.

        Student:
        {student}

        Program information:
        {programs}

        Explain:
        1. Which programs the student appears eligible for.
        2. Which programs the student does not appear eligible for.
        3. Why.
        """,

        expected_output="""
        A simple eligibility assessment with reasons.
        """,

        agent=eligibility_agent
    )

    recommendation_task = Task(

        description="""
        Recommend suitable university programs.

        Student:
        {student}

        Available programs:
        {programs}

        Previous eligibility assessment:
        {eligibility}

        Consider:
        - student's qualification
        - percentage
        - subjects
        - interests

        Recommend programs that appear suitable.
        Explain why each program is recommended.
        """,

        expected_output="""
        A list of suitable programs with reasons.
        """,

        agent=recommendation_agent
    )

    advisor_task = Task(

        description="""
        Create the final admission advice for the student.

        Student:
        {student}

        Admission requirements:
        {requirements}

        Eligibility assessment:
        {eligibility}

        Program recommendations:
        {recommendations}

        Provide a simple report containing:

        1. Student summary
        2. Eligibility results
        3. Recommended programs
        4. Reasons
        5. Important next steps

        Do not invent admission requirements.

        Clearly explain that the result is an assessment
        based on the supplied information and does not
        guarantee university admission.
        """,

        expected_output="""
        A clear and beginner-friendly final admission report.
        """,

        agent=advisor_agent
    )

    return (
        requirements_task,
        eligibility_task,
        recommendation_task,
        advisor_task
    )
