import json
import requests


def get_url(url: str, route: str, port: int=5000, protocol: str="http"):
    return protocol + "://" + url + ":" + str(port) + route


def GET(url: str):
    print("GET: " + url)
    r = requests.get(url)
    print(r.text)
    try:
        response = r.json()
        valid_response = True
    except json.JSONDecodeError:
        response = dict()
        valid_response = False
    out = dict()
    out["response"] = response
    out["response_raw"] = r.text
    out["exit_code"] = 201
    out["valid_response"] = valid_response
    return out


def POST(url: str, data: dict):
    print("POST: " + url)
    payload = json.dumps(data)
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=payload, headers=headers)
    try:
        response = r.json()
        valid_response = True
    except json.JSONDecodeError:
        response = dict()
        valid_response = False
    out = dict()
    out["response"] = response
    out["response_raw"] = r.text
    out["exit_code"] = 201
    out["valid_response"] = valid_response
    print("DATA: " + str())
