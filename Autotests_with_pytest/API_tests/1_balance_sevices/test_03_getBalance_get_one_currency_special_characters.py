# check currency with special characters
import os
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions
from test_library.test_params import BaseUrlRequests as BUR
import allure


@allure.feature("проверка баланса")
@allure.description("проверка что баланс с символами отображается некорректно")
class Test:
    def test_currency_special_characters(self):
        url_2 = "/v1/balances"
        url_currency = "currency=RU!%"

        response = BUR.url_get(self, url_2, url_currency=url_currency)

        if debug_log_true.debug_true:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url, url_2,
                                 url_currency, method="GET")

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], False)
        Assertions.json_result_error(response.json()["result"]["error"], "CurrencyNotFound")
        Assertions.json_result_errorCode(response.json()["result"]["errorCode"], 139)
