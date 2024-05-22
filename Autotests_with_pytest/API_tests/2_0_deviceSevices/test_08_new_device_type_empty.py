# new device - empty type
import requests
import os
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions


class Test:
    request_body = {
        "name": "ngage",
        "model": "s55",
        "type": "",
        "status": "DEVICE_STATUS_ACTIVE",
    }

    def test_add_new_device(self):
        request_payload = self.request_body

        response = requests.post(
            f"{test_params.baseUrl}/v1/devices?signature={test_params.clientSecret}",
            headers=test_params.request_headers, json=request_payload)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()['result']['success'], False)
        Assertions.json_result_error(response.json()['result']['error'], "RequestNotValid")
        Assertions.json_result_errorCode(response.json()['result']['ErrorCode'], 900)

