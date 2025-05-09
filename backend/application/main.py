from application.create import create_application_record
from application.update import update_application_record
from documents.main import save_application_documents
from ats.main import get_ats_score
from sqlmodel import Session

def handle_application_process(
    session: Session,
    company_name: str,
    job_title: str,
    resume_file,
    jd_text: str
):
    # Step 1: Create base DB record
    app = create_application_record(session, company_name, job_title)

    # Step 2: Save resume + JD
    doc_result = save_application_documents(
        app_id=str(app.id),
        company=company_name,
        position=job_title,
        resume_file=resume_file,
        jd_text=jd_text
    )

    # Step 3: Run ATS scoring
    ats_score = get_ats_score(doc_result["resume_path"], doc_result["jd_path"])

    # Step 4: Update DB record with full data
    updated_app = update_application_record(
        session,
        app_id=app.id,
        resume_path=doc_result["resume_path"],
        jd_path=doc_result["jd_path"],
        ats_score=ats_score
    )

    return updated_app
