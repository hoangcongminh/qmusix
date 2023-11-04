from config import Config, DevConfig
from flask import Flask

# from framework.authentication import register_jwt_manager
from framework.blueprints import register_blueprint
from framework.database import register_db


def create_app(config: Config = DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    register_db(app)
    register_blueprint(app)
    # register_jwt_manager(app)
    return app


app = create_app(DevConfig)

if __name__ == "__main__":
    app.run()
