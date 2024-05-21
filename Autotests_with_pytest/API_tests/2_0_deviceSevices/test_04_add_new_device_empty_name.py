# add new device with empty name
import os
import debug_log_true
import requests
import test_params


class TestClass:
    request_body = {

    }

    def test_add_new_device(self):
        request_payload = self.request_body

        response = requests.post(
            f"{test_params.baseUrl}/v1/devices?signature={test_params.clientSecret}",
            headers=test_params.request_headers, json=request_payload)

        ar_name = response.json().get("name")  # actual response name
        er_name = "siemens mobile"  # expected response name

        # debug log displays if debug_true = True
        if debug_log_true.debug_true == True:
            debug_log_true.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)
            print(f"response name: {ar_name} is empty and is incorrect. All good")

        # assertion must be != 200 or == 400 bad request
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert ar_name != er_name, f"Phone name is correct, its {ar_name}"
        assert response.json()["result"][
                   "success"] == False, f"Expected False, got {response.json()['result']['success']}"
        assert response.json()["result"][
                   "error"] == "InvalidArgument", f"Expected InvalidArgument, got {response.json()['result']['error']}"
