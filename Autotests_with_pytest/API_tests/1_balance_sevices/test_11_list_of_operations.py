# check list of operations
import os
import requests
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions
from test_library.test_params import BaseUrlRequests as BUR


class Test:
    def test_list_of_operations(self):  # sourcery skip: extract-method
        url_2 = "/v1/balances/operations"

        response = BUR.url_get(self, url_2, None, None,
                               None, None, None)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], True)
        Assertions.json_result_errorData(response.json()["result"]["errorData"], {})
        Assertions.json_result_items(response.json()["items"], [])
        Assertions.json_result_total_isinstance(response.json()["total"], int)
