from dotenv import load_dotenv
load_dotenv()

import json
from config.logger import logger
from agents.researcher import create_researcher_agent
from agents.writer import writer_agent
from agents.editor import editor_agent
from crewai import Crew  # <-- اینجا تغییر دادیم
from config.settings import MAX_TOKENS, SERPER_MAX_RESULTS


OUTPUT_FILE_TXT = "output/results.txt"
OUTPUT_FILE_JSON = "output/result.json"

def main():
    try: 
        logger.info("Starting CrewAI pipeline")

        # Initialize Agents with their own prompts, rules, and token limits
        researcher = create_researcher_agent(
           max_results=SERPER_MAX_RESULTS,
           token_limit=MAX_TOKENS
        )
        writer = writer_agent(token_limit=MAX_TOKENS)
        editor = editor_agent(token_limit=MAX_TOKENS)

        # Chain agents in order
        agent_pipeline = [researcher, writer, editor]
 
        # Execute the pipeline using Crew orchestration
        crew = Crew(
            agents=agent_pipeline,
            verbose=True
        )

        structured_output = crew.run(
            return_structured=True  
        )
        logger.info("Pipeline executed successfully.")

        # Save JSON output
        with open(OUTPUT_FILE_JSON, "w", encoding="utf-8") as f:
            json.dump(structured_output, f, indent=2, ensure_ascii=False)
        logger.info(f"JSON output saved: {OUTPUT_FILE_JSON}")

        # Save TXT output
        final_text = "\n\n".join(
            [f"=== {agent} ===\n{content}" for agent, content in structured_output.items()]
        )
        with open(OUTPUT_FILE_TXT, "w", encoding="utf-8") as f:
            f.write(final_text)
        logger.info(f"🔹 TXT output saved: {OUTPUT_FILE_TXT}")

    except Exception as e:
        logger.exception(f"❌ Pipeline failed: {e}")

if __name__ == "__main__":
    main()
