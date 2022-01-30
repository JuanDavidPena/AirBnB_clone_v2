#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage
import os

app = Flask(__name__)


@app.route('/states', defaults={'id': None}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def list_states_or_cities(id):
    ''' Display HTML page with states '''
    from models.state import State
    from models.city import City
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        return render_template('9-states.html', ls_states=State.cities())
    list_state = list(storage.all(State).values())
    if id is None:
        return render_template(
            '9-states.html',
            ls_states=list_state,
            id='None')
    else:
        for state in list_state:
            if state.id == id:
                list_cities = list(storage.all(City).values())
                return render_template(
                    '9-states.html',
                    state=state,
                    ls_cities=list_cities,
                    id=id,
                    state_exists='True')
        return render_template(
            '9-states.html',
            ls_states=list_state,
            id=id,
            state_exists='False')


@app.teardown_appcontext
def teardown_x(self):
    ''' Closes session when request ends '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
