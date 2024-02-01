from datetime import datetime

import pytest

from app import create_app
from auth.models import Role, User, Owner, Report, MachineTypes, Machine
from db import db as _db


@pytest.fixture
def admin_credentials():
    return {
        'name': 'Rustam Karimov',
        'email': 'spalm@list.ru',
        'password': '0000',
        'creation_date':  datetime.now(),
        # Circular import issue: the "db" fixture tries to access "admin_credentials",
        # but "admin_credentials" needs "db" fixture to execute "Role.get()" :)
        'role':  Role.get(Role.title == 'Директор'),
        'is_admin': True
    }


@pytest.fixture
def manager_credentials():
    return {
        'name': 'Andrey Petrov',
        'email': 'andrey@mail.ru',
        'password': '1111',
        'creation_date':  datetime.now(),
        'role':  Role.get(Role.title == 'Менеджер'),
        'is_admin': False
    }


@pytest.fixture
def driver_credentials():
    return {
        'name': 'Piter Ivanov',
        'email': 'piter@mail.ru',
        'password': '2222',
        'creation_date':  datetime.now(),
        'role':  Role.get(Role.title == 'Машинист'),
        'is_admin': False
    }


@pytest.fixture
def db(app, admin_credentials: dict, manager_credentials: dict, driver_credentials: dict):
    models = [User, Owner, Report, MachineTypes, Machine, Role]
    _db.drop_tables(models)
    _db.create_tables(models)

    Role.create(title='Менеджер')
    Role.create(title='Директор')
    Role.create(title='Машинист')

    User.create(**admin_credentials)
    User.create(**manager_credentials)
    driver = User.create(**driver_credentials)

    astral = Owner.create(title='Астра-Л')
    tehno = Owner.create(title='Техно_ресурс')

    MachineTypes.create(title='Мини-погрузчик')
    MachineTypes.create(title='Колесный экскаватор')
    MachineTypes.create(title='Гусеничный экскаватор')
    # MachineTypes.create(title='Экскаватор-погрузчик')
    # MachineTypes.create(title='Мини-экскаватор')

    Machine.create(
        model='Bobcat s650',
        type=MachineTypes.get(MachineTypes.title == 'Мини-погрузчик'),
        number='9878рт78',
        owner=astral,
        user=driver
    )
    Machine.create(
        model='CAT 315D',
        type=MachineTypes.get(MachineTypes.title == 'Колесный экскаватор'),
        number='8547рт78',
        owner=astral,
        user=driver
    )
    Machine.create(
        model='CAT 320DL',
        type=MachineTypes.get(MachineTypes.title == 'Гусеничный экскаватор'),
        number='8952рс98',
        owner=tehno,
        user=None
    )


@pytest.fixture
def app():
    _app = create_app('TestConfig', '../test.env')
    _app.app_context().push()
    return _app
