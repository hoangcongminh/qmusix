"""Default function to handle application error"""
import json

DEFAULT_ERROR = [404, 400]


def default_error_handler(e):
    """Default error message"""
    return {"message": str(e), "status_code": e.code}, int(e.code)


def register_error_handlers(app):
    for error_code in DEFAULT_ERROR:
        app.register_error_handler(error_code, default_error_handler)
