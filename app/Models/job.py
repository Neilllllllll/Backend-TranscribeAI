import uuid
from sqlalchemy.sql import func
from app.Services.database import db

class Job(db.Model):
    __tablename__ = "job"
    # Specifie le le schema "Queue" pour cette table
    __table_args__ = {"schema": "Queue"}

    uuid = db.Column(db.UUID(as_uuid=True), primary_key=True)
    status = db.Column(db.String(20), nullable=False, default="PENDING")
    file_path = db.Column(db.String(255), nullable=False)
    transcription = db.Column(db.Text)
    socket_id = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
