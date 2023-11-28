from db import db
from flask.cli import AppGroup

from auth.models import User, Role, Owner, MachineTypes, Machine

models = [User, Role, Owner, MachineTypes, Machine]

wishlist = AppGroup('wishlist')


@wishlist.command('create_db')
def create_db():
    db.create_tables(models)


@wishlist.command('reset_db')
def drop_db():
    db.drop_tables(models)
    db.create_tables(models)


@wishlist.command('populate_db')
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
