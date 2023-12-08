from flask import Flask
from flask.cli import AppGroup

from db import db
from auth.models import User, Role, Owner, MachineTypes, Machine, Report

models = [User, Role, Owner, MachineTypes, Machine, Report]

start_data = AppGroup('start_data')


@start_data.command('create_db')
def create_db():
    db.create_tables(models)


@start_data.command('reset_db')
def drop_db():
    db.drop_tables(models)
    db.create_tables(models)


@start_data.command('populate_db')
def populate_db():
    User.create(name='Рустам Каримов', email='spalm@list.ru', password='0000',
                creation_date='2023-11-01', role=1, is_admin=True)
    User.create(name='Андрей Петров', email='adndrey@mail.ru', password='1111',
                creation_date='2023-11-01', role=1, is_admin=False)
    User.create(name='Сергей Иванов', email='sergey@mail.ru', password='2222',
                creation_date='2023-11-01', role=1, is_admin=False)
    User.create(name='Григорий Сергеев', email='gregori@mail.ru', password='3333',
                creation_date='2023-11-01', role=1, is_admin=False)
    User.create(name='Анатолий Якушев', email='tolik@mail.ru', password='4444',
                creation_date='2023-11-01', role=1, is_admin=False)
    User.create(name='Тимур Денисов', email='timur@mail.ru', password='5555',
                creation_date='2023-11-01', role=1, is_admin=False)
    User.create(name='Александр Игнатьев', email='alex@mail.ru', password='6666',
                creation_date='2023-11-01', role=1, is_admin=False)

    Role.create(title="директор")
    Role.create(title="менеджер")
    Role.create(title="машинист")

    Owner.create(title='Астра-Л')
    Owner.create(title='ТЕХНО-РЕСУРС')
    Owner.create(title='Маршал')

    MachineTypes.create(title='мини-погрузчик')
    MachineTypes.create(title='мини-экскаватор')
    MachineTypes.create(title='экскаватор-погрузчик')
    MachineTypes.create(title='колесный экскаватор')
    MachineTypes.create(title='гусеничный экскаватор')
    MachineTypes.create(title='автокран')

    Machine.create(model='JCB 160', number='1122рс98', type=4, owner=2)
    Machine.create(model='JCB 3CX', number='2342рт78', type=3, owner=2)
    Machine.create(model='Автокран 25т', number='4565рс78', type=6, owner=3)
    Machine.create(model='CAT 320DL', number='4579рс78', type=5, owner=3)
    Machine.create(model='Bobcat s630', number='5785рс78', user=4, type=1, owner=1)
    Machine.create(model='Bobcat s650', number='6875рс78', user=5, type=1, owner=1)
    Machine.create(model='Bobcat s650', number='9578рс78', user=6, type=3, owner=1)
    Machine.create(model='LonKing', number='3287рс78', user=7, type=2, owner=1)
    Machine.create(model='Komatsu', number='9886рт78', user=3, type=3, owner=1)


def register_cli_commands(app: Flask) -> None:
    app.cli.add_command(start_data)

"""См урок 7.11.2023"""