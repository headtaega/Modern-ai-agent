Modern AI Agent

A simple Python-based AI coding agent that uses LLM function calling to interact with files, modify code, and execute Python scripts.
Features

    Read and inspect files.
    Create and modify files.
    Execute Python scripts.
    Use LLM function calling to perform tasks.
    Iterative agent execution.

Tech Stack

    Python
    OpenRouter
    OpenAI SDK
    UV

Getting Started

1. Clone the repository
bash

git clone https://github.com/headtaega/Modern-ai-agent.git
cd Modern-ai-agent

2. Install dependencies
bash

uv sync

3. Configure your API key

Create a .env file:
env

OPENROUTER_API_KEY=your_api_key

Get your API key from OpenRouter.
Usage

Run the agent with a natural-language instruction:
bash

uv run main.py "Explain how the calculator works"

Other examples:
bash

uv run main.py "List all files"
uv run main.py "Create a hello.py file"
uv run main.py "Run the calculator"

Enable verbose output:
bash

uv run main.py "Analyze the project" --verbose

Project Structure
text

Modern-ai-agent/
├── calculator/
├── functions/
├── main.py
├── call_function.py
├── config.py
├── prompts.py
├── tests/
├── pyproject.toml
└── README.md

Testing
bash

uv run pytest

License

MIT

Author

@headtaega
