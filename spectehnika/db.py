import os

from dotenv import load_dotenv
from peewee import PostgresqlDatabase, Model

load_dotenv()

db = PostgresqlDatabase(
    os.environ.get('DB_NAME'),
    host=os.environ.get('DB_HOST'),
    port=os.environ.get('DB_PORT'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD')
)


class BaseModel(Model):
    class Meta:
        database = db
