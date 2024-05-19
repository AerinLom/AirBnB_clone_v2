#!/usr/bin/python3
"""
script that starts a Flask web application
"""


from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display a list of states """
    states = storage.all(State)
    list_of_states = []
    for key, val in states.items():
        list_of_states.append(val)
    return render_template('7-states_list.html', states=list_of_states)


@app.teardown_appcontext
def teardown_session(exception):
    """ Remove the current SQLAlchemy Session after each request """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
