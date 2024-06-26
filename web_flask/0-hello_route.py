#!/usr/bin/python3
'''
Flash framework HBnB project
'''
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_HBNB():
    '''
    Hello Flask!
    '''
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
