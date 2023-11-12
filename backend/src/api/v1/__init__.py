from flask import Blueprint
from flask_restx import Api
from src.api.v1.login.endpoints import login_namespace
from src.api.v1.register.endpoints import register_namespace

api_v1_bp = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(
    api_v1_bp, version="1.0", title="Flask API for qmusix web app", doc="/swagger-ui"
)
api.add_namespace(register_namespace)
api.add_namespace(login_namespace)
