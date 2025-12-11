from flask import Blueprint, request
from ..Controllers.transcription_controller import TranscriptionController
from ..Middlewares.check_audio_middleware import checkIsAudio

transcription_bp = Blueprint("transcription", __name__)

@transcription_bp.before_request
def check_audio():
    return checkIsAudio()

@transcription_bp.post("/generate")
def generate_transcription():
    return TranscriptionController.generate_transcription(request)
