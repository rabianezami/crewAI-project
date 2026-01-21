from crewai import Agent

def create_editor_agent():
    return Agent(
        role="Content Editor",
        goal=(
            "Improve clarity and natural tone while preserving "
            "the original meaning."
        ),
        backstory=(
            "You are a senior editor focused on making AI-generated "
            "content sound human and readable."
        ),
        rules=[
            "Do not delegate tasks to other agents under any circumstances."
            "Do not add new information",
            "Do not change meaning",
            "Remove robotic phrasing",
            "Keep sentences short and direct"
        ],
        verbose=True
    )
