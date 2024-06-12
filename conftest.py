import pytest
import os
from playwright.sync_api import Page, Playwright
import tests_library.tests_params
# from tests_library.assertions import AssertionsFrontend
from tests_library.debug_log_true import debug_true, DebugLogs
# from tests_library.tests_params import no_gui, login, password, frontend_url


# @pytest.fixture()
# def page(context):
#     page: Page = context.new_page()
#     page.set_viewport_size({"width": 1920, "height": 1080})
#     yield
#     page.close()


# @pytest.fixture()
# def page_login(playwright: Playwright) -> None:
#     """
#     логин с корректными данными с правами админ
#     """

    # browser = playwright.chromium.launch(channel='chrome', headless=no_gui)
    # # context = browser.new_context()
    # # page = context.new_page()
    # page = browser.new_page()
    # response = page.goto(tests_library.test_params.url_base)
    # if debug_true:
    #     DebugLogs.debug_logs_response(os.path.basename(__file__), None,
    #                                   response.status, response.url, url_api=None, method=None)

    # AssertionsFrontend.status_code_check_frontend(response.status, 200,
    #                                               "ответ сервера после логина")

    # page.locator("#username").click()
    # page.locator("#username").fill(login)
    # page.locator("#username").press("Tab")
    # page.locator("#password").fill(password)
    # page.locator(".enter-button").click()

    # response = page.goto(tests_params.frontend_url)

    # browser.close()
    # yield
    # print("123")
    # browser.close()
