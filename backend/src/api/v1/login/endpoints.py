from http import HTTPStatus

from flask_restx import Namespace, Resource
from src.api.v1.login.deserialize import login_schema
from src.api.v1.login.function_handler import process_login_request

login_namespace = Namespace("login")
login_namespace.models[login_schema.name] = login_schema


@login_namespace.route("/")
class RegisterUser(Resource):
    """Handles HTTP requests to URL: /api/v1/auth/register."""

    @login_namespace.expect(login_schema, validate=True)
    @login_namespace.response(int(HTTPStatus.CREATED), "Success")
    @login_namespace.response(
        int(HTTPStatus.BAD_REQUEST), "Bad request, schema mismatch"
    )
    @login_namespace.response(int(HTTPStatus.NOT_FOUND), "username not found")
    @login_namespace.response(int(HTTPStatus.UNAUTHORIZED), "Password incorrect")
    def post(self):
        username = login_namespace.payload["username"]
        password = login_namespace.payload["password"]
        return process_login_request(username, password)
