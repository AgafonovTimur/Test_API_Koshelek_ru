# check if authorization is correct
import os
import debug_log_true
import requests
import test_params


def test_correct_auth():  # sourcery skip: extract-method
    response = requests.get(
        f"{test_params.baseUrl}/v1/devices?signature=18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d49",
        # +1 at the end
        headers=test_params.request_headers)

    # debug log displays if debug_true = True
    if debug_log_true.debug_true == True:
        debug_log_true.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["result"]["success"] == False, f"Expected False, got {response.json()['result']['success']}"
    assert response.json()["result"][
               "error"] == "SignatureNotValid", f"Expected SignatureNotValid, got {response.json()['result']['error']}"
    assert response.json()["result"]["ErrorCode"] == 115, f"Expected 115, got {response.json()['result']['ErrorCode']}"
