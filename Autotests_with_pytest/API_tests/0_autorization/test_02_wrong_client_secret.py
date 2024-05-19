# check if authorization is correct
import os
import json
import requests
import testVariables


def test_correct_auth():
    response = requests.get(
        f"{testVariables.baseUrl}/v1/devices?signature=18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d49", # +1 at the end
        headers=testVariables.request_headers)
    testVariables.ccc(os.path.basename(__file__), response)
    assert response.status_code == 200
    assert response.json()["result"]["success"] == False
    assert response.json()["result"]["error"] == "SignatureNotValid"
    assert response.json()["result"]["ErrorCode"] == 115
