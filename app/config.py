import json

with open('./config.json') as  config_file:
    config = json.load(config_file)

class Config:
    # DB Connection settings
    DB_ENDPOINT = config.get('DB_ENDPOINT')
    DB_NAME     = config.get('DB_NAME')
    DB_USERNAME = config.get('DB_USERNAME')
    DB_PASSWORD = config.get('DB_PASSWORD')
