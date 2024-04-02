#!/usr/bin/python3
"""Starts a Flask web application"""


from flask import Flask, render_template, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_session(self):
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host, port, threaded=True)
