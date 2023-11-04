from flask import request
from flask_jwt_extended import generate_password_hash
from flask_restx import Namespace, Resource, api, fields

from backend.framework.database import db
from backend.models.user import User

register_ns = Namespace("register")


@register_ns.route("/")
class Register(Resource):
    def post(self):
        user = User(
            username=register_ns.payload["username"],
            password_hash=generate_password_hash(register_ns.payload["password"]),
        )
        # db.session.add(user)
        # db.session.commit()
        return {"message": "abc"}
