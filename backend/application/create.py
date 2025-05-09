from sqlmodel import Session
from database.models.application import Application

def create_application_record(
    session: Session,
    company_name: str,
    job_title: str
) -> Application:
    """
    Creates a new Application DB record with only basic info.
    Resume/JD paths and score will be updated later.
    """
    app = Application(
        company_name=company_name,
        job_title=job_title
    )
    session.add(app)
    session.commit()
    session.refresh(app)
    return app
