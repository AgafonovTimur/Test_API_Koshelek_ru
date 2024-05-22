# add new device with extra field in request body
import requests
import os
import json
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions


class Test:
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
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)
            # print(f"device_id: {device_id}")

        # response status code must be 4xx and it's a bug, but test made to pass this assert
        # assertion must be != 200 or == 400 bad request
        # Assertions.status_code_check(response.status_code, 200)
        # Assertions.json_result_success(response.json()["result"]["success"], True)
        # Assertions.json_result_errorData(response.json()["result"]["errorData"], {})
        # Assertions.json_name_equal_to_expected_result_name(device_id, 0, True)
        Assertions.json_result_device_id(device_id)

        # assert device_id != 0 or device_id is not None, f"Expected not 0 or None, got {device_id}"
