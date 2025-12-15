import requests

# Service pour gérer les interactions avec le service Whisper
class TranscriptionService:
    def __init__(self, URL : str):
        self.URL = URL

    # Fonction pour envoyer le fichier audio au service Whisper et obtenir la transcription
    def send_to_whisper_service(self, audio_file) -> str:
        files = {
            "audioFile": audio_file
        }
        response = requests.post(self.URL, files=files)
        response.raise_for_status()
        return response.json().get("transcription")

    
    # Fonction pour annuler une transcription en cours (si supporté par le service Whisper
    def cancel_transcription(self, job_id: str) -> bool:
        response = requests.post(f"{self.URL}/cancel", json={"job_id": job_id})
        return response.status_code == 200
