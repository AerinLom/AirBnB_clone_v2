#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import render_template, Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    if isinstance(n, int):
        return render_template('5-number.html', input_number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_status(n):
    if isinstance(n, int):
        if n % 2 != 0:
            status = 'odd'
        else:
            status = 'even'
        return render_template('6-number_odd_or_even.html',
                               input_number=n, status=status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
