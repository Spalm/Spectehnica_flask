from peewee import PostgresqlDatabase, Model

db = PostgresqlDatabase(None)


class BaseModel(Model):
    class Meta:
        database = db
