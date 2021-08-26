import pytest

from Blog import app as flask_app
from Blog import db


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()