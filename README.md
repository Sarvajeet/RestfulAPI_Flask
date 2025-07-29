# MCP Agent Configuration

This document describes how to configure and run the MCP agent.

## Prerequisites

- Python 3.10 or later
- pip

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd <project-directory>
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Applications

1. Start the REST API:
   ```
   python RestApi.py
   ```
2. Start the MCP server:
   ```
   python McpServer.py
   ```

## Testing the MCP Server

You can test the MCP server by sending a POST request to `http://127.0.0.1:8080/mcp`.

Example using `curl`:
```
curl -X POST -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" -d '{"jsonrpc": "2.0", "method": "resources/read", "params": {"uri": "user://Nicholas"}, "id": 1}' http://127.0.0.1:8080/mcp
```
