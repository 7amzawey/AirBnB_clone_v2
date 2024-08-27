#!/usr/bin/python3
"""
Start a Flask web appliction.
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/airbnb-onepage', strict_slashes=False)
def hello_again():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
