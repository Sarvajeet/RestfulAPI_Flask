# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:19:59 2019

@author: Sarva
"""

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo", stateless_http=True)

users_dict = {
    "Nicholas": {"age": 42, "occupation": "Network Engineer"},
    "Elvin": {"age": 32, "occupation": "Doctor"},
    "Jass": {"age": 22, "occupation": "Web Developer"}
}

# Add a dynamic greeting resource
@mcp.resource("user://{name}")
def get_user(name: str) -> str:
    """Get a personalized greeting"""
    if name in users_dict:
        user_data = users_dict[name]
        return f"Name: {name}, Age: {user_data['age']}, Occupation: {user_data['occupation']}"
    return "User not found"

import uvicorn

if __name__ == "__main__":
    app = mcp.streamable_http_app()
    uvicorn.run(app, host="127.0.0.1", port=5003)