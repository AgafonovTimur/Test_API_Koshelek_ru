# global variables
import json

clientId = "ID-6892fc719fbc467bae2564f37fdb64f728070be92e744a18b7ede4842ad4181f"
clientSecret = "18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d48"
baseUrl = "https://p2psys-publicoffice.konomik.com"
request_headers = {'Content-Type': 'application/json', 'ClientId': clientId}
currency = "currency=RUB"


# change_console_color_and_add_name_of_test and testVariables.testVariables.debug_print response in json
def ccc(name_of_test, response):
    debug_true = True
    if debug_true:
        print("\033[92m" + "\n" + name_of_test)
        print(json.dumps(json.loads(response.text), indent=2))


# debug testVariables.debug_print
def debug_print(debug_params):
    debug_true = True
    if debug_true:
        print(debug_params)
