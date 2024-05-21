import os
import json

debug_true = True


def debug_logs(*args):
    file_name, response_json, status_code, url = args

    print("\033[92m" + "\n" + file_name + "\n" + "\033[93m"
          + json.dumps(response_json, indent=2))
    print("\033[92m" + f"response status code: {status_code}")
    print(url)

    # if response_json["result"].get("success") is not None:                     # success
    #     print("success : " + str(response_json["result"].get("success")))
    # if response_json["result"].get("errorData") is not None:                    # errorData
    #     print("errorData : " + str(response_json["result"].get("errorData")))
    # if response_json["result"].get("error") is not None:                        # error
    #     print("error : " + response_json["result"].get("error"))
    # if response_json["result"].get("errorCode") is not None:                    # errorCode
    #     print("errorCode : " + str(response_json["result"].get("errorCode")))
    # if response_json.get("items") is not None:                                  # items
    #     print("items : " + str(response_json.get("items")))
    #
    # if response_json.get("total") is not None:                                # total
    #     print(response_json.get("total"))
    # if response_json.get("total") is not None:                                # total - isInstance
    #     print(isinstance(response_json.get("total"), int))
    # if response_json.get("itemsCount") is not None:                           # itemsCount
    #     print(response_json.get("itemsCount"))
    # if response_json.get("itemsCount") is not None:                           # itemsCount - IsInstance
    #     print(isinstance(response_json.get("itemsCount"), int))

