import json
import os
basedir = os.path.abspath(os.path.dirname(__file__))


with open('./config.json') as config_file:
    config = json.load(config_file)

class Config:
    # DB Connection settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "someshabasednumberlkira"
    SQLALCHEMY_DATABASE_URI = config.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'example.db')

    # SQLALCHEMY_DATABASE_URI = "mysql://" + config.get('DB_USERNAME') + ':' + config.get('DB_PASSWORD') + '@' + config.get('DB_ENDPOINT') + '/' + config.get('DB_NAME')
    # DB_ENDPOINT = config.get('DB_ENDPOINT')
    # DB_NAME = config.get('DB_NAME')
    # DB_USERNAME = config.get('DB_USERNAME')
    # DB_PASSWORD = config.get('DB_PASSWORD')
