from .batch_transcription_routes import batch_transcription_bp

# Register all blueprints with the Flask app
def register_routes(app):
    url_prefix = "/api"
    app.register_blueprint(batch_transcription_bp, url_prefix=url_prefix + "/batchTranscription")
