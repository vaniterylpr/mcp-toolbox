import json
import time
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("notes-box")
NOTES = Path.home() / ".mcp_notes.json"


def _load():
    if NOTES.exists():
        return json.loads(NOTES.read_text(encoding="utf-8"))
    return {}


def _save(data):
    NOTES.write_text(json.dumps(data, indent=1), encoding="utf-8")


@mcp.tool()
def add_note(title: str, body: str) -> str:
    # store a note with a title
    data = _load()
    data[title] = {"body": body, "ts": time.time()}
    _save(data)
    return "saved: " + title


@mcp.tool()
def get_note(title: str) -> str:
    # fetch a note by title
    return _load().get(title, {}).get("body", "not found")


@mcp.tool()
def list_notes() -> str:
    # list all note titles
    titles = sorted(_load())
    return "\n".join(titles) if titles else "(empty)"


if __name__ == "__main__":
    mcp.run()
