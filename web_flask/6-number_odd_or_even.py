#!/usr/bin/python3
"""
This module contains a dummy flask application
"""

from flask import Flask, render_template
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


@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """
    This collects an argument from the url
    """
    ans = text.replace("_", " ")
    return f"Python {ans}"


@app.route('/number/<int:num>', strict_slashes=False)
def number(num):
    """
    This collects only nums with the url
    """
    return f"{num} is a number"


@app.route('/number_template/<int:num>', strict_slashes=False)
def html_num(num):
    """
    This returns a html file that contains the number
    """ 
    return render_template('5-number.html', num=num)


@app.route('/number_odd_or_even/<int:num>', strict_slashes=False)
def html_EorO(num):
    """
    This returns a html file that contains the number
    """
    num_type = "odd"
    if num % 2 == 0:
        num_type = "even"

    return render_template('6-number_odd_or_even.html', num=num, num_type=num_type)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
