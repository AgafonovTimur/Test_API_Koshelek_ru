# check currency is incorrect
import os
import json
import requests
import testVariables


def test_correct_auth():
    currency_rub = "currency=rub"

    response = requests.get(
        f"{testVariables.baseUrl}/v1/balances?{currency_rub}&signature={testVariables.clientSecret}",
        headers=testVariables.request_headers)
    testVariables.ccc(os.path.basename(__file__), response)
    assert response.status_code == 200
    assert response.json()["result"]["success"] == True
    assert response.json()["result"]["errorData"] == {}
