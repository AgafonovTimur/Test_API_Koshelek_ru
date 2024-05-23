# check if authorization is correct

import os
import allure
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions
from test_library.test_params import BaseUrlRequests as BUR

@allure.feature("проверка авторизации ")
@allure.title("проверка авторизации с корректными данными")
class Test:
    def test_correct_auth(self):
        url_2 = "/v1/devices"

        response = BUR.url_get(self, url_2, None, None,
                               None, None, None)

        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(),
                                 response.status_code, response.url)

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], True)
        Assertions.json_result_errorData(response.json()["result"]["errorData"], {})
