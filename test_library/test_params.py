# global variables
import requests


clientId = "ID-6892fc719fbc467bae2564f37fdb64f728070be92e744a18b7ede4842ad4181f"
url_base = "https://p2psys-publicoffice.konomik.com"
# request_headers1 = {'Content-Type': 'application/json', 'ClientId': clientId}
url_currency = "currency=RUB"
url_signature = "&signature="


# 1  url_base = "https://p2psys-publicoffice.konomik.com"
# 2 = url_2 = "/v1/devices"
# 3 = url_3 = device_id
# 4 = url_currency = "currency=RUB"
# 5 = url_signature = "&signature="
# 6 = url_clientSecret


class BaseUrlRequests:
    def url_get(self, url_2, url_3, url_currency, url_clientSecret, request_headers, request_body):

        if url_2 is None:
            url_2 = ""
        if url_3 is None:
            url_3 = ""
        if url_currency is None:
            url_currency = ""
        if url_clientSecret is None:
            url_clientSecret = "18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d48"
        if request_headers is None:
            request_headers = {'Content-Type': 'application/json', 'ClientId': clientId}
        if request_body is None:
            request_body = ""

        response = requests.get(f"{url_base}{url_2}{url_3}?{url_currency}{url_signature}{url_clientSecret}",
                                headers=request_headers, json=request_body)
        return response

    def url_post(self, url_2, url_3, url_currency, url_clientSecret, request_headers, request_body):

        if url_2 is None:
            url_2 = ""
        if url_3 is None:
            url_3 = ""
        if url_currency is None:
            url_currency = ""
        if url_clientSecret is None:
            url_clientSecret = "18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d48"
        if request_headers is None:
            request_headers = {'Content-Type': 'application/json', 'ClientId': clientId}
        if request_body is None:
            request_body = ""

        response = requests.post(f"{url_base}{url_2}{url_3}?{url_currency}{url_signature}{url_clientSecret}",
                                headers=request_headers, json=request_body)
        return response

    def url_put(self, url_2, url_3, url_currency, url_clientSecret, request_headers, request_body):

        if url_2 is None:
            url_2 = ""
        if url_3 is None:
            url_3 = ""
        if url_currency is None:
            url_currency = ""
        if url_clientSecret is None:
            url_clientSecret = "18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d48"
        if request_headers is None:
            request_headers = {'Content-Type': 'application/json', 'ClientId': clientId}
        if request_body is None:
            request_body = ""

        response = requests.put(f"{url_base}{url_2}{url_3}?{url_currency}{url_signature}{url_clientSecret}",
                                headers=request_headers, json=request_body)
        return response

    def url_delete(self, url_2, url_3, url_currency, url_clientSecret, request_headers, request_body):

        if url_2 is None:
            url_2 = ""
        if url_3 is None:
            url_3 = ""
        if url_currency is None:
            url_currency = ""
        if url_clientSecret is None:
            url_clientSecret = "18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d48"
        if request_headers is None:
            request_headers = {'Content-Type': 'application/json', 'ClientId': clientId}
        if request_body is None:
            request_body = ""

        response = requests.delete(f"{url_base}{url_2}{url_3}?{url_currency}{url_signature}{url_clientSecret}",
                                headers=request_headers, json=request_body)
        return response
