import os
import redis
from flask import json


redis_url = os.environ.get("REDIS_URL")
if redis_url is None:
    redis_url = 'redis://localhost:6379/0'

regdb = redis.from_url(redis_url)


def store_registration(id, data):
    data['id'] = id
    regdb.set(id, json.dumps(data))


def get_registration(id):
    data = regdb.get(id)
    return json.loads(data) if data is not None else None


def delete_registration(id):
    regdb.delete(id)
