from ..Services.transcription_service import TranscriptionService
from ..Helpers.responses import success, error

class TranscriptionController:

    @staticmethod
    def generate_transcription(request):
        try:
            audio = request.files["audioFile"]
            text = TranscriptionService.transcribe_audio(audio)
            return success({"text": text})
        
        except Exception as e:
            return error(str(e), 500)
