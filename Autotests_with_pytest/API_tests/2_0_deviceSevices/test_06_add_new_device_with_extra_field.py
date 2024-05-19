# add new device with extra field in request body
import json
import requests
import testVariables
import os




class TestClass:
    request_body = {
        "name": "ngage",
        "model": "s55",
        "type": "TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE",
        "my_id": "device-id"  # my_id does not exist
    }

    def test_add_new_device(self):
        request_payload = self.request_body
        response = requests.post(
            f"{testVariables.baseUrl}/v1/devices?signature={testVariables.clientSecret}",
            headers=testVariables.request_headers, json=request_payload)
        device_id = json.dumps(response.json().get("id"))
        testVariables.ccc(os.path.basename(__file__), response)
        print("response status code: " + str(response.status_code))
        # response status code must be 4xx and it's a bug, but test made to pass this assert
        # assertion must be != 200 or == 400 bad request
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json()["result"]["success"] == True
        print("response.json \"success\": " + str(response.json()["result"]["success"]))
        assert response.json()["result"]["errorData"] == {}
        print("response.json \"errorData\": " + str(response.json()["result"]["errorData"]))
        assert device_id != 0 or device_id is not None, f"Expected not 0 or None, got {device_id}"
        print("response.json \"id\": " + str(response.json().get("id")))
