# add new device
import os
import json
import requests
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions


class Test:
    request_body = {
        "name": "Nokia",
        "model": "5100",
        "type": "TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE"
    }

    def test_add_new_device(self):
        request_payload = self.request_body

        response = requests.post(
            f"{test_params.baseUrl}/v1/devices?signature={test_params.clientSecret}",
            headers=test_params.request_headers, json=request_payload)

        device_id = json.dumps(response.json().get("id"))

        #  create new device
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], True)
        Assertions.json_result_errorData(response.json()["result"]["errorData"], {})
        Assertions.json_result_device_id(device_id)
        assert response.json()["name"] == "Nokia", f"Expected Nokia, got {response.json()['name']}"

        ##########################################################################################################

        #  delete device
        response2 = requests.delete(
            f"{test_params.baseUrl}/v1/devices/{device_id}?signature={test_params.clientSecret}",
            headers=test_params.request_headers)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response2.json(), response2.status_code,
                                 response2.url)

        Assertions.status_code_check(response2.status_code, 200)
        Assertions.json_result_success(response2.json()["result"]["success"], True)
        Assertions.json_result_errorData(response2.json()["result"]["errorData"], {})

        ################################################################################################################

        # check that device is not found
        response3 = requests.get(
            f"{test_params.baseUrl}/v1/devices/{device_id}?signature={test_params.clientSecret}",
            headers=test_params.request_headers)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response3.json(), response3.status_code,
                                 response3.url)

        Assertions.status_code_check(response3.status_code, 200)
        Assertions.json_result_success(response3.json()["result"]["success"], False)
        Assertions.json_result_error(response3.json()["result"]["error"], "NotFound")
        Assertions.json_result_errorCode(response3.json()["result"]["errorCode"], 103)
        assert response3.json()["name"] == "", f"Expected \"\", got {response3.json()['name']}"
        assert response3.json()["model"] == "", f"Expected \"\", got {response3.json()['model']}"
