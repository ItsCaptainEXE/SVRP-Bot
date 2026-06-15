import json
import os

CONFIG_FILE = 'bot/config.json'

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def update_config_key(key, value):
    config = load_config()
    config[key] = value
    save_config(config)
