from flask import request
import app.Helpers as Helpers
from flask import current_app

def handleAudio():
    audio_manager = current_app.extensions['audio_manager']
    job_service = current_app.extensions['job_service']
    redis_queue_service = current_app.extensions['redis_queue_service']

    # Générer un identifiant unique pour le job
    job_id = Helpers.generate_token()

    # Enregistrer le fichier audio reçu dans un chemin temporaire
    audio_file = request.files['audioFile']
    audio_file.filename = job_id
    file_path = audio_manager.save_audio(audio_file)

    # Créer une entrée job dans la base de données avec le statut "en attente"
    job_service.create_job(job_id, file_path, None, "PENDING")

    # Enqueue le job dans redis
    redis_queue_service.enqueue_job(job_id)

    return Helpers.success({"job_id": job_id, "status" : "Votre demande est dans la file d'attente"}, 200)

def getTranscriptionByUuid():
    pass


def cancelTranscriptionByUuid(job_id):
    pass
