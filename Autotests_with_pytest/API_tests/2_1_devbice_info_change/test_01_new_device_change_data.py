# add new device
import os
import json
import requests
import testVariables


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
            f"{testVariables.baseUrl}/v1/devices?signature={testVariables.clientSecret}",
            headers=testVariables.request_headers, json=request_payload)

        device_id = json.dumps(response.json().get("id"))

        # debug log displays if debug_true = True
        if testVariables.debug_true == True:
            print(
                "\033[92m" + "\n" + os.path.basename(__file__) + "\n" + "\033[93m" + json.dumps(
                    json.loads(response.text), indent=2))
            print("\033[92m" + f"response status code: {response.status_code}")
            print(response.url)
            print("response.json \"success\": " + str(response.json()["result"]["success"]))
            print("response.json \"errorData\": " + str(response.json()["result"]["errorData"]))
            print("response.json \"id\": " + str(response.json().get("id")))
            print("response.json \"name\": " + str(response.json().get("name")))

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json()["result"][
                   "success"] == True, f"Expected True, got {response.json()['result']['success']}"
        assert response.json()["result"][
                   "errorData"] == {}, f"Expected {{}}, got {response.json()['result']['errorData']}"
        assert device_id != 0 or device_id is not None, f"Expected not 0 or None, got {device_id}"
        assert response.json()["name"] == "motorolla", f"Expected motorolla, got {response.json()['name']}"

        # change device info
        response2 = requests.put(
            f"{testVariables.baseUrl}/v1/devices/{device_id}?signature={testVariables.clientSecret}",
            headers=testVariables.request_headers, json=request_payload2)
        device_id2 = json.dumps(response.json().get("id"))

        # debug log displays if debug_true = True
        if testVariables.debug_true == True:
            print(
                "\033[92m" + "\n" + os.path.basename(__file__) + "\n" + "\033[93m" + json.dumps(
                    json.loads(response2.text), indent=2))
            print("\033[92m" + f"response status code: {response2.status_code}")
            print(response2.url)
            print("response.json \"success\": " + str(response2.json()["result"]["success"]))
            print("response.json \"errorData\": " + str(response2.json()["result"]["errorData"]))
            print("response.json \"id\": " + str(response2.json().get("id")))

        assert response2.status_code == 200, f"Expected 200, got {response2.status_code}"
        assert response2.json()["result"][
                   "success"] == True, f"Expected True, got {response2.json()['result']['success']}"
        assert response2.json()["result"][
                   "errorData"] == {}, f"Expected {{}}, got {response2.json()['result']['errorData']}"
        assert device_id == device_id2, f"Expected {device_id}, got {device_id2}"

        # check that device info was changed
        response3 = requests.get(
            f"{testVariables.baseUrl}/v1/devices/{device_id}?signature={testVariables.clientSecret}",
            headers=testVariables.request_headers, json=request_payload2)
        device_id3 = json.dumps(response3.json().get("id"))

        # debug log displays if debug_true = True
        if testVariables.debug_true == True:
            print(
                "\033[92m" + "\n" + os.path.basename(__file__) + "\n" + "\033[93m" + json.dumps(
                    json.loads(response3.text), indent=2))
            print("\033[92m" + f"response status code: {response3.status_code}")
            print(response3.url)
            print("response.json \"success\": " + str(response3.json()["result"]["success"]))
            print("response.json \"errorData\": " + str(response3.json()["result"]["errorData"]))
            print("response.json \"id\": " + str(response3.json().get("id")))
            print("response.json \"name\": " + str(response3.json().get("name")))
            print("response.json \"model\": " + str(response3.json().get("model")))

        assert response3.status_code == 200, f"Expected 200, got {response3.status_code}"
        assert response3.json()["result"][
                   "success"] == True, f"Expected True, got {response3.json()['result']['success']}"
        assert response3.json()["result"][
                   "errorData"] == {}, f"Expected {{}}, got {response3.json()['result']['errorData']}"
        assert device_id == device_id3, f"Expected {device_id}, got {device_id3}"
        assert response3.json()["name"] == "sony", f"Expected sony, got {response3.json()['name']}"
        assert response3.json()["model"] == "m2", f"Expected m2, got {response3.json()['model']}"
