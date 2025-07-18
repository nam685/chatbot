# chatbot

This is a hands-on project to learn to create chatbot agent using LangChain & LangGraph.
Use hatch package manager

Based on gpt-4o-mini LLM model, with added features:
- Tool calling: multiply tool, web search tool
- Memory: short term memory from conversation thread
- Human-in-the-loop: verify tool call before executing, in case conversational topic is sensitive
- State: add custom state "sensitivity", indicating if conversation topic is sensitive or not

Agent architecture: use 2 chat models for separation of concern
- Helper model to classify if conversation is sensitive or not
- Main model equiped with tools

I also made FastAPI backend and NextJS frontend to interact with chatbot
Deploy chatbot as standalone container via LangGraph Platform

Deploy to AWS ECS as separate services
Current deployment's URL: http://chatbot-alb-468353364.eu-central-1.elb.amazonaws.com/
(I don't keep this URL if I take it down, because I don't pay money for a fixed one))

[![PyPI - Version](https://img.shields.io/pypi/v/chatbot.svg)](https://pypi.org/project/chatbot)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/chatbot.svg)](https://pypi.org/project/chatbot)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

PyPI package: https://pypi.org/project/chatbot_nam685/

```console
pip install chatbot_nam685
```

## License

`chatbot_nam685` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
