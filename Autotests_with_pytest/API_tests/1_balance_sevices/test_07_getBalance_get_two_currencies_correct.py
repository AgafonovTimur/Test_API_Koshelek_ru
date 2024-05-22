# check two currencies is correct
import os
import requests
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions


class Test:
    def test_correct_auth(self):
        currency_usd = "currency=USD"

        response = requests.get(
            f"{test_params.baseUrl}/v1/balances?{test_params.currency}&{currency_usd}&signature={test_params.clientSecret}",
            headers=test_params.request_headers)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], True)
        Assertions.json_result_errorData(response.json()["result"]["errorData"], {})

