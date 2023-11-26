import os

from dotenv import load_dotenv

BASEDIR = os.path.dirname(os.path.realpath(__file__))
INSTALLED_MODULES = ["src.api.v1"]
DOTENV_PATH = os.path.join(os.path.dirname(BASEDIR), ".env")

load_dotenv(DOTENV_PATH)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or "sqlite:///" + os.path.join(
        BASEDIR, "app.db"
    )
    INSTALLED_MODULES = INSTALLED_MODULES
    ERROR_404_HELP=False
    ERROR_401_HELP=False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProdConfig(Config):
    pass


class TestConfig(Config):
    pass
