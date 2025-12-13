import requests

# Service pour gérer les interactions avec le service Whisper
class BatchWhisper:
    def __init__(self, URL : str):
        self.URL = URL

    # Fonction pour envoyer le fichier audio au service Whisper et obtenir la transcription
    def send_to_whisper_service(self, file_path : str) -> str:
        transcription = ""
        with open(file_path, 'rb') as audio_file:
            files = {'audioFile': audio_file}
            response = requests.post(self.URL, files=files)
        transcription = response.json().get("transcription")
        return transcription
