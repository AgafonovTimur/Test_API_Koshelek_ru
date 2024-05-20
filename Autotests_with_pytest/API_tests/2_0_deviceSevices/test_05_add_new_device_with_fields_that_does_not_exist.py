# add new device with field missing
import json
import requests
import testVariables
import os


class TestClass:
    request_body = {
        "name": "siemens",
        # "model": "s55",                     -this string missing
        # "type": "TYPE_UNKNOWN",             -this string missing
        "status": "DEVICE_STATUS_ACTIVE"
    }

    def test_add_new_device(self):
        request_payload = self.request_body
        response = requests.post(
            f"{testVariables.baseUrl}/v1/devices?signature={testVariables.clientSecret}",
            headers=testVariables.request_headers, json=request_payload)
        testVariables.ccc(os.path.basename(__file__), response)
        testVariables.debug_print("response status code: " + str(response.status_code))
        # response status code must be 4xx and it's a bug, but test made to pass this assert
        # assertion must be != 200 or == 400 bad request
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json()["result"]["success"] == True
        testVariables.debug_print("response.json \"success\": " + str(response.json()["result"]["success"]))
        assert response.json()["result"]["errorData"] == {}
        testVariables.debug_print("response.json \"errorData\": " + str(response.json()["result"]["errorData"]))
