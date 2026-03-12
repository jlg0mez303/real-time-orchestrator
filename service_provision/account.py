from dotenv import load_dotenv
import json
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

    def create_account(self):
        url = f"{URL}/service-provision-service/service-provision/account"

        payload = json.dumps(
            {
                "externalId": self.external_id,
            },
        )
        headers = {
            "Accept": "application/json",
            "x-api-key": TOKEN,
            "Content-Type": "application/json",
        }

        response = requests.post(url, headers=headers, data=payload)

        return response

    def get_account(self):
        url = f"{URL}/service-provision-service/service-provision/account/{self.external_id}"

        headers = {
            "Accept": "application/json",
            "x-api-key": TOKEN,
        }

        response = requests.request("GET", url, headers=headers)

        return response

    def update_account(self):
        url = f"{URL}/service-provision-service/service-provision/account"

        payload = json.dumps(
            {
                "externalId": "ruby.test.01.update",
                "name": "AO 7 testing",
                "description": "AO 7 environment testing account",
                "newExternalId": "ruby.test.01",
            }
        )
        headers = {
            "Accept": "application/json",
            "x-api-key": TOKEN,
            "Content-Type": "application/json",
        }

        response = requests.put(url, headers=headers, data=payload)

        return response

    def delete_account(self):
        url = f"{URL}/service-provision-service/service-provision/account/{self.external_id}"

        payload = {}
        headers = {
            "Accept": "application/json",
            "x-api-key": TOKEN,
        }

        response = requests.delete(url, headers=headers, data=payload)

        return response
