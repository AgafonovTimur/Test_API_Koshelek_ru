# if device created - check stats
import pytest
import json
import requests
import testVariables
import pytest
from test_6_add_new_device_with_extra_field import TestClass


class TestClass2:
    request_body = {
        "name": "ngage",
        "model": "s55",
        "type": "TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE",
        "my_id": "device-id"  # my_id does not exist
    }

    # def test_add_new_device(self):
        # request_payload = self.request_body
        # response = requests.get(testVariables.baseUrl + "/v1/devices?signature=" + testVariables.clientSecret,
        #                         headers=testVariables.request_headers, data=json.dumps(request_payload))
        # print("\033[92m")
        # with open('ttest_111.py', 'r') as file:
        #     device_id = file.read()
        #
        # print("device_id: " + str(device_id))
        # # class123 = TestClass()
        # # d_id = class123.test_add_new_device()
        # # # pytest.device_id = d_id.json.dumps(response.json().get("id"))
        # # print("d_id: " + str(d_id))
        # # print(device_id)
        # # print(pytest.device_ID)
        # # assert pytest.device_ID == 12
        # # print(device_ID)
        # # print("response status code: " + str(response.status_code))
        # # response status code must be 4xx and it's a bug, but test made to pass this assert
        # # assertion must be != 200 or == 400 bad request
        # # assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        # # assert response.json()["result"]["success"] == True
        # # print("response.json \"success\": " + str(response.json()["result"]["success"]))
        # # assert response.json()["result"]["errorData"] == {}
        # # print("response.json \"errorData\": " + str(response.json()["result"]["errorData"]))
        # # print("response.json \"id\": " + str(response.json().get("id")))
