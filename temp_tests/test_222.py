# add new device
import os
import json
import requests
import testVariables


class TestClass:
    request_body = {
        "name": "siemens mobile",
        "model": "s55",
        "type": "TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE"
    }

    def test_add_new_device(self):
        request_payload = self.request_body
        response = requests.post(testVariables.baseUrl + "/v1/devices?signature=" + testVariables.clientSecret,
                                 headers=testVariables.request_headers, data=json.dumps(request_payload))
        # actual response name
        # ar_name = response.json().get("name")
        # # expected response name
        # er_name = "siemens mobile"
        testVariables.ccc(os.path.basename(__file__))
        print(json.dumps(response.json()))
        # print("response status code: " + str(response.status_code))
        # assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        # testVariables.device_id = 12
        with open('test_111.py', 'r') as file:
            script_content = file.read()

        script_content = script_content.replace('device_id =', 'device_id = 7 ')

        with open('test_111.py', 'w') as file:
            file.write(script_content)













