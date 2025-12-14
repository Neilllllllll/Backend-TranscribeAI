import time
from app import create_app
from app.config import AUDIO_STORAGE_FOLDER_NAME
from app.Services import redis_queue_service, job_service, whisper_batch_service, audio_manager

def worker_loop():
    while True:
        # Récupérer un job de la file d'attente Redis (bloquant)
        job_uuid = redis_queue_service.pop_job_blocking()
        
        # Mettre à jour le statut du job en "IN_PROGRESS"
        job_service.update_status(job_uuid, "IN_PROGRESS")
        
        try:
            # Récupérer le chemin du fichier audio depuis la base de données
            job = job_service.get_job_by_uuid(job_uuid)
            audio_file_path = job.file_path

            with open(audio_file_path, 'rb') as f:
                audio_file = f.read()
            
            # Envoyer le fichier audio au service Whisper pour transcription
            transcription = whisper_batch_service.send_to_whisper_service(audio_file)
            
            # Mettre à jour le job avec la transcription et le statut "COMPLETED"
            job_service.complete_job(job_uuid, transcription)
        
        except Exception as e:
            # En cas d'erreur, mettre à jour le statut du job en "FAILED"
            job_service.fail_job(job_uuid)
            print(f"Erreur lors du traitement du job {job_uuid}: {e}")

        finally:
            # Supprimer le fichier audio après traitement
            audio_manager.delete_audio_file(audio_file_path)

        # Petite pause pour éviter une boucle trop rapide
        time.sleep(1)

if __name__ == "__main__":
    # 2. On crée l'instance de l'app
    app = create_app()

    # 3. On active le contexte de l'application
    # Cela permet d'accéder à current_app.config, à la BDD, et charge les variables d'env
    with app.app_context():
        print("🚀 Worker démarré avec le contexte de l'application Flask.")
        print(f"📂 Dossier Audio configuré : {app.config.get('AUDIO_STORAGE_FOLDER_NAME')}") # Debug
    worker_loop()
