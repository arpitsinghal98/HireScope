from sqlmodel import Session
from database.models.application import Application

def update_application_record(
    session: Session,
    app_id: str,
    resume_path: str,
    jd_path: str,
    ats_score: float
) -> Application:
    """
    Updates an existing application with resume path, JD path, and ATS score.
    """
    app = session.get(Application, app_id)
    if not app:
        raise Exception("Application not found.")

    app.resume_path = resume_path
    app.job_description_path = jd_path
    app.ats_score = ats_score

    session.add(app)
    session.commit()
    session.refresh(app)
    return app
