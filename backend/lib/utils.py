import json
from bson import json_util

from flask import make_response, jsonify
def parse_json(data):
    return json.loads(json_util.dumps(data))


def serverResponse(data, status_code, msg):
    packet = {
        "data": data,
        "description": msg
    }
    r = make_response(jsonify(parse_json(packet)))
    r.status_code = status_code
    r.headers.add('Access-Control-Allow-Origin', '*')
    return r