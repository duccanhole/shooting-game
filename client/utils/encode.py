
import json


def encode(data: dict):
    return json.dumps(data).encode()