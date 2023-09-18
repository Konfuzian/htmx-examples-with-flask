
# Description

Here, I implemented the examples from https://htmx.org/examples/ as a Flask app.

Most of the backend code is implemented using Blueprints and found in the `blueprints` directory.

For each example, there is a Python file in that directory, and a folder in the `templates` directory for the HTML.

# Instructions

## Setup

Create the virtual environment:

`python -m venv env`


Activate the virtual environment (Windows):

`.\env\Scripts\activate`


Install the packages:

`pip install -r requirements.txt`

## Running the server

Activate the virtual environment (Windows):

`.\env\Scripts\activate`


Run the server (with auto reload and debugging):

`python app.py --debug`


The server will run on http://127.0.0.1:5000.
