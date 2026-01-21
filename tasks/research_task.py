from crewai import Task

def create_research_task(agent):
    return Task(
        description=(
            "Research exactly 3 recent and practical AI topics suitable "
            "for beginners in 2024–2025."
        ),
        expected_output=(
            "Plain text list of 3 topics. "
            "Each topic includes why it matters and where it is used."
        ),
        agent=agent
    )
