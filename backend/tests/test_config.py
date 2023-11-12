from src.config import DevConfig
from src.main import create_app


def test_config_development():
    app = create_app(DevConfig)
    assert app.config["SECRET_KEY"] == "4b008cae1755bd05459fe089"
    assert app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] == False
    assert app.config["INSTALLED_MODULES"] == ["src.app.music"]
