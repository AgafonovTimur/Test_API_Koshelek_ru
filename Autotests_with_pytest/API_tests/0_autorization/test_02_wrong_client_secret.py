# check if authorization is correct
import os
import requests
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions


class Test:
    def test_correct_auth(self):  # sourcery skip: extract-method
        response = requests.get(
            f"{test_params.baseUrl}/v1/devices?signature=18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d49",
            # +1 at the end
            headers=test_params.request_headers)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], False)
        Assertions.json_result_error(response.json()["result"]["error"], "SignatureNotValid")
        Assertions.json_result_errorCode(response.json()["result"]["ErrorCode"], 115)
