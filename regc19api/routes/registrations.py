"""Symptoms registration routes."""

import uuid
from flask import request, make_response, abort
from regc19api import app
from regc19api.db.registrationsdb import store_registration, get_registration, delete_registration


def get_by_id(id):
    json_data = get_registration(id)
    if json_data is None:
        abort(404)
    return json_data


@app.route('/c19/registrations', methods=['POST'])
def register():
    """Register c19 symptoms.

    TODO:
    - Add json validation, Be conservative in what you do, be liberal in what
    you accept

    """
    json_data = request.get_json()
    reg_id = str(uuid.uuid4())
    store_registration(reg_id, json_data)
    return make_response(json_data, 201)


@app.route('/c19/registrations/<id>', methods=['PUT'])
def update(id):
    """Update registration."""
    json_data = request.get_json()
    get_by_id(id)  # 404 if registration doesn't exist
    store_registration(id, json_data)
    return make_response(json_data, 200)


@app.route('/c19/registrations/<id>', methods=['GET'])
def get(id):
    """Get registration."""
    json_data = get_by_id(id)
    return make_response(json_data, 200)


@app.route('/c19/registrations/<id>', methods=['DELETE'])
def delete(id):
    """Remove registration."""
    json_data = get_by_id(id)
    delete_registration(id)
    return make_response(json_data, 200)
