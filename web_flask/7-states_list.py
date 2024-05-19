#!/usr/bin/python3
"""
starts a Flask web application
"""

<<<<<<< HEAD

=======
>>>>>>> fc02d0a53463d85459b8f92bbfb86c780b835daa
from flask import Flask, render_template

from models import *
from models import storage
<<<<<<< HEAD
from models.state import State
=======

>>>>>>> fc02d0a53463d85459b8f92bbfb86c780b835daa
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
