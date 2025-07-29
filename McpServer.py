from mcp.server.fastmcp import FastMCP
import httpx

# Create an MCP server
mcp = FastMCP("Demo", stateless_http=True)

@mcp.resource("user://{name}")
async def get_user(name: str) -> str:
    """Get a personalized greeting"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://127.0.0.1:5003/user/{name}")
        if response.status_code == 200:
            user_data = response.json()
            return f"Name: {user_data['name']}, Age: {user_data['age']}, Occupation: {user_data['occupation']}"
        return "User not found"

if __name__ == "__main__":
    import uvicorn
    app = mcp.streamable_http_app()
    uvicorn.run(app, host="127.0.0.1", port=8080)
