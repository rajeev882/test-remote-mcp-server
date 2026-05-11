from fastmcp import FastMCP
import random

mcp = FastMCP("simple Calculator Server")

@mcp.tool
def add(a: int, b : int) -> int:
    return a + b

@mcp.tool
def random_number(min_val: int =1 , max_val: int =100) -> int:
    return random.randint(min_val, max_val)


@mcp.resource("info://server_info")
def server_info() -> str:
    return "This is a simple calculator server that can perform addition and generate random numbers."


if __name__ == "__main__":
    mcp.run(transport="http" , host="0.0.0.0", port=8080)

