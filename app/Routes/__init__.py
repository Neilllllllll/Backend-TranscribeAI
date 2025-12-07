from .transcription import transcription_bp

# Register all blueprints with the Flask app
def register_routes(app, url_prefix = ""):
    app.register_blueprint(transcription_bp, url_prefix=url_prefix)
