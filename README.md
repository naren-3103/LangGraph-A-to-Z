# LangGraph: Basic to Advanced (with Ollama)

A hands-on Jupyter notebook that teaches **LangGraph** from first principles to advanced agent patterns. Every LLM call runs locally through **Ollama**, so no API key is needed.

## What's in this folder

| File | Purpose |
|---|---|
| `LangGraph_Basic_to_Advanced_Ollama.ipynb` | The tutorial notebook (25 parts, run top to bottom) |
| `mcp_math_server.py` | A small MCP server (math + notes tools), written by the notebook's MCP section |
| `mcp_agent_client.py` | A script that connects a LangGraph agent to that MCP server |
| `.vscode/settings.json` | Points VS Code at `.venv` and sets Python type checking to `basic` |
| `.gitignore` | Keeps the venv, caches and generated databases out of git |

## Quick start

1. Install Ollama from https://ollama.com/download, then pull the models:
   ```bash
   ollama pull llama3.1:8b
   ollama pull nomic-embed-text
   ```
2. Create and activate a virtual environment, then install the libraries:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate          # Windows
   pip install langgraph langchain langchain-core langchain-ollama langchain-mcp-adapters mcp pydantic langgraph-checkpoint-sqlite numpy ipykernel
   ```
3. Open the notebook in VS Code, choose **Select Kernel → `.venv`**, and run the cells in order.

To use another model, change `MODEL` in the config cell (Part 0). Small local models sometimes make odd tool calls or routing choices, so re-run a cell if the result looks wrong. A full run takes more than 10 minutes.

## Section guide (one line each)

| # | Section | What happens here
|---|---|---|
| 0 | Setup | Install Ollama, pull the models, install the packages, and check that the LLM answers. |
| 1 | LLM basics with `ChatOllama` | How to call a local model: `invoke`, messages, streaming, batch, prompts and simple chains. |
| 2 | Your first graph | A graph is shared **state**, **nodes** (Python functions) and **edges** (what runs next), compiled into a runnable app. |
| 3 | State deep-dive | Reducers such as `add_messages` decide how a node's update is merged into state, and schemas control what goes in and out. |
| 4 | LLM chatbot graph | Put an LLM call inside a node so the graph becomes a chatbot. |
| 5 | Conditional edges and routing | Let the graph (or an LLM) choose the next node at runtime. |
| 6 | Structured output | Force the model to return a validated Pydantic object instead of free text. |
| 7 | Tools and tool calling | The LLM *requests* a function call, your code runs it, and the result goes back in a loop (the ReAct pattern). |
| 8 | Prebuilt agents | `create_agent` / `create_react_agent` give you the standard tool-calling agent in one line. |
| 9 | Short-term memory | A checkpointer saves state per `thread_id`, giving conversation memory, state inspection and time travel. |
| 10 | Long conversations | Trim or summarize old messages so the chat fits a small model's context window. |
| 11 | Long-term memory | A `Store` keeps facts across conversations, with optional semantic search over embeddings. |
| 12 | Streaming | Watch a run live by streaming state, node updates, LLM tokens or custom progress events. |
| 13 | Human-in-the-loop | `interrupt()` pauses the graph for a human to approve, edit or reject, and `Command(resume=...)` continues it. |
| 14 | `Command` | A node can update state and choose the next node in one return value. |
| 15 | Parallelism and map-reduce | Run branches at the same time, and use `Send` to create as many branches as the data needs. |
| 16 | Subgraphs | Compile a graph and use it as a node inside another graph to build reusable pieces. |
| 17 | Multi-agent systems | A supervisor LLM decides which specialist agent works next. |
| 18 | Agentic workflow patterns | Prompt chaining, generate-and-grade retry loops, and plan-then-execute. |
| 19 | RAG and agentic RAG | Retrieve relevant documents with Ollama embeddings, then let the graph decide, grade and rewrite before answering. |
| 20 | Functional API | Get persistence, streaming and interrupts with plain Python code using `@entrypoint` and `@task`. |
| 21 | Production features | Runtime context, retries, caching, recursion limits, fallback models and a SQLite checkpointer. |
| 22 | MCP integration | Use tools from an MCP server inside a LangGraph agent, so one tool server can be reused across apps. |
| 23 | Async and deployment | Run many graphs concurrently with `ainvoke` and serve them with the LangGraph CLI or your own API. |
| 24 | Cheat sheet and exercises | A quick reference of the main APIs plus practice tasks, ending with a capstone project. |

## Tools vs MCP

A **tool** is a function the LLM can call, defined inside your app. **MCP** is a standard protocol for serving tools (and resources and prompts) from a separate process, so the same tool works in any MCP-aware app or language. The notebook's Part 22 turns MCP tools into ordinary LangChain tools, so the agent treats them the same way.

## Notes

- The notebook writes `mcp_math_server.py` and `mcp_agent_client.py` itself. The SQLite demo in Part 21 creates `langgraph_checkpoints.db`, which is ignored by git.
- MCP stdio inside Jupyter on Windows needs the real process stderr (`sys.__stderr__`), which the notebook's MCP cell already passes.
