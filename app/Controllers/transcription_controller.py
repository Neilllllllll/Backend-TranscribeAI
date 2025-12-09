from ..Services.transcription_service import TranscriptionService
from ..Helpers.responses import success, error

class TranscriptionController:

    @staticmethod
    def generate_transcription(request):
        try:
            if "file" not in request.files:
                return error("Missing audio file", 400)

            audio = request.files["file"]

            text = TranscriptionService.transcribe_audio(audio)

            return success({"transcription": text})

        except Exception as e:
            return error(str(e), 500)
