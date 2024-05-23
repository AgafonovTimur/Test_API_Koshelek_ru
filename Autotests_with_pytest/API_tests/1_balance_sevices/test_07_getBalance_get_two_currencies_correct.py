# check two currencies is correct
import os
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions
from test_library.test_params import BaseUrlRequests as BUR
import allure


@allure.feature("проверка баланса")
@allure.description("проверка что баланс с двумя валютами отображается корректно")
class Test:
    def test_currency_correct(self):
        url_2 = "/v1/balances"
        url_currency = "currency=USD"

        response = BUR.url_get(self, url_2, url_currency=url_currency)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], True)
        Assertions.json_result_errorData(response.json()["result"]["errorData"], {})
