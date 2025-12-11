from ..Models.transcription_model import transcriptionModel
from ..Config.setting import AI_URL
import requests

class TranscriptionService():
    @staticmethod
    def transcribe_audio(audio): 
        files = {"audioFile": audio}
        response = requests.post(AI_URL + "/transcribe", files=files)
        return response.json()