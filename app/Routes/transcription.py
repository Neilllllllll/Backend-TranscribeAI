from flask import Blueprint, jsonify

transcription_bp = Blueprint("transcription", __name__)

@transcription_bp.post("/transcriptions")
def list_users():
    return jsonify({"message": "post transcription"})

@transcription_bp.get("/transcriptions")
def get_transcriptions():
    return jsonify({"message": "get transcriptions"})