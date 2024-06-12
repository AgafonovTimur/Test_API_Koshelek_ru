from tests_library import debug_log_true
import allure


class Assertions:
    @staticmethod
    def status_code_check(response: object, status_code: int):
        if debug_log_true.debug_true:
            print(f"Expected response code: {status_code}, got {response}")
        with allure.step(f"Response code check. Expected {status_code}, got {response}"):
            assert response == status_code, f"Expected {status_code}, got {response}"

    @staticmethod
    def json_result_success(success: bool, expected_result):
        if debug_log_true.debug_true:
            print(f"Expected json: {expected_result}, got {success}")
        with allure.step(f"Success check. Expected {expected_result}, got {success}"):
            assert success == expected_result, f"Expected {expected_result}, got {success}"

    @staticmethod
    def json_result_errorData(errorData: bool, expected_result):
        if debug_log_true.debug_true:
            print(f"Expected errorData: {expected_result}, got {errorData}")
        with allure.step(f"Error data check. Expected {expected_result}, got {errorData}"):
            assert errorData == expected_result, f"Expected {expected_result}, got {errorData}"

    @staticmethod
    def json_result_error(error: bool, expected_result):
        if debug_log_true.debug_true:
            print(f"Expected error: {expected_result}, got {error}")
        with allure.step(f"Error check. Expected {expected_result}, got {error}"):
            assert error == expected_result, f"Expected {expected_result}, got {error}"

    @staticmethod
    def json_result_errorCode(ErrorCode: bool, expected_result):
        if debug_log_true.debug_true:
            print(f"Expected errorCode: {expected_result}, got {ErrorCode}")
        with allure.step(f"Error code check. Expected {expected_result}, got {ErrorCode}"):
            assert ErrorCode == expected_result, f"Expected {expected_result}, got {ErrorCode}"

    @staticmethod
    def json_name_equal_to_expected_result_name(actual_result_name, expected_result, eql):
        if debug_log_true.debug_true:
            print(f"Expected json_name: {expected_result}, got {actual_result_name}")
        if eql:
            with allure.step(f"Name check. Expected {expected_result}, got {actual_result_name}"):
                assert actual_result_name == expected_result, f"Expected {expected_result}, got {actual_result_name}"
        elif not eql:
            with allure.step(f"Name check. Expected {expected_result}, got {actual_result_name}"):
                assert actual_result_name != expected_result, f"Expected {expected_result}, got {actual_result_name}"
        else:
            with allure.step(f"Name check. Expected {expected_result}, got {actual_result_name}, but Exception raised"):
                raise Exception("actual_result_name or expected_result must be True or False")

    @staticmethod
    def json_result_device_id(actual_result_name):
        if debug_log_true.debug_true:
            print(f"Expected device_id: {actual_result_name} != 0 and not None")
        with allure.step(f"Name check. Expected {actual_result_name} != 0 and not None"):
            assert actual_result_name != 0 and not None, f"Result {actual_result_name} != 0 and not None"

    @staticmethod
    def json_result_items(items: bool, expected_result):
        if debug_log_true.debug_true:
            print(f"Expected json_items: {expected_result}, got {items}")
        with allure.step(f"Items check. Expected {expected_result}, got {items}"):
            assert items == expected_result, f"Expected {expected_result}, got {items}"

    @staticmethod
    def json_result_total_isinstance(is_instance, expected_result):
        if debug_log_true.debug_true:
            print(f"Expected isinstance: {expected_result}, got {is_instance}")
        with allure.step(f"Is_instance and not None. Expected {expected_result}, got {is_instance}"):
            assert isinstance(is_instance,
                              expected_result) and not None, f"Expected {expected_result}, got {is_instance}"

    @staticmethod
    def json_result_itemsCount_isinstance(is_instance, expected_result):
        if debug_log_true.debug_true:
            print(f"Expected isinstance: {expected_result}, got {is_instance}")
        with allure.step(f"Is_instance and not None. Expected {expected_result}, got {is_instance}"):
            assert isinstance(is_instance,
                              expected_result) and not None, f"Expected {expected_result}, got {is_instance}"
