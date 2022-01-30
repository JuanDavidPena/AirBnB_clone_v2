#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage
import os

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_states_cities():
    ''' Display HTML page with states '''
    from models.state import State
    from models.city import City
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        return render_template(
            '8-cities_by_states.html',
            ls_cities=State.cities())
    else:
        list_state = list(storage.all(State).values())
        list_cities = list(storage.all(City).values())
        return render_template(
            '8-cities_by_states.html',
            ls_states=list_state,
            ls_cities=list_cities)


@app.teardown_appcontext
def teardown_x(self):
    ''' Closes session when request ends '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
