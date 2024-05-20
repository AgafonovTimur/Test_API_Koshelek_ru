# check list of operations
import os
import json
import requests
import testVariables


def test_correct_auth():  # sourcery skip: extract-method
    response = requests.get(
        f"{testVariables.baseUrl}/v1/balances/operations?{testVariables.currency}&type=2&signature={testVariables.clientSecret}",
        headers=testVariables.request_headers)

    # debug log displays if debug_true = True
    if testVariables.debug_true == True:
        print("\033[92m" + "\n" + os.path.basename(__file__) + "\n" + "\033[93m" + json.dumps(
            json.loads(response.text), indent=2))
        print("\033[92m" + f"response status code: {response.status_code}")
        print(response.url)
        print(f"response success: {response.json()['result']['success']}")
        print(response.json()["result"]["errorData"])
        print(f"response items: {response.json()['items']}")
        print(isinstance(response.json()["total"], int))

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["result"]["success"] == True, f"Unexpected response {response.json()}"
    assert response.json()["result"]["errorData"] == {}, f"Expected {{}}, got {response.json()['result']['errorData']}"
    assert response.json()["items"] == [], f"Expected [], got {response.json()['items']}"
    assert isinstance(response.json()["total"], int), f"Expected int, got {type(response.json()['total'])}"
