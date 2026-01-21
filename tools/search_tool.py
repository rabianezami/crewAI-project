from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from crewai_tools import SerperDevTool
from config.settings import SERPER_MAX_RESULTS

class SearchInput(BaseModel):
    query: str = Field(..., description="Search query")

class SearchTool(BaseTool):
    name = "web_search"
    description = "Search the web for recent information"
    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str) -> str:
        tool = SerperDevTool(n_results=SERPER_MAX_RESULTS)
        return tool.run(query)
