# request number of devices
import os
import json
import requests
import testVariables


def test_list_of_devices():
    response = requests.get(
        f"{testVariables.baseUrl}/v1/devices?signature={testVariables.clientSecret}",
        headers=testVariables.request_headers)
    testVariables.ccc(os.path.basename(__file__), response)
    testVariables.debug_print(json.dumps(dict(response.headers)))
    testVariables.debug_print(response.url)
    testVariables.debug_print(f"response status code: {response.status_code}")
    assert response.status_code == 200
    assert response.json()["result"]["success"] == True
    assert isinstance(response.json()["itemsCount"], int)
    testVariables.debug_print("response.json \"success\": " + str(response.json()["result"]["success"]))

