from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.main import get_session
from database.models.application import Application

router = APIRouter()

@router.get("/applications")
def get_all_applications(session: Session = Depends(get_session)):
    apps = session.exec(select(Application)).all()
    return apps

@router.get("/applications/{app_id}")
def get_application(app_id: str, session: Session = Depends(get_session)):
    app = session.get(Application, app_id)
    if not app:
        raise HTTPException(status_code=404, detail="Application not found")
    return app
