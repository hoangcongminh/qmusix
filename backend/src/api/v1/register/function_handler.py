"""
Collection of functions to handle underlying logic
"""

from http import HTTPStatus

from flask import abort, jsonify
from src.framework.database import db
from src.models.user import User


def process_register_new_user(username, password):
    if User.find_by_username(username):
        abort(HTTPStatus.CONFLICT, f"User {username} already registered")
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    response = jsonify(
        status="success",
        message=f"{username} successfully registered",
    )
    response.status_code = HTTPStatus.CREATED
    return response


def process_change_password(username, old_password, new_password):
    if old_password == new_password:
        abort(HTTPStatus.BAD_REQUEST, "New and old password are identical")
    if not User.find_by_username(username):
        abort(HTTPStatus.NOT_FOUND, f"Username {username} not found")

    user = User.find_by_username(username)
    if not user.check_password(old_password):
        abort(HTTPStatus.UNAUTHORIZED, "Incorrect password")
    user.password = new_password
    db.session.commit()
    response = jsonify({"message": "Password changed"})
    response.status_code = HTTPStatus.OK
    return response
