from playwright.sync_api import Playwright, sync_playwright, expect


class Main:

    def __init__(self, cenarios) -> None:
        self.cenarios = cenarios

    def run(self, playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        exec(self.cenarios.cenarios["inputUsuario"])

    def start(self):
        with sync_playwright() as playwright:
            self.run(playwright)
