# check two currencies is correct
import os
import debug_log_true
import requests
import test_params


def test_correct_auth():
    currency_usd = "currency=USD"

    response = requests.get(
        f"{test_params.baseUrl}/v1/balances?{test_params.currency}&{currency_usd}&signature={test_params.clientSecret}",
        headers=test_params.request_headers)

    # debug log displays if debug_true = True
    if debug_log_true.debug_true == True:
        debug_log_true.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["result"]["success"] == True, f"Expected True, got {response.json()['result']['success']}"
    assert response.json()["result"]["errorData"] == {}, f"Expected {{}}, got {response.json()['result']['errorData']}"
