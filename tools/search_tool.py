from crewai.tools import BaseTool
from typing import Type 
from pydantic import BaseModal, Field
from crewai_tools import SerperDevTool
from config.settings import SERPER_MAX_RESULTS

class SearchInput(BaseModal):
    query: str = Field(..., description="Search query")

class SearchTool(BaseModal):
    name = "web_search"
    description = "Search the web for up-to-date information"
    args_schema: Type[BaseModal] = SearchInput

    def _run(self, query: str) -> str:
        tool = SerperDevTool(
            n_results=SERPER_MAX_RESULTS,
            search_type="search"
        )

        return tool.run(query)