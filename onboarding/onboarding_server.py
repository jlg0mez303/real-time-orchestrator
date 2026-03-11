from dotenv import load_dotenv
import json
import os
import requests

# Load environment variables from .env (if present).
load_dotenv()
URL = os.getenv("ONBOARDING_URL")
TOKEN = os.getenv("ONBOARDING_TOKEN")
AOID = os.getenv("DEV_AOID")


def register_device(device_id):
    url = f"{URL}/devs/update"

    payload = json.dumps(
        [
            {
                "devId": device_id,
                "ao": {
                    "aoId": AOID,
                },
            }
        ]
    )
    headers = {
        "Content-Type": "application/json",
        "x-api-key": TOKEN,
    }

    response = requests.post(url, headers=headers, data=payload)

    return response


def get_record(device_id):

    url = f"{URL}/records/getByDevIds"

    payload = json.dumps(
        [
            device_id,
        ],
    )
    headers = {
        "Content-Type": "application/json",
        "x-api-key": TOKEN,
    }

    response = requests.get(url, headers=headers, data=payload)

    return response
