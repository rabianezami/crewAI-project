from crewai import Task
writing_task = Task(
    description=(
        "Write a short, clear explanation based strictly on the provided  research. "
        "The content must be suitable for beginners with no prior AI background."
    ),

    expected_output=(
        "A concise plain-text explanation (100-120 words).\n"
        "No bullet points.\n"
        "No marketing language.\n"
        "No additional facts beyond the input."
    ),

    agent=None
)
