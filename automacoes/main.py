from re import sub
from types import ModuleType
from unittest import TextTestResult
from urllib import response
from playwright.sync_api import Playwright, sync_playwright, expect
import random
from .testesApi import TestesApi
import subprocess
from .testesYaml.montaYaml import MontaYaml

class Main:

    def __init__(self, cenarios, banco) -> None:
        self.cenarios = cenarios
        self.banco = banco()
        self.testesYaml = MontaYaml()

    def run(self, playwright: Playwright, teste, plataforma) -> None:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        if plataforma == 'mobile':
            print("EXECUTANDO TESTE MOBILE",teste)
            #self.testesYaml.monta(['- tapOn: "matrixcargo - Motorista"','- tapOn: "matrixcargo - Motorista"'])
            #response = subprocess.run('maestro test automacoes/testesYaml/arquivo.yaml',shell=True, capture_output=True, text=True)
        else:
            print("EXECUTANDO TESTE WEB", teste)
            exec(teste)


    def start(self, teste, plataforma):
        with sync_playwright() as playwright:
            self.run(playwright, teste, plataforma)


 
        


