# new device - wrong type

import json
import requests
import testVariables
import os


class TestClass2:
    request_body = {
        "name": "ngage",
        "model": "s55",
        "type": "1TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE",
    }

    def test_add_new_device(self):
        request_payload = self.request_body
        response = requests.post(testVariables.baseUrl + "/v1/devices?signature=" + testVariables.clientSecret,
                                 headers=testVariables.request_headers, data=json.dumps(request_payload))
        testVariables.change_console_color_and_add_name_of_test(os.path.basename(__file__))
        print(json.dumps(response.json()))
        print("response status code: " + str(response.status_code))
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json()['result'][
                   'success'] == False, f"Expected False, got {response.json()['result']['success']}"
        print(response.json()['result']['success'])
        assert response.json()['result'][
                   'error'] == "RequestNotValid", f"Expected False, got {response.json()['result']['error']}"
        print(response.json()['result']['error'])
        assert response.json()['result'][
                   'ErrorCode'] == 900, f"Expected False, got {response.json()['result']['ErrorCode']}"
        print(response.json()['result']['ErrorCode'])