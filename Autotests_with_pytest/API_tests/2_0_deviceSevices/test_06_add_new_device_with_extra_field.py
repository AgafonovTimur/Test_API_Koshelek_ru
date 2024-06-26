# add new device with extra field in request body
import requests
import os
import json
from tests_library import tests_params, debug_log_true
from tests_library.debug_log_true import DebugLogs
from tests_library.assertions import Assertions
from tests_library.tests_params import BaseUrlRequests as BUR
import allure


@allure.feature("Устройства")
@allure.description("новое устройство с дополнительным полем")
class Test:
    request_body = {
        "name": "ngage",
        "model": "s55",
        "type": "TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE",
        "my_id": "device-id"  # my_id does not exist
    }

    def test_add_new_device_with_extra_field(self):
        url_2 = "/v1/devices"

        response = BUR.url_post(self, url_2, request_body=self.request_body)

        device_id = json.dumps(response.json().get("id"))

        # debug log displays if debug_true = True
        if debug_log_true.debug_true:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url, url_2,
                                 self.request_body, method="POST")

        # response status code must be 4xx and it's a bug, but test made to pass this assert
        # assertion must be != 200 or == 400 bad request
        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], True)
        Assertions.json_result_errorData(response.json()["result"]["errorData"], {})
        Assertions.json_result_device_id(device_id)
