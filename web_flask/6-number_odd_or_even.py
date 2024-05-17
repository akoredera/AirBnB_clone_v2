#!/usr/bin/python3
'''
script that starts a Flask web application
'''
from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_HBNB():
    '''
    Hello Flask!
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def _HBNB():
    '''
    Hello Flask!
    '''
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c_route(text):
    '''
    display "C" followed by the value of the text variable
    '''
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    '''
    display Python, followed by the value of the text
    variable (replace underscore _ symbols with a space)
    The default value of text is "is cool"
    '''
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    '''
    display "n is a number" only if n is an integer
    '''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    '''
    display a HTML page only if n is an integer
    '''
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''
    display a HTML page only if n is an integer
    '''
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
