# new device - empty type
import json
import requests
import testVariables
import os


class TestClass2:
    request_body = {
        "name": "ngage",
        "model": "s55",
        "type": "",
        "status": "DEVICE_STATUS_ACTIVE",
    }

    def test_add_new_device(self):
        request_payload = self.request_body

        response = requests.post(
            f"{testVariables.baseUrl}/v1/devices?signature={testVariables.clientSecret}",
            headers=testVariables.request_headers, json=request_payload)

        # debug log displays if debug_true = True
        if testVariables.debug_true == True:
            print(
                "\033[92m" + "\n" + os.path.basename(__file__) + "\n" + "\033[93m" + json.dumps(
                    json.loads(response.text), indent=2))
            print("\033[92m" + f"response status code: {response.status_code}")
            print(response.url)
            print(response.json()['result']['success'])
            print(response.json()['result']['error'])
            print(response.json()['result']['ErrorCode'])

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json()['result'][
                   'success'] == False, f"Expected False, got {response.json()['result']['success']}"
        assert response.json()['result'][
                   'error'] == "RequestNotValid", f"Expected RequestNotValid, got {response.json()['result']['error']}"
        assert response.json()['result'][
                   'ErrorCode'] == 900, f"Expected 900, got {response.json()['result']['ErrorCode']}"
