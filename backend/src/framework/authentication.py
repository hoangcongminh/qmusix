from flask_jwt_extended import JWTManager

# authorizations = {
#     "jsonWebToken": {"type": "apiKey", "in": "header", "name": "Authorization"}
# }


# # Refactor the token_required decorator
# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = None
#         # JWT token is now expected in the "Authorization" header
#         if "Authorization" in request.headers:
#             auth_header = request.headers["Authorization"]
#             # Check for the "Bearer" token prefix
#             if auth_header.startswith("Bearer "):
#                 token = auth_header.split("Bearer ")[1]

#         # Return 401 if the token is missing
#         if not token:
#             return jsonify({"message": "Token is missing !!"}), 401

#         try:
#             # Decode the JWT token to fetch the stored details
#             data = jwt.decode(token, app.config["SECRET_KEY"])
#             current_user = User.query.filter_by(public_id=data["public_id"]).first()
#         except:
#             return jsonify({"message": "Token is invalid !!"}), 401

#         # Return the current logged-in user's context to the routes
#         return f(current_user, *args, **kwargs)

#     return decorated
