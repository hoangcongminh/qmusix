from src.constant import AppErrorCode
from werkzeug.exceptions import HTTPException


class CustomHTTPException(HTTPException):
    def __init__(self,code:int = 500, alerta_message:str=None ,app_code:int= AppErrorCode.UNDEFINED_APP_ERROR, error_message:str=None):
        super().__init__(error_message)
        self.alerta_message = alerta_message
        self.code = code
        self.app_code = app_code
        if self.description == None:
            self.description = self.alerta_message
        # self.error_message= error_message

class CustomAppException(Exception):
    def __init__(self, error_message:str,alerta_message:str="Something Wrong", app_code:int = AppErrorCode.UNDEFINED_APP_ERROR):
        super().__init__(error_message)
        self.app_code = app_code
        self.alerta_message = alerta_message
