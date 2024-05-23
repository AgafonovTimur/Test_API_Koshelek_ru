# add new device
import os
import json
import requests
from test_library import test_params, debug_log_true
from test_library.debug_log_true import DebugLogs
from test_library.assertions import Assertions
from test_library.test_params import BaseUrlRequests as BUR

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

    def test_add_new_device(self):
        url_2 = "/v1/devices"

        response = BUR.url_post(self, url_2, None, None, None, None, self.request_body)

        # request_payload = self.request_body
        # request_payload2 = self.request_body2

        # response = requests.post(
        #     f"{test_params.baseUrl}/v1/devices?signature={test_params.clientSecret}",
        #     headers=test_params.request_headers, json=request_payload)

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
        response2 = BUR.url_put(self, url_2, device_id, None, None, None, self.request_body2)

        # response2 = requests.put(
        #     f"{test_params.url_base}{url_2}{device_id}?signature=18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d48",
        #     headers={'Content-Type': 'application/json', 'ClientId': test_params.clientId}, json=self.request_body2)

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
        response3 = BUR.url_get(self, url_2, device_id, None, None, None, self.request_body2)

        # response3 = requests.get(
        #     f"{test_params.url_base}/v1/devices/{device_id}?signature=18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d48",
        #     headers={'Content-Type': 'application/json', 'ClientId': test_params.clientId}, json=self.request_body2)
        # # response3 = requests.get(
        #     f"https://p2psys-publicoffice.konomik.com/v1/devices/{device_id}?signature=signature=18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d48"
        # )

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
