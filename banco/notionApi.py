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

#print(NotionApi().get_pages_info())



