#!/usr/bin/python3
"""A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text
  (replace underscore _ symbols with a space)
/python/<text>: display “Python ”, followed by the value of the text
   (replace underscore _ symbols with a space)
   The default value of text is “is cool”
"""
from flask import Flask

web_flask = Flask(__name__)

@web_flask.route('/', strict_slashes=False)
def homepage():
    return "Hello HBNB!"



@web_flask.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@web_flask.route('/c/<text>', strict_slashes=False)
def ctext(text):
    return "C {}".format(text.replace("_", " "))


@web_flask.route('/python/<text>', strict_slashes=False)
def pythontext(text="is cool"):
    return "Python {}".format(text.replace("_", " "))

if __name__ == "__main__":
    web_flask.run(port=5000, host="0.0.0.0", debug=None)
