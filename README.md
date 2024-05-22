to run test in console use python -s pytest

to run test with prints and debug info : set debug_true = True
in file test_params

to run only test with no info : set debug_true = False
in file test_params

in debug : yellow - response json, green : debug info from prints

asserts in assertion.py class Assertions

python -s pytest --alluredir=allure_report .\Autotests_with_pytest\