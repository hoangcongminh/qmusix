from flask import Blueprint
from flask_restx import Api

api_v1_bp = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(
    api_v1_bp, version="1.0", title="Flask API for qmusix web app", doc="/swagger-ui"
)
