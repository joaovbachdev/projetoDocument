from playwright.sync_api import Playwright, sync_playwright, expect


class Main:

    def __init__(self, cenarios) -> None:
        self.cenarios = cenarios

    def run(self, playwright: Playwright, testes) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        print(testes)
        print(testes[0])
        for i in testes:
            exec('\n'.join(i))


    def start(self, testes):
        with sync_playwright() as playwright:
            self.run(playwright, testes)
