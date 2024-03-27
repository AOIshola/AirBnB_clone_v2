#!/usr/bin/python3
"""Print list of states in the database"""

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)
states = storage.all(State)

@app.route("/states_list", strict_slashes=False)
def list_state():
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def close(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
