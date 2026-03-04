import json

import requests
import os
import dotenv
dotenv.load_dotenv()
key = os.getenv('API_KEY')
url = "https://api.translateapi.ai/api/v1/translate/"


class TranslatorBot:
    def __init__(self, data):
        self.url = "https://api.translateapi.ai/api/v1/translate/"
        self.key = os.getenv('API_KEY')
        self.headers = {
    "Authorization": f"Bearer {self.key}",
    "Content-Type": "application/json"
}
        self.data = data
    def translate(self):
        response = requests.post(self.url, headers=self.headers, json=self.data).json()
        return response["translated_text"]