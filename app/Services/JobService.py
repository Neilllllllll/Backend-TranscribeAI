from app.Services.database import db
from app.Models.job import Job

class JobService:

    def create_job(self, job_uuid : str, file_path : str, socket_id : str, status : str) -> Job:
        job = Job(
            uuid=job_uuid,
            file_path=file_path,
            socket_id=socket_id,
            status=status
        )
        db.session.add(job)
        db.session.commit()
        return job

    def update_status(self, job_uuid, status: str) -> Job:
        job = Job.query.get(job_uuid)
        if not job:
            return None
        job.status = status
        db.session.commit()
        return job

    def complete_job(self, job_uuid, transcript: str):
        job = Job.query.get(job_uuid)
        if not job:
            return None
        job.status = "COMPLETED"
        job.transcript = transcript
        db.session.commit()
        return job
    
    def delete_job(self, job_uuid):
        job = Job.query.get(job_uuid)
        if not job:
            return False
        if job.status == "COMPLETED":
            db.session.delete(job)
            db.session.commit()
            return True
        return False

    def fail_job(self, job_uuid):
        job = Job.query.get(job_uuid)
        if not job:
            return None
        job.status = "FAILED"
        job.transcript = "La transcription a échoué"
        db.session.commit()
        return job
