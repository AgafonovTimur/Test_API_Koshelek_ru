from playwright.sync_api import Playwright, expect, Page
from tests_library import tests_params, debug_log_true
# from tests_library.test_params import no_gui
from tests_library.debug_log_true import DebugLogs
import os
import allure


@allure.feature("UI test2")
# @allure.description("playwright test")
def test_visit_youtube(page: Page) -> None:

    # browser_type.launch(channel='msedge', headless=no_gui)
    page.goto("https://www.youtube.com/")

