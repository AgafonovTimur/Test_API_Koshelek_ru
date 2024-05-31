# new device - wrong type

import os
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions
from test_library.test_params import BaseUrlRequests as BUR
import allure


@allure.feature("Устройства")
@allure.description("создать новое устройство с опечаткой в типе")
class Test:
    request_body = {
        "name": "ngage",
        "model": "s55",
        "type": "1TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE",
    }

    def test_add_new_device_wrong_type(self):
        url_2 = "/v1/devices"

        response = BUR.url_post(self, url_2, request_body=self.request_body)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url, url_2,
                                 self.request_body)

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()['result']['success'], False)
        Assertions.json_result_error(response.json()['result']['error'], "RequestNotValid")
        Assertions.json_result_errorCode(response.json()['result']['ErrorCode'], 900)
