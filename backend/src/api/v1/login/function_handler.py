"""Function to process underlying logic"""
from http import HTTPStatus

from flask import abort, jsonify
from src.constant import AppErrorCode
from src.framework.exception import CustomHTTPException
from src.models.user import User
from src.utils.response import Response


def process_login_request(username, password):
    user = User.find_by_username(username)
    if not user:
        raise CustomHTTPException(int(HTTPStatus.NOT_FOUND), alerta_message=f"{username} not found", app_code=AppErrorCode.EXPECTED_APP_EXCEPTION_NOT_ERROR)
    if not user.check_password(password):
        raise CustomHTTPException(int(HTTPStatus.UNAUTHORIZED), alerta_message=f"Password for {username} is incorrect",app_code=AppErrorCode.EXPECTED_APP_EXCEPTION_NOT_ERROR)
    aceess_token = user.encode_access_token()
    request = jsonify(Response.OK(data={"token": aceess_token, "message": "Successfully logged in"}))
    request.status_code = HTTPStatus.CREATED
    return request
