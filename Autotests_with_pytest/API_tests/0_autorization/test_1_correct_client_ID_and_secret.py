# check if authorization is correct
import os
import json
import requests
import testVariables
import debug_log_true


def test_correct_auth():
    response = requests.get(
        f"{testVariables.baseUrl}/v1/devices?signature={testVariables.clientSecret}",
        headers=testVariables.request_headers)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["result"]["success"] == True, f"Expected True, got {response.json()['result']['success']}"
    assert response.json()["result"]["errorData"] == {}, f"Expected {{}}, got {response.json()['result']['errorData']}"

    if debug_log_true.debug_true == True:
        debug_log_true.prints(os.path.basename(__file__), response.json(), response.status_code, response.url)
