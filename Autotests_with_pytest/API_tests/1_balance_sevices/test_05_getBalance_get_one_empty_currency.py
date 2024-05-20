# check currency is empty
import os
import json
import requests
import testVariables


def test_correct_auth():
    currency_rub = "currency="

    response = requests.get(
        f"{testVariables.baseUrl}/v1/balances?{currency_rub}&signature={testVariables.clientSecret}",
        headers=testVariables.request_headers)

    # debug log displays if debug_true = True
    if testVariables.debug_true == True:
        print("\033[92m" + "\n" + os.path.basename(__file__) + "\n" + json.dumps(json.loads(response.text), indent=2))
        print(f"response status code: {response.status_code}")
        print(response.url)
        print(response.json()["result"]["success"])
        print(response.json()["result"]["error"])
        print(response.json()["result"]["errorCode"])

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["result"]["success"] == False, f"Expected False, got {response.json()['result']['success']}"
    assert response.json()["result"][
               "error"] == "CurrencyNotFound", f"Expected CurrencyNotFound, got {response.json()['result']['error']}"
    assert response.json()["result"]["errorCode"] == 139, f"Expected 139, got {response.json()['result']['errorCode']}"
