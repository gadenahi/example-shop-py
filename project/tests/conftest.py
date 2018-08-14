import pytest

from project.app import create_app
from project.app import db

pytest_plugins = [
    "project.tests.factories",
]


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(scope='session')
def app():
    _app = create_app('project.config.TestingConfig')
    ctx = _app.app_context()
    ctx.push()
    yield _app
    ctx.pop()


@pytest.fixture(scope="session")
def _db(app):
    """
    Returns session-wide initialised database.
    """
    db.drop_all()
    db.create_all()
    return db
