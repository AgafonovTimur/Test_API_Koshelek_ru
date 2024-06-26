# check can get balance
import os
from tests_library import tests_params, debug_log_true
from tests_library.debug_log_true import DebugLogs
from tests_library.assertions import Assertions
from tests_library.tests_params import BaseUrlRequests as BUR
import allure
import pytest


@allure.feature("проверка баланса")
@allure.description("проверка что баланс отображается некорректно")
class Test:
    @pytest.mark.parametrize(
        "url_currency_incorrect_params",
        [
            ("currency=RRUB"),
            ("currency=RrUB"),
            ("currency=RRuB"),
            ("currency=RRUb"),
            ("currency=RuUB"),
            ("currency=RUuB"),
            ("currency=RUBB"),
            ("currency=Rubb"),
            ("currency=RuBb"),
            ("currency=rubb"),
        ]
    )
    def test_currency_incorrect(self, url_currency_incorrect_params):
        url2 = "/v1/balances"

        response = BUR.url_get(self, url2, url_currency=url_currency_incorrect_params)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url, url2,
                                 url_currency_incorrect_params, method="GET")

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], False)
        Assertions.json_result_error(response.json()["result"]["error"], "CurrencyNotFound")
        Assertions.json_result_errorCode(response.json()["result"]["errorCode"], 139)
