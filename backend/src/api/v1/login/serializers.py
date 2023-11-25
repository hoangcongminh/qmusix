"""
Serializers model for login namespace
"""
from pydantic import BaseModel


class LoginSchema(BaseModel):
    username: str
    password: str
    class Config:
        strict = True
