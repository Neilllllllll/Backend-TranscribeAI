from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

# Création de l'application Flask pour le serveur API
def create_app():
    app = Flask(__name__)

    # Initialisation des services et configurations

    # Initialisation de la base de données
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from app.Services.AudioManager import AudioManager
    from app.Services.TranscriptionService import TranscriptionService
    from app.Services.JobService import JobService
    from app.Services.RedisQueueService import RedisQueueService

    # Initialisation du service de gestion des jobs
    job_service = JobService(db)
    app.extensions['job_service'] = job_service
    
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Initialisation du gestionnaire de fichiers audio
    app.config['AUDIO_STORAGE_PATH'] = os.getenv('AUDIO_STORAGE_PATH')
    audio_manager = AudioManager(app.config['AUDIO_STORAGE_PATH'])
    app.extensions['audio_manager'] = audio_manager

    # Initialisation du service de transcription
    app.config['WHISPER_SERVICE_URL'] = os.getenv('WHISPER_SERVICE_URL')   
    transcription_service = TranscriptionService(app.config['WHISPER_SERVICE_URL']) 
    app.extensions['transcription_service'] = transcription_service

    # Initialisation du service de file d'attente Redis
    app.config['REDIS_URL'] = os.getenv('REDIS_URL')
    redis_queue_service = RedisQueueService(app.config['REDIS_URL'])
    app.extensions['redis_queue_service'] = redis_queue_service
    
    # Configuration du CORS
    from flask_cors import CORS
    app.config['FRONTEND_URL'] = os.getenv('FRONTEND_URL')
    CORS( app, resources={r"/api/*": {"origins": str(app.config['FRONTEND_URL'])}}, supports_credentials=True)

    # Load de toutes les routes
    from app.Routes import register_routes
    register_routes(app)

    return app

# Création de l'application Flask pour le worker
# Faire 2 create_app 1 pour le worker et 1 pour l'API