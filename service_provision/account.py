from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()
URL = os.getenv("DEV_URL")
TOKEN = os.getenv("DEV_TOKEN")


class Account:
    def __init__(self, external_id, name=None, description=None):
        self.external_id = external_id
        self.name = name
        self.description = description

    def get_account(self):
        url = f"{URL}/service-provision-service/service-provision/account/{self.external_id}"

        headers = {
            "Accept": "application/json",
            "x-api-key": TOKEN,
        }

        response = requests.request("GET", url, headers=headers)

        return response
