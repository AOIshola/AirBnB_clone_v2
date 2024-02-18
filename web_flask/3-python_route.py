#!/usr/bin/python3
"""Display HBNB within a Flask app"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display Hello HBNB!"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_is(text):
    """Display C + <text>"""
    text = text.replace("_", " ")
    return f"C {escape(text)}"

@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_text(text="is cool"):
    """Display Python + <text>"""
    text = text.replace("_", " ")
    return f"Python {escape(text)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
