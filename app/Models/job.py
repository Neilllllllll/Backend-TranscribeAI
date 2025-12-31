from sqlalchemy.sql import func
from sqlalchemy import Enum
from app import db

class Job(db.Model):
    __tablename__ = "job"
    uuid = db.Column(db.String(255), primary_key=True)
    status = db.Column(
        Enum("PENDING", "PROCESSING", "COMPLETED", "FAILED", name="job_status"),
        nullable=False,
        server_default="PENDING"
    )
    file_path = db.Column(db.String(255), nullable=False)
    transcription = db.Column(db.Text)
    socket_id = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
