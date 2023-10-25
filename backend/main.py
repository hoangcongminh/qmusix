from config import Config, DevConfig
from flask import Flask
from framework.blueprints import register_blueprint
from framework.database import register_db


def create_app(config: Config = DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    register_db(app)
    register_blueprint(app)
    # api = Api(app, doc="/swagger-ui")
    # api.add_namespace(recipe_ns)
    # with app.app_context():
    #     db.create_all()
    return app


app = create_app(DevConfig)


# @app.shell_context_processor
# def make_shell_context():
#     return {"RECIPE": Recipe}


if __name__ == "__main__":
    app.run()
