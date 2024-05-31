# check if client ID is correct
import os
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions
from test_library.test_params import BaseUrlRequests as BUR
import allure
import pytest


# add no client ID
@allure.feature("проверка авторизации")
@allure.description("проверка авторизации с некорректными данными")
class Test:
    @pytest.mark.parametrize(
        "request_headers1_params",
        [
            {
                "Content-Type": "application/json",
                "ClientId": "ID-6892fc719fbc467bae2564f37fdb64f728070be92e744a18b7ede4842ad4181g"
            },
            {
                "Content-Type": "application/json",
                "ClientId": "ID-6892fc719fbc467bae2564f37fdb64f728070be92e744a18b7ede4842ad4181F"
            },
            {
                "Content-Type": "application/json",
                "ClientId": "id-6892fc719fbc467bae2564f37fdb64f728070be92e744a18b7ede4842ad4181f"
            },
            {
                "Content-Type": "application/json",
                "ClientId": "ID"
            },
            {
                "Content-Type": "application/json",
                "ClientId": ""
            },
            {
                "Content-Type": "application/json",
                "ClientId": "ID-ID-ID-ID-ID-ID-ID-ID-ID-ID-ID-ID-ID-ID-ID-ID-ID-ID-ID-ID-ID-ID-ID"
            },
            {
                "Content-Type": "application/json",
                "ClientId": "+7(111)111-11-11"},
            {
                "Content-Type": "application/json",
                "ClientId": "()(**&$@@@@_)___)++++___-----====-----(*$#######)(!!!!!!??????(*?*"
            },
            {
                "Content-Type": "application/json",
                "ClientId": "_"},
            {
                "Content-Type": "application/json",
                "ClientId": "ID-6892fC719fBC467BAE2564f37FDB64F728070BE92E744A18B7EDE4842AD4181F"
            },
            {
                "Content-Type": "application/json",
                "ClientId": "ClientId"
            },
        ],
    )
    def test_wrong_id(self, request_headers1_params):
        url_2 = "/v1/devices"

        response = BUR.url_get(self, url_2, request_headers=request_headers1_params)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url, url_2,
                                 request_headers1_params)

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], False)
        Assertions.json_result_error(response.json()["result"]["error"], "ApiKeyNotFound")
        Assertions.json_result_errorCode(response.json()["result"]["ErrorCode"], 125)
