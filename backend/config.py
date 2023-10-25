import os

from dotenv import load_dotenv

load_dotenv()

BASEDIR = os.path.dirname(os.path.realpath(__file__))
INSTALLED_MODULES = ["app.music"]


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or "sqlite:///" + os.path.join(
        BASEDIR, "app.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = "main.py"
    INSTALLED_MODULES = INSTALLED_MODULES


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProdConfig(Config):
    pass


class TestConfig(Config):
    pass
