"""
Serializers model for register namespace
"""
from flask_restx import Model, fields

login_schema = Model(
    "LoginSchema",
    {
        "username": fields.String(required=True),
        "password": fields.String(required=True),
    },
)
