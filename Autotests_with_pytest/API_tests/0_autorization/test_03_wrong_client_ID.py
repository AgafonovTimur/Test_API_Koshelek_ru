# check if client ID is correct
import os
import json
import requests
import testVariables


def test_correct_auth():
    request_headers = {'Content-Type': 'application/json',
                       'ClientId': "18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d49"}

    response = requests.get(
        f"{testVariables.baseUrl}/v1/devices?signature={testVariables.clientSecret}",
        headers=request_headers)
    testVariables.ccc(os.path.basename(__file__), response)
    assert response.status_code == 200
    assert response.json()["result"]["success"] == False
    assert response.json()["result"]["error"] == "ApiKeyNotFound"
    assert response.json()["result"]["ErrorCode"] == 125
