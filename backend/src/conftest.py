import pytest
from config import DevConfig
from framework.database import db
from main import create_app
from models.user import User


@pytest.fixture
def app():
    app = create_app("testing")
    return app


# @pytest.fixture
# def db(app, client, request):
#     database.drop_all()
#     database.create_all()
#     database.session.commit()

#     def fin():
#         database.session.remove()

#     request.addfinalizer(fin)
#     return database
