#!/usr/bin/python3
'''
script that starts a Flask web application
'''
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
