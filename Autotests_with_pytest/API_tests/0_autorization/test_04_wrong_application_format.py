import os
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions
from test_library.test_params import BaseUrlRequests as BUR
import allure
import pytest


@allure.feature("проверка авторизации")
@allure.description("проверка только json формата. Не важно какой формат передаётся : xml, json, prettyjson, "
                    "javascript, soap+xml - все форматы проходят - BUG")
class Test:

    @pytest.mark.parametrize(
        "request_headers",
        [
            {
                "Content-Type": "application/xml",
                "ClientId": "ID-6892fc719fbc467bae2564f37fdb64f728070be92e744a18b7ede4842ad4181f"
            },
            {
                "Content-Type": "application/json+xml",
                "ClientId": "ID-6892fc719fbc467bae2564f37fdb64f728070be92e744a18b7ede4842ad4181f"
            },
            {
                "Content-Type": "application/prettyjson",
                "ClientId": "ID-6892fc719fbc467bae2564f37fdb64f728070be92e744a18b7ede4842ad4181f"
            },
            {
                "Content-Type": "application/javascript",
                "ClientId": "ID-6892fc719fbc467bae2564f37fdb64f728070be92e744a18b7ede4842ad4181f"
            },
            {
                "Content-Type": "application/vnd.api+json",
                "ClientId": "ID-6892fc719fbc467bae2564f37fdb64f728070be92e744a18b7ede4842ad4181f"
            },
            {
                "Content-Type": "application/soap+xml",
                "ClientId": "ID-6892fc719fbc467bae2564f37fdb64f728070be92e744a18b7ede4842ad4181f"
            },
            {
                "Content-Type": "application/rss+xml",
                "ClientId": "ID-6892fc719fbc467bae2564f37fdb64f728070be92e744a18b7ede4842ad4181f"
            },
            {
                "Content-Type": "application/graphql",
                "ClientId": "ID-6892fc719fbc467bae2564f37fdb64f728070be92e744a18b7ede4842ad4181f"
            },
        ],
    )
    def test_wrong_id(self, request_headers):
        url_2 = "/v1/devices"

        response = BUR.url_get(self, url_2, request_headers=request_headers)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], True)
        Assertions.json_result_errorData(response.json()["result"]["errorData"], {})
