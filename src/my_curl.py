import json
import requests


def get_url(domain: str, route: str, port: int=5000, protocol: str="http") -> str:
    """
    Creates an url

    :domain str: The domain (example.com)
    :route str: The route beginning from / (/users/sign_up)
    :port int: The services port (default is 5000)
    :protocol str: The protocol to use (default is "http")

    :returns str: url
    """
    return str(protocol) + "://" + str(domain) + ":" + str(port) + str(route)


def GET(url: str) -> dict:
    """
    Makes an HTTP GET request to the given url.

    :url str: Url to get

    :returns dict{"response": dict, "response_raw": str, "exit_code": int, "valid_response": bool}: The response parsed as json string, the raw response, the exit code of the connection and a boolean that says if it was a valid json response
    """
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


def POST(url: str, data: dict) -> dict:
    """
    Makes an HTTP POST request to the given url.

    :url str: Url to get
    :data dict: Data that should be attatched to the body

    :returns dict{"response": dict, "response_raw": str, "exit_code": int, "valid_response": bool}: The response parsed as json string, the raw response, the exit code of the connection and a boolean that says if it was a valid json response
    """
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
