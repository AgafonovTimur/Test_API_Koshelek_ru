# check list of transactions on balances
import os
import requests
from test_library import test_params, debug_log_true


def test_correct_auth():
    response = requests.get(
        f"{test_params.baseUrl}/v1/balances/changes?{test_params.currency}&signature={test_params.clientSecret}",
        headers=test_params.request_headers)

    # debug log displays if debug_true = True
    if debug_log_true.debug_true == True:
        debug_log_true.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["result"]["success"] == True, f"Expected True, got {response.json()['result']['success']}"
    assert response.json()["result"]["errorData"] == {}, f"Expected {{}}, got {response.json()['result']['errorData']}"
    assert response.json()["items"] == [], f"Expected [], got {response.json()['items']}"
