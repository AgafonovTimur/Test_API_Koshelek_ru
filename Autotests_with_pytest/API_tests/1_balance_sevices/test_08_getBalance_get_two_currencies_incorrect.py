# check two currencies is correct
import os
import debug_log_true
import requests
import testVariables


def test_correct_auth():
    currency_usd = "currency=few"

    response = requests.get(
        f"{testVariables.baseUrl}/v1/balances?{testVariables.currency}&{currency_usd}&signature={testVariables.clientSecret}",
        headers=testVariables.request_headers)

    # debug log displays if debug_true = True
    if debug_log_true.debug_true == True:
        debug_log_true.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["result"]["success"] == False, f"Expected False, got {response.json()['result']['success']}"
    assert response.json()["result"][
               "error"] == "CurrencyNotFound", f"Expected CurrencyNotFound, got {response.json()['result']['error']}"
    assert response.json()["result"]["errorCode"] == 139, f"Expected 139, got {response.json()['result']['errorCode']}"
