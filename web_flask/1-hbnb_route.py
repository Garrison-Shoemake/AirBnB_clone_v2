#!/usr/bin/python3
""" this program starts a flask web application """

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return "Hello HBNB!"


@app.route('/hbnb')
def howdy():
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
