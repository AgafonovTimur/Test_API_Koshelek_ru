# request number of devices
import os
from tests_library import tests_params, debug_log_true
from tests_library.debug_log_true import DebugLogs
from tests_library.assertions import Assertions
from tests_library.tests_params import BaseUrlRequests as BUR
import allure


@allure.feature("Устройства")
@allure.description("запросить список устройств")
class Test:
    def test_list_of_devices(self):
        url_2 = "/v1/devices"

        response = BUR.url_get(self, url_2)

        # debug log displays if debug_true = True
        if debug_log_true.debug_true:
            DebugLogs.debug_logs(os.path.basename(__file__), response.json(),
                                 response.status_code, response.url, url_2, method="GET")

        Assertions.status_code_check(response.status_code, 200)
        Assertions.json_result_success(response.json()["result"]["success"], True)
        Assertions.json_result_itemsCount_isinstance(response.json()["itemsCount"], int)
