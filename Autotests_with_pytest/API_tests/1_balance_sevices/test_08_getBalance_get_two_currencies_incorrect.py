# check two currencies is correct
import os
import json
import requests
import testVariables


def test_correct_auth():
    currency_usd = "currency=few"

    response = requests.get(
        f"{testVariables.baseUrl}/v1/balances?{testVariables.currency}&{currency_usd}&signature={testVariables.clientSecret}",
        headers=testVariables.request_headers)
    testVariables.ccc(os.path.basename(__file__), response)
    assert response.status_code == 200
    assert response.json()["result"]["success"] == False
    assert response.json()["result"]["error"] == "CurrencyNotFound"
    assert response.json()["result"]["errorCode"] == 139
