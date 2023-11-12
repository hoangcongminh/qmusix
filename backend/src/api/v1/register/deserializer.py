"""
Serializers model for register namespace
"""
from flask_restx import Model, fields

register_schema = Model(
    "RegisterSchema",
    {
        "username": fields.String(required=True),
        "password": fields.String(required=True),
    },
)

change_password_schema = Model(
    "ChangePasswordSchema",
    {
        "username": fields.String(required=True),
        "old_password": fields.String(required=True),
        "new_password": fields.String(required=True),
    },
)
