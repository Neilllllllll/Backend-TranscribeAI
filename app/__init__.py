from flask import Flask
from flask_cors import CORS
from .Routes import register_routes
from .Middlewares.logger_middleware import logger_middleware
from .Middlewares.check_key_middleware import check_key_middleware
from .Config.setting import FRONTEND_URL



def create_app():
    app = Flask(__name__)
    # Allow the front to contact the server
    CORS( app, resources={r"/api/*": {"origins": str(FRONTEND_URL)}}, supports_credentials=True)
    # Middleware pour toutes les requêtes
    app.before_request(logger_middleware)
    app.before_request(check_key_middleware)
    # Load de toutes les routes
    register_routes(app)
    return app