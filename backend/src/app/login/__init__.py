from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

authorizations = {
    "jsonWebToken": {"type": "apiKey", "in": "header", "name": "Authorization"}
}
