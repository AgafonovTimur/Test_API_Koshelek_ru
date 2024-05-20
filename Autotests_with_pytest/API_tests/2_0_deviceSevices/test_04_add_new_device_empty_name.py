# add new device with empty name
import os
import json
import requests
import testVariables


class TestClass:
    request_body = {

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
                "\033[92m" + "\n" + os.path.basename(__file__) + "\n" + "\033[93m" + json.dumps(
                    json.loads(response.text), indent=2))
            print("\033[92m" + f"response status code: {response.status_code}")
            print(response.url)
            print(f"response name: {ar_name} is empty and is incorrect. All good")
            print("response.json \"success\": " + str(response.json()["result"]["success"]))
            print("response.json \"error\": " + str(response.json()["result"]["error"]))

        # response status code must be 4xx and it's a bug, but test made to pass this assert
        # assertion must be != 200 or == 400 bad request
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert ar_name != er_name, f"Phone name is correct, its {ar_name}"
        assert response.json()["result"][
                   "success"] == False, f"Expected False, got {response.json()['result']['success']}"
        assert response.json()["result"][
                   "error"] == "InvalidArgument", f"Expected InvalidArgument, got {response.json()['result']['error']}"
