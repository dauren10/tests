import pytest
import json
import requests

def main_url():
    return "https://reqres.in"


def test_valid_login():
    url="https://reqres.in/api/login/"
    data={'email':'eve.holt@reqres.in','password':'cityslicka'}
    response=requests.post(url,data=data)
    token1=json.loads(response.text)
    assert response.status_code == 200
    assert token1['token'] == "QpwL5tke4Pnpja7X42"
