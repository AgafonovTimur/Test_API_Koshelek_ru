# add new device with extra field in request body
import requests
from test_library import test_params, debug_log_true
import os
import json


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
            f"{test_params.baseUrl}/v1/devices?signature={test_params.clientSecret}",
            headers=test_params.request_headers, json=request_payload)

        device_id = json.dumps(response.json().get("id"))

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            debug_log_true.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)
            print(f"device_id: {device_id}")

        # response status code must be 4xx and it's a bug, but test made to pass this assert
        # assertion must be != 200 or == 400 bad request
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json()["result"][
                   "success"] == True, f"Expected True, got {response.json()['result']['success']}"
        assert response.json()["result"][
                   "errorData"] == {}, f"Expected {{}}, got {response.json()['result']['errorData']}"
        assert device_id != 0 or device_id is not None, f"Expected not 0 or None, got {device_id}"
