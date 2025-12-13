import os

try:
    # Clé pour authentification
    X_API_KEY = os.getenv("X_API_KEY")
    # Clé pour appeler l'IA
    AI_API_KEY = os.getenv("AI_API_KEY")
    # URL de l'IA
    AI_URL = os.getenv("AI_URL")
    # URL du front
    FRONTEND_URL=os.getenv("FRONTEND_URL")
    # Dossier où les audio seront temporairement stockés
    AUDIO_STORAGE_FOLDER_NAME=os.getenv("AUDIO_STORAGE_FOLDER_NAME")
    # URL de la base de données des jobs
    DB_URL = os.getenv("DB_URL")
    # URL de Redis
    REDIS_URL = os.getenv("REDIS_URL")

except:
    print("Des constantes sont manquantes (variable d'env)")
