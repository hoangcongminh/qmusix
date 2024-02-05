from http import HTTPStatus

from flask_restx import Namespace, Resource
from pydantic import ValidationError
from src.api.v1.login.function_handler import process_login_request
from src.api.v1.login.serializers import LoginSchema
from src.constant import AppErrorCode
from src.framework.exception import CustomHTTPException

login_namespace = Namespace("login")
login_namespace.schema_model(LoginSchema.__name__, LoginSchema.model_json_schema())

@login_namespace.route("")
class RegisterUser(Resource):
    """Handles HTTP requests to URL: /api/v1/auth/register."""

    @login_namespace.param(name="payload", _in = "body", schema=LoginSchema.model_json_schema())
    @login_namespace.response(int(HTTPStatus.CREATED), "Success")
    @login_namespace.response(
        int(HTTPStatus.BAD_REQUEST), "Bad request, schema mismatch"
    )
    @login_namespace.response(int(HTTPStatus.NOT_FOUND), "username not found")
    @login_namespace.response(int(HTTPStatus.UNAUTHORIZED), "Password incorrect")
    def post(self):
        try:
            login_schema = LoginSchema(**login_namespace.payload)
        except ValidationError as e:
            raise CustomHTTPException(HTTPStatus.BAD_REQUEST, "Validation error, schema mismatch", AppErrorCode.EXPECTED_APP_EXCEPTION_NOT_ERROR ,str(e))
        username = login_schema.username
        password = login_schema.password
        return process_login_request(username, password)
