# add new device
import os
import json
import requests
import test_params
import debug_log_true


class TestClass:
    request_body = {
        "name": "Nokia",
        "model": "5100",
        "type": "TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE"
    }

    def test_add_new_device(self):
        request_payload = self.request_body

        response = requests.post(
            f"{test_params.baseUrl}/v1/devices?signature={test_params.clientSecret}",
            headers=test_params.request_headers, json=request_payload)

        device_id = json.dumps(response.json().get("id"))

        #  create new device
        if debug_log_true.debug_true == True:
            debug_log_true.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)
            print("device_id: " + str(response.json().get("id")))
            print("name: " + str(response.json().get("name")))

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json()["result"][
                   "success"] == True, f"Expected True, got {response.json()['result']['success']}"
        assert response.json()["result"][
                   "errorData"] == {}, f"Expected {{}}, got {response.json()['result']['errorData']}"
        assert device_id != 0 or device_id is not None, f"Expected not 0 or None, got {device_id}"
        assert response.json()["name"] == "Nokia", f"Expected Nokia, got {response.json()['name']}"

##########################################################################################################

        #  delete device
        response2 = requests.delete(
            f"{test_params.baseUrl}/v1/devices/{device_id}?signature={test_params.clientSecret}",
            headers=test_params.request_headers)

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

        # check that device is not found
        response3 = requests.get(
            f"{test_params.baseUrl}/v1/devices/{device_id}?signature={test_params.clientSecret}",
            headers=test_params.request_headers)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            debug_log_true.debug_logs(os.path.basename(__file__), response3.json(), response3.status_code,
                                      response3.url)
            print("name: " + str(response3.json()["name"]))
            print("model: " + str(response3.json()["model"]))

        assert response3.status_code == 200, f"Expected 200, got {response3.status_code}"
        assert response3.json()["result"][
                   "success"] == False, f"Expected False, got {response3.json()['result']['success']}"
        assert response3.json()["result"][
                   "error"] == "NotFound", f"Expected NotFound, got {response3.json()['result']['error']}"
        assert response3.json()["result"][
                   "errorCode"] == 103, f"Expected 103, got {response3.json()['result']['errorCode']}"
        assert response3.json()["name"] == "", f"Expected \"\", got {response3.json()['name']}"
        assert response3.json()["model"] == "", f"Expected \"\", got {response3.json()['model']}"
