# new device - device status empty
import requests
import os
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions
from test_library.test_params import BaseUrlRequests as BUR
import allure


@allure.feature("Устройства")
@allure.description("создать новое устройство с пустым статусом")
class Test:
    request_body = {
        "name": "ngage",
        "model": "s55",
        "type": "TYPE_UNKNOWN",
        "status": "1DEVICE_STATUS_ACTIVE",
    }

    def test_add_new_device_empty_status(self):
        url_2 = "/v1/devices"

        response = BUR.url_post(self, url_2, None, None,
                                None, None, self.request_body)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()['result']['success'], False)
        Assertions.json_result_error(response.json()['result']['error'], "RequestNotValid")
        Assertions.json_result_errorCode(response.json()['result']['ErrorCode'], 900)
