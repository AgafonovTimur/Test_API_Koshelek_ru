# request number of devices
import pytest
import json
import requests
import testVariables


def test_list_of_devices():
    response = requests.get(testVariables.baseUrl + "/v1/devices?signature=" + testVariables.clientSecret,
                            headers=testVariables.request_headers)
    print("\033[92m")
    print(json.dumps(dict(response.headers)))
    print(response.url)
    print("response status code: " + str(response.status_code))
    print(response.headers)
    print(json.dumps(response.json()))
    print(response.text)
    assert response.status_code == 200
    assert response.json()["result"]["success"] == True
    assert isinstance(response.json()["itemsCount"], int)
    print("response.json \"success\": " + str(response.json()["result"]["success"]))

