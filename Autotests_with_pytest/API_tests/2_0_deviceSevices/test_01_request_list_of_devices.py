# request number of devices
import os
import debug_log_true
import requests
import testVariables


def test_list_of_devices():
    response = requests.get(
        f"{testVariables.baseUrl}/v1/devices?signature={testVariables.clientSecret}",
        headers=testVariables.request_headers)

    # debug log displays if debug_true = True
    if debug_log_true.debug_true == True:
        debug_log_true.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["result"]["success"] == True, f"Expected True, got {response.json()['result']['success']}"
    assert isinstance(response.json()["itemsCount"], int), f"Expected int, got {type(response.json()['itemsCount'])}"
