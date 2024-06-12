import json

debug_true = True


class DebugLogs:
    if debug_true:
        @staticmethod
        def debug_logs(file_name, response_json, status_code, url, url_2, url_3=None, url_currency=None,
                       url_clientSecret=None,request_headers="", request_body="", method=None):
            print("\033[92m" + "\n" + file_name + "\n" + "\033[94m")
            print("----------------------------------------Request---------------------------------------")
            print("\033[93m" + "\n" + url)
            if method is not None: print(f"{str(method)} used in request")
            if url_3 is not None: print(url_3)
            if url_currency is not None: print(url_currency)
            if url_clientSecret is not None: print(url_clientSecret)
            if request_headers is not None: print(request_headers)
            if request_body is not None: print(request_body)
            print("\033[94m")
            print("----------------------------------------Response---------------------------------------")
            print("\033[93m" + "\n" + json.dumps(response_json, indent=2))
            print("\033[94m")
            print("----------------------------------------Assertions-------------------------------------")
            print("\033[92m")

