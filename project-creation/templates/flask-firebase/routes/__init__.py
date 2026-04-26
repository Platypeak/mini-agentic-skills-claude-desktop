from routes.auth import auth_bp
# Import additional blueprints here as you add them
# from routes.users import users_bp

def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    # app.register_blueprint(users_bp, url_prefix="/api/users")
