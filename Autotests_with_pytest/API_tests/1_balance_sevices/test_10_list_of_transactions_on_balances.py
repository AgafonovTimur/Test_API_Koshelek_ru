# check list of transactions on balances
import os
import debug_log_true
import requests
import testVariables


def test_correct_auth():
    response = requests.get(
        f"{testVariables.baseUrl}/v1/balances/changes?{testVariables.currency}&signature={testVariables.clientSecret}",
        headers=testVariables.request_headers)

    # debug log displays if debug_true = True
    if debug_log_true.debug_true == True:
        debug_log_true.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["result"]["success"] == True, f"Expected True, got {response.json()['result']['success']}"
    assert response.json()["result"]["errorData"] == {}, f"Expected {{}}, got {response.json()['result']['errorData']}"
    assert response.json()["items"] == [], f"Expected [], got {response.json()['items']}"
