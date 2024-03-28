from playwright.sync_api import Playwright, sync_playwright, expect
import random
from .testesApi import TestesApi

class Main:

    def __init__(self, cenarios, banco) -> None:
        self.cenarios = cenarios
        self.banco = banco()

    def run(self, playwright: Playwright, teste) -> None:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()


        exec(teste)


    def start(self, teste):
        with sync_playwright() as playwright:
            self.run(playwright, teste)


 
        


