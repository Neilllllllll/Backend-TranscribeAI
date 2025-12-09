from flask import Blueprint, request
from ..Controllers.transcription_controller import TranscriptionController
from ..Middlewares.audio_middleware import audio_middleware

transcription_bp = Blueprint("transcription", __name__)

# Exemple d'ajout d'un middleware spécifique à cette route

@transcription_bp.before_request
def check_audio():
    return audio_middleware()

@transcription_bp.post("/generate")
def generate_transcription():
    return TranscriptionController.generate_transcription(request)