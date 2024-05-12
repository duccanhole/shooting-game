import json

def decode(data: bytes):
    try:
        res = json.loads(data.decode())
        return res if len(res) > 0 else {}
    except:
        return {}
