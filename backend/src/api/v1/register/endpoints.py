"""
Api endpoint for register namespace
"""
from http import HTTPStatus

from flask import abort
from flask_restx import Namespace, Resource, fields
from pydantic import ValidationError
from src.api.v1.register.function_handler import (
    process_change_password,
    process_register_new_user,
)
from src.api.v1.register.serializers import ChangePasswordSchema, RegisterSchema
from src.constant import AppErrorCode
from src.framework.exception import CustomHTTPException

register_namespace = Namespace("register")
register_namespace.schema_model(ChangePasswordSchema.__name__,RegisterSchema.model_json_schema())
register_namespace.schema_model(RegisterSchema.__name__, RegisterSchema.model_json_schema())

@register_namespace.route("")
class RegisterUser(Resource):
    """Handles HTTP requests to URL: /api/v1/auth/register."""
    @register_namespace.param(name="payload", _in="body", schema=RegisterSchema.model_json_schema())
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
        try:
            register_schema = RegisterSchema(**register_namespace.payload)
        except ValidationError as e:
            raise CustomHTTPException(HTTPStatus.BAD_REQUEST, "Validation error, schema mismatch", AppErrorCode.EXPECTED_APP_EXCEPTION_NOT_ERROR ,str(e))
        username= register_schema.username
        password = register_schema.password
        return process_register_new_user(username, password)
    
    @register_namespace.param(name="payload", _in="body", schema=ChangePasswordSchema.model_json_schema())
    @register_namespace.response(int(HTTPStatus.OK), "Change password successfully")
    @register_namespace.response(
        int(HTTPStatus.UNAUTHORIZED), "Old password is incorrect"
    )
    @register_namespace.response(int(HTTPStatus.NOT_FOUND), "Username not found")
    def put(self):
        """Change password"""
        try:
            change_password_schema = ChangePasswordSchema(**register_namespace.payload)
        except ValidationError as e:
            raise CustomHTTPException(HTTPStatus.BAD_REQUEST, "Validation error, schema mismatch", AppErrorCode.EXPECTED_APP_EXCEPTION_NOT_ERROR ,str(e))
        username = change_password_schema.username
        old_password = change_password_schema.old_password
        new_password = change_password_schema.new_password
        return process_change_password(username, old_password, new_password)
