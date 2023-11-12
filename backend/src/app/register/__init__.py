from flask import Blueprint
from flask_restx import Api

from .routes import register_ns

register_bp = Blueprint("register", __name__)
register_api = Api(register_ns, doc="/swagger-ui")
register_api.add_namespace(register_ns)
