from ats.data_extraction import extract_text_from_pdf, extract_keywords
from ats.scorer import semantic_similarity, keyword_overlap_score
# Centralized function for ATS logic
# This will be called from application/main.py
def get_ats_score(resume_path: str, jd_path: str) -> float:
    """
    Calculates ATS score by comparing resume and job description.
    
    Args:
        resume_path (str): Full path to the saved resume PDF
        jd_path (str): Full path to the saved JD PDF

    Returns:
        float: Final ATS score (0 to 100)
    """

    resume_text = extract_text_from_pdf(resume_path)
    jd_text = extract_text_from_pdf(jd_path)

    # Semantic meaning match
    semantic_score = semantic_similarity(resume_text, jd_text)

    # Entity/keyword match
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)
    keyword_score = keyword_overlap_score(resume_keywords, jd_keywords)

    # Combine both for final ATS score
    final_score = (semantic_score * 0.6) + (keyword_score * 0.4)
    return round(final_score, 2)