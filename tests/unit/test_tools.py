import pytest
from pydantic import ValidationError

from chatbot.utils.tools import multiply


def test_multiply_function():
    result = multiply.invoke({"a": 3, "b": 4})
    assert result == 12
