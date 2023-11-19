"""
Api endpoint for register namespace
"""
from http import HTTPStatus

from flask_restx import Namespace, Resource
from src.api.v1.register.deserializer import change_password_schema, register_schema
from src.api.v1.register.function_handler import (
    process_change_password,
    process_register_new_user,
)

register_namespace = Namespace("register")
register_namespace.models[register_schema.name] = register_schema
register_namespace.models[change_password_schema.name] = change_password_schema


@register_namespace.route("")
class RegisterUser(Resource):
    """Handles HTTP requests to URL: /api/v1/auth/register."""

    # @register_namespace.doc(description="Bearer")
    @register_namespace.expect(register_schema, validate=True)
    @register_namespace.response(
        int(HTTPStatus.CREATED), "New user was successfully created."
    )
    @register_namespace.response(int(HTTPStatus.CONFLICT), "User already registered")
    @register_namespace.response(int(HTTPStatus.BAD_REQUEST), "Validation Error.")
    @register_namespace.response(
        int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error."
    )
    def post(self):
        """Register a new user and return access token"""
        username = register_namespace.payload["username"]
        password = register_namespace.payload["password"]
        return process_register_new_user(username, password)

    @register_namespace.expect(change_password_schema, validate=True)
    @register_namespace.response(int(HTTPStatus.OK), "Change password successfully")
    @register_namespace.response(
        int(HTTPStatus.UNAUTHORIZED), "Old password is incorrect"
    )
    @register_namespace.response(int(HTTPStatus.NOT_FOUND), "Username not found")
    def put(self):
        """Change password"""
        username = register_namespace.payload["username"]
        old_password = register_namespace.payload["old_password"]
        new_password = register_namespace.payload["new_password"]
        return process_change_password(username, old_password, new_password)
