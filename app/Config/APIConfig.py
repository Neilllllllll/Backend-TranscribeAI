from app.Config import BaseConfig
import os 
# Configuration spécifique à l'API Flask
class APIConfig(BaseConfig.BaseConfig):
    FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000") # URL du frontend autorisé pour le CORS
    PORT = 5000 # Port d'écoute de l'API
    HOST = "0.0.0.0" # Écoute sur toutes les interfaces réseau
    FORMAT_AUDIO_ALLOWED = {"wav", "mp3", "ogg", "m4a"} # Formats audio autorisés
    MIN_DURATION_SEC_BATCH_MODE = 1 # durée minimale en secondes pour le mode batch

