"""Function to process underlying logic"""
from http import HTTPStatus

from flask import abort, jsonify
from src.models.user import User


def process_login_request(username, password):
    user = User.find_by_username(username)
    if not user:
        abort(HTTPStatus.NOT_FOUND, f"{username} not found")
    if not user.check_password(password):
        abort(HTTPStatus.UNAUTHORIZED, f"Password for {username} is incorrect")
    aceess_token = user.encode_access_token()
    request = jsonify(token=aceess_token.decode(), message="Successfully logged in")
    request.status_code = HTTPStatus.CREATED
    return request
