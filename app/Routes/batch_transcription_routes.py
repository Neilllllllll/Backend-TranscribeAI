from flask import Blueprint, request
from ..Controllers.batch_transcription_controller import BatchTranscriptionController
from ..Middlewares.check_audio import check_audio

batch_transcription_bp = Blueprint("batchTranscription", __name__)

@batch_transcription_bp.post("/uploadAudio")
@check_audio # Vérifie l'authenticité de l'audio
def uploadAudio():
    return BatchTranscriptionController.handleAudio()

@batch_transcription_bp.get("/result")
def getTranscription():
    return BatchTranscriptionController.getTranscriptionByUuid()

@batch_transcription_bp.delete("/cancel")
def deleteTranscription():
    return BatchTranscriptionController.deleteTranscription()
