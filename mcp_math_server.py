from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MathAndNotes")
NOTES: dict[str, str] = {}


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent."""
    return base ** exponent


@mcp.tool()
def save_note(title: str, content: str) -> str:
    """Save a note with a title."""
    NOTES[title] = content
    return f"Saved note '{title}'."


@mcp.tool()
def list_notes() -> str:
    """List all saved note titles."""
    return ", ".join(NOTES) or "No notes yet."


if __name__ == "__main__":
    mcp.run(transport="stdio")
