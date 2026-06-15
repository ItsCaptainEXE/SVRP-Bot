import requests
import os
import logging
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('SVRP_API_KEY')
WEBHOOK_URL = os.getenv('SVRP_WEBHOOK_URL')
# Assumed API base URL for ERLC
API_BASE = "https://api.erlc.com/v1" 

logger = logging.getLogger('SVRP_API')

def log_to_webhook(message):
    try:
        requests.post(WEBHOOK_URL, json={"content": message})
    except Exception as e:
        logger.error(f"Failed to send to webhook: {e}")

def send_api_request(method, endpoint, data=None):
    url = f"{API_BASE}/{endpoint}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    try:
        response = requests.request(method, url, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        log_to_webhook(f"API Success: {method} {endpoint}")
        return response.json()
    except requests.exceptions.RequestException as e:
        log_to_webhook(f"API Error: {method} {endpoint} - {e}")
        logger.error(f"API Request failed: {e}")
        return None
