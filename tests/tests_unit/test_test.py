from bs4 import BeautifulSoup
from flask import Flask, url_for
from flask.testing import FlaskClient
from flask_login import current_user
from peewee import PostgresqlDatabase
import pytest

from spectehnika.auth.models import User

current_user: User


def test_env(app: Flask):
    assert app.config['DB_NAME'] == 'spectehnika_test'


def test_index(client: FlaskClient):
    response = client.get(url_for('index'))
    assert response.status_code == 302
    assert response.location == url_for('auth.login', _external=False)


class TestAdmin:
    def test_admin_not_authorized(self, client: FlaskClient):
        response = client.get(url_for('admin.administration'))
        assert response.status_code == 302
        assert response.location.startswith(url_for('auth.login', _external=False))

    def test_admin_wrong_role(self, client: FlaskClient, db: PostgresqlDatabase):
        user_credentials = {
            'email': 'andrey@mail.ru',
            'password': '1111'
        }
        with client:
            client.post(url_for('auth.login_post'), data=user_credentials)
            response = client.get(url_for('admin.administration'))
            assert response.status_code == 403

    def test_admin_success(self, client: FlaskClient, db: PostgresqlDatabase, admin_credentials: dict):
        client.post(url_for('auth.login_post'), data=admin_credentials)
        response = client.get(url_for('admin.administration'))
        assert response.status_code == 200

    def test_success_employees_page(self, client: FlaskClient, db: PostgresqlDatabase, admin_credentials):
        with client:
            client.post(url_for('auth.login_post'), data=admin_credentials)
            response = client.get(url_for('emp.employees'))
            assert response.status_code == 200

    def test_success_tehnika_page(self, client: FlaskClient, db: PostgresqlDatabase, admin_credentials):
        with client:
            client.post(url_for('auth.login_post'), data=admin_credentials)
            response = client.get(url_for('teh.tehnika'))
            assert response.status_code == 200


class TestAuth:
    @pytest.mark.parametrize(['credentials'], [
        [
            {
                'email': 'vasya@mail.ru',
                'password': 'pass111'
            }
        ],
        [
            {
                'email': 'vasya@mail.ru',
                'password': 'adsfasdfsadfsadf'
            }
        ],
        [
            {
                'email': 'olya@mail.ru',
                'password': 'pass1234'
            }
        ]
    ])
    def test_wrong_credentials(self, client: FlaskClient, db: PostgresqlDatabase, credentials: dict):
        response = client.post(url_for('auth.login_post'), data=credentials)
        soup = BeautifulSoup(response.text)
        error_tags = soup.select('span.tag.is-danger')
        assert len(error_tags) == 1
        assert error_tags[0].string.strip() == 'Неверный email или пароль'

    def test_current_user(self, client: FlaskClient, db: PostgresqlDatabase):
        user_credentials = {
            'email': 'spalm@list.ru',
            'password': '0000'
        }
        with client:
            client.post(url_for('auth.login_post'), data=user_credentials)
            assert current_user.email == 'spalm@list.ru'
            assert current_user.password == '0000'
            assert current_user.role.title == 'Директор'
            assert current_user.name == 'Rustam Karimov'
            response = client.get(url_for('admin.administration'))
            assert response.status_code == 200

    def test_owners(self, client: FlaskClient, db: PostgresqlDatabase):
        url = url_for('admin.owners')
        params_astral = {'owner': 1}
        params_tehno = {'owner': 2}
        response_astral = client.get(url, query_string=params_astral)
        response_tehno = client.get(url, query_string=params_tehno)

        soup = BeautifulSoup(response_astral.text)
        options = soup.find_all('option')
        assert response_astral.status_code == 200
        assert len(options) == 3

        soup = BeautifulSoup(response_tehno.text)
        options = soup.find_all('option')
        assert response_tehno.status_code == 200
        assert len(options) == 2

    def test_machine(self, client: FlaskClient, db: PostgresqlDatabase):
        url = url_for('admin.owners')
        params_astral = {'owner': 1}
        client.get(url, query_string=params_astral)
        url = url_for('admin.models')
        params = {'machine': '1_1'}
        response = client.get(url, query_string=params)

        soup = BeautifulSoup(response.text)
        options = soup.find_all('option')
        assert response.status_code == 200
        assert len(options) == 2

