import pytest
from flask.testing import FlaskClient


@pytest.fixture
def client(app):
    return FlaskClient(app)
