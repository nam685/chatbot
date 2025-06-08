import pytest
from pydantic import ValidationError

from chatbot.utils.state import State


def test_state_accepts_valid_messages():
    valid_messages = [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there!"},
    ]
    state = State(messages=valid_messages)
    assert state.messages == valid_messages


def test_state_messages_type_enforced():
    with pytest.raises(ValidationError):
        State(messages="not a list")  # type: ignore
