from db import BaseModel, db

from flask_login import UserMixin

from peewee import CharField, IntegerField, DateField, ForeignKeyField, BooleanField


class Role(BaseModel):
    title = CharField()


class User(BaseModel, UserMixin):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    creation_date = DateField()
    role = ForeignKeyField(Role)
    is_admin = BooleanField()


class MachineTypes(BaseModel):
    title = CharField()


class Machine(BaseModel):
    model = CharField()
    type = ForeignKeyField(MachineTypes)
    number = CharField(unique=True)


models = [Role, User]

# db.create_tables(models)
# db.drop_tables(models)
