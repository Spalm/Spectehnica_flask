import os
from pathlib import Path

import dotenv

env_path = os.environ.get('env_path')
if env_path:
    path = Path(env_path)
else:
    path = Path() / '.env'
dotenv.load_dotenv(path)
print(path)


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
    SERVER_NAME = '127.0.0.1:5000'
    TESTING = True
    ...
