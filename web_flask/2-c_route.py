#!/usr/bin/python3
"""
This module contains a dummy flask application
"""

from flask import Flask
app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """
    This function defines what the flask app returnes
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This directs the requests to return hbnb
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cis(text):
    """
    This collects an argument attaches to the curl
    """
    ans = text.replace("_", " ")
    return f"C {ans}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
