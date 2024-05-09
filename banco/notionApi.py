from urllib import response
import requests
import json

class NotionApi:
    def __init__(self) -> None:
        self.token = 'secret_fQtOIe1fYqDGVFOOjk35itXEYvJNQmEt5QAFBaGhh5K'
        self.databaseId = '0bc8205b6a4e4416810a849f05ee379a'

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
            results[i['id']] = i['properties']['Name']['title'][0]['text']['content']
        return results

    def add_to_do(self, pageName, content):
        data = self.get_pages_info()
        key = [chave for chave, valor in data.items() if valor == pageName]

        url = f'https://api.notion.com/v1/blocks/{key[0]}/children'
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
                                ]
                            }
                        }
                    ]
                }
        response = requests.patch(url, json=payload, headers=self.header)
        return response.json()

    def delete_block(self, id):
        response = requests.delete(f'https://api.notion.com/v1/blocks/{id}', headers=self.header)
        return response

#print(NotionApi().add_to_do('TESTE2','ahah'))

#print(NotionApi().get_pages_info())



