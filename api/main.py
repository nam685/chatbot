from fastapi import FastAPI
from langgraph_sdk import get_client
from pydantic import BaseModel

app = FastAPI()

langgraph_client = get_client(url="http://langgraph-api:8000")


class ChatMessage(BaseModel):
    text: str
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "Hello",
                }
            ]
        }
    }


class HumanReview(BaseModel):
    action: str
    data: str
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "action": "feedback",
                    "data": "That's not what I meant! Please try again.",
                },
                {
                    "action": "continue",
                    "data": "",
                },
            ]
        }
    }


@app.get("/")
async def read_main():
    return {"msg": "Hello! Welcome to the LangGraph Chat API"}


@app.get("/chat")
async def list_chat_threads():
    """
    List all chat threads.
    """
    return await langgraph_client.threads.search(
        metadata={"graph_id": "chat"},
    )


@app.get("/chat/{thread_id}")
async def get_chat_history(thread_id: str):
    """
    Get the chat history for the given thread.
    """
    return await langgraph_client.threads.get(thread_id=thread_id)


@app.post("/chat/{thread_id}")
async def chat_with_thread(thread_id: str, message: ChatMessage):
    """
    Take message from user and return response from chatbot.
    If chat thread does not exist, create a new thread.
    """
    return await langgraph_client.runs.wait(
        thread_id=thread_id,
        assistant_id="chat",
        input={"messages": [{"role": "user", "content": message.text}]},
        if_not_exists="create",
    )


@app.post("/chat/{thread_id}/human_review")
async def human_review(thread_id: str, review: HumanReview):
    """
    Submit human review to resume interrupted thread.
    """
    return await langgraph_client.runs.wait(
        thread_id=thread_id,
        assistant_id="chat",
        command={
            "resume": {
                "action": review.action,
                "data": review.data,
            }
        },
    )
