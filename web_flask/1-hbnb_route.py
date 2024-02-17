#!/usr/bin/python3
"""A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
/: display “Hello HBNB!”
/hbnb: display “HBNB”
"""
from flask import Flask

web_flask = Flask(__name__)

@web_flask.route('/', strict_slashes=False)
def homepage():
    return "Hello HBNB!"

@web_flask.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

if __name__ == "__main__":
    web_flask.run(debug=None, port=5000, host="0.0.0.0")
