# add new device
import os
import json
import requests
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions
from test_library.test_params import BaseUrlRequests as BUR
import allure


@allure.feature("Устройства")
@allure.description("изменить данные устройства")
class Test:
    request_body = {
        "name": "motorolla",
        "model": "e350",
        "type": "TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE"
    }

    request_body2 = {
        "name": "sony",
        "model": "m2",
        "type": "TYPE_UNKNOWN"
    }

    def test_add_change_data(self):
        url_2 = "/v1/devices"

        response = BUR.url_post(self, url_2, request_body=self.request_body)

        device_id = json.dumps(response.json().get("id"))

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], True)
        Assertions.json_result_errorData(response.json()["result"]["errorData"], {})
        Assertions.json_result_device_id(device_id)
        assert response.json()["name"] == "motorolla", f"Expected motorolla, got {response.json()['name']}"

        #################################################################################################################

        # change device info
        url_2 = "/v1/devices/"  # /v1/devices/
        response2 = BUR.url_put(self, url_2, url_3=device_id, request_body=self.request_body2)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response2.json(), response2.status_code,
                                 response2.url)

        Assertions.status_code_check(response2.status_code, 200)
        Assertions.json_result_success(response2.json()["result"]["success"], True)
        Assertions.json_result_errorData(response2.json()["result"]["errorData"], {})

        ################################################################################################################

        # check that device info was changed
        # url_2 = "/v1/devices/"  # /v1/devices/
        response3 = BUR.url_get(self, url_2, url_3=device_id, request_body=self.request_body2)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            DebugLogs.debug_logs(os.path.basename(__file__), response3.json(), response3.status_code, response3.url)

        device_id3 = json.dumps(response3.json().get("id"))
        Assertions.status_code_check(response3.status_code, 200)
        Assertions.json_result_success(response3.json()["result"]["success"], True)
        Assertions.json_result_errorData(response3.json()["result"]["errorData"], {})
        assert device_id == device_id3, f"Expected {device_id3}, got {device_id3}"
        assert response3.json()["name"] == "sony", f"Expected sony, got {response3.json()['name']}"
        assert response3.json()["model"] == "m2", f"Expected m2, got {response3.json()['model']}"
