from flask import Flask
from flask_cors import CORS

from .config import Config, DevConfig

# from framework.authentication import register_jwt_manager
from .framework.blueprints import register_blueprint
from .framework.cors import cors_config
from .framework.database import register_db


def create_app(config: Config = DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    register_blueprint(app)
    register_db(app)
    cors_config(app)
    return app
