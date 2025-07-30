from mcp.server.fastmcp import FastMCP
import httpx

# Create an MCP server
mcp = FastMCP("Demo", stateless_http=True)

from mcp.model import Resource, Tool

@mcp.resource("user://{name}", title="Get User")
async def get_user(name: str) -> dict:
    """Get a personalized greeting"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://127.0.0.1:5003/user/{name}")
        if response.status_code == 200:
            return response.json()
        return {"error": "User not found"}

@mcp.list_resources()
async def list_resources() -> list[Resource]:
    """List available resources."""
    return [
        Resource(
            uri="user://Nicholas",
            title="Nicholas",
        ),
        Resource(
            uri="user://Elvin",
            title="Elvin",
        ),
        Resource(
            uri="user://Jass",
            title="Jass",
        ),
    ]

@mcp.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="get_user",
            title="Get User",
            description="Get user information",
        )
    ]

if __name__ == "__main__":
    import uvicorn
    print(dir(mcp))
    uvicorn.run("McpServer:mcp.streamable_http_app()", host="127.0.0.1", port=8080, reload=True)
