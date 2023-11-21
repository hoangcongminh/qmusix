from flask import Blueprint
from flask_restx import Api
from src.api.v1.login.endpoints import login_namespace
from src.api.v1.register.endpoints import register_namespace
from src.constant import AppErrorCode
from src.framework.exception import CustomAppException, CustomHTTPException
from src.utils.response import Response
from werkzeug.exceptions import HTTPException

api_v1_bp = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(
    api_v1_bp, version="1.0", title="Flask API for qmusix web app", doc="/swagger-ui"
)
api.add_namespace(register_namespace)
api.add_namespace(login_namespace)

@api.errorhandler(CustomHTTPException)
def handle_exception(e): 
    response = Response.Fail(
            data=None,
            alerta_message=e.alerta_message,
            error_message=e.description,
            code=getattr(e, 'app_code', AppErrorCode.UNDEFINED_APP_ERROR),
        )
    return response, e.code if isinstance(e, HTTPException) else 500

@api.errorhandler(Exception)
def default_error_handler(e):
    response = Response.Fail(
            data=None,
            alerta_message="Something Wrong",
            error_message=str(e),
            code=getattr(e, 'app_code', AppErrorCode.UNDEFINED_APP_ERROR)
        )
    return response, e.code if isinstance(e, HTTPException) else 500

@api.errorhandler(CustomAppException)
def default_error_handler(e):
    response = Response.Fail(
            data=None,
            alerta_message="Something Wrong",
            error_message=str(e),
            code=getattr(e, 'app_code', AppErrorCode.UNDEFINED_APP_ERROR)
        )
    return response, 500
