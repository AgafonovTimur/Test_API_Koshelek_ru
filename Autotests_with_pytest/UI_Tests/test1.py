import os
from playwright.sync_api import Playwright, expect


def test_run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(channel='chrome', headless=False)
    context = browser.new_context()
    page = context.new_page()

    # debug log displays if debug_true = True
    # if debug_log_true.debug_true:
    #     debug_log_true.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)
    #
    #     print("test message 1")
    # browser = playwright.chromium.launch(channel="chrome", headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://playwright.dev/python/")
    # page.get_by_role("link", name="Get started").click()
    # page.get_by_role("link", name="How to install Playwright").click()

    # page.goto("https://www.google.com/")
    page.on("response", lambda response: print(response.status, response.url, response.json, response.body))
    # assert page.url == "https://www.google.com/"
    # response = page.request.get('https://www.google.com/')
    # expect(response.json()).to_be_ok()
    # with page.expect_response("https://www.google.com/") as response:
        # print(response.url)
        # print(response.value)
        # print(response.headers)
    # page.on("response", handler)
    page.wait_for_timeout(100)
    # page.get_by_label("Найти").click()
    # page.get_by_label("Найти").fill("playwrite documentation")
    # page.get_by_label("Найти").press("Enter")
    # page.get_by_role("link", name="Python", exact=True).click()
    # page.get_by_role("link", name="Get started").click()
    # assert page.url == "https://playwright.dev/python/docs/intro"
    # test_params.ccc(os.path.basename(__file__))
    # assert 1 == 2
    # ---------------------
    context.close()
    browser.close()



# with sync_playwright() as playwright:
#     test_run(playwright)
