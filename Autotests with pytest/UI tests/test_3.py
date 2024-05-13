import requests
import testVariables
import json
import re
from playwright.sync_api import Playwright, sync_playwright, expect


class Testtwo:
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.google.com/")
        assert page.url == "https://www.google.com/"
        page.get_by_label("Найти").click()
        page.get_by_label("Найти").fill("playwrite documentation")
        page.get_by_label("Найти").press("Enter")
        page.get_by_role("link", name="Python", exact=True).click()
        page.get_by_role("link", name="Get started").click()
        assert page.url == "https://playwright.dev/python/docs/intro"
        print(page.url)
        # assert 1 == 2
        # ---------------------
        # context.close()
        browser.close()


with sync_playwright() as playwright:
    Testtwo.run(playwright)
