#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    ''' Display HTML page with states '''
    from models.state import State
    list_state = list(storage.all(State).values())
    return render_template('7-states_list.html', ls_states=list_state)


@app.teardown_appcontext
def teardown_x(self):
    ''' Closes session when request ends '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
