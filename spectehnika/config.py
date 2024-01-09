import os
from pathlib import Path

import dotenv

path = Path() / '.env'
dotenv.load_dotenv(path)


class Config:
    DB_NAME = os.environ.get('DB_NAME')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')


class DevelopmentConfig(Config):
    ...


class TestConfig(Config):
    ...