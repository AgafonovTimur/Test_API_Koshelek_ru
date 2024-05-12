# request number of devices
import json

import requests
import testVariables


class TestOne:
    def test_1(self):
        headers1 = {'Content-Type': 'application/json', 'ClientId': testVariables.clientId}
        response = requests.get(testVariables.baseUrl + "/v1/devices?signature=" + testVariables.clientSecret,
                                headers=headers1)

        print(json.dumps(dict(response.headers)))
        print(response.url)
        print(response.status_code)
        print(response.headers)
        print(json.dumps(response.json()))
        print(response.text)
        assert response.status_code == 200
        assert response.json()["result"]["success"] == True
        print(response.json()["result"]["success"])
