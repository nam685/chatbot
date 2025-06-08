from typing import Literal

from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph

from chatbot.utils.nodes import (
    chatbot,
    classify_sensitivity,
    human_review_node,
    tool_node,
)
from chatbot.utils.state import State

load_dotenv()


def route_after_chatbot(state: State) -> Literal[END, "human_review", "tools"]:  # type: ignore
    if len(state.messages[-1].tool_calls) == 0:
        return END
    elif state.sensitive:
        return "human_review"
    else:
        return "tools"


graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("human_review", human_review_node)
graph_builder.add_node("tools", tool_node)
graph_builder.add_node("classify_sensitivity", classify_sensitivity)

graph_builder.add_edge(START, "classify_sensitivity")
graph_builder.add_edge("classify_sensitivity", "chatbot")
graph_builder.add_conditional_edges(
    "chatbot",
    route_after_chatbot,
)
graph_builder.add_edge("tools", "chatbot")

memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)

graph.get_graph().print_ascii()
