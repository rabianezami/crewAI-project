from crewai import Task

def create_editing_task(agent):
    return Task(
        description=(
            "Edit the text to improve clarity and natural tone "
            "without changing meaning."
        ),
        expected_output=(
            "Single clean paragraph. Plain text only."
        ),
        agent=agent
    )
