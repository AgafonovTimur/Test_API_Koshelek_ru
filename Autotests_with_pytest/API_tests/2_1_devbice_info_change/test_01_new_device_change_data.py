# add new device
import os
import json
import requests
import test_params
import debug_log_true


class TestClass:
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
        request_payload = self.request_body
        request_payload2 = self.request_body2

        response = requests.post(
            f"{test_params.baseUrl}/v1/devices?signature={test_params.clientSecret}",
            headers=test_params.request_headers, json=request_payload)

        device_id = json.dumps(response.json().get("id"))

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            debug_log_true.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)
            print("name: " + str(response.json().get("name")))
            print(f"device_id: {device_id}")

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json()["result"][
                   "success"] == True, f"Expected True, got {response.json()['result']['success']}"
        assert response.json()["result"][
                   "errorData"] == {}, f"Expected {{}}, got {response.json()['result']['errorData']}"
        assert device_id != 0 or device_id is not None, f"Expected not 0 or None, got {device_id}"
        assert response.json()["name"] == "motorolla", f"Expected motorolla, got {response.json()['name']}"

#################################################################################################################

        # change device info
        response2 = requests.put(
            f"{test_params.baseUrl}/v1/devices/{device_id}?signature={test_params.clientSecret}",
            headers=test_params.request_headers, json=request_payload2)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            debug_log_true.debug_logs(os.path.basename(__file__), response2.json(), response2.status_code,
                                      response2.url)

        assert response2.status_code == 200, f"Expected 200, got {response2.status_code}"
        assert response2.json()["result"][
                   "success"] == True, f"Expected True, got {response2.json()['result']['success']}"
        assert response2.json()["result"][
                   "errorData"] == {}, f"Expected {{}}, got {response2.json()['result']['errorData']}"

################################################################################################################

        # check that device info was changed
        response3 = requests.get(
            f"{test_params.baseUrl}/v1/devices/{device_id}?signature={test_params.clientSecret}",
            headers=test_params.request_headers, json=request_payload2)
        device_id3 = json.dumps(response3.json().get("id"))

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            debug_log_true.debug_logs(os.path.basename(__file__), response3.json(), response3.status_code,
                                      response3.url)
            print("id: " + str(response3.json().get("id")))
            print("name: " + str(response3.json().get("name")))
            print("model: " + str(response3.json().get("model")))

        assert response3.status_code == 200, f"Expected 200, got {response3.status_code}"
        assert response3.json()["result"][
                   "success"] == True, f"Expected True, got {response3.json()['result']['success']}"
        assert response3.json()["result"][
                   "errorData"] == {}, f"Expected {{}}, got {response3.json()['result']['errorData']}"
        assert device_id == device_id3, f"Expected {device_id}, got {device_id3}"
        assert response3.json()["name"] == "sony", f"Expected sony, got {response3.json()['name']}"
        assert response3.json()["model"] == "m2", f"Expected m2, got {response3.json()['model']}"
