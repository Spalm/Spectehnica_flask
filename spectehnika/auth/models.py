from db import BaseModel, db

from flask_login import UserMixin

from peewee import CharField, IntegerField, DateField, ForeignKeyField


class Role(BaseModel):
    title = CharField()


class User(BaseModel, UserMixin):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    creation_date = DateField()
    role = ForeignKeyField(Role)

