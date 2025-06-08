from typing import Annotated

from langgraph.graph.message import add_messages
from pydantic import BaseModel


class State(BaseModel):
    """State for the chatbot application.

    messages: List of messages exchanged in the chat.
    sensitive: Indicates if certain topics (politics, sexual themes,...) should be avoided.
    """

    messages: Annotated[list, add_messages]
    sensitive: bool = False
