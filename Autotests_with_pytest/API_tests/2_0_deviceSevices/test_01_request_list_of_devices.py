# request number of devices
import os
import json
import requests
import testVariables


def test_list_of_devices():
    response = requests.get(
        f"{testVariables.baseUrl}/v1/devices?signature={testVariables.clientSecret}",
        headers=testVariables.request_headers)

    # debug log displays if debug_true = True
    if testVariables.debug_true == True:
        print("\033[92m" + "\n" + os.path.basename(__file__) + "\n" + "\033[93m" + json.dumps(
            json.loads(response.text), indent=2))
        print("\033[92m" + f"response status code: {response.status_code}")
        print(response.url)
        print(json.dumps(dict(response.headers)))
        print(response.url)
        print("response.json \"success\": " + str(response.json()["result"]["success"]))

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["result"]["success"] == True, f"Expected True, got {response.json()['result']['success']}"
    assert isinstance(response.json()["itemsCount"], int), f"Expected int, got {type(response.json()['itemsCount'])}"
