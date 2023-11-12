from flask import Blueprint
from flask_restx import Api

from .routes import music_ns

music_bp = Blueprint("music", __name__)
music_api = Api(music_bp, doc="/swagger-ui")
music_api.add_namespace(music_ns)
