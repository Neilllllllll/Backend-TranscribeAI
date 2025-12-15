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

# Récupérer la transcription par UUID
def getTranscriptionByUuid():

    # Récupérer l'UUID du job depuis les paramètres de la requête
    job_uuid = request.args.get('uuid')
    if not job_uuid:
        return Helpers.error("Missing job_id parameter", 400)
    # Contacter le service de gestion des jobs pour obtenir le statut et la transcription
    job_service = current_app.extensions['job_service']
    job = job_service.get_job_by_uuid(job_uuid)
    if not job:
        return Helpers.error("Job not found", 404)
    elif job.status == "PENDING" or job.status == "PROCESSING":
        return Helpers.success({"job_id": job.uuid,"status": job.status,})
    elif job.status == "FAILED":
        return Helpers.error("Transcription failed", 500)
    else:
        job_service.delete_job(job_uuid)
        return Helpers.success({
            "job_id": job.uuid,
            "status": job.status,
            "transcription": job.transcription
        }, 200)


def cancelTranscriptionByUuid(job_id):
    pass
