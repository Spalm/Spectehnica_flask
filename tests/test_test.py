import pytest

from spectehnika.app import create_app


@pytest.fixture
def app():
    return create_app('TestConfig')


def test_test(app):
    assert app.config['DB_NAME'] == 'spectehnika_test'
