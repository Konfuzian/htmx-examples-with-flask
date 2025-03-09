# HTMX Examples with Flask

Here, I implemented the examples from <https://htmx.org/examples/> as a Flask app.

## Setup

```shell
uv init
uv sync
```

## Usage

Run the server (with auto reload and debugging):

```shell
uv run -m app --debug
```

## Development

Use these tools before pushing to the repo:

```shell
uvx isort src && uvx black src --line-length 100 && uvx ruff check src --fix && uvx djlint --extension=j2 src --reformat
```

The server will run on <http://127.0.0.1:5000>.
