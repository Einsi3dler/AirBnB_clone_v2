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
    val = f"""<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: {num}</H1>
    </BODY>
</HTML>"""
    with open("templates/5-number.html", "w") as f:
        f.write(val)
    
    return render_template('5-number.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
