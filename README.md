# 🚀 FastMCP Simple Calculator Server

A beginner-friendly MCP (Model Context Protocol) server built using FastMCP.

This project demonstrates how to:

- Create MCP tools
- Expose AI-callable functions
- Register MCP resources
- Run MCP server over HTTP
- Connect AI agents like ChatGPT, Claude, Cursor, and Qwen

---

# 📌 What is MCP?

MCP (Model Context Protocol) is a standard that allows AI models to interact with external tools and systems.

Think of MCP as:

```text
REST APIs for AI Agents
```

Instead of humans calling APIs directly:

```text
Frontend → REST API
```

AI agents call MCP tools:

```text
AI Agent → MCP Tool
```

---

# 🏗️ Project Architecture

```text
 ┌─────────────────────┐
 │   AI Client/Agent   │
 │---------------------│
 │ ChatGPT / Claude    │
 │ Cursor / Qwen       │
 └─────────┬───────────┘
           │
           │ MCP Protocol
           ▼
 ┌─────────────────────┐
 │    FastMCP Server   │
 │---------------------│
 │  add()              │
 │  random_number()    │
 │  server_info()      │
 └─────────┬───────────┘
           │
           │ Python Function Calls
           ▼
 ┌─────────────────────┐
 │    Python Runtime   │
 │---------------------│
 │ random.randint()    │
 │ arithmetic logic    │
 └─────────────────────┘
```

---

# 📂 Project Structure

```text
project/
│
├── main.py
├── README.md
└── pyproject.toml
```

---

# ⚙️ Features

## ✅ MCP Tools

### 1. add()

Adds two numbers.

Example:

```python
add(10, 20)
```

Result:

```text
30
```

---

### 2. random_number()

Generates random numbers.

Example:

```python
random_number(1, 100)
```

Result:

```text
57
```

---

# 📚 MCP Resources

## server_info()

Provides metadata about the MCP server.

Resource URI:

```text
info://server_info
```

---

# 🧠 Complete Source Code

```python
from fastmcp import FastMCP
import random

# Create MCP server
mcp = FastMCP("simple Calculator Server")


# MCP Tool 1
@mcp.tool
def add(a: int, b: int) -> int:
    return a + b


# MCP Tool 2
@mcp.tool
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    return random.randint(min_val, max_val)


# MCP Resource
@mcp.resource("info://server_info")
def server_info() -> str:
    return (
        "This is a simple calculator server "
        "that can perform addition and generate random numbers."
    )


# Start server
if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8080
    )
```

---

# 🔥 How MCP Flow Works

## Step 1 — AI Agent Discovers Tools

When an AI client connects:

```text
http://localhost:8080/mcp
```

FastMCP exposes metadata like:

```json
{
  "tools": [
    {
      "name": "add",
      "parameters": {
        "a": "integer",
        "b": "integer"
      }
    }
  ]
}
```

---

## Step 2 — AI Understands Tool Purpose

The AI model learns:

- Tool name
- Input parameters
- Return types
- Descriptions

---

## Step 3 — AI Invokes Tool

AI agent sends:

```json
{
  "tool": "add",
  "arguments": {
    "a": 10,
    "b": 20
  }
}
```

---

## Step 4 — FastMCP Executes Python Function

```python
return a + b
```

---

## Step 5 — Response Returned to AI

```json
{
  "result": 30
}
```

---

# 🛠️ Installation

## Using pip

```bash
pip install fastmcp
```

---

## Using uv (Recommended)

```bash
uv add fastmcp
```

---

# ▶️ Running the MCP Server

## Option 1 — Using Python

```bash
python main.py
```

---

## Option 2 — Using uv

```bash
uv run python main.py
```

---

## Option 3 — Using FastMCP CLI

```bash
uv run fastmcp run main.py
```

---

# 🌐 MCP Endpoint

Once started:

```text
http://localhost:8080/mcp
```

---

# 🧪 Testing with FastMCP Inspector

Start inspector:

```bash
uv run fastmcp dev
```

Open browser:

```text
http://127.0.0.1:6274
```

Connect using:

```text
Transport: HTTP
URL: http://localhost:8080/mcp
```

---

# 🧭 Tool Discovery Example

The inspector will show:

```text
Tools:
 - add
 - random_number

Resources:
 - info://server_info
```

---

# 📡 HTTP Flow Diagram

```text
┌──────────────┐
│ AI Client    │
└──────┬───────┘
       │ HTTP/MCP Request
       ▼
┌──────────────────────┐
│ FastMCP HTTP Server  │
│ localhost:8080/mcp   │
└─────────┬────────────┘
          │
          ▼
┌──────────────────────┐
│ MCP Tool Dispatcher  │
└─────────┬────────────┘
          │
          ▼
┌──────────────────────┐
│ Python Function      │
│ add()                │
│ random_number()      │
└─────────┬────────────┘
          │
          ▼
┌──────────────────────┐
│ Response Returned    │
└──────────────────────┘
```

---

# 🔄 Difference Between REST API and MCP

| REST API | MCP |
|---|---|
| Built for applications | Built for AI agents |
| Frontend calls APIs | AI calls tools |
| Endpoint-based | Tool-based |
| Swagger/OpenAPI | MCP metadata |
| Human-designed flow | AI-driven flow |

---

# 🧠 Why FastMCP is Powerful

FastMCP allows you to:

- Convert Python functions into AI tools
- Make existing services AI-ready
- Build autonomous AI workflows
- Connect enterprise systems to LLMs
- Expose business logic safely to AI agents

---

# 🏢 Real Enterprise Architecture

```text
                ┌──────────────────┐
                │  ChatGPT/Claude  │
                └────────┬─────────┘
                         │
                    MCP Protocol
                         │
                         ▼
               ┌─────────────────┐
               │   FastMCP Layer │
               └────────┬────────┘
                        │
              REST / DB / Kafka
                        │
                        ▼
         ┌──────────────────────────┐
         │ Existing Microservices   │
         │ Spring Boot / Node / Go  │
         └──────────────────────────┘
```

---

# 🚀 Future Improvements

You can extend this server with:

- Database access
- REST API integrations
- Kafka producers/consumers
- Redis cache
- Elasticsearch
- AI workflows
- Authentication
- Streaming responses

---

# 📖 Useful Commands

## List tools

```bash
uv run fastmcp list main.py
```

---

## Inspect server

```bash
uv run fastmcp inspect main.py
```

---

## Run server

```bash
uv run fastmcp run main.py
```

---

# 🎯 Summary

This project demonstrates:

✅ MCP fundamentals  
✅ FastMCP server creation  
✅ Tool registration  
✅ Resource registration  
✅ HTTP transport  
✅ AI tool execution flow  
✅ Remote MCP architecture  

---

# 📚 Learn More

- FastMCP
- MCP Protocol
- AI Agents
- Tool Calling
- Autonomous Workflows
- Agentic AI Systems

---

# ⭐ Final Thought

Traditional systems were designed for humans.

MCP systems are designed for AI agents.

FastMCP helps bridge that gap beautifully.