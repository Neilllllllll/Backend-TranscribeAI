from ..Services.transcription_service import TranscriptionService
from ..Helpers.responses import success, error

class TranscriptionController:

    @staticmethod
    def generate_transcription(request):
        try:
            audio = request.files["audioFile"]
            response = TranscriptionService.transcribe_audio(audio)
            return success({"transcription" : response["transcription"]})
        except Exception as e:
            return error("Service IA injoignable", 500)
