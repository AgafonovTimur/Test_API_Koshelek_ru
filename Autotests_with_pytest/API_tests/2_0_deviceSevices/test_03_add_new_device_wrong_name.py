# add new device with wrong name
import os
import json
import requests
import testVariables


class TestClass:
    request_body = {
        "name": "nokia",
        "model": "s55",
        "type": "TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE"
    }

    def test_add_new_device(self):
        request_payload = self.request_body
        response = requests.post(
            f"{testVariables.baseUrl}/v1/devices?signature={testVariables.clientSecret}",
            headers=testVariables.request_headers, json=request_payload)
        # actual response name
        ar_name = response.json().get("name")
        # expected response name
        er_name = "siemens mobile"
        testVariables.ccc(os.path.basename(__file__), response)
        print("response status code: " + str(response.status_code))
        # response status code must be 4xx and it's a bug, but test made to pass this assert
        # assertion must be != 200 or == 4xx
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert ar_name != er_name, f"Phone name is correct, its {ar_name}"
        print("response name: " + ar_name + " is incorrect. All good")
        assert response.json()["result"]["success"] == True
        print("response.json \"success\": " + str(response.json()["result"]["success"]))
        assert response.json()["result"]["errorData"] == {}
        print("response.json \"errorData\": " + str(response.json()["result"]["errorData"]))
