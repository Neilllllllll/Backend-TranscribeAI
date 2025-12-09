from .transcription_routes import transcription_bp

# Register all blueprints with the Flask app
def register_routes(app):
    url_prefix = "/api"
    app.register_blueprint(transcription_bp, url_prefix=url_prefix + "/transcription")
