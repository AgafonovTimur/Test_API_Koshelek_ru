# add new device
import os
from tests_library import tests_params, debug_log_true
from tests_library.debug_log_true import DebugLogs
from tests_library.assertions import Assertions
from tests_library.tests_params import BaseUrlRequests as BUR
import allure


@allure.feature("Устройства")
@allure.description("создать новое устройство")
class Test:
    request_body = {
        "name": "siemens mobile",
        "model": "s55",
        "type": "TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE"
    }

    def test_add_new_device(self):
        url_2 = "/v1/devices"

        response = BUR.url_post(self, url_2, request_body=self.request_body)

        actual_result_name = response.json().get("name")
        expected_result_name = "siemens mobile"

        with allure.step(f"Перейти на сайт добавив = '{url_2}' и request_body = {self.request_body}"):
            pass
        with allure.step(f"проверить что {actual_result_name} = {expected_result_name}"):
            pass
        with allure.step(f"тут шаг 3"):
            pass
        with allure.step("тут шаг 4"):
            pass
        with allure.step("---------------------------------------Проверки--------------------------------------"):
            pass

        # debug log displays if debug_true = True
        if debug_log_true.debug_true:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url, url_2,
                                 self.request_body, method="POST")
            print(f"response name: {actual_result_name} is correct. All good")

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], True)
        Assertions.json_result_errorData(response.json()["result"]["errorData"], {})
        Assertions.json_name_equal_to_expected_result_name(actual_result_name,
                                                           expected_result_name,
                                                           True)
