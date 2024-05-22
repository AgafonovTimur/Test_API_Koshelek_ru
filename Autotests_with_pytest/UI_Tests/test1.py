from playwright.sync_api import Playwright


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # debug log displays if debug_true = True
    # if debug_log_true.debug_true == True:
    #     debug_log_true.debug_logs(os.path.basename(__file__), response.json(), response.status_code, response.url)
    #
    #     print("test message 1")

    page.goto("https://www.google.com/")
    assert page.url == "https://www.google.com/"
    page.get_by_label("Найти").click()
    page.get_by_label("Найти").fill("playwrite documentation")
    page.get_by_label("Найти").press("Enter")
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
