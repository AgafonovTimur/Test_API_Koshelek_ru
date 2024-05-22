# check currency is incorrect
import os
import requests
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs


class Test:
    def test_correct_auth(self):
        response = requests.get(
            f"{test_params.baseUrl}/v1/balances?{test_params.currency}&signature={test_params.clientSecret}",
            headers=test_params.request_headers)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(self, os.path.basename(__file__), response.json(), response.status_code, response.url)

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json()["result"][
                   "success"] == True, f"Expected True, got {response.json()['result']['success']}"
        assert response.json()["result"][
                   "errorData"] == {}, f"Expected {{}}, got {response.json()['result']['errorData']}"
