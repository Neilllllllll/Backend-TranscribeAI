from flask import Blueprint
import app.Controllers as Controllers
import app.Middlewares as Middlewares

batch_transcription_bp = Blueprint("batchTranscription", __name__)

@batch_transcription_bp.post("/uploadAudio")
@Middlewares.check_audio # Vérifie l'authenticité de l'audio
def uploadAudio():
    return Controllers.handleAudio()

@batch_transcription_bp.get("/result")
def getTranscription():
    return Controllers.getTranscriptionByUuid()

@batch_transcription_bp.delete("/cancel")
def deleteTranscription():
    return Controllers.deleteTranscription()
