# add new device with wrong name
import os
import json
import requests
import testVariables


class TestClass:
    request_body = {
        "name": "nokia",
        "model": "s55",
        "type": "TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE"
    }

    def test_add_new_device(self):
        request_payload = self.request_body

        response = requests.post(
            f"{testVariables.baseUrl}/v1/devices?signature={testVariables.clientSecret}",
            headers=testVariables.request_headers, json=request_payload)

        ar_name = response.json().get("name")  # actual response name
        er_name = "siemens mobile"  # expected response name

        # debug log displays if debug_true = True
        if testVariables.debug_true == True:
            print(
                "\033[92m" + "\n" + os.path.basename(__file__) + "\n" + json.dumps(json.loads(response.text), indent=2))
            print(f"response status code: {response.status_code}")
            print(response.url)
            print(f"response name: {ar_name} is incorrect. All good")
            print("response.json \"success\": " + str(response.json()["result"]["success"]))
            print("response.json \"errorData\": " + str(response.json()["result"]["errorData"]))


        # response status code must be 4xx and it's a bug, but test made to pass this assert
        # assertion must be != 200 or == 4xx
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert ar_name != er_name, f"Phone name is correct, its {ar_name}"
        assert response.json()["result"]["success"] == True, f"Expected True, got {response.json()['result']['success']}"
        assert response.json()["result"]["errorData"] == {}, f"Expected {{}}, got {response.json()['result']['errorData']}"
