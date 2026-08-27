# mcp-toolbox

MCP server template I base new tools on

## Usage

```bash
# claude_desktop_config.json
# {
#   "mcpServers": {
#     "notes-box": {"command": "python", "args": ["server.py"]}
#   }
# }
python server.py
```

## Getting started

```bash
pip install -r requirements.txt
```

## What it does

- State persisted to a JSON file in the home dir
- Includes Claude Desktop config snippet
- FastMCP style: decorators, zero boilerplate
- Three tools: add / get / list notes

## Project structure

```text
├── docs/
│   ├── configuration.md
│   ├── faq.md
│   └── usage.md
├── examples/
│   └── quickstart.md
├── .gitattributes
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── Makefile
├── SECURITY.md
├── requirements.txt
└── server.py
```

## Development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
```

## License

MIT. Do whatever you want.
