from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Application(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    job_title: str
    company_name: str
    job_description_path: Optional[str]
    resume_path: Optional[str]
    cover_letter_path: Optional[str]
    is_referred: bool = False
    referrer_name: Optional[str]
    referrer_linkedin: Optional[str]
    ats_score: Optional[float]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})
    notes: Optional[str] = None