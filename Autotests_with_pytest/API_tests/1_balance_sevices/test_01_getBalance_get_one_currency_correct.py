# check currency is incorrect
import os
from tests_library import tests_params, debug_log_true
from tests_library.debug_log_true import DebugLogs
from tests_library.assertions import Assertions
from tests_library.tests_params import BaseUrlRequests as BUR
import allure
import pytest


# rUb Rub RUB rub
@allure.feature("проверка баланса")
@allure.description("проверка что баланс отображается корректно")
class Test:
    @staticmethod
    def currency_dict_correct_params():
        r_dict = ["r", "R"]
        u_dict = ["u", "U"]
        b_dict = ["b", "B"]
        currency_dict = []
        for r in r_dict:
            for u in u_dict:
                for b in b_dict:
                    currency_dict.append(r + u + b)
        return currency_dict

    @pytest.mark.parametrize("url_currency_correct_params", currency_dict_correct_params())
    def test_currency_correct(self, url_currency_correct_params):
        url_2 = "/v1/balances"

        response = BUR.url_get(self, url_2, url_currency=url_currency_correct_params)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url, url_2,
                                 url_currency_correct_params, method="GET")

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], True)
        Assertions.json_result_errorData(response.json()["result"]["errorData"], {})
