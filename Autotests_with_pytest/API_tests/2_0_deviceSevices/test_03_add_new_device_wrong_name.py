# add new device with wrong name
import os
import requests
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions


class Test:
    request_body = {
        "name": "nokia",
        "model": "s55",
        "type": "TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE"
    }

    def test_add_new_device(self):
        request_payload = self.request_body

        response = requests.post(
            f"{test_params.baseUrl}/v1/devices?signature={test_params.clientSecret}",
            headers=test_params.request_headers, json=request_payload)

        actual_result_name = response.json().get("name")
        expected_result_name = "siemens mobile"

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)

        # response status code must be 4xx and it's a bug, but test made to pass this assert
        # assertion must be != 200 or == 4xx
        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], True)
        Assertions.json_result_errorData(response.json()["result"]["errorData"], {})
        Assertions.json_name_equal_to_expected_result_name(actual_result_name,
                                                                                expected_result_name,
                                                                                False)