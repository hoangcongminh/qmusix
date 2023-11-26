"""
Collection of functions to handle underlying logic
"""

from http import HTTPStatus

from flask import abort, jsonify
from src.constant import AppErrorCode
from src.framework.database import db
from src.framework.exception import CustomAppException, CustomHTTPException
from src.models.user import User
from src.utils.response import Response


def process_register_new_user(username, password):
    if User.find_by_username(username):
        raise CustomHTTPException(code=int(HTTPStatus.CONFLICT), app_code=AppErrorCode.EXPECTED_APP_EXCEPTION_NOT_ERROR, alerta_message=f"{username} already registered")
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    response = jsonify(Response.OK(f"{username} Successfully Created"))
    response.status_code = HTTPStatus.CREATED
    return response


def process_change_password(username, old_password, new_password):
    if old_password == new_password:
        raise CustomHTTPException(code=int(HTTPStatus.CONFLICT), app_code=AppErrorCode.EXPECTED_APP_EXCEPTION_NOT_ERROR, alerta_message="New password is the same with old password")
    if not User.find_by_username(username):
        raise CustomHTTPException(code=int(HTTPStatus.CONFLICT), app_code=AppErrorCode.EXPECTED_APP_EXCEPTION_NOT_ERROR, alerta_message=f"Username {username} not found")
    user = User.find_by_username(username)
    if not user.check_password(old_password):
        raise CustomHTTPException(code=int(HTTPStatus.UNAUTHORIZED), app_code=AppErrorCode.EXPECTED_APP_EXCEPTION_NOT_ERROR ,alerta_message="Password incorrect")
    user.password = new_password
    db.session.commit()
    response = jsonify(Response.OK(data="Password changed"))
    response.status_code = HTTPStatus.OK
    return response
