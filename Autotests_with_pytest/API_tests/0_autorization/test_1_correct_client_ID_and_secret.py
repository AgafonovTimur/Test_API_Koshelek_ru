# check if authorization is correct
import os
import json
import requests
import testVariables


def test_correct_auth():
    response = requests.get(
        f"{testVariables.baseUrl}/v1/devices?signature={testVariables.clientSecret}",
        headers=testVariables.request_headers)

    # debug log displays if debug_true = True
    if testVariables.debug_true == True:
        print("\033[92m" + "\n" + os.path.basename(__file__) + "\n" + json.dumps(json.loads(response.text), indent=2))
        print(f"response status code: {response.status_code}")
        print(response.url)
        print(response.json()["result"]["success"])
        print(response.json()["result"]["errorData"])

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["result"]["success"] == True, f"Expected True, got {response.json()['result']['success']}"
    assert response.json()["result"]["errorData"] == {}, f"Expected {{}}, got {response.json()['result']['errorData']}"
