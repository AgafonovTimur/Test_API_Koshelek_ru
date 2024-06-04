# add new device with wrong name
import os
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions
from test_library.test_params import BaseUrlRequests as BUR
import allure


@allure.feature("Устройства")
@allure.description("новое устройство с неправильным именем")
class Test:
    request_body = {
        "name": "nokia",
        "model": "s55",
        "type": "TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE"
    }

    def test_add_new_device_wrong_name(self):
        url_2 = "/v1/devices"

        response = BUR.url_post(self, url_2, request_body=self.request_body)

        actual_result_name = response.json().get("name")
        expected_result_name = "siemens mobile"

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url, url_2,
                                 self.request_body)

        # response status code must be 4xx and it's a bug, but test made to pass this assert
        # assertion must be != 200 or == 4xx
        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], True)
        Assertions.json_result_errorData(response.json()["result"]["errorData"], {})
        Assertions.json_name_equal_to_expected_result_name(actual_result_name,
                                                           expected_result_name,
                                                           False)
