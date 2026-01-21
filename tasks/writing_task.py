from crewai import Task

def create_writing_task(agent):
    return Task(
        description=(
            "Write a beginner-friendly explanation strictly based "
            "on the provided research."
        ),
        expected_output=(
            "100–120 words. Plain text. No bullet points. No marketing language."
        ),
        agent=agent
    )
