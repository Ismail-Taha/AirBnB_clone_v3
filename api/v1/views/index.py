#!/usr/bin/python3
"""Define routes for blueprint
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """Return status of application
    """
    return jsonify({'status': 'OK'})


@app_views.route('/stats', strict_slashes=False)
def counts():
    """Retrieve counts of various objects in storage."""
    from models.amenity import Amenity
    from models.city import City
    from models.place import Place
    from models.review import Review
    from models.state import State
    from models.user import User

    class_map = {"amenity_counts": Amenity, "city_counts": City,
                 "place_counts": Place, "review_counts": Review,
                 "state_counts": State, "user_counts": User}
    counts_dict = {}

    for key, model in class_map.items():
        counts_dict[key] = storage.count(model)

    return jsonify(counts_dict)
