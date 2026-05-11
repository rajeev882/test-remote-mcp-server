"""
===========================================================================================
FastMCP Example Server
===========================================================================================

This example demonstrates how to build a very simple MCP (Model Context Protocol) server
using FastMCP.

The server exposes:
1. Tools
   - add()              -> performs addition
   - random_number()    -> generates random numbers

2. Resources
   - server_info()      -> returns metadata/information about the server

The MCP server can then be connected to:
- ChatGPT
- Claude Desktop
- Cursor
- Qwen
- VS Code AI Agents
- Any MCP-compatible client

===========================================================================================
What is MCP?
===========================================================================================

MCP (Model Context Protocol) is a standard protocol that allows AI models to:
- discover tools
- call functions
- access resources
- interact with external systems

Think of MCP as:
    "REST APIs for AI agents"

Instead of exposing HTTP endpoints directly to humans/apps,
we expose AI-friendly tools and resources.

===========================================================================================
"""

# Import FastMCP framework
#
# FastMCP is the main framework used to create MCP servers.
#
# It provides:
# - Tool registration
# - Resource registration
# - MCP protocol handling
# - HTTP / stdio transports
# - AI-agent compatibility
#
from fastmcp import FastMCP


# Import Python's built-in random module
#
# This module is used for generating random numbers.
#
import random


# Create an MCP server instance
#
# FastMCP("simple Calculator Server")
#
# The string passed here is the server name.
#
# This name is visible to:
# - AI clients
# - MCP inspectors
# - Debug tools
# - IDE integrations
#
# Think of this like:
#   SpringBootApplication name
# or
#   Service/Application identifier
#
mcp = FastMCP("simple Calculator Server")


# =========================================================================================
# TOOL 1 : ADDITION TOOL
# =========================================================================================

# @mcp.tool
#
# This decorator converts the Python function into an MCP Tool.
#
# MCP tools are callable functions that AI agents can invoke automatically.
#
# Once registered:
# - AI models can discover this tool
# - understand its parameters
# - call it automatically
#
# The function name becomes the tool name.
#
# Tool Name:
#   add
#
# AI clients will see metadata like:
#
# {
#   "name": "add",
#   "parameters": {
#       "a": "integer",
#       "b": "integer"
#   }
# }
#
@mcp.tool
def add(a: int, b: int) -> int:
    """
    Add two integers and return the result.

    Parameters:
        a (int): First number
        b (int): Second number

    Returns:
        int: Sum of a and b

    Example:
        add(10, 20) -> 30
    """

    # Return the sum of two numbers
    return a + b


# =========================================================================================
# TOOL 2 : RANDOM NUMBER GENERATOR
# =========================================================================================

# Another MCP tool.
#
# This tool generates a random integer between:
# - min_val
# - max_val
#
# Default values:
#   min_val = 1
#   max_val = 100
#
# This means AI agents can call:
#
#   random_number()
#
# OR
#
#   random_number(10, 500)
#
@mcp.tool
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """
    Generate a random integer between min_val and max_val.

    Parameters:
        min_val (int): Minimum value (default = 1)
        max_val (int): Maximum value (default = 100)

    Returns:
        int: Random integer

    Example:
        random_number() -> 42
        random_number(10, 20) -> 13
    """

    # random.randint(a, b)
    #
    # Returns a random integer N such that:
    #
    #   a <= N <= b
    #
    return random.randint(min_val, max_val)


# =========================================================================================
# MCP RESOURCE
# =========================================================================================

# @mcp.resource(...)
#
# Resources are different from tools.
#
# Tools:
#   - perform actions
#   - execute logic
#   - accept parameters
#
# Resources:
#   - expose information/data
#   - similar to readonly documents
#   - usually do not perform business actions
#
# Resource URI:
#   info://server_info
#
# Think of it like:
#   metadata endpoint
# or
#   readonly information source
#
# AI models can read this resource to understand:
# - server purpose
# - available capabilities
# - documentation
#
@mcp.resource("info://server_info")
def server_info() -> str:
    """
    Returns information about this MCP server.

    Returns:
        str: Description of server capabilities
    """

    return (
        "This is a simple calculator server that can perform "
        "addition and generate random numbers."
    )


# =========================================================================================
# APPLICATION ENTRY POINT
# =========================================================================================

# __name__ == "__main__"
#
# This condition ensures that:
#
# - the server starts ONLY when this file is directly executed
# - the server does NOT auto-start when imported as a module
#
# Similar to:
#
#   public static void main(String[] args)
#
# in Java.
#
if __name__ == "__main__":

    # Start the MCP server
    #
    # mcp.run(...)
    #
    # This launches the FastMCP runtime.
    #
    # =====================================================================================
    # TRANSPORT
    # =====================================================================================
    #
    # transport="http"
    #
    # Starts the server using HTTP transport.
    #
    # This makes the MCP server remotely accessible.
    #
    # Other possible transports:
    #
    # - "stdio"
    #       Used for local desktop integrations
    #       Example:
    #           Claude Desktop
    #           Cursor
    #
    # - "http"
    #       Used for remote/cloud deployment
    #
    # =====================================================================================
    # HOST
    # =====================================================================================
    #
    # host="0.0.0.0"
    #
    # Means:
    #   listen on all network interfaces
    #
    # Important for:
    # - Docker
    # - Kubernetes
    # - Remote deployment
    # - Cloud hosting
    #
    # If you use:
    #
    #   host="127.0.0.1"
    #
    # then only local machine access is allowed.
    #
    # =====================================================================================
    # PORT
    # =====================================================================================
    #
    # port=8080
    #
    # HTTP server port.
    #
    # Final MCP endpoint typically becomes:
    #
    #   http://localhost:8080/mcp
    #
    # =====================================================================================
    #
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8080
    )


"""
===========================================================================================
How To Run This Server
===========================================================================================

1. Install dependencies

    pip install fastmcp

OR

    uv add fastmcp


===========================================================================================
Run the Server
===========================================================================================

Using uv:

    uv run python main.py

OR

    uv run fastmcp run main.py


===========================================================================================
Test With Inspector
===========================================================================================

Start inspector:

    uv run fastmcp dev

Then connect to:

    http://localhost:8080/mcp


===========================================================================================
Example AI Tool Calls
===========================================================================================

AI agent may invoke:

    add(a=10, b=20)

Result:

    30


AI agent may invoke:

    random_number(min_val=1, max_val=50)

Result:

    27


===========================================================================================
Architecture
===========================================================================================

        AI Client
            ↓
       MCP Protocol
            ↓
       FastMCP Server
            ↓
         Python Code


===========================================================================================
"""