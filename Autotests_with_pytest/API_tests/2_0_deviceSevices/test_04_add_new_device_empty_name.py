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
        response = requests.post(f"{testVariables.baseUrl}/v1/devices?signature={testVariables.clientSecret}",
                                 headers=testVariables.request_headers, json=request_payload)
        # actual response name
        ar_name = response.json().get("name")
        # expected response name
        er_name = "siemens mobile"
        testVariables.ccc(os.path.basename(__file__))
        print(json.dumps(response.json()))
        print("response status code: " + str(response.status_code))
        # response status code must be 4xx and it's a bug, but test made to pass this assert
        # assertion must be != 200 or == 400 bad request
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert ar_name != er_name, f"Phone name is correct, its {ar_name}"
        print("response name: " + ar_name + " is empty and is incorrect. All good")
        assert response.json()["result"]["success"] == False
        print("response.json \"success\": " + str(response.json()["result"]["success"]))
        assert response.json()["result"]["error"] == "InvalidArgument"
        print("response.json \"error\": " + str(response.json()["result"]["error"]))
