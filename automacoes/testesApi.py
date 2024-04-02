from unittest import TextTestResult
import requests
import json

class TestesApi:
    def __init__(self) -> None:
        self.urlViagem = 'https://integration-hom.matrixcargo.com.br/api/viasoft_integration/trips'
        self.tokenAcelerador = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIxYzI1ODY4MS1mYmUwLTRlNjUtYmJmZi1hNTliMTViODg1YzciLCJkYXRhIjp7ImNvbXBhbnkiOiJjYXJnb2xpZnQifSwiaWF0IjoxNjkyOTY0NDgzfQ.byWzfOhCT_1H2aZgqIXOo4-5dWKUf05Iu1QiR2-JZq4"
        self.headerAcelerador = {'Authorization':f'Bearer {self.tokenAcelerador}',
                       'Content-Type': 'application/json'}

    def criaViagem(self):
        with open('automacoes/payloadsApiTestes/viagem.json','r+') as f:
            data = json.load(f)
            response = requests.post(self.urlViagem, json=data,headers=self.headerAcelerador)
        return response.status_code

#TestesApi().criaViagem()