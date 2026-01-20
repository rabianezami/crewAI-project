from crewai import Task

def research_ai_topics_task(agent):
    return Task(
        description="""
You are assigned to research recent AI topics suitable for beginners.

OBJECTIVE:
Identify exactly 3 recent and practical AI topics that beginners can realistically start learning in 2024-2025.

CONTEXT:
The output will be used by a writting agent to produce educational content.
Accuracy, clarity, and beginner-friendliness are critical.

RULES & CONSTRAINTS: 
- Do not include advanced mathematical or academic-only topics
- Topics must be actively discussed or used in real-world applications
- Avoid hype-only or speculative research areas
- No marketing language or exaggerated claims
- Use simple, clear language

OUTPUT FORMAT (STRICT):
Return a plain text list in the following format:

1. Topic Name 
     - Why it matters (1 sentence)
     - Where beginners see it used (1 sentence)

LIMITS: 
- Exactly 3 topics 
- Max 120 words total
""",

        agent=agent,
        expected_output="A clean, structured list of 3 beginner-friendly AI topics"
    )
