#!/usr/bin/python3
""" this program starts a flask web application """

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return "Hello HBNB!"


@app.route('/hbnb')
def howdy():
    return "HBNB"


@app.route('/c/<text>')
def bonjour(text):
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python/')
@app.route('/python/<text>')
def hola(text="is cool"):
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>')
def ni_hao(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def privet(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def aloha(n):
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
