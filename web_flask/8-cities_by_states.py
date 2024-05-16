#!/usr/bin/python3
"""Script to start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Closes the SQLAlchemy session after each request."""
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    """Retrieves all states and their cities, then renders a template."""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
