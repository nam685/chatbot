from langchain_core.tools import tool
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field


class MultiplyInputSchema(BaseModel):
    """Multiply two numbers"""

    a: int = Field(description="First operand")
    b: int = Field(description="Second operand")


@tool("multiply_tool", args_schema=MultiplyInputSchema)
def multiply(a: int, b: int) -> int:
    return a * b


search = TavilySearch(max_results=2)
