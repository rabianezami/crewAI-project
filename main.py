from dotenv import load_dotenv
load_dotenv()

import json
from crewai import Crew
from langchain_openai import ChatOpenAI

from config.logger import logger
from config.settings import MAX_TOKENS, TEMPERATURE

from agents.researcher import create_researcher_agent
from agents.writer import create_writer_agent
from agents.editor import create_editor_agent

from tasks.research_task import create_research_task
from tasks.writing_task import create_writing_task
from tasks.editing_task import create_editing_task


def main():
    try:
        logger.info("Starting CrewAI pipeline")

        llm = ChatOpenAI(
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS
        )

        researcher = create_researcher_agent()
        writer = create_writer_agent()
        editor = create_editor_agent()

        tasks = [
            create_research_task(researcher),
            create_writing_task(writer),
            create_editing_task(editor)
        ]

        crew = Crew(
            agents=[researcher, writer, editor],
            tasks=tasks,
            llm=llm,
            verbose=True
        )

        result = crew.kickoff()

        with open("output/result.txt", "w", encoding="utf-8") as f:
            f.write(str(result))

        logger.info("Pipeline completed successfully")

    except Exception as e:
        logger.exception(f"Pipeline failed: {e}")

if __name__ == "__main__":
    main()
