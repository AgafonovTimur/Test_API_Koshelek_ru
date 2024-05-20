# check if authorization is correct
import os
import json
import requests
import testVariables


def test_correct_auth():  # sourcery skip: extract-method
    response = requests.get(
        f"{testVariables.baseUrl}/v1/devices?signature=18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d49",
        # +1 at the end
        headers=testVariables.request_headers)

    # debug log displays if debug_true = True
    if testVariables.debug_true == True:
        print("\033[92m" + "\n" + os.path.basename(__file__) + "\n" + json.dumps(json.loads(response.text), indent=2))
        print(f"response status code: {response.status_code}")
        print(response.url)
        print(response.json()["result"]["success"])
        print(response.json()["result"]["error"])
        print(response.json()["result"]["ErrorCode"])
        
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["result"]["success"] == False, f"Expected False, got {response.json()['result']['success']}"
    assert response.json()["result"][
               "error"] == "SignatureNotValid", f"Expected SignatureNotValid, got {response.json()['result']['error']}"
    assert response.json()["result"]["ErrorCode"] == 115, f"Expected 115, got {response.json()['result']['ErrorCode']}"
