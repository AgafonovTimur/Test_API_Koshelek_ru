# add new device
import os
import json
import requests
import testVariables


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
            f"{testVariables.baseUrl}/v1/devices?signature={testVariables.clientSecret}",
            headers=testVariables.request_headers, json=request_payload)

        device_id = json.dumps(response.json().get("id"))

        #  create new device
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
        assert response.json()["name"] == "Nokia", f"Expected Nokia, got {response.json()['name']}"

        #  delete device
        response2 = requests.delete(
            f"{testVariables.baseUrl}/v1/devices/{device_id}?signature={testVariables.clientSecret}",
            headers=testVariables.request_headers)

        # debug log displays if debug_true = True
        if testVariables.debug_true == True:
            print(
                "\033[92m" + "\n" + os.path.basename(__file__) + " part 2\n" + "\033[93m" + json.dumps(
                    json.loads(response2.text), indent=2))
            print("\033[92m" + f"response status code: {response2.status_code}")
            print(response2.url)
            print("response.json \"success\": " + str(response2.json()["result"]["success"]))
            print("response.json \"errorData\": " + str(response2.json()["result"]["errorData"]))

        assert response2.status_code == 200, f"Expected 200, got {response2.status_code}"
        assert response2.json()["result"][
                   "success"] == True, f"Expected True, got {response2.json()['result']['success']}"
        assert response2.json()["result"][
                   "errorData"] == {}, f"Expected {{}}, got {response2.json()['result']['errorData']}"

        # check that device is not found
        response3 = requests.get(
            f"{testVariables.baseUrl}/v1/devices/{device_id}?signature={testVariables.clientSecret}",
            headers=testVariables.request_headers)

        # debug log displays if debug_true = True
        if testVariables.debug_true == True:
            print(
                "\033[92m" + "\n" + os.path.basename(__file__) + " part 3\n" + "\033[93m" + json.dumps(
                    json.loads(response3.text), indent=2))
            print("\033[92m" + f"response status code: {response3.status_code}")
            print(response3.url)
            print("response.json \"success\": " + str(response3.json()["result"]["success"]))
            print("response.json \"error\": " + str(response3.json()["result"]["error"]))
            print("response.json \"errorCode\": " + str(response3.json()["result"]["errorCode"]))
            print("response.json \"name\": " + str(response3.json()["name"]))
            print("response.json \"model\": " + str(response3.json()["model"]))

        assert response3.status_code == 200, f"Expected 200, got {response3.status_code}"
        assert response3.json()["result"][
                   "success"] == False, f"Expected False, got {response3.json()['result']['success']}"
        assert response3.json()["result"][
                   "error"] == "NotFound", f"Expected NotFound, got {response3.json()['result']['error']}"
        assert response3.json()["result"][
                   "errorCode"] == 103, f"Expected 103, got {response3.json()['result']['errorCode']}"
        assert response3.json()["name"] == "", f"Expected \"\", got {response3.json()['name']}"
        assert response3.json()["model"] == "", f"Expected \"\", got {response3.json()['model']}"
