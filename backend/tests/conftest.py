import pytest
from src.config import DevConfig
from src.framework.database import db as database
from src.main import create_app
from src.models.user import User

USERNAME = "namtran"
PASSWORD = "namtran"


@pytest.fixture
def app():
    app = create_app(DevConfig)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db(app, client, request):
    database.drop_all()
    database.create_all()
    database.session.commit()

    def fin():
        database.session.remove()

    request.addfinalizer(fin)
    return database


@pytest.fixture
def user(db):
    user = User(username=USERNAME, password=PASSWORD)
    db.session.add(user)
    db.session.commit()
    return user
