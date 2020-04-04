"""Symptoms registration routes."""

from flask import request, make_response
from regc19api import app


@app.route('/c19/registrations', methods=['POST'])
def register():
    """Register c19 symptoms.

    TODO:
    - Add json validation, Be conservative in what you do, be liberal in what
    you accept

    """
    json_data = request.get_json()
    return make_response(json_data, 201)


@app.route('/c19/registrations/<id>', methods=['PUT'])
def update(id):
    """Update registration."""
    json_data = request.get_json()
    return make_response(json_data, 200)


@app.route('/c19/registrations/<id>', methods=['GET'])
def get(id):
    """Get registration."""
    data = {
        'property': 'value'
    }
    return make_response(data, 200)


@app.route('/c19/registrations/<id>', methods=['DELETE'])
def delete(id):
    """Remove registration."""
    data = {
        'property': 'value'
    }
    return make_response(data, 200)
