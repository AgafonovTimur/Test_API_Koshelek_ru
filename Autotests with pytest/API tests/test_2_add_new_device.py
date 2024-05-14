# add new device
import pytest
import json
import requests
import testVariables


class TestClass:
    phoneNames = [{
        "name": "siemens mobile",
        "model": "s55",
        "type": "TYPE_UNKNOWN",
        "status": "DEVICE_STATUS_ACTIVE"
    },
        {
            "name": "siemens mobile 2",
            "model": "s55",
            "type": "TYPE_UNKNOWN",
            "status": "DEVICE_STATUS_ACTIVE"
        },
        {

        }]

    @pytest.mark.parametrize("phoneName", phoneNames)
    def test_add_new_device(self, phoneName):
        headers1 = {'Content-Type': 'application/json', 'ClientId': testVariables.clientId}
        payload1 = phoneName
        response = requests.post(testVariables.baseUrl + "/v1/devices?signature=" + testVariables.clientSecret,
                                 headers=headers1, data=json.dumps(payload1))
        json_dumps = json.dumps(dict(response.json()))
        print(json_dumps)
        if len(phoneName) == 0:
            print("Phone name is empty")
        else:
            assert "siemens mobile" in json.dumps(
                dict(response.json())), f"Expected 'siemens mobile', got {json_dumps}"
            print(dict(response.json()))
            assert response.json().get("name") == phoneName.get("name")
            print(response.status_code)
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
