# add new device
import pytest
import json
import requests
import testVariables


class TestClass:
    phone_name = {
        "name": "siemens mobile",
        "model": "s55",
        "type": "TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE"
    }

    def test_add_new_device(self):
        payload1 = self.phone_name
        response = requests.post(testVariables.baseUrl + "/v1/devices?signature=" + testVariables.clientSecret,
                                 headers=testVariables.request_headers, data=json.dumps(payload1))
        # actual response name
        ar_name = response.json().get("name")
        # expected response name
        er_name = "siemens mobile"
        print("\033[92m")
        print("response status code: " + str(response.status_code))
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        print("response name: " + ar_name)
        assert ar_name == er_name, f"Phone name is incorrect, its {ar_name}"
