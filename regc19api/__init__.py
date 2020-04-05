# flake8: noqa
from flask import Flask
from flask_cors import CORS

API_NAME = "regc19api"

app = Flask(API_NAME)
CORS(app)

import regc19api.routes.common
import regc19api.routes.registrations
