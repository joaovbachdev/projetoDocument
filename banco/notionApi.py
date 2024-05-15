from email import header
from tabnanny import check
from urllib import response
import requests
import json

class NotionApi:
    def __init__(self) -> None:
        self.token = 'secret_fQtOIe1fYqDGVFOOjk35itXEYvJNQmEt5QAFBaGhh5K'
        self.databaseId = '2225bc7775314a4bb6e13e1d6209c34d'#https://www.notion.so/2225bc7775314a4bb6e13e1d6209c34d?v=b840b7eb853d409391c8d2a329db5865&pvs=4

        self.header = {
            "Authorization":"Bearer " + self.token,
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }

    def get_pages_info(self):
        url = f"https://api.notion.com/v1/databases/{self.databaseId}/query"
        payload = {"page_size":100}
        response = requests.post(url, json=payload, headers = self.header)
        data = response.json()
        results = {}

        for i in data['results']:
            results[i['id']] = i['properties']['Nome']['title'][0]['text']['content']
        return results

    def add_to_do(self, pageName, content, checked):
        data = self.get_pages_info()
        validacaoToggleId = self.get_validacoes_id(list(data.keys())[0])
        key = [chave for chave, valor in data.items() if valor == pageName]
        url = f'https://api.notion.com/v1/blocks/{validacaoToggleId}/children'
        
        payload = {
            	"children":[
                        {
                            "object":"block",
                            "type":"to_do",
                            "to_do":{
                                "rich_text":[
                                    {
                                        "type": "text",
                            "text": {
                            "content": f"{content}",
                            "link": None
                            }
                                    }
                                ],
                                "checked":checked

                            }
                        }
                    ]
                }
        response = requests.patch(url, json=payload, headers=self.header)
        return response.json()

    def delete_block(self, id):
        response = requests.delete(f'https://api.notion.com/v1/blocks/{id}', headers=self.header)
        return response

    def check_to_do(self, id, checked):
        print(id, "VALOR DE DASDADBADBASDMNBASDMNASBDMNSABD", checked)
        url = f'https://api.notion.com/v1/blocks/{id}'
        payload = {
                "object":"block",
                "to_do":{
                    "checked":checked
                }
                
            }
        
        response = requests.patch(url, json=payload, headers = self.header)
        return response

    def get_ocorrencias_table(self, pageId):
        url = f"https://api.notion.com/v1/blocks/{pageId}/children"
        response = requests.get(url, headers=self.header)
        toggleId = [i['id'] for i in response.json()['results'] if i['type'] == "toggle"][1]
        
        urlToggle = f"https://api.notion.com/v1/blocks/{toggleId}/children"
        responseToggle = requests.get(url=urlToggle, headers=self.header)
        
        tabbleIid = [i['id'] for i in responseToggle.json()['results'] if i['type'] == 'table'][0]
        tableContent_url = f"https://api.notion.com/v1/blocks/{tabbleIid}/children"
        tableContent = requests.get(url=tableContent_url, headers=self.header)
        
        return tableContent.json()
    
    def get_validacoes_id(self, pageId):
        url = f"https://api.notion.com/v1/blocks/{pageId}/children"
        response = requests.get(url, headers=self.header)
        toggleId = [i['id'] for i in response.json()['results'] if i['type'] == "toggle"][0]
        
        urlToggle = f"https://api.notion.com/v1/blocks/{toggleId}/children"
        responseToggle = requests.get(url=urlToggle, headers=self.header)
        
        return toggleId
        #print(response.json())
#print(NotionApi().add_to_do('TESTE2','ahah'))
#print(NotionApi().get_pages_info())
#print(NotionApi().get_validacoes_cotent("3fe45f98-db2d-445f-855a-e85a2f01b099"))


