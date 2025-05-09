import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.getenv("DOCUMENTS_PATH")  # e.g., /Users/arpit/Documents/HireScopeDocs

def sanitize(name: str) -> str:
    """Sanitizes folder names by removing extra spaces and replacing with _"""
    return name.strip().replace(" ", "_").replace("/", "_")

def create_folder(company: str, position: str, app_id: str) -> str:
    """
    Creates the folder where resume and JD will be saved.
    
    Format: /base_dir/CompanyName/PositionName-UUID/

    Returns:
        str: full path to the created folder
    """
    safe_company = sanitize(company)
    safe_position = sanitize(position)

    folder_path = Path(BASE_DIR) / safe_company / f"{safe_position}-{app_id}"
    folder_path.mkdir(parents=True, exist_ok=True)

    return str(folder_path)
