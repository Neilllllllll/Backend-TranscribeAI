from app.Models.job import Job as JobModel
class JobService:
    def __init__(self, db):
        self.db = db

    def create_job(self, job_uuid : str, file_path : str, socket_id : str, status : str) -> JobModel:
        job = JobModel(
            uuid=job_uuid,
            file_path=file_path,
            socket_id=socket_id,
            status=status
        )
        self.db.session.add(job)
        self.db.session.commit()
        return job

    def update_status(self, job_uuid, status: str) -> JobModel:
        job = JobModel.query.get(job_uuid)
        if not job:
            return None
        job.status = status
        self.db.session.commit()
        return job

    def complete_job(self, job_uuid, transcription: str):
        job = JobModel.query.get(job_uuid)
        if not job:
            return None
        job.status = "COMPLETED"
        job.transcription = transcription
        self.db.session.commit()
        return job
    
    def get_job_by_uuid(self, job_uuid):
        job = JobModel.query.get(job_uuid)
        return job
    
    def delete_job(self, job_uuid):
        job = JobModel.query.get(job_uuid)
        if not job:
            return False
        if job.status == "COMPLETED":
            self.db.session.delete(job)
            self.db.session.commit()
            return True
        return False

    def fail_job(self, job_uuid):
        job = JobModel.query.get(job_uuid)
        if not job:
            return None
        job.status = "FAILED"
        job.transcript = "La transcription a échoué"
        self.db.session.commit()
        return job
