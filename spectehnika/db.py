import os

from peewee import PostgresqlDatabase, Model

db = PostgresqlDatabase(
    os.environ.get('DB_NAME'),
    host=os.environ.get('DB_HOST'),
    port=os.environ.get('DB_PORT'),
    user=os.environ.get('DB_USER')
)


class BaseModel(Model):
    class Meta:
        database = db
