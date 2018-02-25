import json

def GET(url: str):
    print("GET: " + url)
    response_j = '{"successful": 1}'
    response = json.loads(response_j)
    out = dict()
    out["response"] = response
    out["exit_code"] = 201
    return out

def POST(url: str, data: dict):
    print("POST: " + url)
    print("DATA: " + str(data))
