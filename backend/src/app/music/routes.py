from flask_restx import Namespace, Resource, fields
from src.models.music import Music

music_ns = Namespace("music")

music_model = music_ns.model(
    "Music",
    {"url": fields.String()},
)


@music_ns.route("/")
class MusicAPI(Resource):
    @music_ns.marshal_with(music_model)
    def get(self):
        return Music.query.all()
