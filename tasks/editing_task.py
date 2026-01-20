from crewai import Task 
from agents.editor import editor_agent

editing_task = Task(
    decription=(
       "Review and refine the provided text to improve clarity, readability, "
       "and natural human tone. Remove any robotic or AI-like phrasing while "
       "preserving the original meaning and intent."
    ),

    agent=editor_agent,

    expected_output=(
        "A single clean, natural-sounding paragraph written in plain text. "
        "The content must feel human-written, clear, and concise. "
        "No headings, bullet points, explanations, or formatting."
    )
)