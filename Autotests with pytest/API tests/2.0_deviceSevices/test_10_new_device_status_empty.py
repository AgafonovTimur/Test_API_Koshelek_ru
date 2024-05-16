# new device - device status empty
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
        response = requests.post(testVariables.baseUrl + "/v1/devices?signature=" + testVariables.clientSecret,
                                 headers=testVariables.request_headers, data=json.dumps(request_payload))
        testVariables.change_console_color_and_add_name_of_test(os.path.basename(__file__))
        print(json.dumps(response.json()))
        print("response status code: " + str(response.status_code))
        assert response.status_code == 400, f"Expected 400, got {response.status_code}"
        assert response.json()["code"] == 3, f"Expected 3, got {response.json()['code']}"
        assert response.json()["details"] == [], f"Expected [], got {response.json()['details']}"
        assert response.json()[
                   "message"] == "Object reference not set to an instance of an object.", f"Expected 'Object reference not set to an instance of an object.', got {response.json()['message']}"
