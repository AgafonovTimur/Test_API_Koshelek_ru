# new device - empty type^
import json
import requests
import testVariables
import os


class TestClass2:
    request_body = {
        "name": "ngage",
        "model": "s55",
        "type": "TYPE_UNKNOWN",
        "status": "1DEVICE_STATUS_ACTIVE",
    }

    def test_add_new_device(self):
        request_payload = self.request_body
        response = requests.post(
            f"{testVariables.baseUrl}/v1/devices?signature={testVariables.clientSecret}",
            headers=testVariables.request_headers, json=request_payload)
        testVariables.ccc(os.path.basename(__file__), response)
        print("response status code: " + str(response.status_code))
        assert response.json()['result'][
                   'success'] == False, f"Expected False, got {response.json()['result']['success']}"
        print(response.json()['result']['success'])
        assert response.json()['result'][
                   'error'] == "RequestNotValid", f"Expected False, got {response.json()['result']['error']}"
        print(response.json()['result']['error'])
        assert response.json()['result'][
                   'ErrorCode'] == 900, f"Expected False, got {response.json()['result']['ErrorCode']}"
        print(response.json()['result']['ErrorCode'])
