# add new device
import json
import requests
import testVariables


class TestTwo:
    def test_add_new_device(self):
        headers1 = {'Content-Type': 'application/json', 'ClientId': testVariables.clientId}
        payload1 = {
            "name": "siemens mobile",
            "model": "s55",
            "type": "TYPE_UNKNOWN",
            "status": "DEVICE_STATUS_ACTIVE"
        }
        response = requests.post(testVariables.baseUrl + "/v1/devices?signature=" + testVariables.clientSecret,
                                 headers=headers1, data=json.dumps(payload1))

        print(json.dumps(dict(response.headers)))
        print(dict(response.cookies))
        print(response.text)
        print(response.json().get("id"))
        print(response.json().get("name"))
        assert response.json().get(
            "name") == "siemens mobile", f"Expected siemens mobile, got {response.json().get("name")}"
        print(response.status_code)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

