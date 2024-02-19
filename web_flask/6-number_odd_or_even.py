#!/usr/bin/python3
"""Display HBNB within a Flask app"""

from flask import Flask, render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """Display n is a number if n is an integer"""
    try:
        n = int(n)
        return f"{escape(n)} is a number"
    except ValueError:
        return


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display HTML if n is an integer"""
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>",strict_slashes=False)
def odd_or_even(n):
    """Display n is even or n is odd"""
    if n % 2 == 0:
        result = "even"
    else:
        result = "odd"
    return render_template("6-number_odd_or_even.html", n=n, result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
