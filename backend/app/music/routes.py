from flask_restx import Namespace, Resource

music_ns = Namespace("music")


@music_ns.route("/")
class Hello(Resource):
    def get(self):
        return {"message": "Hello World"}
