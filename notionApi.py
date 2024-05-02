from email import header
import json
from pydoc import getpager
from urllib import request
import requests
import json
import matplotlib.pyplot as plt

token = 'secret_fN1jFly7RbwIn8PO5NdFF2y8sdeIB9dvRneUefVJx9m'
databaseId = '1255023f42db41d7911da47a02406013'

header = {
    "Authorization":"Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def get_pages():
    url = f"https://api.notion.com/v1/databases/{databaseId}/query"
    payload = {"page_size":100}
    response = requests.post(url, json=payload, headers = header)

    data = response.json()

    with open('db.json', 'w', encoding='utf8') as f:
        json.dump(data,f, ensure_ascii=False, indent=4)
    
    results = data["results"]
    return results

def createPage(data: dict):
    create__url = "https://api.notion.com/v1/pages"

    payload = {"parent":{"database_id":databaseId}, "properties":data}

    res = requests.post(create__url, headers=header, json=payload)
    print(res.json())
    return res

def getDadosCache():
    with open('db.json','r+') as f:
        data = json.load(f)
        return data["results"]

def extraiDados():
    pages = getDadosCache()
    newData = {'\ufeffDATA ABERTURA':[],'CARD':[],'STATUS':[],'ID':[], 'TEMPO SOLUÇÃO':[], 'STATUS CARD':[],'ANALISE':[],
    'TÍTULO':[], 'PRAZO DE ENTREGA':[], 'REQUISIÇÃO':[], 'PRODUTO':[],'FIM ANALISE':[],'DATA FIM ANALISE':[], 'OBS':[],'Fórmula':[]}
    for index,i in enumerate(pages):
        if index >-1:
            try:
                newData['\ufeffDATA ABERTURA'].append(i["properties"]['\ufeffDATA ABERTURA']['title'][0]['plain_text'])
                newData['CARD'].append(i["properties"]['CARD']['url'])
                newData['STATUS'].append(i["properties"]['STATUS']['select']['name'])
                newData['ID'].append(i["properties"]['ID']['number'])
                newData['TEMPO SOLUÇÃO'].append(i["properties"]['TEMPO SOLUÇÃO']['rich_text'][0]['plain_text'])
                newData['STATUS CARD'].append(i["properties"]['STATUS CARD']['rich_text'][0]["text"]["content"])
                newData['ANALISE'].append(i["properties"]['ANALISE']['select']['name'])
                newData['TÍTULO'].append(i["properties"]['TÍTULO']['rich_text'][0]['plain_text'])
                newData['PRAZO DE ENTREGA'].append(i["properties"]['PRAZO DE ENTREGA']['date'])
                newData['REQUISIÇÃO'].append(i["properties"]['REQUISIÇÃO']['select']['name'])
                newData['PRODUTO'].append(i["properties"]['PRODUTO']['select']['name'])
                newData['FIM ANALISE'].append(i["properties"]['FIM ANALISE']['rich_text'][0]['plain_text'])
                newData['DATA FIM ANALISE'].append(i["properties"]['DATA FIM ANALISE']['rich_text'][0]['plain_text'])
                newData['OBS'].append(i["properties"]['OBS']['rich_text'][0]['plain_text'])
                newData['Fórmula'].append(i["properties"]['Fórmula']['rich_text'][0]['plain_text'])
            except:
                newData['\ufeffDATA ABERTURA'].append('none')
                newData['CARD'].append(i["properties"]['CARD']['url'])
                newData['STATUS'].append(i["properties"]['STATUS']['select']['name'])
                newData['ID'].append(i["properties"]['ID']['number'])
                newData['TEMPO SOLUÇÃO'].append('none')
                newData['STATUS CARD'].append('none')
                newData['ANALISE'].append(i["properties"]['ANALISE']['select']['name'])
                newData['TÍTULO'].append('none')
                newData['PRAZO DE ENTREGA'].append(i["properties"]['PRAZO DE ENTREGA']['date'])
                newData['REQUISIÇÃO'].append(i["properties"]['REQUISIÇÃO']['select']['name'])
                newData['PRODUTO'].append(i["properties"]['PRODUTO']['select']['name'])
                newData['FIM ANALISE'].append('none')
                newData['DATA FIM ANALISE'].append('none')
                newData['OBS'].append('none')
                newData['Fórmula'].append('none')

    return newData

print(extraiDados())


url = "criado1"
tag = "cria1"
data = {
    "url":{"title": [{"text": {"content":url}}]},
    "Tags":{"multi_select":[{"name":tag}]} 
}
#createPage(data)
#get_pages()