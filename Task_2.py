import requests
import json
import os
import requests as requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.json())
        return response.json()

    def upload(self, file_path: str):
        result = self._get_upload_link(file_path=file_path)
        href = result.get('href', '')
        response = requests.put(href, data=open('test.txt', 'rb'))
        if response.status_code ==201:
            print('Success')
