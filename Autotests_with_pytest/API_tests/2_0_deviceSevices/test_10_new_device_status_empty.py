# new device - device status empty
import requests
import os
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs

class Test:
    request_body = {
        "name": "ngage",
        "model": "s55",
        "type": "TYPE_UNKNOWN",
        "status": "1DEVICE_STATUS_ACTIVE",
    }

    def test_add_new_device(self):
        request_payload = self.request_body

        response = requests.post(
            f"{test_params.baseUrl}/v1/devices?signature={test_params.clientSecret}",
            headers=test_params.request_headers, json=request_payload)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(self, os.path.basename(__file__), response.json(), response.status_code, response.url)

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json()['result'][
                   'success'] == False, f"Expected False, got {response.json()['result']['success']}"
        assert response.json()['result'][
                   'error'] == "RequestNotValid", f"Expected RequestNotValid, got {response.json()['result']['error']}"
        assert response.json()['result'][
                   'ErrorCode'] == 900, f"Expected 900, got {response.json()['result']['ErrorCode']}"
