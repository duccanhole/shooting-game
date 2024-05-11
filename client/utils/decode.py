import json

def decode(data: bytes):
    res = json.loads(data.decode())
    return res if len(res) > 0 else {}
