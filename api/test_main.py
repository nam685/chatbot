import os

from fastapi.testclient import TestClient

os.environ["LANGGRAPH_API_URI"] = "http://localhost:8000"

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello! Welcome to the LangGraph Chat API"}
