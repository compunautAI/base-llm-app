# 🧠 LLM Starter Agent (Ollama + LangChain CLI)

This is a minimal template for building local, containerized LLM apps using [Ollama](https://ollama.com) and [LangChain](https://www.langchain.com/). We will use this as the base of our AI Agent application. Feel free to use this code to start your own project!

---

## 🛠 Features

- Python CLI chatbot using local LLM (e.g. Qwen 2.5)
- venv for standardized environment
- Dockerized for reproducibility & scalability
- Base project: can be extended with memory, prompt chaining, RAG, etc.

---

## Run Locally

Make sure [Ollama is installed](https://ollama.com/download) and the model (e.g. `qwen2.5:1.5b`) is pulled:

### Installing Ollama locally

Install for Mac

```bash
brew install ollama
```

Install for Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Using ollama & downloading foundational model

start up ollama

```bash
ollama serve
```

download the llm you want to use

```bash
ollama pull qwen2.5:1.5b
```

### Installing the applcation

In your command line, run the following

Download the code from github

```bash
git clone https://github.com/yourname/llm-starter-agent.git
```

move into the project directory

```bash
cd base-llm-app
```

### Once in the project directory, set up the same environment

Create virtual environment

```bash
python -m venv .venv
```

Activate it

```bash
source .venv/bin/activate
```

Install the necessary dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```

## Run with Docker

```docker
docker build -t llm-agent .
docker run -it llm-agent
```
