from test_library import debug_log_true


class Assertions:
    @staticmethod
    def status_code_check(response: object, status_code: int):
        assert response == status_code, f"Expected {status_code}, got {response}"

    @staticmethod
    def json_result_success(success: bool, expected_result):
        if debug_log_true.debug_true == True:
            print(f"Expected {expected_result}, got {success}")
        assert success == expected_result, f"Expected {expected_result}, got {success}"

    @staticmethod
    def json_result_errorData(errorData: bool, expected_result):
        if debug_log_true.debug_true == True:
            print(f"Expected {expected_result}, got {errorData}")
        assert errorData == expected_result, f"Expected {expected_result}, got {errorData}"

    @staticmethod
    def json_result_error(error: bool, expected_result):
        if debug_log_true.debug_true == True:
            print(f"Expected {expected_result}, got {error}")
        assert error == expected_result, f"Expected {expected_result}, got {error}"

    @staticmethod
    def json_result_errorCode(ErrorCode: bool, expected_result):
        if debug_log_true.debug_true == True:
            print(f"Expected {expected_result}, got {ErrorCode}")
        assert ErrorCode == expected_result, f"Expected {expected_result}, got {ErrorCode}"

    @staticmethod
    def json_name_equal_to_expected_result_name(actual_result_name, expected_result, eql):
        if debug_log_true.debug_true == True:
            print(f"Expected {expected_result}, got {actual_result_name}")
        if eql == True:
            assert actual_result_name == expected_result, f"Expected {expected_result}, got {actual_result_name}"
        elif eql == False:
            assert actual_result_name != expected_result, f"Expected {expected_result}, got {actual_result_name}"
        else:
            raise Exception("actual_result_name or expected_result must be True or False")

    @staticmethod
    def json_result_device_id(actual_result_name):
        if debug_log_true.debug_true == True:
            print(f"Expected {actual_result_name} != 0 and not None")
        assert actual_result_name != 0 and not None, f"Result {actual_result_name} != 0 and not None"

    @staticmethod
    def json_result_items(items: bool, expected_result):
        if debug_log_true.debug_true == True:
            print(f"Expected {expected_result}, got {items}")
        assert items == expected_result, f"Expected {expected_result}, got {items}"


    @staticmethod
    def json_result_total_isinstance(is_instance, expected_result):
        if debug_log_true.debug_true == True:
            print(f"Expected {expected_result}, got {is_instance}")
        assert isinstance(is_instance, expected_result) and not None, f"Expected {expected_result}, got {is_instance}"

    @staticmethod
    def json_result_itemsCount_isinstance(is_instance, expected_result):
        if debug_log_true.debug_true == True:
            print(f"Expected {expected_result}, got {is_instance}")
        assert isinstance(is_instance, expected_result) and not None, f"Expected {expected_result}, got {is_instance}"









    # if response_json.get("total") is not None:                                # total
    #     print(response_json.get("total"))
    # if response_json.get("total") is not None:                                # total - isInstance
    #     print(isinstance(response_json.get("total"), int))

    # @staticmethod
    # def assert_json_has_key(response: object, key: str):
    #     try:
    #         response_as_dict = response.json()
    #     except json.JSONDecodeError:
    #         assert False, f"Response is not in JSON format. Response text is '{response.text}'"
    #
    #     assert key in response_as_dict, f"Response JSON doesn't have key '{key}'"
    #
    # @staticmethod
    # def assert_json_has_keys(response: object, keys: list):
    #     try:
    #         response_as_dict = response.json()
    #     except json.JSONDecodeError:
    #         assert False, f"Response is not in JSON format. Response text is '{response.text}'"
    #
    #     for key in keys:
    #         assert key in response_as_dict, f"Response JSON doesn't have key '{key}'"
