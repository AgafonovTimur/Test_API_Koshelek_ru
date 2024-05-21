import os
import json

debug_true = True


def prints(*args):
    file_name, response_json, status_code, url = args
    response = response_json
    print("\033[92m" + "\n" + file_name + "\n" + "\033[93m"
          + json.dumps(response, indent=2))
    print(status_code)
    print(url)
    print(response["result"]["success"])
    print(response["result"]["errorData"])

