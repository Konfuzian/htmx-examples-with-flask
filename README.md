# HTMX Examples with Flask

Here, I implemented the examples from <https://htmx.org/examples/> as a Flask app.

Most of the backend code is implemented using Blueprints and found in the
`examples/blueprints` directory.

For each example, there is a Python file in that directory, and a folder in the
`examples/templates` directory for the HTML.

## Setup

```shell
poetry install
```

## Usage

Run the server (with auto reload and debugging):

```shell
poetry run server --debug
```

The server will run on <http://127.0.0.1:5000>.
