from typing import Literal

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import ToolNode
from langgraph.types import Command, interrupt

from .state import State
from .tools import multiply, search

llm = init_chat_model("gpt-4o-mini")
llm_with_tools = llm.bind_tools([multiply, search])


def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state.messages)]}


def classify_sensitivity(state: State) -> dict[str, bool]:
    prompt = [
        SystemMessage(
            content="Determine if the conversation topic is sensitive (political, sexual theme,...). Return True or False."
        ),
        state.messages[-1],
        HumanMessage(content="Is this topic sensitive? Respond with True or False."),
    ]
    response = llm.invoke(prompt)
    sensitive = response.text().strip().lower() == "true"
    return {"sensitive": sensitive}


tool_node = ToolNode(tools=[multiply, search], name="tools")


def human_review_node(state: State) -> Command[Literal["chatbot", "tools"]]:
    last_message = state.messages[-1]
    tool_call = last_message.tool_calls[-1]

    human_review = interrupt(
        {
            "question": "Is this correct?",
            "tool_call": tool_call,
        }
    )
    review_action = human_review["action"]
    review_data = human_review.get("data")

    if review_action == "feedback":
        tool_message = {
            "role": "tool",
            "content": review_data,
            "name": tool_call["name"],
            "tool_call_id": tool_call["id"],
        }
        return Command(goto="chatbot", update={"messages": [tool_message]})
    else:  # review_action == "continue":
        return Command(goto="tools")
