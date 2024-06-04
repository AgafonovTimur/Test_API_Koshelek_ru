import os
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions
from test_library.test_params import BaseUrlRequests as BUR
import allure
import pytest


#  add no client secret
@allure.feature("проверка авторизации")
# @allure.description("проверка авторизации с некорректным данными")
class Test:

    @pytest.mark.parametrize(
        "url_clientSecret_params",
        [
            ("18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d49"),
            ("18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d47"),
            ("A8c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff93d2f1520d4222229"),
            ("23c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff93d2f1520d42222"),
            ("!!@#$%^fwefwefweff^&*^&*^(*&^*&^*&^#6481764964#$*!&^$*^!$"),
            ("gjerkjgjerjgjerojgапоукщшопщшукопозщукопшщоукщпощшуокШО№ЩШОШ№О;ШЩООШО;ОЩ№;О"),
            ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@&&&&&&&&&&&"),
            ("")
        ]
    )
    def test_wrong_secret(self, url_clientSecret_params):
        '''
    1
    описание теста 2
    тут шаг 1
    тут шаг 2
    тут шаг 3
    тут шаг 4
    2
    3
    '''

        url_2 = "/v1/balances"

        response = BUR.url_get(self, url_2=url_2, url_clientSecret=url_clientSecret_params)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url, url_2,
                                 url_clientSecret_params)

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], False)
        Assertions.json_result_error(response.json()["result"]["error"], "SignatureNotValid")
        Assertions.json_result_errorCode(response.json()["result"]["ErrorCode"], 115)
