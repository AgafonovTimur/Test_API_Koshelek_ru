# add new device
import os
import json
import requests
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs

class Test:
    request_body = {
        "name": "nokia",
        "model": "6600",
        "type": "TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE"
    }

    def test_add_new_device(self):
        request_payload = self.request_body

        response = requests.post(
            f"{test_params.baseUrl}/v1/devices?signature={test_params.clientSecret}",
            headers=test_params.request_headers, json=request_payload)

        device_id = json.dumps(response.json().get("id"))

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(self, os.path.basename(__file__), response.json(), response.status_code, response.url)

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json()["result"][
                   "success"] == True, f"Expected True, got {response.json()['result']['success']}"
        assert response.json()["result"][
                   "errorData"] == {}, f"Expected {{}}, got {response.json()['result']['errorData']}"

##########################################################################################################

        #  get requsites
        response2 = requests.get(
            f"{test_params.baseUrl}/v1/devices/{device_id}?signature={test_params.clientSecret}",
            headers=test_params.request_headers, json=request_payload)

        device_id2 = json.dumps(response2.json().get("id"))

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(self, os.path.basename(__file__), response2.json(), response2.status_code,
                                      response2.url)
            print(f"name: {response2.json().get("name")}")
            print(f"model: {response2.json().get("model")}")
            print(f"device_id: {response2.json().get("id")}")

        assert response2.status_code == 200, f"Expected 200, got {response2.status_code}"
        assert response2.json()["result"][
                   "success"] == True, f"Expected True, got {response2.json()['result']['success']}"
        assert response2.json()["result"][
                   "errorData"] == {}, f"Expected {{}}, got {response2.json()['result']['errorData']}"
        assert device_id == device_id2, f"Expected {device_id}, got {device_id2}"
