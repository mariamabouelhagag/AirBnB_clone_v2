#!/usr/bin/python3
"""Importing Flask to run the web app"""
from flask import Flask, render_template
from models import storage
from models.state import State


web_flask = Flask(__name__)


@web_flask.teardown_appcontext
def close(self):
    """ Method to close the session """
    storage.close()


@we_flask.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays a html page with states and cities"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    web_flask.run(host="0.0.0.0", port="5000")
