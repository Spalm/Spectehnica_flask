from db import BaseModel, db

from flask_login import UserMixin

from peewee import CharField, IntegerField, DateField, ForeignKeyField, BooleanField, FloatField


class Role(BaseModel):
    title = CharField()


class User(BaseModel, UserMixin):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    creation_date = DateField()
    role = ForeignKeyField(Role)
    is_admin = BooleanField()


class Owner(BaseModel):
    title = CharField(unique=True)


class MachineTypes(BaseModel):
    title = CharField(unique=True)


class Machine(BaseModel):
    model = CharField()
    type = ForeignKeyField(MachineTypes)
    number = CharField(unique=True)
    owner = ForeignKeyField(Owner)
    user = ForeignKeyField(User, null=True)


class Report(BaseModel):
    date = DateField()
    address = CharField()
    owner = ForeignKeyField(Owner)
    type = ForeignKeyField(MachineTypes)
    model = ForeignKeyField(Machine)
    hours = FloatField()
    cost = IntegerField()
    price = IntegerField()


models = [Role, User, MachineTypes, Machine, Owner, Report]

# db.drop_tables(models)
# db.create_tables(models)

