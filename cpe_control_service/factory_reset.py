from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env
load_dotenv()
URL = os.getenv("STAGING_URL")
TOKEN = os.getenv("STAGING_TOKEN")


def factory_reset(device_id):
    url = (
        f"{URL}/cpe-control-service/axon-networks/factory-reset/{device_id}?force=true"
    )
    params = {
        "force": True,
    }
    payload = {}
    headers = {
        "x-api-key": TOKEN,
    }

    response = requests.get(url, headers=headers, params=params, data=payload)

    return response
