from . import BaseConfig
import os
# Configuration spécifique aux workers de traitement en arrière-plan
class WorkerConfig(BaseConfig.BaseConfig):
    WHISPER_SERVICE_URL = os.getenv("WHISPER_SERVICE_URL", "http://localhost:5001")
    WORKER_CONCURRENCY = 1  # Nombre de workers parallèles
    WORKER_RETRY_LIMIT = 3  # Nombre de tentatives en cas d'échec d'un job
    WORKER_TIMEOUT = 300    # Temps maximum (en secondes) pour traiter un job avant d'abandonner
    WORKER_SLEEP_TIME = 5  # Temps d'attente (en secondes) entre les vérifications de la file d'attente