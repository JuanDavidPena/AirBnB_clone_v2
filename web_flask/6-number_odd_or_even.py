#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    ''' Returns Hello HBNB in / URL '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def name():
    ''' Returns HBNB on path /hbnb'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text_c(text):
    ''' Returns C with specified message'''
    return 'C ' + text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_python(text):
    ''' Returns Python with specified message'''
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    ''' Returns message if is a number, error instead. '''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_number_template(n):
    ''' Display page if number is an integer, error instead. '''
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_odd_even(n):
    ''' Display page if number is odd or even, error instead. '''
    if n % 2 == 0:
        o_even = 'even'
    else:
        o_even = 'odd'
    return render_template('6-number_odd_or_even.html', number=n, type=o_even)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
