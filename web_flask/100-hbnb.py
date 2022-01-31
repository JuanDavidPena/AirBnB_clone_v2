#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage
import os

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def list_places():
    ''' Display HTML page with places '''
    from models.state import State
    from models.city import City
    from models.amenity import Amenity
    from models.place import Place
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        return render_template('100-hbnb.html', ls_states=State.cities())
    list_states = list(storage.all(State).values())
    list_cities = list(storage.all(City).values())
    list_amenities = list(storage.all(Amenity).values())
    list_places = list(storage.all(Place).values())
    return render_template(
        '100-hbnb.html',
        ls_states=list_states,
        ls_cities=list_cities,
        ls_amenities=list_amenities,
        ls_places=list_places)


@app.teardown_appcontext
def teardown_x(self):
    ''' Closes session when request ends '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
