from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
import time

db = SQLAlchemy()

# Création de l'application Flask pour le serveur API
def create_app(config_class):
    app = Flask(__name__)

    # Charger la configuration
    app.config.from_object(config_class)

    # Initialisation de la base de données
    db.init_app(app)

    from app.Services.AudioManager import AudioManager

    from app.Services.JobService import JobService
    from app.Services.RedisQueueService import RedisQueueService

    # Initialisation du service de gestion des jobs
    app.extensions['job_service'] = JobService(db)

    # On tente de créer la table job avec une boucle de reconnexion
    with app.app_context():
        retries = 5
        while retries > 0:
            try:
                db.create_all()
                print("Base de données initialisée avec succès.")
                break
            except OperationalError:
                retries -= 1
                print(f"Postgres n'est pas prêt... Nouvelle tentative dans 2s ({retries} essais restants)")
                time.sleep(2)

        if retries <= 0:
            print("Erreur : Impossible de se connecter à Postgres après plusieurs tentatives.")

    # Initialisation du service de gestion des fichiers audio
    app.extensions['audio_manager'] = AudioManager(app.config['AUDIO_STORAGE_PATH'])

    # Initialisation du service de file d'attente Redis
    app.extensions['redis_queue_service'] = RedisQueueService(app.config['REDIS_URL'])

    # Load de toutes les routes
    from app.Routes import register_routes
    register_routes(app)

    return app

def create_app_worker_batch(config_class):

    app = create_app(config_class)

    # Configuration spécifique aux workers peut être ajoutée ici
    from app.Services.TranscriptionService import TranscriptionService
    app.extensions['transcription_service'] = TranscriptionService(app.config['WHISPER_SERVICE_URL'])

    return app

def create_app_api(config_class):
    # Appelle la fonction create_app avec la configuration commune
    app = create_app(config_class)

    # Configuration spécifique à l'API peut être ajoutée ici   
    # Configuration du CORS
    CORS(app, resources={r"/api/*": {"origins": app.config['FRONTEND_URL']}}, supports_credentials=True)

    return app

