# check list of operations
import os
import json
import requests
import testVariables


def test_correct_auth():
    response = requests.get(
        f"{testVariables.baseUrl}/v1/balances/operations?{testVariables.currency}&type=2&signature={testVariables.clientSecret}",
        headers=testVariables.request_headers)
    testVariables.ccc(os.path.basename(__file__), response)
    assert response.status_code == 200
    assert response.json()["result"]["success"] == True
    assert response.json()["result"]["errorData"] == {}
    assert response.json()["items"] == []
    assert isinstance(response.json()["total"], int)
