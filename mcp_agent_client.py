import asyncio
import sys

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_ollama import ChatOllama

MODEL = sys.argv[1] if len(sys.argv) > 1 else "llama3.1:8b"


def make_agent(model, tools, system_prompt):
    try:
        from langchain.agents import create_agent
        return create_agent(model, tools, system_prompt=system_prompt)
    except ImportError:
        from langgraph.prebuilt import create_react_agent
        return create_react_agent(model, tools, prompt=system_prompt)


async def main():
    client = MultiServerMCPClient({
        "math": {"command": sys.executable, "args": ["mcp_math_server.py"], "transport": "stdio"},
        # Example HTTP server:
        # "weather": {"url": "http://localhost:8000/mcp", "transport": "streamable_http"},
    })
    tools = await client.get_tools()
    print("MCP tools:", [t.name for t in tools])

    agent = make_agent(ChatOllama(model=MODEL, temperature=0), tools,
                       "You are a helpful assistant. Use the MCP tools for maths and notes.")
    result = await agent.ainvoke({"messages": [{"role": "user", "content": "What is 2 to the power of 10, plus 24?"}]})
    for m in result["messages"]:
        m.pretty_print()


if __name__ == "__main__":
    asyncio.run(main())
