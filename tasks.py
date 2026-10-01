from crewai import Task


def create_tasks(
    requirements_agent,
    eligibility_agent,
    recommendation_agent,
    advisor_agent
):

    requirements_task = Task(
        description="""
        Analyze the student's information.

        Student:
        {student}

        Available university programs and requirements:
        {programs}

        Identify the admission requirements relevant
        to this student.

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
        Determine whether the student meets the
        admission requirements.

        Student:
        {student}

        Available programs:
        {programs}

        Use the previous Admission Requirements Agent
        result as context.

        Explain:

        1. Which programs the student appears eligible for.
        2. Which programs the student does not appear eligible for.
        3. The reason for each result.

        Do not invent requirements.
        """,
        expected_output="""
        A clear eligibility assessment with reasons.
        """,
        agent=eligibility_agent,
        context=[requirements_task]
    )

    recommendation_task = Task(
        description="""
        Recommend suitable university programs.

        Student:
        {student}

        Available programs:
        {programs}

        Use the previous eligibility assessment as context.

        Consider:

        - qualification
        - percentage
        - subjects
        - interests

        Recommend programs that appear suitable.
        Explain why each program may be suitable.

        Do not invent admission requirements.
        """,
        expected_output="""
        A list of suitable programs with clear reasons.
        """,
        agent=recommendation_agent,
        context=[eligibility_task]
    )

    advisor_task = Task(
        description="""
        Create the final admission advice.

        Student:
        {student}

        Available programs:
        {programs}

        Use all previous agent results as context.

        Provide:

        1. Student summary
        2. Eligibility results
        3. Recommended programs
        4. Reasons
        5. Important next steps

        Do not invent admission requirements.

        Clearly state that this is an AI assessment
        based on the supplied information and does not
        guarantee university admission.
        """,
        expected_output="""
        A clear and beginner-friendly final admission report.
        """,
        agent=advisor_agent,
        context=[
            requirements_task,
            eligibility_task,
            recommendation_task
        ]
    )

    return (
        requirements_task,
        eligibility_task,
        recommendation_task,
        advisor_task
    )
