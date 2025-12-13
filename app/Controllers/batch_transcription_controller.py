from flask import request
from app.Services import audio_manager, job_service, redis_queue_service
from app.Helpers.token_generator import generate_token
from app.Helpers.responses import success

class BatchTranscriptionController:
    @staticmethod
    def handleAudio():
        # Générer un UUID pour le job
        job_id = generate_token()
        """ 
        Enregistrer le fichier audio reçu dans un chemin temporaire
        Change son nom de fichier pour éviter les conflits
        """
        audio_file = request.files['audioFile']
        audio_file.filename = job_id
        file_path = audio_manager.save_audio(audio_file)
        # créer une entrée job dans la base de données avec le statut "en attente"
        job_service.create_job(job_id, file_path, "je sais pas quoi mettre pour l'instant", "PENDING")
        # créer une entrer dans redis avec le statut
        redis_queue_service.enqueue_job(job_id)
        return success({"job_id": job_id, "status" : "Votre demande est dans la file d'attente"}, 200)

    @staticmethod
    def getTranscriptionByUuid():
        pass

    @staticmethod
    def cancelTranscriptionByUuid(job_id):
        pass
