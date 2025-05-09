from fastapi import UploadFile
from pathlib import Path

def save_resume(file: UploadFile, folder_path: str) -> str:
    """
    Saves the uploaded resume file to the specified folder as 'resume.pdf'.
    
    Args:
        file (UploadFile): The uploaded file from FastAPI
        folder_path (str): The directory path to save the file in

    Returns:
        str: Full path where the resume was saved
    """
    resume_path = Path(folder_path) / "Arpit Singhal Resume.pdf"
    
    with open(resume_path, "wb") as f:
        f.write(file.file.read())

    return str(resume_path)
