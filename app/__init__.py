from flask import Flask
from flask_cors import CORS
from app.Services.database import db
from app.Routes import register_routes
from app.Middlewares.logger_middleware import logger_middleware
from app.Middlewares.check_key_middleware import check_key_middleware
from app.config import FRONTEND_URL, DB_URL

# Création de l'application Flask
def create_app():
    app = Flask(__name__)

    # Configuration de la base de données
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Allow the front to contact the server
    CORS( app, resources={r"/api/*": {"origins": str(FRONTEND_URL)}}, supports_credentials=True)

    # Middleware pour toutes les requêtes
    app.before_request(logger_middleware)
    app.before_request(check_key_middleware)

    # Load de toutes les routes
    register_routes(app)

    return app