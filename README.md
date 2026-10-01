# 🎓 Pakistan University Admission Advisor

A beginner-friendly Multi-Agent University Admission System.

## Technologies

- Python
- CrewAI
- Groq
- GPT-OSS 120B
- Streamlit

## Agents

The application uses four agents:

### 1. Admission Requirements Agent

Checks the admission requirements for university programs.

### 2. Eligibility Agent

Checks whether the student appears to meet those requirements.

### 3. Program Recommendation Agent

Suggests suitable programs based on the student's background and interests.

### 4. Final Admission Advisor

Combines all previous results into a final student-friendly assessment.

## Workflow

Student
↓
Requirements Agent
↓
Eligibility Agent
↓
Recommendation Agent
↓
Final Advisor
↓
Streamlit Result

## Deployment

The application is designed to be deployed using Streamlit Community Cloud.

Add the following secret:

GROQ_API_KEY

## Important

The admission requirements included in this project are demo requirements for educational purposes.

For real admission decisions, requirements should be verified from the official university sources.
