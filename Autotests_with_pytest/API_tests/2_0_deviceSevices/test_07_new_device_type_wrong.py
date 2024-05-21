# new device - wrong type

import debug_log_true
import requests
import test_params
import os


class TestClass2:
    request_body = {
        "name": "ngage",
        "model": "s55",
        "type": "1TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE",
    }

    def test_add_new_device(self):
        request_payload = self.request_body

        response = requests.post(
            f"{test_params.baseUrl}/v1/devices?signature={test_params.clientSecret}",
            headers=test_params.request_headers, json=request_payload)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            debug_log_true.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json()['result'][
                   'success'] == False, f"Expected False, got {response.json()['result']['success']}"
        assert response.json()['result'][
                   'error'] == "RequestNotValid", f"Expected RequestNotValid, got {response.json()['result']['error']}"
        assert response.json()['result'][
                   'ErrorCode'] == 900, f"Expected 900, got {response.json()['result']['ErrorCode']}"
