
import json

debug_true = True

class DebugLogs():
    def debug_logs(self, *args):
        file_name, response_json, status_code, url = args

        print("\033[92m" + "\n" + file_name + "\n" + "\033[93m"
              + json.dumps(response_json, indent=2))
        print("\033[92m" + f"response status code: {status_code}")
        print(url)

