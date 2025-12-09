from flask import Flask
from .Routes import register_routes
from .Middlewares.logger_middleware import logger_middleware
from .Middlewares.auth_middleware import auth_middleware

def create_app():
    app = Flask(__name__)
    # Middleware pour toutes les requêtes
    app.before_request(logger_middleware)
    app.before_request(auth_middleware)
    # Load de toutes les routes
    register_routes(app)
    return app