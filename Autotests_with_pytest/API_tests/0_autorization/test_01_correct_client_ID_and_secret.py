import os
import allure
import pytest

from tests_library import tests_params, debug_log_true
from tests_library.debug_log_true import DebugLogs
from tests_library.assertions import Assertions
from tests_library.tests_params import BaseUrlRequests as BUR


@pytest.mark.smoke
@allure.feature("проверка авторизации ")
@allure.description("проверка авторизации с корректными данными")
class Test:
    def test_correct_auth(self):
        """
    1
    описание теста 1
    тут шаг 1
    тут шаг 2
    тут шаг 3
    тут шаг 4
    2
    3
    """
        url_2 = "/v1/balances"

        response = BUR.url_get(self, url_2=url_2)

        if debug_log_true.debug_true:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(),
                                 response.status_code, response.url, url_2, method="GET")

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], True)
        Assertions.json_result_errorData(response.json()["result"]["errorData"], {})
