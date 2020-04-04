"""Common routes for root and version."""

from flask import json
from regc19api import app


@app.route('/')
def root():
    """Base url endpoint."""
    return get_version()


@app.route('/version', methods=['GET'])
def get_version():
    return json.jsonify({
        'name': app.name,
        'version': 'dev'
    })
