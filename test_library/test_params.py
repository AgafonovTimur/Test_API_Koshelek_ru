# global variables
import requests
import allure

clientId = "ID-6892fc719fbc467bae2564f37fdb64f728070be92e744a18b7ede4842ad4181f"
url_base = "https://p2psys-publicoffice.konomik.com"
url_clientSecret = "18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d48"
# request_headers1 = {'Content-Type': 'application/json', 'ClientId': clientId}
url_currency = "currency=RUB"
url_signature = "&signature="
no_gui = True


# ? description of URL link
# 1  url_base = "https://p2psys-publicoffice.konomik.com"
# 2 = url_2 = "/v1/devices"
# 3 = url_3 = device_id
# 4 = url_currency = "currency=RUB"
# 5 = url_signature = "&signature="
# 6 = url_clientSecret


class BaseUrlRequests:

    def url_get(self, url_2="",
                url_3="",
                url_currency="",
                url_clientSecret=url_clientSecret,
                request_headers=None,
                request_body=""):
        if request_headers is None:
            request_headers = {"Content-Type": "application/json", "ClientId": clientId}
        response = requests.get(f"{url_base}{url_2}{url_3}?{url_currency}{url_signature}{url_clientSecret}",
                                headers=request_headers, json=request_body)
        with allure.step("GET used in request"):
            pass
        return response

    def url_post(self, url_2="",
                 url_3="",
                 url_currency="",
                 url_clientSecret=url_clientSecret,
                 request_headers=None,
                 request_body=""):
        if request_headers is None:
            request_headers = {"Content-Type": "application/json", "ClientId": clientId}
        response = requests.post(f"{url_base}{url_2}{url_3}?{url_currency}{url_signature}{url_clientSecret}",
                                 headers=request_headers, json=request_body)
        with allure.step("POST used in request"):
            pass
        return response

    def url_put(self, url_2="",
                url_3="",
                url_currency="",
                url_clientSecret=url_clientSecret,
                request_headers=None,
                request_body=""):
        if request_headers is None:
            request_headers = {"Content-Type": "application/json", "ClientId": clientId}
        response = requests.put(f"{url_base}{url_2}{url_3}?{url_currency}{url_signature}{url_clientSecret}",
                                headers=request_headers, json=request_body)
        with allure.step("PUT used in request"):
            pass
        return response

    def url_delete(self, url_2="",
                   url_3="",
                   url_currency="",
                   url_clientSecret=url_clientSecret,
                   request_headers=None,
                   request_body=""):
        if request_headers is None:
            request_headers = {"Content-Type": "application/json", "ClientId": clientId}
        response = requests.delete(f"{url_base}{url_2}{url_3}?{url_currency}{url_signature}{url_clientSecret}",
                                   headers=request_headers, json=request_body)
        with allure.step("DELETE used in request"):
            pass
        return response
