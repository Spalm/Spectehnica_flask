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
    Role.create(title="директор")
    Role.create(title="менеджер")
    Role.create(title="машинист")

    User.create(name='Рустам Каримов', email='spalm@list.ru', password='2510ru80',
                creation_date='2024-02-20', role=1, is_admin=True)
    User.create(name='Виктор Шиханов', email='viktor_shihanov@mail.ru', password='seriousvik1981',
                creation_date='2024-02-20', role=1, is_admin=True)
    User.create(name='Андрей Петров', email='pavmf@mail.ru', password='pavmf2024',
                creation_date='2024-02-20', role=1, is_admin=False)
    User.create(name='Имом Авазов', email='imim@mail.ru', password='1111',
                creation_date='2024-02-20', role=1, is_admin=False)
    User.create(name='Адилет Маламбердиев', email='adilet@mail.ru', password='2222',
                creation_date='2024-02-20', role=1, is_admin=False)
    User.create(name='Дилшод', email='dilshod@mail.ru', password='3333',
                creation_date='2024-02-20', role=1, is_admin=False)

    Owner.create(title='Астра-Л')
    Owner.create(title='ТЕХНО-РЕСУРС')
    Owner.create(title='Маршал')
    Owner.create(title='СОУЛ.РЕНТ')
    Owner.create(title='ИСТ')
    Owner.create(title='РТ')
    Owner.create(title='ВИОТРАНС')
    Owner.create(title='Лиговка-270')
    Owner.create(title='НГ-ЭНЕРГО')
    Owner.create(title='ЭДЕЛЬВЕЙС')
    Owner.create(title='СТК АЛЬЯНС')
    Owner.create(title='НОВЫН ГОРИЗОНТЫ')
    Owner.create(title='ТД ТЕХНОНЕРУД')
    Owner.create(title='ИСТ')
    Owner.create(title='ЭТАЛОН')
    Owner.create(title='А1')
    Owner.create(title='МИР СПЕЦТЕХНИКИ')
    Owner.create(title='СП-ТЕХНОЛОГИЯ')
    Owner.create(title='НЬЮТРАНС')
    Owner.create(title='ПМ')
    Owner.create(title='АВТОЛАЙН')
    Owner.create(title='МЕКАР')
    Owner.create(title='ХОРТА')
    Owner.create(title='СЕВЕРНЫЙ ТРАНСПОРТ')
    Owner.create(title='АНДРЕАС РЕНТ')
    Owner.create(title='МИР СПЕЦТЕХНИКИ')

    MachineTypes.create(title='мини-погрузчик')
    MachineTypes.create(title='мини-экскаватор')
    MachineTypes.create(title='экскаватор-погрузчик')
    MachineTypes.create(title='колесный экскаватор')
    MachineTypes.create(title='гусеничный экскаватор')
    MachineTypes.create(title='самосвал')
    MachineTypes.create(title='асфальтоукладчик')
    MachineTypes.create(title='каток')
    MachineTypes.create(title='автокран')

    Machine.create(model='Bobcat s630', number='4417рк78', user=4, type=1, owner=1)
    Machine.create(model='Bobcat s650', number='4127рх78', user=5, type=1, owner=1)
    Machine.create(model='CAT 315D', number='0458РТ78', user=6, type=4, owner=1)
    Machine.create(model='LonKing 4026', number='0000рс00', user=7, type=2, owner=1)
    Machine.create(model='Terex 860', number='9649рт78', user=3, type=3, owner=1)


def register_cli_commands(app: Flask) -> None:
    app.cli.add_command(start_data)

"""См урок 7.11.2023 и 8.12.23 (01:15)"""