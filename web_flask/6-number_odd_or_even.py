#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def is_number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def is_number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def is_number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
