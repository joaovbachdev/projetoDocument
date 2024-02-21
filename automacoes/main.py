from playwright.sync_api import Playwright, sync_playwright, expect
import random

class Main:

    def __init__(self, cenarios) -> None:
        self.cenarios = cenarios

    def run(self, playwright: Playwright, teste) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        exec(teste)


    def start(self, teste):
        with sync_playwright() as playwright:
            self.run(playwright, teste)

