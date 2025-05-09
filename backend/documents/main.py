from documents.folder import create_folder
from documents.resume import save_resume
from documents.jd import save_jd_as_pdf
from fastapi import UploadFile

def save_application_documents(
    app_id: str,
    company: str,
    position: str,
    resume_file: UploadFile,
    jd_text: str
) -> dict:
    """
    Orchestrates saving resume and JD to disk.

    Args:
        app_id (str): UUID from the Application record
        company (str): Company name
        position (str): Job title
        resume_file (UploadFile): Uploaded resume
        jd_text (str): JD text from frontend

    Returns:
        dict: {
            "resume_path": <full_path>,
            "jd_path": <full_path>,
            "folder_path": <folder_path>
        }
    """
    # Step 1: Create folder
    folder_path = create_folder(company, position, app_id)

    # Step 2: Save resume as PDF
    resume_path = save_resume(resume_file, folder_path)

    # Step 3: Save JD text as jd.pdf
    jd_path = save_jd_as_pdf(jd_text, folder_path)

    return {
        "folder_path": folder_path,
        "resume_path": resume_path,
        "jd_path": jd_path,
    }
